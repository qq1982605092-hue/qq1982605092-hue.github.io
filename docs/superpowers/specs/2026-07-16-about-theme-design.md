# About Narrative and Theme Toggle Design

Date: 2026-07-16

## Goal

Add a real About section and a site-wide light/dark theme control without making the homepage denser or turning the biography into a technology list.

The About section should explain the credible progression behind the portfolio:

> agent memory and model post-training -> multimodal and industrial perception -> memory-augmented embodied agents

It must distinguish implemented experience from future research direction. It must not imply completed VLA, real-robot, robot-foundation-model, or reinforcement-learning work.

## Visual thesis

Use an editorial academic layout: strong typographic rhythm, a thin divider, a small uppercase section label, and two readable biography paragraphs. The light theme keeps the current white and blue palette. The dark theme uses charcoal surfaces, warm off-white text, and a restrained blue-green accent.

The design borrows the reference site's information hierarchy, not its biography, titles, metrics, or exact visual skin.

## Content plan

### Hero

Keep the existing compact hero, portrait, research statement, and links. The hero remains the first-view identity statement.

### About

Create a separate section between Hero and Selected Work. Move the `about` anchor from the Hero to this section so the navigation label points to actual biographical content.

Use a two-column editorial structure on desktop:

- left: small uppercase `ABOUT` label;
- right: two paragraphs with a maximum readable line length;
- mobile: stack the label above the text.

Approved narrative content:

1. Current identity and research question: an M.S. student in Computer Science at East China Normal University working across agent memory, model post-training, and multimodal systems; interested in how agents retain experience, make inspectable decisions, and turn perception into reliable action over long horizons.
2. Evidence and direction: state-driven agent workflows and task-specific training at Nuanwa Technology; earlier industrial vision integration with downstream production and control systems at Uceng Intelligence; current exploration of memory-augmented embodied agents.

Use emphasis sparingly on the university, the two organizations, and the embodied-agent direction. Do not add cards, tags, statistics, a second portrait, or unsupported model-training claims.

Because the About section now carries the narrative bridge, compress the existing `Current focus` copy to avoid repeating the same paragraph later on the page.

### Selected Work and later sections

Keep the existing project order, research questions, and experience entries. No project claims change in this scope.

## Theme system

Add one icon button at the right edge of the primary navigation.

- Moon icon means the current light page can switch to dark.
- Sun icon means the current dark page can switch to light.
- Button has an accessible label that describes the action, not merely the icon.
- Minimum interactive size is 44 by 44 pixels.

Theme selection rules:

1. On first visit, follow `prefers-color-scheme`.
2. After an explicit toggle, store `light` or `dark` in `localStorage` under `site-theme`.
3. Apply the stored preference before the stylesheet paints to avoid a visible flash.
4. Set `color-scheme` so native controls match the active theme.
5. If storage is unavailable, the toggle still works for the current page without throwing an error.

Use CSS custom properties for both themes. All existing sections, project pages, navigation, diagrams, borders, footer, and links must remain readable in both modes. Theme transitions are short and disabled when `prefers-reduced-motion: reduce` is active.

## Interaction thesis

- Preserve the existing restrained hero entrance.
- Animate theme colors with a short surface/text transition, not a full-page effect.
- Give the theme icon a small rotation/cross-fade when toggled.
- Keep link and project affordance motion unchanged.

## Component boundaries

- `_includes/head.html`: early theme bootstrap and theme-color metadata.
- `_layouts/default.html`: semantic theme-toggle button and small dependency-free script.
- `index.md`: new About section and reduced duplicate focus copy.
- `_sass/_site.scss`: theme tokens, button styles, About layout, responsive states, and reduced-motion behavior.

No framework or external icon library is added. Icons are inline SVG.

## Accessibility and failure behavior

- Toggle is a native `<button type="button">` with an updated `aria-label` and `title`.
- Decorative SVGs are hidden from assistive technology.
- Keyboard focus remains clearly visible in both themes.
- Text and interactive controls target WCAG AA contrast.
- With JavaScript disabled, the system-preferred theme still renders through CSS and all content remains available.
- With local storage blocked, the control changes the current document theme but does not persist it.

## Verification

1. Add source-contract tests for a separate About section, narrative boundaries, the toggle button, storage key, and theme tokens.
2. Run the complete clean-target test suite and `git diff --check`.
3. Build through GitHub Pages and require a successful deployment workflow.
4. Capture and inspect desktop and mobile screenshots in both light and dark themes.
5. Verify the homepage and three project pages return HTTP 200.
6. Confirm the public page contains no unsupported VLA, real-robot, or inflated leadership claims.

## Acceptance criteria

- `About` navigation lands on a distinct biography section below the Hero.
- The biography explains identity, evidence, and embodied-agent direction in two paragraphs.
- Light/dark selection works across homepage and project pages and survives reload.
- The control is usable by pointer, keyboard, and assistive technology.
- Desktop and mobile layouts have no clipping or horizontal overflow.
- Existing unrelated working-tree changes are not included in this feature's commits.
