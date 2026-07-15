# Academic Homepage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Replace the placeholder site with a Hao-Shi-inspired academic profile for Shu Cheng.

**Architecture:** Work from a clean clone at /Users/apple/Documents/jd/.githubio-implementation on the existing main branch, leaving the rejected local draft untouched. Adapt the MIT-licensed Jekyll academic-page structure used by Hao Shi. A Python standard-library contract test verifies the generated HTML before publication.

**Tech Stack:** Jekyll, Liquid, Markdown, SCSS, HTML5, Python unittest, GitHub Pages.

## Global Constraints

- Preserve https://qq1982605092-hue.github.io/ and publish from main root.
- Preserve the supplied portrait without AI face editing.
- Retain the MIT license notice for template code.
- White academic layout, dark text, one muted blue accent, no marketing effects.
- No unfinished VLA project, unverified metric, publication, award, or production claim.
- English-first, single-page first release.

---

### Task 1: Clean checkout and failing site contract

**Files:**
- Create: /Users/apple/Documents/jd/.githubio-implementation/tests/test_site_contract.py
- Create: /Users/apple/Documents/jd/.githubio-implementation/.gitignore

**Interfaces:**
- Consumes: existing remote main.
- Produces: isolated checkout and HTML contract.

- [ ] **Step 1: Clone without creating a branch**

~~~bash
git clone https://github.com/qq1982605092-hue/qq1982605092-hue.github.io.git /Users/apple/Documents/jd/.githubio-implementation
cd /Users/apple/Documents/jd/.githubio-implementation
git branch --show-current
~~~

Expected: main.

- [ ] **Step 2: Write the failing contract**

~~~python
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
        self.assertIn("I build memory and reasoning systems for embodied agents.", self.html)

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
~~~

- [ ] **Step 3: Verify RED**

~~~bash
python3 -m unittest tests/test_site_contract.py -v
~~~

Expected: error for missing _site/index.html.

- [ ] **Step 4: Ignore build artifacts and commit**

~~~gitignore
_site/
.jekyll-cache/
.sass-cache/
.bundle/
vendor/
~~~

~~~bash
git add tests/test_site_contract.py .gitignore
git commit -m "test: define academic homepage contract"
~~~

---

### Task 2: Jekyll academic foundation

**Files:**
- Create: Gemfile
- Create: _config.yml
- Create: _data/navigation.yml
- Create: _layouts/default.html
- Create: _includes/head.html
- Create: _includes/author-profile.html
- Create: assets/css/main.scss
- Create: _sass/_site.scss
- Modify: LICENSE

**Interfaces:**
- Consumes: site.author YAML values.
- Produces: responsive navigation, sticky identity rail, and compiled CSS.

- [ ] **Step 1: Add dependencies and identity**

~~~ruby
source "https://rubygems.org"
gem "github-pages", group: :jekyll_plugins
~~~

~~~yaml
locale: en-US
title: "Shu Cheng"
description: "Memory and reasoning systems for embodied agents."
url: "https://qq1982605092-hue.github.io"
baseurl: ""
repository: "qq1982605092-hue/qq1982605092-hue.github.io"
markdown: kramdown
author:
  name: "Shu Cheng (舒橙)"
  title: "M.S. Student in Computer Science"
  affiliation: "East China Normal University"
  location: "Shanghai, China"
  avatar: "/assets/images/profile/shu-cheng.png"
  email: "18074599386@163.com"
  github: "qq1982605092-hue"
  cv: "/assets/files/Shu_Cheng_Resume.pdf"
exclude: [tests, docs, README.md]
~~~

- [ ] **Step 2: Add navigation**

~~~yaml
main:
  - title: "About"
    url: "/#about"
  - title: "Selected Work"
    url: "/#selected-work"
  - title: "Experience"
    url: "/#experience"
  - title: "Education"
    url: "/#education"
  - title: "CV"
    url: "/assets/files/Shu_Cheng_Resume.pdf"
~~~

- [ ] **Step 3: Implement semantic layout**

The default layout renders a skip link, masthead, navigation, aside.profile, and main#main. The author include renders the supplied portrait, name, degree title, affiliation, location, email, GitHub, and CV from site.author. External links use rel="noreferrer".

- [ ] **Step 4: Implement the visual tokens**

~~~scss
:root {
  --paper: #ffffff;
  --ink: #202124;
  --muted: #68717d;
  --line: #e4e8ed;
  --accent: #315f9b;
  --page-width: 1180px;
  --profile-width: 250px;
}
~~~

Desktop uses a two-column layout with a sticky profile rail. Below 800px it becomes one column with a 132px portrait and scrollable navigation. The portrait uses object-fit: cover and object-position: 50% 24%, with no image filter.

- [ ] **Step 5: Preserve licensing and commit**

Append: "Adapted in 2026 for Shu Cheng's academic homepage. Personal text, portrait, and project assets are not covered by the template license."

~~~bash
git add Gemfile _config.yml _data _layouts _includes assets/css _sass LICENSE
git commit -m "feat: add academic profile foundation"
~~~

---

### Task 3: Verified profile content and assets

**Files:**
- Create: index.md
- Create: _includes/project-entry.html
- Copy: assets/images/profile/shu-cheng.png
- Copy: assets/files/Shu_Cheng_Resume.pdf

**Interfaces:**
- Consumes: default layout and project-entry include.
- Produces: About, Selected Work, Research Interests, Experience, Education, and workflow content.

- [ ] **Step 1: Implement reusable project entry**

~~~html
<article class="project-entry">
  <div class="project-media" aria-hidden="true"><span>{{ include.index }}</span></div>
  <div class="project-copy">
    <p class="project-label">{{ include.label }}</p>
    <h3>{{ include.title }}</h3>
    <p class="project-problem">{{ include.problem }}</p>
    {{ include.body }}
  </div>
</article>
~~~

- [ ] **Step 2: Write the identity story**

The first line is exactly: "I build memory and reasoning systems for embodied agents." The supporting copy connects current work in long-horizon memory, model post-training, retrieval adaptation, and multimodal systems to embodied intelligence without claiming completed VLA research.

- [ ] **Step 3: Add four selected works**

Use these titles: Dual-Time Agent Memory; State-Driven AI Calling Agent; Qwen3 Reranker Fine-tuning; Multimodal Structured Perception Pipeline. Each has one problem sentence and two contribution bullets. Do not include unsupported percentages or links.

- [ ] **Step 4: Add experience, education, and workflow**

Lead with AI Algorithm Engineering Intern at Nuanwa Technology, Shanghai. Education is exactly "East China Normal University — M.S. in Computer Science, 2025–2028". Include: "Agent harnesses: Codex, Claude Code, and Cursor for research prototyping, code review, experiment orchestration, and reproducible engineering workflows."

- [ ] **Step 5: Copy assets and commit**

~~~bash
mkdir -p assets/images/profile assets/files
cp /Users/apple/Documents/jd/qq1982605092-hue.github.io/assets/images/profile/shu-cheng.png assets/images/profile/shu-cheng.png
cp /Users/apple/Documents/jd/qq1982605092-hue.github.io/assets/Shu_Cheng_Resume.pdf assets/files/Shu_Cheng_Resume.pdf
git add index.md _includes/project-entry.html assets/images/profile/shu-cheng.png assets/files/Shu_Cheng_Resume.pdf
git commit -m "feat: add profile content and verified assets"
~~~

---

### Task 4: Build, responsive review, and publication

**Files:**
- Modify only for verified failures: _sass/_site.scss
- Modify only for verified failures: index.md
- Create: README.md

**Interfaces:**
- Consumes: complete Jekyll source.
- Produces: verified public main and GitHub Pages deployment.

- [ ] **Step 1: Build locally**

~~~bash
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll build --trace
~~~

Expected: exit 0 and _site/index.html exists.

- [ ] **Step 2: Verify GREEN**

~~~bash
python3 -m unittest tests/test_site_contract.py -v
~~~

Expected: 5 tests, 0 failures.

- [ ] **Step 3: Inspect responsive previews**

Run bundle exec jekyll serve --host 127.0.0.1 --port 4173 and inspect 1440x1000 plus 390x844. Verify portrait crop, navigation, stacking, readable type, focus states, and no horizontal overflow.

- [ ] **Step 4: Validate source boundaries**

Search source and generated HTML for Hao Shi, his research titles, and forbidden metrics. Expected: no copied biography or research content; Hao Shi may appear only in attribution documentation.

- [ ] **Step 5: Document maintenance and commit**

README records public URL, build commands, index.md, _sass/_site.scss, asset paths, and MIT attribution.

~~~bash
git add README.md index.md _sass/_site.scss
git commit -m "docs: document homepage maintenance"
git status --short
~~~

Expected: clean.

- [ ] **Step 6: Publish existing main and verify**

~~~bash
git push origin main
gh api repos/qq1982605092-hue/qq1982605092-hue.github.io/pages --jq '{status,html_url,source}'
curl -I -L --max-time 20 https://qq1982605092-hue.github.io/
~~~

Expected: Pages status built, source main root, HTTP 200.

