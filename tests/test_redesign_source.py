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
        cls.scss = (ROOT / "_sass/_site.scss").read_text(encoding="utf-8")
        cls.head = (ROOT / "_includes/head.html").read_text(encoding="utf-8")

    def test_section_structure(self):
        for section_id in ("about", "selected-work", "research", "experience"):
            self.assertIn(f'id="{section_id}"', self.index)
        self.assertNotIn('id="education"', self.index)

    def test_research_narrative(self):
        self.assertIn("MEMORY · AGENTS · EMBODIED AI", self.index)
        self.assertIn("Cheng Shu", self.index)
        self.assertNotIn("Shu Cheng", self.index)
        self.assertIn("memory and reasoning systems for long-horizon agents", self.index)
        self.assertIn("site.data.projects", self.index)
        self.assertIn("Questions I care about", self.index)

    def test_project_component(self):
        self.assertIn("include.project", self.project)
        self.assertIn(
            "project-visual--{{ include.project.diagram }}", self.project
        )
        self.assertIn("include.project.contributions", self.project)
        self.assertIn(
            "include.project.links and include.project.links != empty", self.project
        )
        self.assertIn("unless include.project.diagram", self.project)

    def test_navigation_and_footer(self):
        self.assertIn('url: "/#research"', self.nav)
        self.assertNotIn('url: "/#education"', self.nav)
        self.assertIn("Codex", self.layout)
        self.assertIn("Claude Code", self.layout)
        self.assertIn("Cursor", self.layout)

    def test_favicon_is_declared_and_present(self):
        self.assertIn('rel="icon"', self.head)
        self.assertTrue((ROOT / "assets/images/favicon.svg").is_file())

    def test_experience_boundary(self):
        self.assertIn("Nuanwa Technology", self.index)
        self.assertIn("Uceng Intelligence", self.index)
        self.assertNotIn("Fanhan", self.index)

    def test_visual_components_have_explicit_styles(self):
        for selector in (
            ".hero",
            ".project-entry",
            ".project-visual",
            ".project-visual--memory",
            ".project-visual--agent",
            ".project-visual--ranking",
            ".project-visual--perception",
            ".question-grid",
            ".experience-focus",
        ):
            self.assertIn(selector, self.scss)

    def test_mobile_and_motion_boundaries(self):
        self.assertIn("@media (max-width: 760px)", self.scss)
        self.assertIn("@media (prefers-reduced-motion: reduce)", self.scss)
        self.assertIn("overflow-wrap: anywhere", self.scss)
        self.assertIn("min-height: 44px", self.scss)
        self.assertIn(".hero-links a", self.scss)
        self.assertIn(".project-entry--text-only", self.scss)


if __name__ == "__main__":
    unittest.main()
