import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AboutThemeContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = (ROOT / "index.md").read_text(encoding="utf-8")
        cls.head = (ROOT / "_includes/head.html").read_text(encoding="utf-8")
        cls.layout = (ROOT / "_layouts/default.html").read_text(encoding="utf-8")
        cls.scss = (ROOT / "_sass/_site.scss").read_text(encoding="utf-8")

    def about_copy(self):
        matches = re.findall(
            r'<([a-z][\w-]*)[^>]*class="about-copy"[^>]*>(.*?)</\1>',
            self.index,
            flags=re.DOTALL,
        )
        self.assertEqual(len(matches), 1)
        return matches[0][1]

    def test_about_is_a_distinct_editorial_section(self):
        self.assertIn('<section id="about" class="page-section about-section">', self.index)
        self.assertNotIn('<section id="about" class="hero">', self.index)
        self.assertIn('class="about-label">About</p>', self.index)
        self.assertEqual(self.index.count('class="about-copy"'), 1)
        about_copy = self.about_copy()
        paragraphs = re.findall(r"<p(?:\s[^>]*)?>.*?</p>", about_copy, flags=re.DOTALL)
        self.assertEqual(len(paragraphs), 2)
        self.assertEqual(len(re.findall(r"<p(?:\s[^>]*)?>", about_copy)), 2)

    def test_about_tells_a_bounded_research_story(self):
        for text in (
            "East China Normal University",
            "Nuanwa Technology",
            "Uceng Intelligence",
            "memory-augmented embodied agents",
        ):
            self.assertIn(text, self.index)
        about_copy = self.about_copy().lower()
        for unsupported_pattern in (
            r"\bvlas?\b",
            r"\bvision[ -]language[ -]action\b",
            r"\brl\b",
            r"\breinforcement[ -]learning\b",
            r"\brobot[ -]foundation[ -]models?\b",
            r"\breal[ -]robots?\b",
            r"\bphysical[ -]robots?\b",
            r"\bfoundation[ -]model research\b",
            r"\bten[ -]thousand[ -]gpus?\b",
        ):
            self.assertNotRegex(about_copy, unsupported_pattern)

    def test_theme_bootstraps_before_paint(self):
        self.assertIn('localStorage.getItem("site-theme")', self.head)
        self.assertIn('document.documentElement.dataset.theme', self.head)
        self.assertIn('name="theme-color"', self.head)

    def test_theme_toggle_is_accessible_and_persistent(self):
        self.assertIn('class="theme-toggle"', self.layout)
        self.assertIn('type="button"', self.layout)
        self.assertIn('aria-label="Switch to dark theme"', self.layout)
        self.assertIn('localStorage.setItem("site-theme"', self.layout)
        self.assertIn('data-icon="moon"', self.layout)
        self.assertIn('data-icon="sun"', self.layout)

    def test_theme_and_about_styles_are_complete(self):
        for selector in (
            ':root[data-theme="dark"]',
            ".theme-toggle",
            ".about-section",
            ".about-label",
            ".about-copy",
        ):
            self.assertIn(selector, self.scss)
        self.assertIn("@media (prefers-color-scheme: dark)", self.scss)
        self.assertIn(":root:not([data-theme])", self.scss)
        self.assertIn("prefers-reduced-motion: reduce", self.scss)


if __name__ == "__main__":
    unittest.main()
