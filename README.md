# Shu Cheng academic homepage

Single-page Jekyll site for [qq1982605092-hue.github.io](https://qq1982605092-hue.github.io/), published from the `main` branch root.

## Maintenance map

- `index.md` is the homepage content and section order.
- `_layouts/default.html` and `_includes/` provide the shared page structure.
- `_sass/_site.scss` contains the responsive layout and visual tokens; `assets/css/main.scss` imports it.
- `_data/navigation.yml` controls the masthead links.
- `_data/projects.yml` is the content source for Selected Work; keep two evidence-based contribution bullets per project.
- `_includes/project-entry.html` renders each project and omits artifact links when none are verified.
- Browser acceptance requires real 1440 px and 390 px screenshots after every major layout change.
- `assets/images/profile/shu-cheng.png` is the supplied portrait.
- `assets/files/Shu_Cheng_Resume.pdf` is the linked CV.

The old root-level placeholder `index.html` is intentionally absent. Keeping it beside `index.md` would let a static file shadow the Jekyll-generated homepage on GitHub Pages.

## Local build and preview

Use a Ruby version supported by the `github-pages` gem:

```bash
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll build --trace
bundle exec jekyll serve --host 127.0.0.1 --port 4173
```

The build output is `_site/index.html`. The repository contract can be checked with:

```bash
python3 -m unittest tests/test_site_contract.py -v
git diff --check
```

## Attribution

The layout structure is adapted from the MIT-licensed academic homepage pattern by Hao Shi. The MIT notice is retained in `LICENSE`; Shu Cheng's text, portrait, and project assets are personal material and are not covered by the template license.
