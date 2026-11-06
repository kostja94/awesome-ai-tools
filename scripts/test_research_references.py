import unittest
from unittest.mock import patch
import catalog

class ResearchReferenceTests(unittest.TestCase):
    def run_check(self, reference=True, evidence=True):
        entity = {"id": "chatgpt", "type": "product", "status": "active", "name": "ChatGPT", "description": "Conversational application.", "websites": ["https://chatgpt.com"], "categories": ["chat-assistant"], "facts": [{"field": "operating-model", "value": "Deep research workflow", "sources": ["src-official"]}] if evidence else []}
        selection = {"schema": "awesome-selection/v2", "sections": [{"id": "chat-social", "title": "Chat", "group_id": "chat", "group_title": "Chat", "items": [{"registry_id": "chatgpt"}]}, {"id": "deep-research-applications", "title": "Research", "group_id": "research", "group_title": "Research", "items": [{"registry_id": "chatgpt", "reference_only": reference}]}]}
        with patch.object(catalog, "load_guides", return_value={"schema": "awesome-section-guides/v1", "sections": {}}):
            return catalog.validate(selection, {"chatgpt": entity})

    def test_evidenced_research_reference_preserves_identity(self):
        errors, _, selected = self.run_check()
        self.assertEqual(errors, [])
        self.assertEqual([entity["id"] for _, entity in selected], ["chatgpt", "chatgpt"])

    def test_unmarked_duplicate_stays_blocked(self):
        self.assertTrue(any("duplicate registry_id" in x for x in self.run_check(reference=False)[0]))

    def test_unsourced_research_reference_stays_blocked(self):
        self.assertTrue(any("lacks sourced" in x for x in self.run_check(evidence=False)[0]))
