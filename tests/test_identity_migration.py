from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class IdentityMigrationContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = {
            path: (ROOT / path).read_text(encoding="utf-8")
            for path in (
                "_config.yml",
                "index.md",
                "_layouts/default.html",
                "README.md",
                "LICENSE",
            )
        }

    def test_public_identity_uses_given_name_first(self):
        for path in ("_config.yml", "index.md", "_layouts/default.html", "README.md"):
            self.assertIn("Cheng Shu", self.sources[path], path)
            self.assertNotIn("Shu Cheng", self.sources[path], path)

    def test_site_uses_new_github_namespace(self):
        combined = "\n".join(self.sources.values())
        self.assertIn("https://chengshu-ai.github.io", combined)
        self.assertIn("chengshu-ai/chengshu-ai.github.io", combined)
        self.assertIn('github: "chengshu-ai"', self.sources["_config.yml"])
        self.assertNotIn("qq1982605092-hue", combined)


if __name__ == "__main__":
    unittest.main()
