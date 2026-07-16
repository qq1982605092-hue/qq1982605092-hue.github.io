# About Narrative and Theme Toggle Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an editorial About section and a persistent, accessible light/dark theme toggle across the Jekyll site.

**Architecture:** Keep the homepage content in `index.md`, the early no-flash theme bootstrap in `_includes/head.html`, the semantic toggle and dependency-free interaction script in `_layouts/default.html`, and all visual states in `_sass/_site.scss`. Add one focused source-contract test file so the feature can be validated without depending on a local Jekyll build.

**Tech Stack:** Jekyll, Liquid, semantic HTML, SCSS custom properties, vanilla JavaScript, Python `unittest`, GitHub Pages.

## Global Constraints

- The About section uses two short paragraphs and does not claim completed VLA, real-robot, robot-foundation-model, or reinforcement-learning work.
- The theme control applies across homepage and project pages.
- The explicit preference key is exactly `site-theme`, with allowed values `light` and `dark`.
- No JavaScript framework, external icon package, card grid, second portrait, metrics strip, or new dependency is added.
- Existing unrelated changes in `tests/test_project_data.py`, `tests/test_project_pages.py`, `tests/test_site_contract.py`, and `test-results/` are preserved and excluded from feature commits.

---

### Task 1: Lock the About and theme source contracts

**Files:**
- Create: `tests/test_about_theme.py`

**Interfaces:**
- Consumes: source files `index.md`, `_includes/head.html`, `_layouts/default.html`, `_sass/_site.scss`.
- Produces: `AboutThemeContract`, the regression contract for Tasks 2 and 3.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_about_theme.py` with tests that require:

```python
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

    def test_about_is_a_distinct_editorial_section(self):
        self.assertIn('<section id="about" class="page-section about-section">', self.index)
        self.assertNotIn('<section id="about" class="hero">', self.index)
        self.assertIn('class="about-label">About</p>', self.index)
        self.assertEqual(self.index.count('class="about-copy"'), 1)

    def test_about_tells_a_bounded_research_story(self):
        for text in (
            "East China Normal University",
            "Nuanwa Technology",
            "Uceng Intelligence",
            "memory-augmented embodied agents",
        ):
            self.assertIn(text, self.index)
        for unsupported in ("real-robot", "foundation-model research", "ten-thousand-GPU"):
            self.assertNotIn(unsupported, self.index)

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
        self.assertIn("prefers-reduced-motion: reduce", self.scss)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test to verify RED**

Run:

```bash
python3 -m unittest tests/test_about_theme.py -v
```

Expected: failures for the missing About section, bootstrap script, toggle, and theme styles.

- [ ] **Step 3: Commit the RED contract**

```bash
git add tests/test_about_theme.py
git commit -m "test: define about and theme contracts"
```

---

### Task 2: Implement the editorial About narrative

**Files:**
- Modify: `index.md`
- Modify: `_sass/_site.scss`
- Test: `tests/test_about_theme.py`

**Interfaces:**
- Consumes: `.page-section` spacing tokens and the existing Hero/Selected Work sequence.
- Produces: `#about`, `.about-section`, `.about-label`, and `.about-copy` for navigation and responsive layout.

- [ ] **Step 1: Move the Hero anchor and insert the About section**

Change the Hero opening tag to `<section class="hero">`. Between Hero and Selected Work, insert:

```html
<section id="about" class="page-section about-section">
  <p class="about-label">About</p>
  <div class="about-copy">
    <p>I’m an M.S. student in Computer Science at <strong>East China Normal University</strong>, working at the intersection of agent memory, model post-training, and multimodal systems. My central question is how an agent can retain useful experience, make inspectable decisions, and eventually turn perception into reliable action over long horizons.</p>
    <p>At <strong>Nuanwa Technology</strong>, I build state-driven agent workflows and task-specific model adaptation pipelines. Earlier, at <strong>Uceng Intelligence</strong>, I connected industrial vision outputs with downstream production and control systems, gaining experience across the loop from perception to physical execution. I’m now exploring how these pieces can support <strong>memory-augmented embodied agents</strong>.</p>
  </div>
</section>
```

Compress the final Current Focus paragraph to one sentence that points forward without repeating this biography.

- [ ] **Step 2: Add the editorial and responsive SCSS**

Add a top divider, two-column grid, uppercase label, Georgia body copy, readable line length, sparse emphasis, and a single-column mobile state. Use existing variables only:

```scss
.about-section {
  display: grid;
  grid-template-columns: minmax(120px, 0.28fr) minmax(0, 1fr);
  gap: clamp(2rem, 6vw, 6rem);
  border-top: 1px solid var(--line);
}

.about-label {
  margin: 0;
  color: var(--muted);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
}

.about-copy {
  max-width: 860px;
}

.about-copy p {
  margin: 0;
  font-family: Georgia, "Times New Roman", serif;
  font-size: clamp(1.2rem, 2vw, 1.55rem);
  line-height: 1.72;
}

.about-copy p + p {
  margin-top: 1.35rem;
}

.about-copy strong {
  color: var(--accent);
  font-weight: 600;
}
```

At the existing mobile breakpoint, set `.about-section { grid-template-columns: 1fr; gap: 1.25rem; }` and reduce the paragraph size to `1.12rem`.

- [ ] **Step 3: Run the focused About tests**

```bash
python3 -m unittest tests/test_about_theme.py -v
```

Expected: the two About tests pass; theme tests remain failing.

- [ ] **Step 4: Commit the About section**

```bash
git add index.md _sass/_site.scss
git commit -m "feat: add editorial about narrative"
```

---

### Task 3: Implement persistent site-wide themes

**Files:**
- Modify: `_includes/head.html`
- Modify: `_layouts/default.html`
- Modify: `_sass/_site.scss`
- Test: `tests/test_about_theme.py`

**Interfaces:**
- Consumes: `site-theme`, `document.documentElement.dataset.theme`, system `prefers-color-scheme`, and existing CSS variables.
- Produces: `.theme-toggle`, `[data-icon="moon"]`, `[data-icon="sun"]`, light/dark tokens, and accessible action labels.

- [ ] **Step 1: Add the early no-flash bootstrap**

Before the stylesheet link in `_includes/head.html`, add theme-color metadata and an inline script that reads `site-theme`, falls back to `prefers-color-scheme`, and sets `document.documentElement.dataset.theme`. Wrap storage access in `try/catch`.

- [ ] **Step 2: Add the semantic control and behavior**

Wrap the navigation and toggle in `.masthead__actions`. Add a `button.theme-toggle` with two inline SVG icons. At the end of `<body>`, add a dependency-free script that:

```javascript
const root = document.documentElement;
const toggle = document.querySelector(".theme-toggle");
const syncThemeControl = () => {
  const dark = root.dataset.theme === "dark";
  toggle.setAttribute("aria-label", dark ? "Switch to light theme" : "Switch to dark theme");
  toggle.title = toggle.getAttribute("aria-label");
  toggle.setAttribute("aria-pressed", String(dark));
};

toggle.addEventListener("click", () => {
  const next = root.dataset.theme === "dark" ? "light" : "dark";
  root.dataset.theme = next;
  try { localStorage.setItem("site-theme", next); } catch (error) {}
  syncThemeControl();
});

syncThemeControl();
```

- [ ] **Step 3: Add theme variables and control styles**

Define dark variables under `:root[data-theme="dark"]`, use variable-backed masthead surfaces instead of hard-coded white, and style the toggle as a 44-pixel rounded square with a border and restrained icon transition. Show the moon in light mode and sun in dark mode. Add `color-scheme` for both roots and preserve focus rings.

- [ ] **Step 4: Complete reduced-motion behavior**

Within the existing `@media (prefers-reduced-motion: reduce)` block, disable theme surface and icon transitions alongside existing animations.

- [ ] **Step 5: Run the full clean-target test suite**

Construct a temporary tree from `HEAD` plus the feature's staged diff, so unrelated dirty tests are excluded:

```bash
tmpdir=$(mktemp -d /tmp/githubio-about-theme-XXXXXX)
git archive HEAD | tar -x -C "$tmpdir"
git diff --cached --binary | git -C "$tmpdir" apply
python3 -m unittest discover -s "$tmpdir/tests" -v
result=$?
rm -rf "$tmpdir"
exit $result
```

Expected: all source tests pass; rendered-site tests may skip if `_site` is absent.

- [ ] **Step 6: Commit the theme system**

```bash
git add _includes/head.html _layouts/default.html _sass/_site.scss tests/test_about_theme.py
git commit -m "feat: add persistent light and dark themes"
```

---

### Task 4: Visual QA and deploy

**Files:**
- Verify only: homepage and project pages.
- Create temporary screenshots outside the repository under `/tmp/chengshu-about-theme-check/`.

**Interfaces:**
- Consumes: committed About/theme feature and GitHub Pages workflow.
- Produces: verified public deployment at `https://chengshu-ai.github.io/`.

- [ ] **Step 1: Push through the configured local proxy path without persisting Git settings**

```bash
HTTPS_PROXY=http://127.0.0.1:7890 HTTP_PROXY=http://127.0.0.1:7890 git push origin main
```

- [ ] **Step 2: Wait for the matching Pages workflow**

Use `gh run list` to locate the run whose `headSha` matches `git rev-parse HEAD`, then run `gh run watch RUN_ID --exit-status`.

- [ ] **Step 3: Capture four screenshots**

Use headless Chrome at 1440 by 1100 and 390 by 844 in both light and dark modes. Set the theme through local storage before capture and inspect every image for hierarchy, clipping, contrast, and overflow.

- [ ] **Step 4: Verify public routes and identity**

Require HTTP 200 from:

```text
/
/projects/agent-memory/
/projects/calling-agent/
/projects/qwen3-reranker/
```

Verify the homepage contains `Cheng Shu`, `About`, `Nuanwa Technology`, and `memory-augmented embodied agents`, and that the theme control is present.

- [ ] **Step 5: Report the live URL and preview evidence**

Return the public URL, Pages run URL, commit ID, test summary, and the desktop light/dark screenshot paths.
