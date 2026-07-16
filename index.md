---
layout: default
title: Home
---

<section class="hero">
  <div class="hero-copy">
    <p class="eyebrow">MEMORY · AGENTS · EMBODIED AI</p>
    <h1 class="hero-name">Cheng Shu</h1>
    <p class="hero-topics">Agent memory · model post-training · multimodal systems</p>
    <p class="hero-statement">I build memory and reasoning systems for long-horizon agents — and study how these capabilities can support embodied intelligence.</p>
    <p class="hero-links">
      <a class="hero-link-primary" href="#selected-work">Selected work</a>
      <a href="mailto:{{ site.author.email }}">Email</a>
      <a href="https://github.com/{{ site.author.github }}">GitHub</a>
      <a href="{{ site.author.cv | relative_url }}">CV</a>
    </p>
  </div>
  {% include author-profile.html %}
</section>

<section id="about" class="page-section about-section">
  <p class="about-label">About</p>
  <div class="about-copy">
    <p>I’m an M.S. student in Computer Science at <strong>East China Normal University</strong>, working at the intersection of agent memory, model post-training, and multimodal systems. My central question is how an agent can retain useful experience, make inspectable decisions, and eventually turn perception into reliable action over long horizons.</p>
    <p>At <strong>Nuanwa Technology</strong>, I build state-driven agent workflows and task-specific model adaptation pipelines. Earlier, at <strong>Uceng Intelligence</strong>, I connected industrial vision outputs with downstream production and control systems, gaining experience across the loop from perception to physical execution. I’m now exploring how these pieces can support <strong>memory-augmented embodied agents</strong>.</p>
  </div>
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
    <p>I am now focused on turning these foundations into memory-augmented agents that can reason and act reliably over long horizons.</p>
    <p class="focus-tags"><span>Agent Memory</span><span>Post-training</span><span>Retrieval</span><span>Multimodal Systems</span><span>Embodied AI</span></p>
  </div>
</section>
