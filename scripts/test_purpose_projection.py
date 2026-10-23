import json
import unittest
from pathlib import Path

import yaml

from purpose_projection import ROOT, SELECTION, audit, allowed_sections


class PurposeProjectionTests(unittest.TestCase):
    def test_selected_items_match_registry_purpose(self):
        selection = yaml.safe_load(SELECTION.read_text(encoding="utf-8"))
        registry = Path(selection["registry_root"])
        entities = {item["id"]: item for path in (registry / "data" / "entities").glob("*/*.json")
                    for item in [json.loads(path.read_text(encoding="utf-8"))]}
        self.assertEqual(audit(selection, entities), [])

    def test_pure_organization_has_no_display_purpose(self):
        self.assertEqual(allowed_sections({"type": "organization", "categories": []}), set())

    def test_model_sections_are_modality_specific(self):
        self.assertEqual(allowed_sections({"type": "model-family", "categories": ["speech-models"]}),
                         {"speech-models"})


if __name__ == "__main__":
    unittest.main()
