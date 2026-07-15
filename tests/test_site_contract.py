from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class HomepageContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        output = ROOT / "_site/index.html"
        if not output.is_file():
            raise unittest.SkipTest("_site/index.html requires a successful Jekyll build")
        cls.html = output.read_text(encoding="utf-8")

    def test_identity_and_thesis(self):
        for text in (
            "Shu Cheng",
            "舒橙",
            "Memory × Reasoning × Embodied AI",
            "Systems that help agents",
            "remember, reason, and act.",
        ):
            self.assertIn(text, self.html)

    def test_sections(self):
        for section_id in ("about", "selected-work", "research", "experience"):
            self.assertIn(f'id="{section_id}"', self.html)
        self.assertNotIn('id="education"', self.html)

    def test_projects_render_once(self):
        for title in (
            "Dual-Time Agent Memory",
            "State-Driven AI Calling Agent",
            "Qwen3 Reranker Fine-tuning",
            "Multimodal Structured Perception",
        ):
            self.assertEqual(self.html.count(title), 1)

    def test_experience_boundary(self):
        self.assertIn("Nuanwa Technology", self.html)
        self.assertIn("Uceng Intelligence", self.html)
        self.assertNotIn("Fanhan", self.html)

    def test_assets_and_links(self):
        self.assertTrue((ROOT / "assets/images/profile/shu-cheng.png").is_file())
        self.assertTrue((ROOT / "assets/files/Shu_Cheng_Resume.pdf").is_file())
        self.assertIn("mailto:18074599386@163.com", self.html)
        self.assertIn("github.com/qq1982605092-hue", self.html)
        self.assertIn("Shu_Cheng_Resume.pdf", self.html)

    def test_forbidden_claims(self):
        for text in (
            "SOTA",
            "state-of-the-art",
            "100%",
            "99.1%",
            "21.1%",
            "34/34",
            "Code coming soon",
        ):
            self.assertNotIn(text, self.html)


if __name__ == "__main__":
    unittest.main()
