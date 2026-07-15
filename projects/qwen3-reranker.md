---
layout: project
title: "Qwen3 Reranker Fine-tuning"
kicker: "Model post-training · Domain retrieval"
description: "LoRA fine-tuning a Qwen3 reranker for domain-specific query-clause relevance."
question: "How can a ranking model learn domain relevance when surface-level semantic similarity is not enough?"
answer: "Train on explicit query-document decisions with controlled positives and hard negatives, then separate data versions from checkpoint evaluation."
facts:
  - label: "Base model"
    value: "Qwen3-Reranker-0.6B"
  - label: "Training"
    value: "LoRA SFT"
  - label: "Current data"
    value: "15,704 train · 1,749 val"
---

## The question, expanded

Retrieval errors in domain documents often look plausible: two clauses share vocabulary, but only one answers the user's intent. I treated reranking as a supervised decision problem—given a query and one candidate document, the model must explain its ranking through a simple relevance decision learned from **carefully constructed positives and negatives**.

<div class="system-diagram" role="img" aria-label="A query and candidate clause are formatted into a pointwise training pair, evaluated by a LoRA-adapted Qwen3 reranker, and used to reorder upstream candidates.">
  <span class="diagram-label">Training and inference path</span>
  <div class="diagram-flow">
    <div class="diagram-node"><strong>Query</strong><small>A domain intent such as waiting period or exclusion</small></div>
    <div class="diagram-node"><strong>Candidate clause</strong><small>One document returned by the upstream retriever</small></div>
    <div class="diagram-node"><strong>Training pair</strong><small>1 positive + 3 negatives for each supervised unit</small></div>
    <div class="diagram-node diagram-node--accent"><strong>Qwen3-Reranker-0.6B</strong><small>LoRA SFT with pointwise yes/no relevance supervision</small></div>
    <div class="diagram-node"><strong>Reordered candidates</strong><small>Relevant clauses move forward; noise moves back</small></div>
  </div>
</div>

## What I built

The project adapts **Qwen3-Reranker-0.6B** with **LoRA SFT**. Each example presents a query-document pair and supervises a **pointwise yes/no** relevance decision. A training unit contains **1 positive + 3 negatives**, which makes negative selection part of the modeling problem rather than a preprocessing footnote.

At inference time, the model receives candidates already produced upstream and reorders them. Error analysis focuses on false positives that share domain vocabulary but fail to answer the actual query, and on false negatives where the correct evidence is expressed indirectly.

## Evidence

The project currently contains two evidence layers that must not be merged.

<div class="evidence-grid">
  <div class="evidence-card"><span>Current data assets</span><strong>15,704</strong><p>Training samples in the latest prepared dataset</p></div>
  <div class="evidence-card"><span>Current data assets</span><strong>1,749</strong><p>Validation samples in the latest prepared dataset</p></div>
  <div class="evidence-card"><span>Archived evaluation</span><strong>checkpoint-135</strong><p>Evaluated on an earlier validation split</p></div>
  <div class="evidence-card"><span>Archived accuracy</span><strong>85.39%</strong><p>Pointwise yes/no accuracy on the earlier split</p></div>
  <div class="evidence-card"><span>Archived negative recall</span><strong>93.12%</strong><p>4,073 / 4,374 negative candidates correctly rejected</p></div>
</div>

The archived checkpoint result is **not a current-data evaluation**. Keeping that label visible is essential: the current 15,704 / 1,749 assets and the **checkpoint-135** report belong to different experiment versions.

## What this does not prove

<div class="project-boundary">
  <h3>Evaluation boundary</h3>
  <p>The archived result supports the feasibility of domain adaptation, but it cannot be presented as the evaluation of the latest data assets. The model only reorders candidates supplied by an upstream retrieval stage; it does not search the entire document collection by itself.</p>
</div>

## What I would test next

<div class="project-next">
  <h3>Make data design measurable</h3>
  <p>The next controlled study is to hold model and training budget constant while varying negative construction: random negatives, lexical confounders, and retrieval-derived hard negatives. That would turn the current error-analysis intuition into a defensible claim about which training examples improve ranking.</p>
</div>
