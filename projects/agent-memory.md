---
layout: project
permalink: "/projects/agent-memory/"
title: "EvoWalker Agent Memory"
kicker: "Research · Long-horizon agent memory"
description: "A temporal memory graph and query-conditioned retrieval system for long-horizon agents."
question: "How can an agent preserve what happened while still knowing which version of a fact is valid now?"
answer: "Represent memory as evolving evidence, then let each query decide how to traverse relations and recover source detail."
facts:
  - label: "Evaluation"
    value: "1,540 LoCoMo questions"
  - label: "Verified result"
    value: "85.78% overall"
  - label: "Status"
    value: "Research in progress"
---

## The question, expanded

A long-horizon agent does not only need more storage. It needs to distinguish an event from the model's later knowledge of that event, connect evidence across sessions, and still recover the original wording when a compressed fact is insufficient. My working hypothesis is that **memory should be a queryable temporal structure rather than a bag of isolated text chunks**.

<div class="system-diagram" role="img" aria-label="EvoWalker turns conversations into temporal facts, traverses a typed graph, and recovers source evidence for answering.">
  <span class="diagram-label">Method overview</span>
  <div class="diagram-flow">
    <div class="diagram-node"><strong>Sessions</strong><small>Long-running interaction history</small></div>
    <div class="diagram-node"><strong>Fact extraction</strong><small>Compact claims with source pointers</small></div>
    <div class="diagram-node"><strong>Temporal graph</strong><small>Intra-session, cross-session, and update relations</small></div>
    <div class="diagram-node diagram-node--accent"><strong>Query-conditioned walk</strong><small>Multiple starts, typed propagation, temporal reranking</small></div>
    <div class="diagram-node"><strong>Evidence recovery</strong><small>Facts plus utterance, local-window, and session context</small></div>
  </div>
</div>

## What I built

The system stores natural-language facts with source identifiers, recorded time, and a validity interval. When a new fact updates an earlier one, the older fact remains traceable but its active interval is closed. Three relation families then serve different retrieval needs:

- **Intra-session relations** preserve local conversational context.
- **Cross-session relations** connect semantically aligned evidence over long gaps.
- **Update relations** retain the sequence between earlier and later states.

At query time, several relevant facts initialize a restartable random walk. The query changes how relation types contribute to propagation; temporal reranking then distinguishes current and historical evidence. Finally, the system returns to the source utterances and retrieves local windows and session-level context to recover details lost during fact compression.

## Evidence

The current end-to-end run covers the four non-adversarial LoCoMo categories. Answers and evaluation use GPT-4o-mini with the **LoCoMo official LLM-as-a-Judge** policy. The verified aggregate is **1,321 / 1,540** correct, or **85.78%** overall.

<div class="evidence-grid">
  <div class="evidence-card"><span>Multi-hop</span><strong>75.89%</strong><p>214 / 282 questions</p></div>
  <div class="evidence-card"><span>Temporal</span><strong>80.69%</strong><p>259 / 321 questions</p></div>
  <div class="evidence-card"><span>Open-domain</span><strong>71.88%</strong><p>69 / 96 questions</p></div>
  <div class="evidence-card"><span>Single-hop</span><strong>92.63%</strong><p>779 / 841 questions</p></div>
  <div class="evidence-card"><span>Overall</span><strong>85.78%</strong><p>1,321 / 1,540 questions</p></div>
</div>

The category pattern is itself useful: single-hop recall is comparatively stable, while open-domain and multi-hop questions leave more room for better evidence assembly. I treat that as an error-analysis direction, not as proof that any single module caused the result.

## What this does not prove

<div class="project-boundary">
  <h3>Current evidence boundary</h3>
  <p>The end-to-end result is verified, but matched ablations are not yet complete. It therefore does not isolate the contribution of the graph walk, temporal calibration, or raw-evidence recovery. The existing raw-only LongMemEval result is not reported as an EvoWalker result; a full evaluation under the same construction, retrieval, answer, and judge protocol remains future work.</p>
</div>

## Embodied-agent connection

<div class="project-next">
  <h3>From conversational memory to persistent world state</h3>
  <p>Embodied agents face the same underlying problem at a harder scale: an observation may become outdated, an instruction may refer to an earlier event, and a decision should remain traceable to the evidence that supported it. The next step is to replace dialogue-only facts with multimodal events and test whether temporal validity and query-conditioned traversal improve long-horizon task completion.</p>
</div>
