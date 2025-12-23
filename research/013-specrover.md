# SpecRover (Specification Inference for SWE)

**Paper:** SpecRover: Code Intent Extraction via LLMs  
**URL:** https://arxiv.org/html/2408.02232v4  
**Date:** Aug 2024 (latest revisions Nov 2024)  
**Venue:** arXiv preprint (slated for ICSE 2025 per paper)

---

## The Core Idea

SpecRover improves SWE agents by making “specification inference” explicit.

Instead of only retrieving code and patching, it tries to infer *intent*:
- What is this function/module supposed to do?
- What behavior is missing/wrong relative to the issue?

It then uses that inferred spec to guide patching and to produce “evidence” a human can trust.

---

## Workflow (High Level)

SpecRover is a multi-stage agent pipeline (built on AutoCodeRover) with extra spec-centric artifacts:
1. **Reproducer agent**: generate a minimal failing test when possible
2. **Context retrieval + function summaries**: retrieve candidate buggy locations and write a natural-language “intended behavior” summary for relevant functions
3. **Patching agent**: generate candidate patches
4. **Reviewer agent**: vet patches/tests against the issue statement; produce feedback (“why correct/incorrect”)
5. **Selection agent** (if needed): choose among candidates, especially when regression tests are weak

---

## Reported Results (Headlines)

SpecRover reports:
- ~**19%** solve rate on full SWE-bench (2294 issues), roughly **50%+ improvement** vs AutoCodeRover
- ~**31%** solve rate on SWE-bench Lite
- A “reviewer precision” signal (how often surfaced patches are actually correct) reported around **50%** on Lite in their analysis

---

## Why This Matters

This is one of the clearest demonstrations that agents need something like:
- **derived requirements/specs**, not just raw retrieval
- **internal reviewers/verifiers**, not just “generate patch”

It’s also aligned with your goal of agents periodically re-checking work against the *real goal*, not just their local task.

---

## Critical Caveats

1. **Extra stages add cost:** spec inference + reviewer loops are expensive.
2. **Spec quality is fragile:** “function summaries” can hallucinate intent if context is incomplete.
3. **Still benchmark-dependent:** when issues are underspecified, spec inference may just invent requirements.

---

## Relevance to Knowledge & Vibes

### Strong supports
- “North Star” grounding: intent/specs must be explicit to avoid local optimization.
- Post-phase calibration: reviewer-style “does this match the goal?” improves reliability.

### Implementation hint
If you build `/calibrate` as a “socratic seminar”, borrow SpecRover’s discipline:
- Every claim ties back to explicit evidence (tests, code references, issue text)
- Reviewer feedback is a structured artifact, not vibes

