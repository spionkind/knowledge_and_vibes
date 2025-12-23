# MapCoder (Multi‑Agent Code Generation Pipeline)

**Paper:** MapCoder: Multi‑Agent Code Generation for Competitive Problem Solving  
**URL:** https://arxiv.org/abs/2405.11403  
**Date:** May 2024  
**Venue:** ACL 2024 (Long)

---

## Summary

MapCoder is a multi-agent prompting framework that approximates the “human programming loop” using a fixed pipeline of specialized stages:
1. **Retrieval** (recall similar problems/examples)
2. **Planning** (draft a solution plan)
3. **Coding** (implement)
4. **Debugging** (fix with feedback)

The important point isn’t “roles”; it’s that **separating stages** improves reliability and makes failures easier to diagnose.

---

## Key Results (Reported)

MapCoder reports strong pass@1 on program-synthesis benchmarks (with GPT‑4 in their setup), e.g.:
- **HumanEval:** **93.9%**
- **MBPP:** **83.1%**
- **APPS:** **22.0%**
- **CodeContests:** **28.5%**
- **xCodeEval:** **45.3%**

---

## Practical Implications (For Knowledge & Vibes)

1. **Pipeline beats freeform.** Encode “retrieve → plan → implement → debug” as default bead structure, not optional best practice.
2. **Make retrieval explicit.** The retrieval stage should be a first-class step (Warp‑Grep/CASS/Exa), not “just ask the model.”
3. **Debugging is its own stage.** Treat failing tests as a transition to a different workflow (repair loop) rather than continuing generation.

---

## Caveats

- Program synthesis ≠ repo-scale changes. Expect lower absolute performance on real repos; keep the *structure*.

