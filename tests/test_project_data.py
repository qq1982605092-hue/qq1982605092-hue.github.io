from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "_data/projects.yml"


class ProjectDataContract(unittest.TestCase):
    def setUp(self):
        self.assertTrue(PROJECTS.is_file(), "_data/projects.yml must exist")
        self.source = PROJECTS.read_text(encoding="utf-8")

    def test_exact_project_order(self):
        titles = re.findall(r'^\s{2}title: "([^"]+)"$', self.source, re.MULTILINE)
        self.assertEqual(
            titles,
            [
                "Dual-Time Agent Memory",
                "Strategy-Driven AI Calling Agent",
                "Qwen3 Reranker Fine-tuning",
                "Multimodal Structured Perception",
            ],
        )

    def test_required_fields_and_two_contributions(self):
        records = re.split(r"(?m)^- id: ", self.source)[1:]
        self.assertEqual(len(records), 4)
        for record in records:
            for field in ("number:", "label:", "title:", "diagram:", "question:"):
                self.assertIn(field, record)
            self.assertEqual(len(re.findall(r'^\s{4}- "', record, re.MULTILINE)), 2)

    def test_forbidden_content(self):
        for text in (
            "Fanhan",
            "SOTA",
            "state-of-the-art",
            "100%",
            "99.1%",
            "21.1%",
            "34/34",
            "Code coming soon",
        ):
            self.assertNotIn(text, self.source)


if __name__ == "__main__":
    unittest.main()
