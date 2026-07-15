from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RedesignSourceContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = (ROOT / "index.md").read_text(encoding="utf-8")
        cls.project = (ROOT / "_includes/project-entry.html").read_text(
            encoding="utf-8"
        )
        cls.layout = (ROOT / "_layouts/default.html").read_text(encoding="utf-8")
        cls.nav = (ROOT / "_data/navigation.yml").read_text(encoding="utf-8")

    def test_section_structure(self):
        for section_id in ("about", "selected-work", "research", "experience"):
            self.assertIn(f'id="{section_id}"', self.index)
        self.assertNotIn('id="education"', self.index)

    def test_research_narrative(self):
        self.assertIn("Memory × Reasoning × Embodied AI", self.index)
        self.assertIn("Systems that help agents", self.index)
        self.assertIn("remember, reason, and act.", self.index)
        self.assertIn("site.data.projects", self.index)
        self.assertIn("Questions I care about", self.index)

    def test_project_component(self):
        self.assertIn("include.project", self.project)
        self.assertIn(
            "project-visual--{{ include.project.diagram }}", self.project
        )
        self.assertIn("include.project.contributions", self.project)

    def test_navigation_and_footer(self):
        self.assertIn('url: "/#research"', self.nav)
        self.assertNotIn('url: "/#education"', self.nav)
        self.assertIn("Codex", self.layout)
        self.assertIn("Claude Code", self.layout)
        self.assertIn("Cursor", self.layout)

    def test_experience_boundary(self):
        self.assertIn("Nuanwa Technology", self.index)
        self.assertIn("Uceng Intelligence", self.index)
        self.assertNotIn("Fanhan", self.index)


if __name__ == "__main__":
    unittest.main()
