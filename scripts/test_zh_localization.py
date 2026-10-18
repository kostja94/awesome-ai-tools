import unittest

from zh_localization import description, load_locale, validate_locale


class ChineseLocalizationTests(unittest.TestCase):
    def setUp(self):
        self.selection = {"sections": [{"id": "language-models", "group_id": "models",
                                      "items": [{"registry_id": "sample"}]}]}
        self.locale = {"schema": "awesome-zh/v1", "groups": {"models": "模型"},
                       "sections": {"language-models": "语言模型"}, "descriptions": {}}

    def test_untranslated_entry_blocks_publication(self):
        self.assertIn("Chinese description requires review: sample",
                      validate_locale(self.selection, self.locale, strict=True))
        self.assertIsNone(description(self.locale, "sample"))

    def test_legacy_candidate_is_not_published(self):
        self.locale["descriptions"]["sample"] = {
            "status": "candidate", "text": "旧的中文介绍", "source": "legacy README-CN.md"}
        self.assertIn("Chinese description requires review: sample",
                      validate_locale(self.selection, self.locale, strict=True))
        self.assertIsNone(description(self.locale, "sample"))

    def test_approved_provenance_required(self):
        self.locale["descriptions"]["sample"] = {"status": "approved", "text": "经过核实的介绍"}
        self.assertIn("Chinese description lacks provenance: sample",
                      validate_locale(self.selection, self.locale, strict=True))
        self.locale["descriptions"]["sample"]["source"] = "legacy README-CN.md; requires current-fact review"
        self.assertIn("Chinese description still cites unreviewed legacy copy: sample",
                      validate_locale(self.selection, self.locale, strict=True))
        self.locale["descriptions"]["sample"]["source"] = "Registry source review"
        self.assertEqual(validate_locale(self.selection, self.locale, strict=True), [])
        self.assertEqual(description(self.locale, "sample"), "经过核实的介绍")

    def test_full_selection_has_localized_titles(self):
        from catalog import CATALOG, load_yaml
        selection = load_yaml(CATALOG)
        errors = validate_locale(selection, load_locale(), strict=False)
        self.assertFalse([error for error in errors if "title missing" in error], errors[:10])

    def test_candidate_renders_link_only_without_becoming_a_fact(self):
        from unittest.mock import patch
        import catalog

        selection = {"sections": [{"id": "language-models", "title": "Language Models",
                                  "group_id": "models", "group_title": "Models",
                                  "items": [{"registry_id": "sample"}]}]}
        entity = {"id": "sample", "name": "Sample", "status": "active",
                  "websites": ["https://example.com"], "description": "Current English fact."}
        self.locale["descriptions"]["sample"] = {
            "status": "candidate", "text": "未经核实的旧事实", "source": "legacy README-CN.md"}
        with patch.object(catalog, "load_locale", return_value=self.locale), \
             patch.object(catalog, "load_guides", return_value={"sections": {}}):
            docs = catalog.render_documents(selection, [(selection["sections"][0], entity)])
        chinese = docs["README-CN.md"]
        self.assertIn('href="https://example.com"', chinese)
        self.assertNotIn("未经核实的旧事实", chinese)
        self.assertNotIn("Current English fact.", chinese)
        self.assertIn("[语言模型](#section-language-models)", chinese)
        self.assertIn('id="section-language-models"', chinese)
        self.assertIn("Current English fact.", docs["README.md"])

    def test_full_render_has_matching_items_and_section_anchors(self):
        import catalog

        selection = catalog.load_yaml(catalog.CATALOG)
        entities = catalog.load_entities(catalog.DEFAULT_REGISTRY)
        errors, _, selected = catalog.validate(selection, entities)
        self.assertEqual(errors, [])
        docs = catalog.render_documents(selection, selected)
        for name in ("README.md", "README-CN.md"):
            lines = docs[name].splitlines()
            self.assertEqual(sum(line.startswith('- <a href="') for line in lines), len(selected))
            for section in selection["sections"]:
                sid = section["id"]
                self.assertEqual(docs[name].count(f'id="section-{sid}"'), 1)
                self.assertEqual(docs[name].count(f'](#section-{sid})'), 1)
        self.assertEqual(len(docs["INDEX.md"].splitlines()) - 6, len(selected))


if __name__ == "__main__":
    unittest.main()
