# LLMs in Requirements Engineering (Systematic Guideline)

**Paper:** Using Large Language Models for Natural Language Processing Tasks in Requirements Engineering: A Systematic Guideline  
**URL:** https://arxiv.org/abs/2402.13823  
**Date:** Feb 2024  
**Venue:** arXiv preprint

---

## The Core Idea

This paper provides a structured guideline for selecting how to use LLMs in requirements engineering (RE), based on:
- whether you want **automation** vs **human support**
- whether the task is **understanding** (classification/extraction) vs **generation** (summaries/specs)
- what training data exists (fine-tune vs prompt vs retrieve)

The key contribution for practitioners is the “decision framework” mindset: choose the method based on task type and risk, not fashion.

---

## Why This Matters

For a nontechnical operator, RE is the hardest phase. This paper supports making RE a **structured sequence of NLP tasks** (extract → normalize → validate) rather than a single brainstorming session.

It also supports your selective grounding approach: for large contexts and factual constraints, retrieval augmentation is often the right tool.

---

## Critical Caveats

1. It’s a **guideline** paper, not a benchmark proving a single best workflow.
2. It spans many RE tasks; your system should pick the subset that drives correctness (ambiguity detection, completeness checks, acceptance criteria).

---

## Relevance to Knowledge & Vibes

### Supports
- Turning ideation into a series of controlled RE sub-tasks.
- Deciding “truth source” (codebase/docs/history) explicitly.

### Practical implication
Add an explicit “RE task routing” step: each requirement is processed by (extract → QA → AC) rather than freeform drafting.

