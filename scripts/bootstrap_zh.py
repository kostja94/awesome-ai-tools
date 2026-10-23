"""Harvest legacy Chinese prose as unapproved localization candidates.

No candidate is automatically treated as a current fact or published.
"""

from __future__ import annotations

import re
from collections import defaultdict

import yaml

from catalog import CATALOG, DEFAULT_REGISTRY, ROOT, load_mappings, load_yaml, parse_readme
from zh_localization import LOCALE


def legacy_prose(raw: str) -> str | None:
    match = re.search(r"\s[-–—]\s(.+)$", raw)
    if not match:
        return None
    prose = match.group(1).strip()
    return prose if re.search(r"[\u3400-\u9fff]", prose) else None


def main() -> None:
    selection = load_yaml(CATALOG)
    locale = load_yaml(LOCALE)
    selected_ids = {item["registry_id"] for sec in selection["sections"] for item in sec.get("items") or []}
    mappings = load_mappings(DEFAULT_REGISTRY)
    english = {row["ref"]: row for row in parse_readme(ROOT / "README.md")}
    chinese = parse_readme(ROOT / "README-CN.md")
    by_name = defaultdict(list)
    for row in chinese:
        if legacy_prose(row["legacy_text"]):
            by_name[row["name"].casefold()].append(row)
    candidates: dict[str, dict] = {}
    for ref, rid in mappings.items():
        if rid not in selected_ids or ref not in english:
            continue
        en = english[ref]
        matches = by_name.get(en["name"].casefold(), [])
        if len(matches) > 1:
            matches = [row for row in matches if row["url"] == en["url"]]
        if len(matches) != 1:
            continue
        prose = legacy_prose(matches[0]["legacy_text"])
        if prose and rid not in candidates:
            candidates[rid] = {"status": "candidate", "text": prose,
                               "source": "legacy README-CN.md; requires current-fact review"}
    existing = locale.get("descriptions") or {}
    existing.update({rid: row for rid, row in candidates.items() if rid not in existing})
    locale["descriptions"] = dict(sorted(existing.items()))
    LOCALE.write_text(yaml.safe_dump(locale, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8", newline="\n")
    print(f"selected={len(selected_ids)} legacy_candidates={len(candidates)} localized_rows={len(existing)}")


if __name__ == "__main__":
    main()
