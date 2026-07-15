# Research Portfolio Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the current document-like homepage with an evidence-oriented research portfolio that connects Agent Memory, post-training, retrieval, and multimodal work to embodied intelligence.

**Architecture:** Keep the native Jekyll/GitHub Pages site. Move the four project records into `_data/projects.yml`, render them through one semantic include, and let `index.md` own only page-level narrative. A single focused Sass file implements the hero, illustrated project rows, research questions, experience, responsive behavior, and accessibility states.

**Tech Stack:** Jekyll, Liquid, YAML, SCSS, Python `unittest`, GitHub Pages, browser screenshot verification.

## Global Constraints

- English-first and factual.
- The homepage must connect current work to embodied intelligence without presenting unfinished VLA or robotics work as completed.
- No unsupported accuracy, latency, SOTA, publication, production-impact, or scale claims.
- No unfinished ManiSkill, LeRobot, OpenVLA, Isaac, or Memory-enhanced VLA project presented as completed work.
- Nuanwa Technology and Uceng Intelligence are the only homepage experience entries.
- The Fanhan internship must not appear on the homepage.
- Do not edit `assets/files/Shu_Cheng_Resume.pdf`.
- Do not alter the source bytes of `assets/images/profile/shu-cheng.png`.
- Use one muted academic-blue accent, no card grid, no gradients, and no decorative motion.
- The page must work without JavaScript.
- Test real desktop width 1440 px and mobile widths 390 px and 375 px.
- Publish from `main:/` and verify GitHub Pages reports `built` before completion.

---

## File map

- Create `_data/projects.yml`: the single source of truth for the four selected projects.
- Modify `_includes/project-entry.html`: render one semantic project row from a `project` object.
- Modify `_includes/author-profile.html`: render hero identity, portrait, and verified contact links.
- Modify `_layouts/default.html`: simplify the page shell and add the footer workflow line.
- Modify `_data/navigation.yml`: align navigation with the redesigned section order.
- Modify `index.md`: render the hero, projects, research questions, experience, and current focus.
- Modify `_sass/_site.scss`: implement the complete research-portfolio visual system.
- Create `tests/test_project_data.py`: validate project data and forbidden-content boundaries without requiring Jekyll.
- Create `tests/test_redesign_source.py`: validate the new semantic source structure and responsive selectors.
- Modify `tests/test_site_contract.py`: validate the rendered homepage after a successful build.
- Modify `README.md`: document the project-data workflow and visual verification commands.

---

### Task 1: Introduce a validated project-data model

**Files:**
- Create: `tests/test_project_data.py`
- Create: `_data/projects.yml`

**Interfaces:**
- Consumes: no new interface.
- Produces: a YAML list at `site.data.projects`; each item provides `id`, `number`, `label`, `title`, `diagram`, `question`, and exactly two `contributions`.

- [ ] **Step 1: Write the failing project-data contract**

Create `tests/test_project_data.py`:

```python
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
                "State-Driven AI Calling Agent",
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
```

- [ ] **Step 2: Run the contract and verify the intended failure**

Run:

```bash
python3 -m unittest tests/test_project_data.py -v
```

Expected: FAIL with `_data/projects.yml must exist`.

- [ ] **Step 3: Create the four-project data source**

Create `_data/projects.yml`:

```yaml
- id: dual-time-memory
  number: "01"
  label: "Research in progress"
  title: "Dual-Time Agent Memory"
  diagram: "memory"
  question: "How can an agent preserve what happened while also tracking how its knowledge changes?"
  contributions:
    - "Organizes interaction evidence across event time and knowledge-update time."
    - "Studies temporal consistency, evidence traceability, and long-horizon recall."

- id: calling-agent
  number: "02"
  label: "Agent systems"
  title: "State-Driven AI Calling Agent"
  diagram: "agent"
  question: "How do we turn open-ended model behavior into an inspectable production workflow?"
  contributions:
    - "Separates dialogue stages, transition conditions, and external system actions."
    - "Connects model post-training with controllable production integration."

- id: qwen3-reranker
  number: "03"
  label: "Retrieval adaptation"
  title: "Qwen3 Reranker Fine-tuning"
  diagram: "ranking"
  question: "How can a ranking model capture task-specific relevance beyond general semantic similarity?"
  contributions:
    - "Constructs domain-focused training data and evaluation cases for relevance ranking."
    - "Uses retrieval error analysis to guide data and modeling revisions."

- id: multimodal-perception
  number: "04"
  label: "Multimodal perception"
  title: "Multimodal Structured Perception"
  diagram: "perception"
  question: "How can pixels and text become consistent records that a reasoning system can use?"
  contributions:
    - "Integrates OCR and vision-language components to extract complementary evidence."
    - "Uses structured schemas and validation for reliable downstream consumption."
```

- [ ] **Step 4: Run the focused test**

Run:

```bash
python3 -m unittest tests/test_project_data.py -v
```

Expected: 3 tests PASS.

- [ ] **Step 5: Commit the data model**

```bash
git add _data/projects.yml tests/test_project_data.py
git commit -m "feat: add validated project data"
```

---

### Task 2: Render the research narrative with semantic components

**Files:**
- Create: `tests/test_redesign_source.py`
- Modify: `_includes/project-entry.html`
- Modify: `_includes/author-profile.html`
- Modify: `_layouts/default.html`
- Modify: `_data/navigation.yml`
- Modify: `index.md`

**Interfaces:**
- Consumes: `site.data.projects`, with the exact fields defined in Task 1.
- Produces: section IDs `about`, `selected-work`, `research`, and `experience`; project entries use `.project-entry`, `.project-visual--<diagram>`, and `.project-copy`.

- [ ] **Step 1: Write the failing semantic-source contract**

Create `tests/test_redesign_source.py`:

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RedesignSourceContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = (ROOT / "index.md").read_text(encoding="utf-8")
        cls.project = (ROOT / "_includes/project-entry.html").read_text(encoding="utf-8")
        cls.layout = (ROOT / "_layouts/default.html").read_text(encoding="utf-8")
        cls.nav = (ROOT / "_data/navigation.yml").read_text(encoding="utf-8")

    def test_section_structure(self):
        for section_id in ("about", "selected-work", "research", "experience"):
            self.assertIn(f'id="{section_id}"', self.index)
        self.assertNotIn('id="education"', self.index)

    def test_research_narrative(self):
        self.assertIn("Memory × Reasoning × Embodied AI", self.index)
        self.assertIn("Systems that help agents remember, reason, and act.", self.index)
        self.assertIn("site.data.projects", self.index)
        self.assertIn("Questions I care about", self.index)

    def test_project_component(self):
        self.assertIn("include.project", self.project)
        self.assertIn("project-visual--{{ include.project.diagram }}", self.project)
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
```

- [ ] **Step 2: Run the source contract and verify it fails**

Run:

```bash
python3 -m unittest tests/test_redesign_source.py -v
```

Expected: FAIL because the new research hero, `research` section, data loop, and component interface do not yet exist.

- [ ] **Step 3: Replace the project include**

Replace `_includes/project-entry.html` with:

```liquid
<article class="project-entry" id="project-{{ include.project.id }}">
  <div class="project-index" aria-hidden="true">{{ include.project.number }}</div>
  <div
    class="project-visual project-visual--{{ include.project.diagram }}"
    aria-hidden="true"
  >
    <span></span><span></span><span></span><span></span>
  </div>
  <div class="project-copy">
    <p class="project-label">{{ include.project.label }}</p>
    <h3>{{ include.project.title }}</h3>
    <p class="project-question">{{ include.project.question }}</p>
    <ul>
      {% for contribution in include.project.contributions %}
        <li>{{ contribution }}</li>
      {% endfor %}
    </ul>
    {% if include.project.links %}
      <p class="project-links">
        {% for link in include.project.links %}
          <a href="{{ link.url }}">{{ link.label }}</a>
        {% endfor %}
      </p>
    {% endif %}
  </div>
</article>
```

- [ ] **Step 4: Replace the identity include**

Replace `_includes/author-profile.html` with:

```liquid
<div class="hero-identity">
  <img
    class="hero-portrait"
    src="{{ site.author.avatar | relative_url }}"
    alt="Portrait of {{ site.author.name | escape }}"
  >
  <div class="hero-meta">
    <strong>{{ site.author.name }}</strong>
    <span>{{ site.author.title }}</span>
    <span>{{ site.author.affiliation }}</span>
    <span>{{ site.author.location }}</span>
  </div>
</div>
```

- [ ] **Step 5: Simplify the layout and add the workflow footer**

Replace `_layouts/default.html` with:

```liquid
<!doctype html>
<html lang="{{ site.locale | default: 'en-US' }}">
  {% include head.html %}
  <body>
    <a class="skip-link" href="#main">Skip to main content</a>
    <header class="masthead">
      <div class="masthead__inner">
        <a class="site-title" href="{{ '/' | relative_url }}">{{ site.title }}</a>
        <nav class="site-nav" aria-label="Primary navigation">
          {% for item in site.data.navigation.main %}
            <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
          {% endfor %}
        </nav>
      </div>
    </header>
    <main id="main">{{ content }}</main>
    <footer class="site-footer">
      <span>Shu Cheng · East China Normal University</span>
      <span>Research and engineering harnesses: Codex · Claude Code · Cursor</span>
    </footer>
  </body>
</html>
```

- [ ] **Step 6: Replace the navigation data**

Replace `_data/navigation.yml` with:

```yaml
main:
  - title: "About"
    url: "/#about"
  - title: "Selected Work"
    url: "/#selected-work"
  - title: "Research"
    url: "/#research"
  - title: "Experience"
    url: "/#experience"
  - title: "CV"
    url: "/assets/files/Shu_Cheng_Resume.pdf"
```

- [ ] **Step 7: Replace the homepage narrative**

Replace the body of `index.md` after its front matter with:

```liquid
<section id="about" class="hero">
  <div class="hero-copy">
    <p class="eyebrow">Memory × Reasoning × Embodied AI</p>
    <h1>Systems that help agents <em>remember, reason, and act.</em></h1>
    <p class="hero-lead">I build long-horizon memory and model post-training systems, then connect them to grounded perception and reliable decision-making for embodied agents.</p>
    <p class="hero-links">
      <a href="#selected-work">Explore selected work</a>
      <a href="mailto:{{ site.author.email }}">Email</a>
      <a href="https://github.com/{{ site.author.github }}">GitHub</a>
      <a href="{{ site.author.cv | relative_url }}">CV</a>
    </p>
  </div>
  {% include author-profile.html %}
</section>

<section id="selected-work" class="page-section selected-work">
  <header class="section-heading">
    <h2>Selected Work</h2>
    <p>Research questions translated into working systems.</p>
  </header>
  <div class="project-list">
    {% for project in site.data.projects %}
      {% include project-entry.html project=project %}
    {% endfor %}
  </div>
</section>

<section id="research" class="page-section research-questions">
  <header class="section-heading">
    <h2>Questions I care about</h2>
    <p>The bridge from current work to embodied intelligence.</p>
  </header>
  <div class="question-grid">
    <article><span>01 / Memory</span><p>What should an agent retain after the current interaction ends?</p></article>
    <article><span>02 / Reasoning</span><p>How can decisions remain grounded, adaptive, and inspectable?</p></article>
    <article><span>03 / Perception</span><p>How should multimodal evidence become reusable experience?</p></article>
  </div>
</section>

<section id="experience" class="page-section experience-focus">
  <div>
    <h2>Experience</h2>
    <div class="timeline-entry">
      <h3>AI Algorithm Engineering Intern</h3>
      <p class="entry-meta">Nuanwa Technology · Shanghai · 2026–Present</p>
      <p>Developing Agent Memory, model post-training, and state-driven AI systems for applied workflows.</p>
    </div>
    <div class="timeline-entry">
      <h3>Python Systems R&amp;D Intern</h3>
      <p class="entry-meta">Uceng Intelligence · Shanghai · 2024.03–2024.08</p>
      <p>Built Python system components and data-processing workflows.</p>
    </div>
  </div>
  <div class="current-focus">
    <h2>Current focus</h2>
    <p>I am exploring how memory and post-training can support agents that operate across long horizons, perceive structured environments, and eventually learn to act in embodied settings.</p>
    <p class="focus-tags"><span>Agent Memory</span><span>Post-training</span><span>Retrieval</span><span>Multimodal Systems</span><span>Embodied AI</span></p>
  </div>
</section>
```

- [ ] **Step 8: Run the source contracts**

Run:

```bash
python3 -m unittest tests/test_project_data.py tests/test_redesign_source.py -v
```

Expected: 8 tests PASS.

- [ ] **Step 9: Commit the semantic redesign**

```bash
git add _includes/project-entry.html _includes/author-profile.html _layouts/default.html _data/navigation.yml index.md tests/test_redesign_source.py
git commit -m "feat: restructure homepage research narrative"
```

---

### Task 3: Implement the editorial visual system and responsive behavior

**Files:**
- Modify: `tests/test_redesign_source.py`
- Modify: `_sass/_site.scss`

**Interfaces:**
- Consumes: semantic class names produced by Task 2.
- Produces: desktop and mobile layout rules for `.hero`, `.project-entry`, `.project-visual`, `.question-grid`, `.experience-focus`, and `.site-footer`.

- [ ] **Step 1: Add a failing visual-system contract**

Add to `RedesignSourceContract.setUpClass`:

```python
        cls.scss = (ROOT / "_sass/_site.scss").read_text(encoding="utf-8")
```

Add these test methods:

```python
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
```

- [ ] **Step 2: Run the focused test and verify it fails**

Run:

```bash
python3 -m unittest tests/test_redesign_source.py -v
```

Expected: FAIL because the current stylesheet has no project, diagram, research-question, or experience-focus rules.

- [ ] **Step 3: Replace `_sass/_site.scss` with the complete visual system**

Use the approved design tokens and selectors below. Preserve every selector in this block; they are the contract between the semantic markup and responsive presentation.

```scss
:root {
  --paper: #ffffff;
  --ink: #17222d;
  --muted: #687581;
  --line: #dfe5e9;
  --accent: #2d628f;
  --accent-soft: #7898b2;
  --wash: #f3f6f7;
  --dark: #192630;
  --page-width: 1200px;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 16px;
  line-height: 1.65;
}
a {
  color: var(--accent);
  text-decoration-thickness: 1px;
  text-underline-offset: .2em;
  transition: color .18s ease, text-decoration-thickness .18s ease;
  overflow-wrap: anywhere;
}
a:hover, a:focus-visible { text-decoration-thickness: 2px; }
a:focus-visible { outline: 2px solid var(--accent); outline-offset: 4px; }
.skip-link {
  position: fixed;
  top: .75rem;
  left: .75rem;
  z-index: 20;
  padding: .5rem .75rem;
  background: var(--ink);
  color: var(--paper);
  transform: translateY(-180%);
}
.skip-link:focus { transform: translateY(0); }
.masthead {
  position: sticky;
  top: 0;
  z-index: 10;
  border-bottom: 1px solid var(--line);
  background: rgba(255, 255, 255, .96);
  backdrop-filter: blur(12px);
}
.masthead__inner {
  display: flex;
  max-width: var(--page-width);
  min-height: 4.5rem;
  margin: 0 auto;
  padding: 0 1.5rem;
  align-items: center;
  justify-content: space-between;
  gap: 2rem;
}
.site-title {
  color: var(--ink);
  font-family: Georgia, "Times New Roman", serif;
  font-size: 1.3rem;
  font-weight: 700;
  text-decoration: none;
  white-space: nowrap;
}
.site-nav { display: flex; gap: 1.6rem; }
.site-nav a { color: var(--muted); font-size: .88rem; text-decoration: none; white-space: nowrap; }
.site-nav a:hover, .site-nav a:focus-visible { color: var(--accent); }
.hero {
  display: grid;
  grid-template-columns: minmax(0, 1.45fr) minmax(250px, .55fr);
  gap: clamp(3rem, 7vw, 7rem);
  max-width: var(--page-width);
  min-height: 34rem;
  margin: 0 auto;
  padding: clamp(4.5rem, 8vw, 7.5rem) 1.5rem 5rem;
  align-items: center;
}
.eyebrow {
  margin: 0 0 1.2rem;
  color: var(--accent);
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
}
.hero h1 {
  max-width: 780px;
  margin: 0;
  font-family: Georgia, "Times New Roman", serif;
  font-size: clamp(2.9rem, 5.5vw, 5rem);
  font-weight: 500;
  letter-spacing: -.035em;
  line-height: 1.04;
}
.hero h1 em { color: var(--accent); font-style: normal; }
.hero-lead { max-width: 680px; margin: 1.6rem 0 0; color: var(--muted); font-size: 1.08rem; }
.hero-links { display: flex; flex-wrap: wrap; gap: 1.4rem; margin: 1.7rem 0 0; font-size: .9rem; }
.hero-identity { justify-self: end; }
.hero-portrait {
  display: block;
  width: min(280px, 22vw);
  aspect-ratio: 4 / 5;
  object-fit: cover;
  object-position: 50% 20%;
  filter: saturate(.82);
  box-shadow: 18px 18px 0 #dce6eb;
}
.hero-meta { display: grid; gap: .18rem; margin-top: 1.75rem; color: var(--muted); font-size: .86rem; }
.hero-meta strong { color: var(--ink); font-size: 1rem; }
.page-section { padding: 5rem max(1.5rem, calc((100vw - var(--page-width)) / 2 + 1.5rem)); }
.section-heading { display: flex; align-items: end; justify-content: space-between; gap: 2rem; margin-bottom: 2rem; }
.section-heading h2, .experience-focus h2 {
  margin: 0;
  font-family: Georgia, "Times New Roman", serif;
  font-size: clamp(2rem, 3vw, 2.6rem);
  line-height: 1.15;
}
.section-heading p { margin: 0; color: var(--muted); font-size: .84rem; }
.project-list { border-top: 1px solid var(--line); }
.project-entry {
  display: grid;
  grid-template-columns: 3rem minmax(220px, .72fr) minmax(0, 1.28fr);
  gap: clamp(1.5rem, 4vw, 3rem);
  padding: 2.8rem 0;
  border-bottom: 1px solid var(--line);
  align-items: start;
}
.project-index { color: #9aa5ad; font-family: Georgia, "Times New Roman", serif; font-size: 1.25rem; }
.project-visual {
  position: relative;
  min-height: 200px;
  overflow: hidden;
  background: var(--wash);
  transition: transform .2s ease;
}
.project-entry:hover .project-visual { transform: translateY(-3px); }
.project-visual span { position: absolute; display: block; }
.project-visual--memory span { width: 12px; height: 12px; border-radius: 50%; background: var(--accent); box-shadow: 0 0 0 6px rgba(45, 98, 143, .12); }
.project-visual--memory::before, .project-visual--memory::after { content: ""; position: absolute; background: var(--accent-soft); }
.project-visual--memory::before { left: 1.5rem; right: 1.5rem; top: 50%; height: 1px; }
.project-visual--memory::after { top: 1.5rem; bottom: 1.5rem; left: 50%; width: 1px; }
.project-visual--memory span:nth-child(1) { left: 18%; top: 28%; }
.project-visual--memory span:nth-child(2) { left: 46%; top: 64%; }
.project-visual--memory span:nth-child(3) { left: 72%; top: 22%; }
.project-visual--memory span:nth-child(4) { left: 78%; top: 70%; background: var(--accent-soft); }
.project-visual--agent span { width: 28%; height: 3.1rem; border: 1px solid #b9c8d2; background: #fff; }
.project-visual--agent span:nth-child(1) { left: 6%; top: 20%; }
.project-visual--agent span:nth-child(2) { left: 36%; top: 56%; }
.project-visual--agent span:nth-child(3) { right: 6%; top: 20%; }
.project-visual--agent span:nth-child(4) { display: none; }
.project-visual--ranking { display: flex; align-items: center; justify-content: center; gap: .65rem; }
.project-visual--ranking span { position: static; width: 1.55rem; background: var(--accent-soft); }
.project-visual--ranking span:nth-child(1) { height: 3.4rem; }
.project-visual--ranking span:nth-child(2) { height: 7rem; background: var(--accent); }
.project-visual--ranking span:nth-child(3) { height: 4.9rem; }
.project-visual--ranking span:nth-child(4) { height: 2.5rem; }
.project-visual--perception { display: grid; grid-template-columns: 1fr 1fr; gap: 1px; background: #cbd7df; }
.project-visual--perception span { position: static; background: #f4f7f8; }
.project-label { margin: 0; color: var(--accent); font-size: .7rem; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; }
.project-copy h3 { margin: .55rem 0 .7rem; font-family: Georgia, "Times New Roman", serif; font-size: clamp(1.55rem, 2.5vw, 2rem); line-height: 1.2; }
.project-question { margin: 0 0 .9rem; color: #3c4a56; }
.project-copy ul { margin: 0; padding-left: 1.15rem; color: var(--muted); font-size: .9rem; }
.project-links { display: flex; gap: 1rem; margin: 1rem 0 0; font-size: .82rem; }
.research-questions { background: var(--dark); color: #f6f7f8; }
.research-questions .section-heading p { color: #9eadb8; }
.question-grid { display: grid; grid-template-columns: repeat(3, 1fr); border-top: 1px solid #3a4853; }
.question-grid article { padding: 2rem 2rem 1rem 0; border-right: 1px solid #3a4853; margin-right: 2rem; }
.question-grid article:last-child { border-right: 0; margin-right: 0; }
.question-grid span { color: #7fa2bc; font-size: .75rem; }
.question-grid p { margin: .9rem 0; font-family: Georgia, "Times New Roman", serif; font-size: 1.25rem; line-height: 1.45; }
.experience-focus { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(3rem, 7vw, 7rem); }
.timeline-entry { padding: 1.35rem 0; border-bottom: 1px solid var(--line); }
.timeline-entry:first-of-type { margin-top: 1rem; border-top: 1px solid var(--line); }
.timeline-entry h3 { margin: 0; font-size: 1rem; }
.timeline-entry p { margin: .45rem 0 0; color: var(--muted); font-size: .88rem; }
.entry-meta { color: var(--accent) !important; }
.current-focus p { color: var(--muted); }
.focus-tags { display: flex; flex-wrap: wrap; gap: .55rem; }
.focus-tags span { padding: .35rem .6rem; background: var(--wash); color: #53626e; font-size: .76rem; }
.site-footer {
  display: flex;
  max-width: var(--page-width);
  margin: 0 auto;
  padding: 2rem 1.5rem;
  border-top: 1px solid var(--line);
  justify-content: space-between;
  gap: 2rem;
  color: var(--muted);
  font-size: .76rem;
}

@media (max-width: 760px) {
  .masthead__inner { min-height: 3.75rem; padding: 0 1.1rem; }
  .site-nav { gap: 1rem; }
  .site-nav a:nth-child(1), .site-nav a:nth-child(3), .site-nav a:nth-child(4) { display: none; }
  .hero { grid-template-columns: 1fr; gap: 2.2rem; min-height: 0; padding: 3rem 1.1rem 4rem; }
  .hero h1 { font-size: clamp(2.6rem, 13vw, 3.6rem); }
  .hero-identity { display: flex; justify-self: start; align-items: end; gap: 1.4rem; }
  .hero-portrait { width: 118px; box-shadow: 10px 10px 0 #dce6eb; }
  .hero-meta { margin: 0; font-size: .76rem; }
  .page-section { padding: 4rem 1.1rem; }
  .section-heading { display: block; }
  .section-heading p { margin-top: .55rem; }
  .project-entry { grid-template-columns: 2rem minmax(0, 1fr); gap: 1rem; padding: 2.3rem 0; }
  .project-visual, .project-copy { grid-column: 2; }
  .project-visual { min-height: 160px; }
  .question-grid, .experience-focus { grid-template-columns: 1fr; }
  .question-grid article { border-right: 0; border-bottom: 1px solid #3a4853; margin: 0; padding-right: 0; }
  .experience-focus { gap: 3.5rem; }
  .site-footer { display: grid; padding: 1.6rem 1.1rem; }
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after { transition-duration: .01ms !important; }
}
```

- [ ] **Step 4: Run the source and visual contracts**

Run:

```bash
python3 -m unittest tests/test_project_data.py tests/test_redesign_source.py -v
git diff --check
```

Expected: 10 tests PASS; `git diff --check` prints no output.

- [ ] **Step 5: Commit the visual system**

```bash
git add _sass/_site.scss tests/test_redesign_source.py
git commit -m "feat: style research portfolio homepage"
```

---

### Task 4: Validate rendered output, document maintenance, and publish

**Files:**
- Modify: `tests/test_site_contract.py`
- Modify: `README.md`
- Create locally, do not commit: `_site/`
- Create locally, do not commit: `.superpowers/verification/homepage-desktop-1440.png`
- Create locally, do not commit: `.superpowers/verification/homepage-mobile-390.png`

**Interfaces:**
- Consumes: the complete Jekyll source from Tasks 1–3.
- Produces: a deployed GitHub Pages homepage at `https://qq1982605092-hue.github.io/` with Pages status `built`.

- [ ] **Step 1: Replace the rendered-site contract**

Replace `tests/test_site_contract.py` with:

```python
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
            "Systems that help agents remember, reason, and act.",
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
```

- [ ] **Step 2: Update the maintenance documentation**

Add these bullets under `README.md` → `Maintenance map`:

```markdown
- `_data/projects.yml` is the content source for Selected Work; keep two evidence-based contribution bullets per project.
- `_includes/project-entry.html` renders each project and omits artifact links when none are verified.
- Browser acceptance requires real 1440 px and 390 px screenshots after every major layout change.
```

- [ ] **Step 3: Run all source tests before building**

Run:

```bash
python3 -m unittest tests/test_project_data.py tests/test_redesign_source.py -v
git diff --check
```

Expected: 10 tests PASS; whitespace check PASS.

- [ ] **Step 4: Attempt a native Jekyll build without changing global Ruby**

Run:

```bash
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll build --trace
```

Expected when a compatible Ruby is available: exit code 0 and `_site/index.html` exists. If Ruby 2.6 rejects current dependencies, stop local dependency work, record the exact error, and continue with source tests plus the real GitHub Pages build; do not change the system Ruby.

- [ ] **Step 5: Run rendered tests when `_site/index.html` exists**

Run:

```bash
python3 -m unittest tests/test_site_contract.py -v
```

Expected: 6 tests PASS. If local Jekyll remains unavailable, the suite reports one explicit SKIP rather than a false PASS.

- [ ] **Step 6: Preserve the user-provided binary assets**

Run before and after the redesign:

```bash
shasum -a 256 assets/images/profile/shu-cheng.png assets/files/Shu_Cheng_Resume.pdf
```

Expected hashes:

```text
48f7589bd67b5fe8bad4572c319d68141721c02ed935dfed1b313974828a3f3d  assets/images/profile/shu-cheng.png
4f797a794ffad441e38d71ba87b14fbc1a37255b2f855c137b1badeadaba856f  assets/files/Shu_Cheng_Resume.pdf
```

- [ ] **Step 7: Commit the verification contract and documentation**

```bash
git add tests/test_site_contract.py README.md
git commit -m "test: verify research portfolio output"
```

- [ ] **Step 8: Perform an independent pre-publication review**

Review the complete diff from the design-spec commit through the current HEAD. The reviewer must return:

- Spec compliance: PASS or FAIL.
- Code quality: APPROVED or CHANGES REQUESTED.
- Critical, Important, and Minor issues.

Required checks: no Fanhan homepage entry; no unsupported metrics; four project entries; explicit project CSS; mobile rules; original portrait and CV hashes; no Hao Shi biography or assets.

- [ ] **Step 9: Push the approved commits to `main`**

Run:

```bash
git status --short --branch
git push origin main
```

Expected: clean worktree before push; `main` updates successfully. If permissions, branch protection, or authentication blocks the push, stop and report the blocker without creating another branch.

- [ ] **Step 10: Wait for GitHub Pages and verify the public output**

Run:

```bash
gh api repos/qq1982605092-hue/qq1982605092-hue.github.io/pages --jq '{status,html_url,source}'
curl -sS -o /tmp/shu-cheng-homepage.html -w 'HTTP %{http_code} SIZE %{size_download}\n' https://qq1982605092-hue.github.io/
rg -n 'Systems that help agents|Dual-Time Agent Memory|Nuanwa Technology|Uceng Intelligence|Fanhan|Coming soon' /tmp/shu-cheng-homepage.html
```

Expected: Pages `status` is `built`, source is `main:/`, HTTP is 200, required content is present, and `Fanhan` plus `Coming soon` are absent.

- [ ] **Step 11: Capture and inspect real desktop and mobile screenshots**

Open the public homepage in the browser at 1440 × 1000 and 390 × 844. Save full-page captures to:

```text
.superpowers/verification/homepage-desktop-1440.png
.superpowers/verification/homepage-mobile-390.png
```

Inspect both captures for: thesis visible in the first viewport; portrait crop; project diagram and copy alignment; no horizontal overflow; mobile identity compact enough to expose the thesis; visible keyboard focus; readable footer.

- [ ] **Step 12: Report completion evidence**

Report the public URL, commit hashes, test totals, Pages status, HTTP status, screenshot paths, asset hashes, and any local Jekyll limitation. Do not claim native local compilation if the compatible runtime was unavailable.

---

## Final self-review checklist

- Task 1 owns the project data and validates its exact order and boundary.
- Task 2 owns semantic page structure and the Agent Memory to embodied-intelligence narrative.
- Task 3 owns every visual selector identified as missing in the prior review and includes mobile and reduced-motion behavior.
- Task 4 owns rendered output, binary preservation, independent review, deployment, live verification, and real screenshots.
- All names used by Liquid, YAML, tests, and SCSS match exactly.
- No implementation step requires a global Ruby, system configuration change, new branch, or new deployment target.
