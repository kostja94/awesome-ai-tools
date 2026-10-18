import copy
import unittest
from unittest.mock import patch

import catalog
from section_guides import load_guides, validate_guides


class SectionGuideTests(unittest.TestCase):
    def setUp(self):
        self.selection = {"sections": [{"id": "language-models", "title": "Language Models",
                                        "items": [{"registry_id": "example-0"}]},
                                       {"id": "unlinked", "title": "No Guide",
                                        "items": [{"registry_id": "example-1"}]}]}
        self.guides = {"schema": "awesome-section-guides/v1", "sections": {
            "language-models": copy.deepcopy(load_guides()["sections"]["language-models"])}}

    def render(self, guides):
        selected = [(s, {"id": f"example-{i}", "name": "Example", "websites": ["https://example.com"]})
                    for i, s in enumerate(self.selection["sections"])]
        locale = {"schema": "awesome-zh/v1", "groups": {},
                  "sections": {"language-models": "语言模型", "unlinked": "无引导"},
                  "descriptions": {f"example-{i}": {"status": "approved", "text": "示例说明", "source": "test"}
                                   for i in range(2)}}
        with patch.object(catalog, "load_guides", return_value=guides), patch.object(catalog, "load_locale", return_value=locale):
            return catalog.render_documents(self.selection, selected)

    def test_languages_and_unmapped_section(self):
        self.assertEqual([], validate_guides(self.guides, self.selection))
        docs = self.render(self.guides)
        self.assertIn("https://alignify.co/tools/llm", docs["README.md"])
        self.assertNotIn("https://alignify.co/zh/", docs["README.md"])
        self.assertIn("https://alignify.co/zh/tools/llm", docs["README-CN.md"])
        self.assertNotIn("https://alignify.co/tools/", docs["README-CN.md"])
        self.assertNotIn("alignify.co", docs["INDEX.md"])
        self.assertNotIn("alignify.co", docs["README.md"].split("## No Guide")[1])

    def test_no_cross_language_fallback(self):
        del self.guides["sections"]["language-models"]["zh"]
        self.assertNotIn("alignify.co", self.render(self.guides)["README-CN.md"])

    def test_wrong_language_rejected(self):
        self.guides["sections"]["language-models"]["zh"] = self.guides["sections"]["language-models"]["en"]
        self.assertTrue(validate_guides(self.guides, self.selection))

    def test_orphan_rejected(self):
        self.selection["sections"][0]["id"] = "renamed"
        self.assertTrue(validate_guides(self.guides, self.selection))

    def test_generic_anchor_rejected(self):
        self.guides["sections"]["language-models"]["en"] = "[click here](https://alignify.co/tools/llm)"
        self.assertTrue(validate_guides(self.guides, self.selection))

    def test_deterministic_without_mutation(self):
        before = copy.deepcopy(self.guides)
        self.assertEqual(self.render(self.guides), self.render(self.guides))
        self.assertEqual(before, self.guides)

    def test_missing_description_blocks_catalog(self):
        selection = {"schema": "awesome-selection/v1", "sections": [
            {"id": "sample", "title": "Sample", "items": [{"registry_id": "example"}]}]}
        entity = {"id": "example", "type": "product", "name": "Example", "status": "active",
                  "websites": ["https://example.com"]}
        with patch.object(catalog, "load_guides", return_value={"schema": "awesome-section-guides/v1", "sections": {}}):
            for description in (None, "", "   "):
                entity["description"] = description
                errors, _, _ = catalog.validate(selection, {"example": entity})
                self.assertTrue(any("description" in e for e in errors))
            entity["description"] = "A document editing application."
            self.assertEqual([], catalog.validate(selection, {"example": entity})[0])


if __name__ == "__main__":
    unittest.main()
