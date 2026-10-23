"""Split old mixed editorial sections using reviewed Registry purpose categories.

This is a one-time, checked selection migration. Registry taxonomy remains the
purpose SSOT; section placement and ordering remain Awesome editorial choices.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SELECTION = ROOT / "catalog" / "selection.yaml"
NAVIGATION = ROOT / "catalog" / "navigation.yaml"
NEW_SECTIONS = {
    "agent-builders": ("agents", "Agent Development Platforms"),
    "llm-frameworks": ("agents", "LLM & Agent Frameworks"),
    "enterprise-assistants": ("productivity-knowledge", "Enterprise Assistants"),
    "model-access": ("data-cloud", "Model Access & Routing"),
    "search-applications": ("search-web-data", "AI Search Applications"),
    "search-api-services": ("search-web-data", "Search APIs"),
    "meeting-notes": ("productivity-knowledge", "Meeting Notes & Summaries"),
}


def destination(section: str, categories: set[str]) -> str | None:
    if section == "agent-platforms":
        for category, target in (
            ("agent-builder", "agent-builders"), ("customer-service", "customer-service"),
            ("enterprise-assistant", "enterprise-assistants"),
            ("llm-framework", "llm-frameworks"), ("search-api", "search-api-services"),
            ("people-search", "search-retrieval"), ("application-search", "search-retrieval"),
            ("web-scraping", "web-data-browsers"), ("browser-infrastructure", "web-data-browsers"),
            ("data-infrastructure", "data-platforms"),
            ("model-evaluation", "agent-evaluation"), ("auth", "agent-payments-identity"),
            ("agent-payments", "agent-payments-identity"), ("app-deployment", "cloud-infrastructure"),
            ("backend-service", "cloud-infrastructure"), ("sandbox", "cloud-infrastructure"),
            ("sre-incident-response", "coding-tools"),
        ):
            if category in categories:
                return target
    if section == "developer-platforms":
        if "model-routing" in categories:
            return "model-access"
        if categories & {"model-inference", "gpu-cloud", "model-hub"}:
            return "cloud-infrastructure"
    if section == "search-retrieval":
        if "search-engine" in categories:
            return "search-applications"
        if "search-api" in categories:
            return "search-api-services"
    if section == "documents-knowledge" and "meeting-notes" in categories:
        return "meeting-notes"
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    selection = yaml.safe_load(SELECTION.read_text(encoding="utf-8"))
    navigation = yaml.safe_load(NAVIGATION.read_text(encoding="utf-8"))
    registry = Path(selection["registry_root"])
    entities = {e["id"]: e for path in (registry / "data" / "entities").glob("*/*.json")
                for e in [json.loads(path.read_text(encoding="utf-8"))]}
    groups = {g["id"]: g for g in navigation["groups"]}
    sections = {s["id"]: s for s in selection["sections"]}
    for sid, (gid, title) in NEW_SECTIONS.items():
        if sid in sections:
            raise SystemExit(f"already migrated: {sid}")
        group = groups[gid]
        group["sections"].append({"id": sid, "title": title})
        sections[sid] = {"id": sid, "title": title, "group_id": gid,
                         "group_title": group["title"], "items": []}
    moves = []
    for section in selection["sections"]:
        kept = []
        for item in section["items"]:
            rid = item["registry_id"]
            target = destination(section["id"], set(entities[rid].get("categories", [])))
            if target and target != section["id"]:
                sections[target]["items"].append(item)
                moves.append((rid, section["id"], target))
            else:
                kept.append(item)
        section["items"] = kept
    for rid, source, target in moves:
        print(f"MOVE {rid}: {source} -> {target}")
    ordered = []
    for group in navigation["groups"]:
        for nav_section in group["sections"]:
            section = sections.get(nav_section["id"])
            if section and section["items"]:
                ordered.append(section)
    selection["sections"] = ordered
    print(f"moved={len(moves)} sections={len(ordered)} selected={sum(len(s['items']) for s in ordered)}")
    if args.apply:
        SELECTION.write_text(yaml.safe_dump(selection, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8", newline="\n")
        NAVIGATION.write_text(yaml.safe_dump(navigation, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
