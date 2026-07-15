---
layout: project
permalink: "/projects/calling-agent/"
title: "Strategy-Driven AI Calling Agent"
kicker: "Agent systems · Production orchestration"
description: "A memory-aware conversational Agent with inspectable strategy routing and predictive fast-path inference."
question: "How can open-ended model behavior become a controllable workflow without reducing every conversation to a rigid script?"
answer: "Separate state, strategy selection, generation, review, and prediction into modules with an observable fast path and fallback path."
facts:
  - label: "System shape"
    value: "Fast path + fallback path"
  - label: "Control layer"
    value: "Markdown strategy library"
  - label: "Validation"
    value: "Offline replay harness"
---

## The question, expanded

A production conversation has two competing requirements. It must respond flexibly to language, but its actions should still be inspectable and recoverable. I designed this Agent around a simple separation: **Memory records the interaction, routing chooses intent-level behavior, generation realizes that behavior, and replay makes the path observable**.

<div class="system-diagram" role="img" aria-label="The calling Agent uses memory and cached predictions, then chooses either a reranked fast path or a router-generator fallback before verification and state update.">
  <span class="diagram-label">Runtime loop</span>
  <div class="diagram-flow">
    <div class="diagram-node"><strong>Memory</strong><small>Write input, recent history, and evolving summary</small></div>
    <div class="diagram-node"><strong>Prediction Cache</strong><small>Read candidates prepared after the previous turn</small></div>
    <div class="diagram-node diagram-node--accent"><strong>Rerank decision</strong><small>Match the current input against predicted directions</small></div>
    <div class="diagram-node"><strong>Fast path</strong><small>FastComposer, or Fallback path through Router and Generator</small></div>
    <div class="diagram-node"><strong>Verifier → response</strong><small>Optional review, Memory update, then Predictor prepares the next turn</small></div>
  </div>
</div>

## What I built

- **Memory** maintains full history, a recent-turn window, and a model-generated state summary.
- **Router** loads a Markdown strategy library and selects a strategy from the current input, summary, and recent context.
- **Generator** combines the selected objective, knowledge slots, constraints, and conversation context into a bounded response.
- **Verifier** can inspect the draft against strategy constraints and request a limited number of revisions.
- **Predictor** prepares likely next-turn directions; **Prediction Cache**, **Rerank**, and **FastComposer** form a low-latency route when a candidate matches.

The important design choice is not any one model call. It is the fallback structure: the Agent can exploit prepared candidates when confidence is sufficient, while retaining a general Router–Generator route when the prediction does not fit.

## Evidence

The implemented runtime records which route produced a response. I also built an **offline replay** workflow that runs conversations through the same orchestration path and exports prompts, outputs, chosen strategies, rerank scores, route labels, and elapsed time for later inspection.

<div class="evidence-grid">
  <div class="evidence-card"><span>Memory surface</span><strong>3 views</strong><p>Full history, recent context, and compressed state summary</p></div>
  <div class="evidence-card"><span>Control surface</span><strong>7 strategies</strong><p>Externally maintained Markdown strategy definitions</p></div>
  <div class="evidence-card"><span>Prediction surface</span><strong>5 candidates</strong><p>Prepared directions cached for the following turn</p></div>
</div>

The replay artifact is the core engineering evidence: it turns a multi-module Agent from a black box into a sequence that can be inspected by route, decision, output, and timing.

## What this does not prove

<div class="project-boundary">
  <h3>Public claim boundary</h3>
  <p>This case study reports implemented orchestration paths and replay instrumentation only. It makes no model-training, business-outcome, or production-performance claim, and the review module is treated as an additional control layer rather than an absolute safety guarantee.</p>
</div>

## Why this matters for embodied agents

<div class="project-next">
  <h3>Keep policy and execution inspectable</h3>
  <p>A robot policy also needs memory, action selection, execution constraints, and a recovery route when a prediction fails. This project gives me an engineering vocabulary for those boundaries: observable state, explicit routing, bounded generation, and replayable decisions.</p>
</div>
