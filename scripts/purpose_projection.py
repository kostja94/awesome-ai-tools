"""Allowed Awesome sections for Registry v2 purpose categories.

Registry owns category meaning. This is only the public list's editorial
crosswalk: a multi-purpose item may remain in any section matching one of its
purpose leaves, while a model always stays under the unified Models group.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SELECTION = ROOT / "catalog" / "selection.yaml"
NAVIGATION = ROOT / "catalog" / "navigation.yaml"
MODEL_TYPES = {"model-family", "model-version"}
MODEL_CATEGORY_SECTION = {
    "llm": "language-models", "llm-search": "language-models", "llm-web-dev": "language-models",
    "image-generation": "image-models", "video-generation": "video-models",
    "speech-models": "speech-models", "music-generation": "music-models", "3d": "spatial-models",
}
SECTION_CATEGORIES = {
    "agent-platforms": "agent-infrastructure",
    "agent-builders": "agent-builder",
    "llm-frameworks": "llm-framework",
    "agent-payments-identity": "agent-payments auth",
    "agent-evaluation": "model-evaluation",
    "coding-tools": "coding coding-task-execution code-completion code-security developer-environment software-testing sre-incident-response terminal-tools",
    "app-builders": "app-builder ui-code-generation website-builder",
    "developer-platforms": "developer-platform",
    "image-creation-editing": "image-generation image-editing",
    "creative-workflows": "content-creation",
    "design-tools": "design user-research",
    "video-generation-editing": "video-generation video-editing avatar screen-recording",
    "filmmaking-localization": "filmmaking short-drama video-translation",
    "speech-applications": "voice-services transcription voice-changer speech-models",
    "music-podcasts": "music-tools music-generation audio-creation podcast-hosting podcast-tools",
    "search-retrieval": "people-search enterprise-search application-search retrieval-model-services",
    "search-applications": "search-engine",
    "search-api-services": "search-api",
    "web-data-browsers": "web-scraping browser browser-infrastructure",
    "cloud-infrastructure": "gpu-cloud model-inference training-tools sandbox app-deployment backend-service",
    "model-access": "model-routing",
    "model-hubs": "model-hub",
    "model-runtime-tools": "model-runtime",
    "data-platforms": "data-analytics data-annotation data-infrastructure data-viz synthetic-data spreadsheet",
    "documents-knowledge": "knowledge-management documentation pdf-tools",
    "meeting-notes": "meeting-notes",
    "productivity-automation": "project-management forms scheduling collaborative-workspace workspace-assistant task-execution automation rpa",
    "enterprise-assistants": "enterprise-assistant",
    "marketing-content": "seo-marketing seo geo seo-localization sales-content content-detection link-in-bio sales-outreach sales-crm",
    "customer-service": "customer-service conversation-intelligence",
    "commerce-shopping": "shopping ecommerce-search",
    "finance-accounting": "finance-ops financial-analysis financial-infrastructure mortgage-operations",
    "learning-tools": "education education-notes homework study-tools language-learning math tutoring classroom book-summary",
    "research-writing": "academic-writing",
    "recruiting-careers": "recruiting recruiting-notes job-search",
    "healthcare": "healthcare healthcare-operations",
    "legal": "legal",
    "spatial-3d": "3d 3d-ecommerce cad motion-capture",
    "games-interactive": "game-dev gaming metaverse",
    "writing-publishing": "story-generation writing-assistant web-novel journal-tools voice-writing presentation",
    "chat-social": "chat-assistant character-chatbot nsfw-chatbot specialized-chatbot",
    "industry-operations": "beauty construction defense emergency-response event-planning hospitality location-analytics manufacturing nonprofit plant-identification supply-chain travel vertical-solutions",
    "tool-discovery": "tool-discovery",
}
CATEGORY_SECTION = {cat: section for section, cats in SECTION_CATEGORIES.items() for cat in cats.split()}
PREFERRED_SECTION = {
    "amazon-bedrock": "model-access",
    "azure-ai-foundry": "cloud-infrastructure",
    "vertex-ai": "cloud-infrastructure",
    "higgsfield-platform": "video-generation-editing",
    "fliki": "video-generation-editing",
    "gendo": "image-creation-editing",
    "monograph": "industry-operations",
    "hugging-face-hub": "model-hubs",
    "notebooklm": "documents-knowledge",
    "creatify": "video-generation-editing",
    "daily": "developer-platforms",
    "pepper-content": "marketing-content",
}


def allowed_sections(entity: dict) -> set[str]:
    if entity["type"] in MODEL_TYPES:
        return {MODEL_CATEGORY_SECTION[cat] for cat in entity.get("categories", [])
                if cat in MODEL_CATEGORY_SECTION}
    return {CATEGORY_SECTION[cat] for cat in entity.get("categories", []) if cat in CATEGORY_SECTION}


def audit(selection: dict, entities: dict[str, dict]) -> list[tuple[str, str, list[str]]]:
    problems = []
    for section in selection["sections"]:
        for item in section["items"]:
            rid = item["registry_id"]
            if rid not in entities:
                continue
            allowed = allowed_sections(entities[rid])
            preferred = PREFERRED_SECTION.get(rid)
            if preferred and preferred not in allowed:
                raise ValueError(f"preferred section unsupported by categories: {rid} -> {preferred}")
            if section["id"] not in allowed or (preferred and section["id"] != preferred):
                problems.append((rid, section["id"], sorted(allowed)))
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    selection = yaml.safe_load(SELECTION.read_text(encoding="utf-8"))
    navigation = yaml.safe_load(NAVIGATION.read_text(encoding="utf-8"))
    registry = Path(selection["registry_root"])
    entities = {e["id"]: e for path in (registry / "data" / "entities").glob("*/*.json")
                for e in [json.loads(path.read_text(encoding="utf-8"))]}
    all_categories = {cat for section in selection["sections"] for item in section["items"]
                      for cat in entities[item["registry_id"]].get("categories", [])
                      if entities[item["registry_id"]]["type"] not in MODEL_TYPES}
    missing = sorted(all_categories - CATEGORY_SECTION.keys())
    if missing:
        print(f"UNMAPPED CATEGORIES: {missing}")
        return 1
    problems = audit(selection, entities)
    for rid, source, allowed in problems:
        print(f"MISMATCH {rid}: {source} -> {allowed}")
    print(f"selected={sum(len(s['items']) for s in selection['sections'])} mismatches={len(problems)}")
    if not args.apply:
        return int(bool(problems))
    new_sections = {
        "creative-workflows": ("image-design", "Multimodal Creation"),
        "model-hubs": ("data-cloud", "Model Hubs & Communities"),
        "model-runtime-tools": ("data-cloud", "Model Runtime Tools"),
    }
    groups = {group["id"]: group for group in navigation["groups"]}
    known_sections = {s["id"] for group in navigation["groups"] for s in group["sections"]}
    for sid, (gid, title) in new_sections.items():
        if sid not in known_sections:
            groups[gid]["sections"].append({"id": sid, "title": title})
    if "tool-discovery" not in known_sections:
        navigation["groups"].append({"id": "discovery", "title": "Tool Discovery",
                                     "sections": [{"id": "tool-discovery", "title": "AI Tool Directories"}]})
    specs = {s["id"]: (group["id"], group["title"], s["title"])
             for group in navigation["groups"] for s in group["sections"]}
    sections = {s["id"]: s for s in selection["sections"]}
    for sid, (gid, gtitle, title) in specs.items():
        sections.setdefault(sid, {"id": sid, "title": title, "group_id": gid,
                                  "group_title": gtitle, "items": []})
    for rid, source, allowed in problems:
        if not allowed:
            raise SystemExit(f"no destination for {rid}")
        target = PREFERRED_SECTION.get(rid, allowed[0])
        item = next(item for item in sections[source]["items"] if item["registry_id"] == rid)
        sections[source]["items"].remove(item)
        sections[target]["items"].append(item)
        print(f"MOVE {rid}: {source} -> {target}")
    selection["sections"] = [sections[s["id"]] for group in navigation["groups"]
                             for s in group["sections"] if sections[s["id"]]["items"]]
    remaining = audit(selection, entities)
    if remaining:
        raise SystemExit(f"still mismatched: {remaining}")
    SELECTION.write_text(yaml.safe_dump(selection, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8", newline="\n")
    NAVIGATION.write_text(yaml.safe_dump(navigation, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8", newline="\n")
    print(f"applied={len(problems)} selected={sum(len(s['items']) for s in selection['sections'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
