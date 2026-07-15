---
layout: default
title: Home
---

<section id="about" class="page-section about-section">
  <h2>About</h2>
  <p class="lead">I build memory and reasoning systems for embodied agents.</p>
  <p>My current work studies long-horizon memory, model post-training, retrieval adaptation, and multimodal systems. I am interested in how these capabilities can give embodied agents more persistent context, grounded perception, and reliable decision support.</p>
</section>

<section id="selected-work" class="page-section">
  <h2>Selected Work</h2>

  {% capture dual_time_body %}
  <ul>
    <li>Designed a research prototype that organizes interaction evidence across event time and knowledge-update time.</li>
    <li>Developing retrieval experiments around temporal consistency, evidence traceability, and long-horizon recall.</li>
  </ul>
  {% endcapture %}
  {% include project-entry.html
    index="01"
    label="Research in progress"
    title="Dual-Time Agent Memory"
    problem="Long-horizon agents need memory structures that preserve event sequences while tracking how knowledge changes over time."
    body=dual_time_body
  %}

  {% capture calling_agent_body %}
  <ul>
    <li>Built state-driven orchestration that separates dialogue stages, transition conditions, and system actions.</li>
    <li>Worked on model post-training and production integration to make agent behavior easier to inspect and control.</li>
  </ul>
  {% endcapture %}
  {% include project-entry.html
    index="02"
    label="Agent systems"
    title="State-Driven AI Calling Agent"
    problem="Production calling agents must coordinate dialogue state, business rules, model behavior, and external actions without losing control of the interaction."
    body=calling_agent_body
  %}

  {% capture reranker_body %}
  <ul>
    <li>Constructed domain-focused training data and evaluation cases for relevance ranking.</li>
    <li>Fine-tuned a Qwen3 reranker and analyzed retrieval errors to guide data and modeling revisions.</li>
  </ul>
  {% endcapture %}
  {% include project-entry.html
    index="03"
    label="Retrieval adaptation"
    title="Qwen3 Reranker Fine-tuning"
    problem="Domain retrieval requires ranking models that distinguish task-specific relevance beyond general semantic similarity."
    body=reranker_body
  %}

  {% capture perception_body %}
  <ul>
    <li>Integrated OCR and vision-language components to extract complementary visual and textual evidence.</li>
    <li>Designed structured schemas and validation steps so downstream systems can consume the results consistently.</li>
  </ul>
  {% endcapture %}
  {% include project-entry.html
    index="04"
    label="Multimodal perception"
    title="Multimodal Structured Perception Pipeline"
    problem="Screen and video content must be converted from pixels and text into consistent records that reasoning systems can use."
    body=perception_body
  %}
</section>

<section id="research-interests" class="page-section">
  <h2>Research Interests</h2>
  <ul class="research-questions">
    <li>How can long-horizon agents retain useful experience while keeping changing knowledge temporally consistent?</li>
    <li>How can reasoning and decision learning make embodied agents more adaptive, grounded, and reliable?</li>
    <li>How should multimodal models be post-trained and evaluated for structured perception and agent use?</li>
  </ul>
</section>

<section id="experience" class="page-section">
  <h2>Experience</h2>
  <div class="timeline-entry">
    <h3>AI Algorithm Engineering Intern</h3>
    <p class="entry-meta">Nuanwa Technology · Shanghai · 2026–Present</p>
    <p>Developing agent memory, model post-training, and state-driven AI systems for applied workflows.</p>
  </div>
  <div class="timeline-entry">
    <h3>Java Backend Development Intern</h3>
    <p class="entry-meta">Fanhan Information Technology · Shanghai · 2025.03–2025.06</p>
    <p>Developed and maintained backend services and supporting application interfaces.</p>
  </div>
  <div class="timeline-entry">
    <h3>Python Systems R&amp;D Intern</h3>
    <p class="entry-meta">Uceng Intelligence · Shanghai · 2024.03–2024.08</p>
    <p>Built Python-based system components and data-processing workflows.</p>
  </div>
</section>

<section id="education" class="page-section">
  <h2>Education</h2>
  <p><strong>East China Normal University — M.S. in Computer Science, 2025–2028</strong></p>
</section>

<section id="workflow" class="page-section workflow-note">
  <h2>Workflow</h2>
  <p>Agent harnesses: Codex, Claude Code, and Cursor for research prototyping, code review, experiment orchestration, and reproducible engineering workflows.</p>
</section>
