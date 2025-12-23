# From Requirements to Code (How Practitioners Actually Work with LLMs)

**Paper:** From Requirements to Code: Understanding Developer Practices in LLM-Assisted Software Engineering  
**URL:** https://arxiv.org/abs/2507.07548  
**Date:** Jul 2025  
**Venue:** arXiv preprint (accepted to RE per author announcements)

---

## The Core Idea

Interviews with practitioners show that “requirements” as normally written are too abstract for direct LLM code generation.

What developers actually do:
- **decompose** requirements into concrete programming tasks
- enrich prompts with **design constraints** (architecture boundaries, infra constraints)
- include **interfaces/data formats/tests** to make generated code integrable

In other words: RE remains necessary, but LLMs shift the work toward *decomposition + constraint packaging*.

---

## Why This Matters

This paper is strong evidence that your system’s core mechanics are right:
- breaking work into bead-sized tasks
- forcing explicit contracts/tests
- capturing architectural constraints in artifacts

It also suggests that an operator-led pipeline should focus on generating the *promptable task units* (beads) rather than expecting a single requirements doc to “compile into code.”

---

## Critical Caveats

1. Practitioner interviews reflect current tooling (2024–2025); patterns may evolve as models improve.
2. It’s descriptive (what people do), not a controlled benchmark; still highly relevant for workflow design.

---

## Relevance to Knowledge & Vibes

### Supports
- Your “lossless decomposition” approach (requirements → programming tasks).
- Embedding constraints + tests + interfaces into each task/bead.

### Practical implication
Make “task packaging” (context + constraints + acceptance tests) an explicit pipeline stage for nontechnical users.

