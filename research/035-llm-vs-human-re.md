# LLMs vs Human Experts in Requirements Engineering

**Paper:** Analysis of LLMs vs Human Experts in Requirements Engineering  
**URL:** https://arxiv.org/abs/2501.19297  
**Date:** Jan 2025  
**Venue:** arXiv preprint

---

## The Core Idea

Requirements elicitation is expensive and hard. This paper empirically compares LLM-generated requirements to human expert-generated requirements.

Key findings reported:
- LLM requirements were rated **more aligned** (+~1.12 on their scale) and trended **more complete** (+~10.2%).
- LLM output was **~720× faster** and **~0.06% of cost** versus human experts.
- Participants sometimes *perceived* human work as more aligned even when ratings favored the LLM.

---

## Why This Matters

This is direct evidence for your product thesis:
> A nontechnical but AI-savvy operator can get “expert-like” requirements quality by using LLMs, if they have a structured process.

It supports building an operator-facing pipeline that spends heavy effort on requirements quality up front.

---

## Critical Caveats

1. **Study context matters:** results depend on the task framing and evaluation rubric.
2. **Perception gap:** humans may mistrust LLM output even when it’s good—explanations and evidence help.
3. **Still needs acceptance criteria:** “aligned requirements” aren’t executable until translated into tests/AC.

---

## Relevance to Knowledge & Vibes

### Supports
- Making REQ/AC the primary operator deliverable.
- Treating requirements as first-class artifacts that drive the entire plan.

### Practical implication
Add a dedicated “requirements quality pass” (ambiguity/completeness/consistency) before architecture decisions.

