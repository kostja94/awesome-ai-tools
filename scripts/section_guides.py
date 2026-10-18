"""Editorial section reading links; never copied into Registry entity facts."""
from pathlib import Path
import re
from urllib.parse import urlsplit

import yaml

GUIDES = Path(__file__).resolve().parents[1] / "catalog" / "section-guides.yaml"
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def load_guides():
    return yaml.safe_load(GUIDES.read_text(encoding="utf-8")) or {}


def validate_guides(document, selection):
    errors = []
    if document.get("schema") != "awesome-section-guides/v1":
        errors.append("invalid section-guides schema")
    sections = document.get("sections")
    if not isinstance(sections, dict):
        return errors + ["section-guides sections must be a mapping"]
    known = {section["id"] for section in selection.get("sections", [])}
    for sid, locales in sections.items():
        if sid not in known:
            errors.append(f"section guide has unknown section ID: {sid}; remap or remove explicitly")
        if not isinstance(locales, dict):
            errors.append(f"{sid}: guide must be a locale mapping")
            continue
        for locale, paragraph in locales.items():
            if locale not in {"en", "zh"} or not isinstance(paragraph, str):
                errors.append(f"{sid}: invalid guide locale/text {locale}")
                continue
            links = LINK.findall(paragraph)
            if not links or len(links) > 2 or "\n" in paragraph:
                errors.append(f"{sid}/{locale}: use one paragraph with one or two contextual links")
            for anchor, url in links:
                parsed = urlsplit(url)
                prefix = "/zh/" if locale == "zh" else "/"
                path = parsed.path[len(prefix):] if parsed.path.startswith(prefix) else ""
                if (parsed.scheme != "https" or parsed.netloc != "alignify.co"
                        or not re.fullmatch(r"(?:tools|blog)/[a-z0-9-]+", path)
                        or parsed.query or parsed.fragment):
                    errors.append(f"{sid}/{locale}: invalid or wrong-language article URL: {url}")
                if anchor.strip().lower() in {"click here", "visit", "read more", "点击这里", "请访问", "了解更多"}:
                    errors.append(f"{sid}/{locale}: anchor must describe the article topic")
    return errors
