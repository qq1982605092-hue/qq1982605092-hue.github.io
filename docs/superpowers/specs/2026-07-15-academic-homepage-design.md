# Shu Cheng Academic Homepage Design

Date: 2026-07-15

## 1. Goal

Build an English-first academic homepage for Shu Cheng, aimed at embodied-intelligence, VLA, Agent, and research internship opportunities.

The visitor should understand within ten seconds:

> I build memory and reasoning systems for embodied agents.

The page must connect current evidence—Agent Memory, LLM post-training, retrieval fine-tuning, multimodal perception, and AI-system integration—to the longer-term embodied-agent direction without presenting unfinished VLA work as completed research.

## 2. Reference and adaptation

Use the open-source structure of Hao Shi's academic homepage as the primary reference:

- Reference site: <https://shihao1895.github.io/>
- Reference repository: <https://github.com/shihao1895/shihao1895.github.io>
- License: MIT; retain the original license notice for reused template code.

Reuse the restrained academic layout, not Hao Shi's identity, copy, images, publications, claims, or research assets.

## 3. Visual thesis

A quiet, white academic page that feels credible before it feels designed: compact navigation, a persistent identity column, editorial typography, generous whitespace, one academic-blue accent, and project evidence presented as illustrated research entries rather than cards.

### Visual rules

- White background with dark charcoal text.
- One muted academic-blue accent for links and section rules.
- No gradients, glass effects, dashboards, metric tiles, or marketing slogans.
- Maximum two typefaces; prioritize readable system and serif/sans academic typography.
- Desktop uses a left identity sidebar and a wider reading column.
- Mobile stacks identity above content and keeps all links touch-friendly.
- Motion is limited to subtle link and image hover feedback; no entrance spectacle or scroll animation.

## 4. Information architecture

Top navigation:

1. Home
2. Selected Work
3. Experience
4. Education
5. CV

Single-page sections appear in this order:

### Identity sidebar

- Portrait
- Shu Cheng (舒橙)
- M.S. Student in Computer Science
- East China Normal University
- Shanghai, China
- Email
- GitHub
- CV

Google Scholar and ORCID are omitted until genuine profiles are available.

### About

Two short paragraphs only:

1. Current identity and the research problems of interest.
2. The progression from memory and reasoning systems toward embodied agents.

The fixed opening line is:

> I build memory and reasoning systems for embodied agents.

### Selected Work

Use four featured entries in this order:

1. Dual-Time Agent Memory — long-horizon memory organization and retrieval research.
2. State-Driven AI Calling Agent — agent state machine, LLM post-training, and production-system integration.
3. Qwen3 Reranker Fine-tuning — domain retrieval, training-data construction, and ranking-model adaptation.
4. Multimodal Structured Perception Pipeline — screen/video understanding, OCR/VLM extraction, and structured outputs.

Each entry uses the same evidence-oriented format:

- one representative image or diagram;
- project title and domain label;
- one sentence defining the problem;
- two concise contribution bullets;
- links only when a real code repository, report, demo, or artifact exists.

No unpublished accuracy, latency, SOTA, paper-acceptance, or production-impact claim is displayed without a traceable artifact.

### Experience

Lead with the recent Nuanwa experience. Describe responsibility and system ownership, then connect the work to the selected projects. Earlier experience is compressed to one or two lines per role.

### Research Interests

Keep three coherent themes, written as research questions rather than a keyword list:

- Memory for long-horizon agents
- Reasoning and decision learning for embodied agents
- Post-training and evaluation of multimodal models

### Education

- East China Normal University — M.S. in Computer Science, 2025–2028

Do not repeat the degree in the About paragraph and Education section. Do not append “expected” to the date.

### Tools and workflow

Do not create a dense technology wall. Mention tools where they explain how work was performed. A single compact line near the bottom may state:

> Agent harnesses: Codex, Claude Code, and Cursor for research prototyping, code review, experiment orchestration, and reproducible engineering workflows.

## 5. Content voice

- English-first, concise, factual, and research-oriented.
- Describe problems and decisions before naming frameworks.
- Prefer “built / designed / evaluated / integrated” followed by evidence.
- Avoid “passionate,” “cutting-edge,” “expert,” and other unsupported self-evaluation.
- Do not present current learning goals as completed projects.

## 6. Technical architecture

- Jekyll site compatible with native GitHub Pages.
- Adapt the MIT-licensed academic-page structure used by the reference site.
- Main content lives in a small number of Markdown/YAML files so future projects and publications can be added without rewriting layout code.
- Project images live under `assets/images/projects/`.
- CV lives under `assets/files/`.
- No database, analytics tracker, contact form backend, or JavaScript framework.
- Preserve the existing public URL: <https://qq1982605092-hue.github.io/>.

## 7. Responsive and accessibility requirements

- Usable at 375 px mobile width and common desktop widths.
- Portrait, project images, and icons have meaningful alternative text.
- Keyboard-visible focus states for navigation and external links.
- Body text contrast meets WCAG AA.
- Page remains understandable with CSS or JavaScript disabled.

## 8. Verification

Before publication:

1. Build the Jekyll site locally without errors.
2. Check desktop and mobile screenshots.
3. Confirm there are no copied biographies, claims, or research assets from the reference site.
4. Confirm all project claims against the resume, repositories, reports, or local evidence.
5. Validate internal links, CV download, email link, GitHub link, favicon, and image paths.
6. Push to `main`, wait for GitHub Pages status `built`, and verify the public URL returns HTTP 200.

## 9. Explicit exclusions for the first release

- No Publications section until there is a genuine publication or preprint.
- No Honors, Talks, Service, Blog, dark mode, bilingual toggle, or visitor analytics.
- No unfinished ManiSkill, LeRobot, OpenVLA, or Memory-enhanced VLA project presented as completed work.
- No skill grid or résumé-style wall of technologies.

