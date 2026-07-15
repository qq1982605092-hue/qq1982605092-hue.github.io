from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class HomepageContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "_site/index.html").read_text(encoding="utf-8")

    def test_identity(self):
        self.assertIn("Shu Cheng", self.html)
        self.assertIn("舒橙", self.html)
        self.assertIn(
            "I build memory and reasoning systems for embodied agents.", self.html
        )

    def test_sections(self):
        for section_id in ("about", "selected-work", "experience", "education"):
            self.assertIn(f'id="{section_id}"', self.html)

    def test_projects(self):
        for title in (
            "Dual-Time Agent Memory",
            "State-Driven AI Calling Agent",
            "Qwen3 Reranker Fine-tuning",
            "Multimodal Structured Perception Pipeline",
        ):
            self.assertIn(title, self.html)

    def test_assets(self):
        self.assertTrue((ROOT / "assets/images/profile/shu-cheng.png").is_file())
        self.assertTrue((ROOT / "assets/files/Shu_Cheng_Resume.pdf").is_file())

    def test_forbidden_claims(self):
        for text in ("SOTA", "state-of-the-art", "100%", "99.1%", "21.1%", "34/34"):
            self.assertNotIn(text, self.html)


if __name__ == "__main__":
    unittest.main()
