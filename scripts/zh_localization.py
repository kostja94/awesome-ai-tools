"""Checked Chinese projection of the Registry-backed catalogue.

Legacy Chinese prose is an editorial candidate, not a verified Registry fact.
It must be reviewed against the current entity before status becomes approved.
"""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
LOCALE = ROOT / "catalog" / "zh.yaml"


def load_locale(path: Path = LOCALE) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def validate_locale(selection: dict, locale: dict, *, strict: bool = False) -> list[str]:
    errors: list[str] = []
    if locale.get("schema") != "awesome-zh/v1":
        errors.append("Chinese locale schema must be awesome-zh/v1")
    groups = locale.get("groups") or {}
    sections = locale.get("sections") or {}
    descriptions = locale.get("descriptions") or {}
    used_ids = set()
    for section in selection.get("sections") or []:
        sid = section["id"]
        gid = section.get("group_id")
        if not sections.get(sid):
            errors.append(f"Chinese section title missing: {sid}")
        if gid and not groups.get(gid):
            errors.append(f"Chinese group title missing: {gid}")
        for item in section.get("items") or []:
            rid = item["registry_id"]
            used_ids.add(rid)
            row = descriptions.get(rid)
            if not strict:
                continue
            if not isinstance(row, dict) or row.get("status") != "approved":
                errors.append(f"Chinese description requires review: {rid}")
            elif not isinstance(row.get("text"), str) or not row["text"].strip():
                errors.append(f"Chinese description empty: {rid}")
            elif not row.get("source"):
                errors.append(f"Chinese description lacks provenance: {rid}")
            elif "requires current-fact review" in str(row["source"]):
                errors.append(f"Chinese description still cites unreviewed legacy copy: {rid}")
    for rid, row in descriptions.items():
        if rid not in used_ids:
            errors.append(f"Orphan Chinese description: {rid}")
        elif not isinstance(row, dict) or row.get("status") not in {"candidate", "approved"}:
            errors.append(f"Invalid Chinese description status: {rid}")
    return errors


def description(locale: dict, rid: str) -> str | None:
    row = (locale.get("descriptions") or {}).get(rid)
    if isinstance(row, dict) and row.get("status") == "approved":
        return row.get("text")
    return None
