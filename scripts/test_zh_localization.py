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


if __name__ == "__main__":
    unittest.main()
