from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class CompactHeroContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = (ROOT / "index.md").read_text(encoding="utf-8")
        cls.profile = (ROOT / "_includes/author-profile.html").read_text(
            encoding="utf-8"
        )
        cls.scss = (ROOT / "_sass/_site.scss").read_text(encoding="utf-8")

    def test_compact_research_hierarchy(self):
        for text in (
            "MEMORY · AGENTS · EMBODIED AI",
            "Cheng Shu",
            "Agent memory · model post-training · multimodal systems",
        ):
            self.assertIn(text, self.index)
        self.assertNotIn("Shu Cheng", self.index)
        self.assertNotIn("舒橙", self.index)
        self.assertNotIn("Systems that help agents", self.index)
        self.assertNotIn("site.author.title", self.profile)
        self.assertNotIn("site.author.affiliation", self.profile)
        self.assertNotIn("site.author.location", self.profile)

    def test_required_layout_and_accessibility_hooks(self):
        for selector in (
            ".hero-name",
            ".hero-topics",
            ".hero-statement",
            ".hero-portrait",
        ):
            self.assertIn(selector, self.scss)
        self.assertNotIn(".hero-name-local", self.scss)
        self.assertIn("max-width: 270px", self.scss)
        self.assertIn("@media (max-width: 960px)", self.scss)
        self.assertIn("prefers-reduced-motion: reduce", self.scss)


if __name__ == "__main__":
    unittest.main()
