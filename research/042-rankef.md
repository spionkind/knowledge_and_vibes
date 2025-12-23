# RankEF (Execution‑Feedback Reranking)

**Paper:** Sifting through the Chaff: On Utilizing Execution Feedback for Ranking the Generated Code Candidates  
**URL:** https://arxiv.org/abs/2408.13976  
**Date:** Aug 2024  
**Venue:** ASE 2024

---

## Summary

RankEF targets a common failure mode of “sample N solutions, pick the best”: ranking candidates by surface heuristics is weak, but running every candidate can be expensive or unsafe.

RankEF trains a ranker that:
- classifies candidate code as correct/incorrect **and**
- learns to **predict templated execution feedback** (error type, location, mismatch)

This helps the ranker learn *why* code fails, improving selection **without executing at ranking time**.

---

## Key Results (Reported)

- Outperforms prior non-execution rankers (e.g., CodeRanker) on APPS/MBPP/HumanEval.
- Reports large relative pass@1 gains on APPS (e.g., up to **+30.97%** relative improvement in some settings).

---

## Practical Implications (For Knowledge & Vibes)

1. **Selection is a first-class step.** For hard beads, generate multiple candidates and select using *evidence signals* (tests, static checks, lint) rather than “best sounding.”
2. **Cheaper proxy for execution:** when execution is too expensive, use failure-prediction heuristics (UBS/static checks/typecheck) as an approximation.
3. **Reranking in calibration:** when multiple approaches exist, prefer ones that can be discriminated by fast checks.

---

## Caveats

- Benchmark setting differs from repo engineering; still, the principle “diversity + selection needs a good discriminator” transfers directly.

