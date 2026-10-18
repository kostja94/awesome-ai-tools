"""Rebuild the editorial selection's navigation from the reviewed crosswalk."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SELECTION = ROOT / "catalog" / "selection.yaml"
NAVIGATION = ROOT / "catalog" / "navigation.yaml"
MODEL_TYPES = {"model-family", "model-version"}
MODEL_CATEGORIES = {
    "image-generation": "image-models",
    "video-generation": "video-models",
    "speech-models": "speech-models",
    "music-generation": "music-models",
    "text-to-3d": "spatial-models",
    "image-to-3d": "spatial-models",
    "llm": "language-models",
    "llm-web-dev": "language-models",
    "llm-search": "language-models",
}


def read_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def load_entities(registry: Path) -> dict[str, dict]:
    return {
        entity["id"]: entity
        for path in (registry / "data" / "entities").glob("*/*.json")
        for entity in [json.loads(path.read_text(encoding="utf-8"))]
    }


def migrate(selection: dict, navigation: dict, entities: dict[str, dict]) -> tuple[dict, list[str]]:
    errors: list[str] = []
    old_sections = selection.get("sections") or []
    source_ids = [section["id"] for section in old_sections]
    if len(source_ids) != len(set(source_ids)):
        errors.append("duplicate source section ID")

    destinations: dict[str, dict] = {}
    source_map: dict[str, str] = {}
    ordered: list[dict] = []
    group_ids: set[str] = set()
    for group in navigation.get("groups") or []:
        if group["id"] in group_ids:
            errors.append(f"duplicate group ID: {group['id']}")
        group_ids.add(group["id"])
        for section in group.get("sections") or []:
            sid = section["id"]
            if sid in destinations:
                errors.append(f"duplicate destination section ID: {sid}")
            target = {"id": sid, "title": section["title"], "group_id": group["id"],
                      "group_title": group["title"], "items": []}
            destinations[sid] = target
            ordered.append(target)
            for source in section.get("sources") or []:
                if source in source_map:
                    errors.append(f"duplicate source mapping: {source}")
                source_map[source] = sid
    if set(source_ids) != set(source_map):
        errors.append(f"source coverage mismatch: missing={sorted(set(source_ids)-set(source_map))}, "
                      f"extra={sorted(set(source_map)-set(source_ids))}")

    seen: set[str] = set()
    for section in old_sections:
        for item in section.get("items") or []:
            rid = item.get("registry_id")
            if rid in seen:
                errors.append(f"duplicate selected entity: {rid}")
                continue
            seen.add(rid)
            entity = entities.get(rid)
            if entity is None:
                errors.append(f"unknown Registry entity: {rid}")
                continue
            if entity.get("type") in MODEL_TYPES:
                candidates = {MODEL_CATEGORIES[category] for category in entity.get("categories") or []
                              if category in MODEL_CATEGORIES}
                if len(candidates) != 1:
                    errors.append(f"uncertain model classification: {rid} categories={entity.get('categories')}")
                    continue
                destination = candidates.pop()
            else:
                destination = source_map.get(section["id"])
            if destination not in destinations:
                errors.append(f"no destination for {rid} from {section['id']}")
                continue
            destinations[destination]["items"].append(dict(item))

    output = dict(selection)
    output["schema"] = "awesome-selection/v2"
    output["sections"] = [section for section in ordered if section["items"]]
    output["generated_from"] = "Registry facts plus catalog/navigation.yaml editorial crosswalk"
    return output, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    selection = read_yaml(SELECTION)
    navigation = read_yaml(NAVIGATION)
    entities = load_entities(Path(selection["registry_root"]))
    if selection.get("schema") == "awesome-selection/v2":
        expected = {section["id"]: (group["id"], group["title"], section["title"])
                    for group in navigation.get("groups") or [] for section in group.get("sections") or []}
        seen: set[str] = set()
        errors: list[str] = []
        for section in selection.get("sections") or []:
            sid = section["id"]
            if expected.get(sid) != (section.get("group_id"), section.get("group_title"), section.get("title")):
                errors.append(f"navigation mismatch: {sid}")
            for item in section.get("items") or []:
                rid = item["registry_id"]
                if rid in seen or rid not in entities:
                    errors.append(f"duplicate or unknown entity: {rid}")
                seen.add(rid)
                if rid in entities and entities[rid].get("type") in MODEL_TYPES and section.get("group_id") != "models":
                    errors.append(f"model outside Models: {rid}")
        for error in errors:
            print(f"ERROR {error}")
        print(f"destination_sections={len(selection.get('sections') or [])} selected={len(seen)} errors={len(errors)}")
        return bool(errors)
    output, errors = migrate(selection, navigation, entities)
    for error in errors:
        print(f"ERROR {error}")
    print(f"source_sections={len(selection.get('sections') or [])} "
          f"destination_sections={len(output['sections'])} "
          f"selected={sum(len(section['items']) for section in output['sections'])} "
          f"errors={len(errors)}")
    if errors:
        return 1
    if args.apply:
        SELECTION.write_text(yaml.safe_dump(output, allow_unicode=True, sort_keys=False, width=120),
                             encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
