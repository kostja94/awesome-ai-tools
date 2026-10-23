"""Remove organization identities from the published-product selection.

Registry keeps the company records and their relations. This script changes only
the editorial selection; it does not delete factual Registry identities.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SELECTION = ROOT / "catalog" / "selection.yaml"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    selection = yaml.safe_load(SELECTION.read_text(encoding="utf-8"))
    registry = Path(selection["registry_root"])
    types = {
        item["id"]: item["type"]
        for path in (registry / "data" / "entities").glob("*/*.json")
        for item in [json.loads(path.read_text(encoding="utf-8"))]
    }
    removed = []
    for section in selection["sections"]:
        kept = []
        for item in section["items"]:
            rid = item["registry_id"]
            if types.get(rid) == "organization":
                removed.append((section["id"], rid))
            else:
                kept.append(item)
        section["items"] = kept
    selection["sections"] = [section for section in selection["sections"] if section["items"]]
    for section, rid in removed:
        print(f"REMOVE {section}: {rid}")
    print(f"organizations_removed={len(removed)} selected={sum(len(s['items']) for s in selection['sections'])}")
    if args.apply:
        SELECTION.write_text(yaml.safe_dump(selection, allow_unicode=True, sort_keys=False, width=120),
                             encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
