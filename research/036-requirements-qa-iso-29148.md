# Requirements QA with LLMs (ISO 29148)

**Paper:** Leveraging LLMs for the Quality Assurance of Software Requirements  
**URL:** https://arxiv.org/abs/2408.10886  
**Date:** Aug 2024  
**Venue:** RE 2024 (IEEE Requirements Engineering Conference)

---

## The Core Idea

This paper evaluates using an LLM to assess requirement quality against ISO 29148 characteristics (e.g., unambiguous, complete, consistent), and to propose improved requirement statements.

The key practical point: LLMs can be effective “first-pass reviewers” for requirements quality, especially when they provide explanations.

---

## Reported Findings (High Level)

The paper reports patterns like:
- High recall in finding flawed requirements (catch many issues)
- Lower precision in some settings (false positives), but agreement improves when humans see the model’s explanation
- Proposed re-writes can improve requirement statements per human evaluators

---

## Why This Matters

For nontechnical operators, the risk is shipping ambiguous requirements into downstream agents.

This paper supports adding a **requirements QA gate** (ISO-like rubric) before “plan → code”.

---

## Critical Caveats

1. **False positives:** QA should not be purely automatic; explanations help reduce wasted rework.
2. **Domain dependence:** requirement quality heuristics vary by domain and risk profile.

---

## Relevance to Knowledge & Vibes

### Supports
- A dedicated “REQ QA pass” before decomposition/execution.
- Treating requirement rewrites as a legitimate optimization step.

### Practical implication
Add a template-driven QA checklist for each `REQ-*` and require the operator to confirm intent after rewrites.

