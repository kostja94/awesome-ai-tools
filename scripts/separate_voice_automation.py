"""One-time editorial migration of legacy 'Voice Agents' to purpose sections.

The legacy source mixed builders, telephony, evaluation and sector applications.
Agent identity is an evidence trait in Registry, not inferred from that heading.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SELECTION = ROOT / "catalog" / "selection.yaml"
NAVIGATION = ROOT / "catalog" / "navigation.yaml"
TARGETS = {
    "agent-platforms": "thoughtly bland-ai boost-ai rasa syllable synthflow trillet ada kore-ai happyrobot livekit",
    "agent-evaluation": "hamming coval",
    "speech-applications": "daily cresta marr-labs goodcall canonical-ai",
    "customer-service": "replicant voctiv",
    "finance-accounting": "skit-ai kastle-ai aviary-ai",
    "industry-operations": "liberate toma numa kea voiceplug hi-auto loman-ai slang-ai fleetworks sameday-ai avoca",
    "healthcare": "hippocratic-ai standard-practice hello-patient super-dial arini hyro infinitus assort-health clarion health-harbor",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    selection = yaml.safe_load(SELECTION.read_text(encoding="utf-8"))
    navigation = yaml.safe_load(NAVIGATION.read_text(encoding="utf-8"))
    sections = {s["id"]: s for s in selection["sections"]}
    source = sections["voice-agents"]
    current = {i["registry_id"]: i for i in source["items"]}
    route = {rid: target for target, ids in TARGETS.items() for rid in ids.split()}
    if set(route) != set(current):
        raise SystemExit(f"voice coverage mismatch: missing={sorted(set(current)-set(route))}, extra={sorted(set(route)-set(current))}")
    for rid, item in current.items():
        sections[route[rid]]["items"].append(item)
        print(f"MOVE {rid}: voice-agents -> {route[rid]}")
    selection["sections"] = [s for s in selection["sections"] if s["id"] != "voice-agents"]
    for group in navigation["groups"]:
        if group["id"] == "agents":
            group["title"] = "Agent Development Infrastructure"
        group["sections"] = [s for s in group["sections"] if s["id"] != "voice-agents"]
        for s in group["sections"]:
            if s["id"] == "agent-platforms":
                s["title"] = "Agent Frameworks & Infrastructure"
    for s in selection["sections"]:
        if s["group_id"] == "agents":
            s["group_title"] = "Agent Development Infrastructure"
        if s["id"] == "agent-platforms":
            s["title"] = "Agent Frameworks & Infrastructure"
    print(f"moved={len(current)} selected={sum(len(s['items']) for s in selection['sections'])}")
    if args.apply:
        SELECTION.write_text(yaml.safe_dump(selection, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8", newline="\n")
        NAVIGATION.write_text(yaml.safe_dump(navigation, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
