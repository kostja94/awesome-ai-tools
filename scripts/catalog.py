from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import sys
import uuid
from collections import OrderedDict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

from section_guides import load_guides, validate_guides
from purpose_projection import audit as audit_purpose_projection
from zh_localization import description as zh_description, load_locale, validate_locale


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "selection.yaml"
DEFAULT_REGISTRY = Path(r"E:\data\ai-product-registry")
TEMP_RUNS = Path(r"E:\temp\runs")
ALLOWED_TYPES = {
    "product", "model-family", "model-version", "open-source-project"
}
DEFAULT_EXCLUDED_STATUSES = {"inactive", "shutdown", "acquired", "discontinued", "merged", "unknown"}

SECTION_RE = re.compile(r"^(#{2,3})\s+(.+?)\s*$")
ENTRY_RE = re.compile(r"^\s*-\s+(.*)$")


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def save_yaml(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(value, allow_unicode=True, sort_keys=False, width=120),
        encoding="utf-8",
        newline="\n",
    )


def load_entities(registry: Path) -> dict[str, dict]:
    entities: dict[str, dict] = {}
    for path in sorted((registry / "data" / "entities").glob("*/*.json")):
        entity = json.loads(path.read_text(encoding="utf-8"))
        entities[entity["id"]] = entity
    return entities


def load_mappings(registry: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted((registry / "data" / "mappings").glob("map-aat-*.json")):
        mapping = json.loads(path.read_text(encoding="utf-8"))
        if mapping.get("project") != "awesome-ai-tools" or mapping.get("status") != "mapped":
            continue
        ref = (mapping.get("project_ref") or {}).get("value")
        if ref:
            result[ref] = mapping["registry_entity"]
    return result


def parse_readme(path: Path) -> list[dict]:
    rows: list[dict] = []
    section = ""
    order_by_section: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        heading = SECTION_RE.match(line)
        if heading:
            title = heading.group(2).strip()
            if title not in {"Contents", "About", "Data Sources", "License", "Acknowledgments"}:
                section = title
            else:
                section = ""
            continue
        entry = ENTRY_RE.match(line)
        if not entry or not section:
            continue
        body = entry.group(1).strip()
        if body.startswith("[!") or body.startswith("!["):
            continue
        name, url, rest = parse_entry(body)
        if not name:
            continue
        order_by_section[section] = order_by_section.get(section, 0) + 1
        rows.append(
            {
                "ref": f"{section}#{html.unescape(name).strip()}",
                "section": section,
                "order": order_by_section[section],
                "name": html.unescape(name).strip(),
                "url": url.strip() if url else None,
                "legacy_text": re.sub(r"\s+", " ", rest or "").strip(),
            }
        )
    return rows


def parse_entry(body: str) -> tuple[str | None, str | None, str]:
    match = re.match(r'<a\s+href="([^"]+)"[^>]*>([^<]+)</a>(.*)$', body)
    if match:
        return html.unescape(match.group(2)).strip(), match.group(1).strip(), match.group(3)
    match = re.match(r"\[([^\]]+)\]\(([^)]+)\)(.*)$", body)
    if match:
        return match.group(1).strip(), match.group(2).strip(), match.group(3)
    match = re.match(r"(`[^`]+`|__[^_]+__|\*\*[^*]+\*\*|[A-Za-z0-9][^-(]{0,80}?)(\s*[-–—](?:\s*\(|\s)(.*))?$", body)
    if match:
        return match.group(1).strip("`_* "), None, match.group(3) or ""
    return None, None, body


def command_bootstrap(args: argparse.Namespace) -> int:
    registry = Path(args.registry)
    mappings = load_mappings(registry)
    entities = load_entities(registry)
    prior = load_yaml(CATALOG) if CATALOG.exists() else {}
    exclusions = prior.get("exclusions") or []
    excluded_refs = {row["ref"] for row in exclusions if row.get("ref")}
    prior_items: dict[str, tuple[dict, int, dict]] = {}
    for prior_section in prior.get("sections") or []:
        for index, item in enumerate(prior_section.get("items") or []):
            prior_items[item["registry_id"]] = (prior_section, index, item)
    rows = parse_readme(ROOT / "README.md")
    sections: OrderedDict[str, list[dict]] = OrderedDict()
    section_meta: dict[str, dict] = {}
    unresolved: list[dict] = []
    seen_ids: set[str] = set()

    for row in rows:
        if row["ref"] in excluded_refs:
            continue
        registry_id = mappings.get(row["ref"])
        if registry_id and registry_id in entities:
            entity = entities[registry_id]
            prior_item = prior_items.get(registry_id)
            if entity.get("status") in DEFAULT_EXCLUDED_STATUSES and not (
                prior_item and prior_item[2].get("include_inactive_reason")
            ):
                unresolved.append({**row, "registry_id": registry_id,
                                   "reason": f"Registry status requires editorial review: {entity.get('status')}"})
                continue
            if registry_id in seen_ids:
                unresolved.append({**row, "reason": f"duplicate registry_id: {registry_id}"})
                continue
            seen_ids.add(registry_id)
            destination = prior_item[0]["id"] if prior_item else slugify(row["section"])
            section_meta[destination] = prior_item[0] if prior_item else {"id": destination, "title": row["section"]}
            item = dict(prior_item[2]) if prior_item else {"registry_id": registry_id}
            sections.setdefault(destination, []).append(item)
        else:
            unresolved.append({**row, "reason": "no verified Registry mapping"})

    # Preserve curated selections that cannot be reconstructed from a unique README
    # reference (for example, the legacy README repeats the same label twice).
    for registry_id, (prior_section, _index, item) in prior_items.items():
        if registry_id not in seen_ids and registry_id in entities:
            destination = prior_section["id"]
            section_meta[destination] = prior_section
            sections.setdefault(destination, []).append(dict(item))
            seen_ids.add(registry_id)

    document = {
        "schema": prior.get("schema", "awesome-selection/v1"),
        "registry_root": registry.as_posix(),
        "generated_from": "README.md plus Registry map-aat-* mappings",
        "publish_ready": prior.get("publish_ready", False),
        "sections": [{**{k: v for k, v in section_meta[sid].items() if k != "items"}, "items": items}
                     for sid, items in sections.items()],
        "exclusions": exclusions,
        "unresolved": unresolved,
    }
    if CATALOG.exists() and not args.force:
        raise SystemExit(f"{CATALOG} already exists; pass --force to replace it")
    save_yaml(CATALOG, document)
    print(f"wrote {CATALOG}: {len(seen_ids)} selected, {len(unresolved)} unresolved")
    return 0


def slugify(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value or "section"


def validate(selection: dict, entities: dict[str, dict]) -> tuple[list[str], list[str], list[tuple[dict, dict]]]:
    errors: list[str] = []
    warnings: list[str] = []
    selected: list[tuple[dict, dict]] = []
    seen: dict[str, str] = {}
    errors.extend(validate_guides(load_guides(), selection))

    if selection.get("schema") not in {"awesome-selection/v1", "awesome-selection/v2"}:
        errors.append("selection schema must be awesome-selection/v1 or v2")
    for section in selection.get("sections") or []:
        title = section.get("title")
        if not title:
            errors.append("section missing title")
            continue
        if selection.get("schema") == "awesome-selection/v2" and not (section.get("group_id") and section.get("group_title")):
            errors.append(f"{title}: section missing group metadata")
        for item in section.get("items") or []:
            rid = item.get("registry_id")
            if not rid:
                errors.append(f"{title}: item missing registry_id")
                continue
            if rid in seen:
                errors.append(f"duplicate registry_id {rid!r} in {seen[rid]!r} and {title!r}")
                continue
            seen[rid] = title
            entity = entities.get(rid)
            if not entity:
                errors.append(f"{title}: unknown registry_id {rid!r}")
                continue
            if entity.get("type") not in ALLOWED_TYPES:
                errors.append(f"{title}: {rid} has non-display type {entity.get('type')!r}")
            if entity.get("status") in DEFAULT_EXCLUDED_STATUSES and not item.get("include_inactive_reason"):
                errors.append(f"{title}: {rid} status={entity.get('status')} requires include_inactive_reason")
            if not entity.get("websites"):
                warnings.append(f"{title}: {rid} has no website")
            description = entity.get("description")
            if not isinstance(description, str) or not description.strip():
                errors.append(f"{title}: {rid} requires an objective Registry description before publication")
            selected.append((section, entity))

    unresolved = selection.get("unresolved") or []
    if selection.get("schema") == "awesome-selection/v2":
        for rid, current, allowed in audit_purpose_projection(selection, entities):
            errors.append(f"{rid}: purpose/section mismatch {current} -> {allowed}")
    if unresolved:
        warnings.append(f"{len(unresolved)} unresolved legacy entries block publish")
    return errors, warnings, selected


def render_documents(selection: dict, selected: list[tuple[dict, dict]]) -> dict[str, str]:
    locale = load_locale()
    # Unreviewed legacy Chinese descriptions stay in catalog/zh.yaml as
    # candidates. They are never rendered; a link-only entry is safer than
    # asserting an obsolete fact or silently substituting English prose.
    locale_errors = validate_locale(selection, locale, strict=False)
    if locale_errors:
        raise ValueError(f"Chinese publication blocked: {len(locale_errors)} locale errors; first: {locale_errors[0]}")
    grouped: OrderedDict[tuple[str, str], list[dict]] = OrderedDict()
    guides = load_guides().get("sections", {})
    section_ids = {}
    section_group_ids = {}
    for section, entity in selected:
        grouped.setdefault((section.get("group_title", ""), section["title"]), []).append(entity)
        section_ids[(section.get("group_title", ""), section["title"])] = section["id"]
        section_group_ids[(section.get("group_title", ""), section["title"])] = section.get("group_id")

    def entry(entity: dict, *, chinese: bool = False) -> str:
        site = (entity.get("websites") or [""])[0]
        name = entity["name"]
        line = f'- <a href="{site}" target="_blank">{name}</a>' if site else f"- **{name}**"
        prose = zh_description(locale, entity["id"]) if chinese else entity.get("description")
        if prose:
            line += f" - {prose}"
        return line

    body = ['<a href="README.md" target="_blank">English</a> | <a href="README-CN.md" target="_blank">中文</a>', "", "# Awesome AI Tools", "", "> A curated selection backed by AI Product Registry facts.", "", "## Contents", ""]
    body_cn = ['<a href="README.md" target="_blank">English</a> | 中文', "", "# Awesome AI Tools", "", "> 由 AI Product Registry 客观事实驱动的精选 AI 工具目录。", "", "中文条目以名称和官网链接为主；仅在描述核实后展示中文说明。", "", "## 目录", ""]
    index = ["# Product Index", "", "Quick reference index of selected products.", "", "| Product | Category | Status |", "|---|---|---|"]
    seen_groups: set[str] = set()
    for group, title in grouped:
        sid = section_ids[(group, title)]
        gid = section_group_ids[(group, title)]
        if group and gid not in seen_groups:
            body.append(f"- [{group}](#group-{gid})")
            body_cn.append(f"- [{locale['groups'][gid]}](#group-{gid})")
            seen_groups.add(gid)
        indent = "  " if group else ""
        body.append(f"{indent}- [{title}](#section-{sid})")
        body_cn.append(f"{indent}- [{locale['sections'][sid]}](#section-{sid})")
    body.append("")
    body_cn.append("")
    last_group = None
    for (group, title), entities in grouped.items():
        if group and group != last_group:
            gid = section_group_ids[(group, title)]
            body += [f'<a id="group-{gid}"></a>', "", f"## {group}", ""]
            body_cn += [f'<a id="group-{gid}"></a>', "", f"## {locale['groups'][gid]}", ""]
        heading = "###" if group else "##"
        guide = guides.get(section_ids[(group, title)], {})
        sid = section_ids[(group, title)]
        body += [f'<a id="section-{sid}"></a>', "", f"{heading} {title}", ""]
        body_cn += [f'<a id="section-{sid}"></a>', "", f"{heading} {locale['sections'][sid]}", ""]
        if guide.get("en"):
            body += [guide["en"], ""]
        if guide.get("zh"):
            body_cn += [guide["zh"], ""]
        body += [entry(e) for e in entities] + [""]
        body_cn += [entry(e, chinese=True) for e in entities] + [""]
        last_group = group
        for entity in entities:
            site = (entity.get("websites") or [""])[0]
            name = f"[{entity['name']}]({site})" if site else entity["name"]
            index.append(f"| {name} | {title} | {entity.get('status', '')} |")
    body += [
        "---", "", "## About", "",
        "Curated and maintained by **[Kostja](https://alignify.co)**. Product facts are maintained in AI Product Registry; inclusion and placement are editorial choices for this list.", "",
        "Contributions are welcome through [GitHub Issues](https://github.com/kostja94/awesome-ai-tools/issues) or **zyjstc@gmail.com**.", "",
        "## License", "", "This project is licensed under the [MIT License](LICENSE).", "",
        "## Acknowledgments", "", "Thanks to contributors and the AI community for their support and feedback.", "",
    ]
    body_cn += [
        "---", "", "## 关于", "",
        "本目录由 **[Kostja](https://alignify.co)** 整理维护。产品事实在 AI Product Registry 中维护；本清单的收录与栏目位置属于编辑选择。", "",
        "欢迎通过 [GitHub Issues](https://github.com/kostja94/awesome-ai-tools/issues) 或 **zyjstc@gmail.com** 提交建议。", "",
        "## 许可证", "", "本项目采用 [MIT 许可证](LICENSE)。", "",
        "## 致谢", "", "感谢贡献者与 AI 社区的支持和反馈。", "",
    ]
    return {
        "README.md": "\n".join(body).rstrip() + "\n",
        "README-CN.md": "\n".join(body_cn).rstrip() + "\n",
        "INDEX.md": "\n".join(index).rstrip() + "\n",
    }


def create_temp_run(retention: str) -> tuple[Path, Path]:
    now = datetime.now(timezone(timedelta(hours=8)))
    name = f"{now:%Y%m%d-%H%M%S}-awesome-ai-tools-catalog-{uuid.uuid4().hex[:6]}"
    run_dir = TEMP_RUNS / name
    work_dir = run_dir / "work"
    work_dir.mkdir(parents=True, exist_ok=False)
    manifest = {
        "schema": "temp-run/v1",
        "created_at": now.isoformat(timespec="seconds"),
        "project": "awesome-ai-tools",
        "task": "catalog-render",
        "owner": "catalog.py",
        "status": "running",
        "retention": retention,
        "source_root": ROOT.as_posix(),
    }
    save_yaml(run_dir / "manifest.yaml", manifest)
    return run_dir, work_dir


def update_temp_status(run_dir: Path, status: str) -> None:
    manifest_path = run_dir / "manifest.yaml"
    manifest = load_yaml(manifest_path)
    manifest["status"] = status
    save_yaml(manifest_path, manifest)


def command_check(args: argparse.Namespace, render: bool = False, publish: bool = False) -> int:
    selection = load_yaml(CATALOG)
    registry = Path(args.registry or selection.get("registry_root") or DEFAULT_REGISTRY)
    entities = load_entities(registry)
    errors, warnings, selected = validate(selection, entities)
    for message in warnings:
        print(f"WARN  {message}")
    for message in errors:
        print(f"ERROR {message}")
    print(f"selected={len(selected)} unresolved={len(selection.get('unresolved') or [])} errors={len(errors)} warnings={len(warnings)}")
    if not (render or publish):
        locale_errors = validate_locale(selection, load_locale(), strict=True)
        print(f"chinese_publication_pending={len(locale_errors)}")
    if errors:
        return 1
    if publish and selection.get("publish_ready") is not True:
        print("ERROR publish blocked until catalog publish_ready is explicitly true")
        return 1
    if publish and selection.get("unresolved"):
        print("ERROR publish blocked until unresolved is empty")
        return 1
    if render or publish:
        locale_errors = validate_locale(selection, load_locale(), strict=False)
        if locale_errors:
            for message in locale_errors[:10]:
                print(f"ERROR {message}")
            print(f"ERROR Chinese publication blocked: {len(locale_errors)} locale errors")
            return 1
        docs = render_documents(selection, selected)
        run_dir, work_dir = create_temp_run("delete-on-success" if publish else "delete-daily")
        for name, text in docs.items():
            (work_dir / name).write_text(text, encoding="utf-8", newline="\n")
        update_temp_status(run_dir, "completed")
        print(f"rendered preview to {work_dir}")
        if publish:
            for name in docs:
                shutil.copyfile(work_dir / name, ROOT / name)
            shutil.rmtree(run_dir)
            print("published README.md, README-CN.md and INDEX.md")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Awesome AI Tools as a curated Registry projection")
    parser.add_argument("command", choices=("bootstrap", "check", "render", "publish"))
    parser.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    if args.command == "bootstrap":
        return command_bootstrap(args)
    return command_check(args, render=args.command in {"render", "publish"}, publish=args.command == "publish")


if __name__ == "__main__":
    sys.exit(main())
