# IRIS (LLM‑Assisted Static Analysis for Security)

**Paper:** IRIS: LLM‑Assisted Static Analysis for Detecting Security Vulnerabilities  
**URL:** https://arxiv.org/abs/2405.17238  
**Date:** May 2024 (updated Apr 2025)  
**Venue:** arXiv preprint

---

## Summary

IRIS combines LLMs with static analysis to do whole-repo reasoning for security:
- use an LLM to infer/augment analysis specs (e.g., taint specifications)
- run static analysis with improved context/specs
- use the LLM to interpret and refine results

It’s evidence that hybrid “LLM + program analysis” systems can outperform either alone for repo-level properties (security flows).

---

## Key Results (Reported)

On a Java vulnerability benchmark (CWE-Bench-Java):
- IRIS (with GPT‑4 in their setup) reportedly detects more issues than CodeQL (e.g., **55 vs 27** in one headline comparison)
- improves false discovery rate by ~**5 percentage points**
- finds previously unknown real-world vulnerabilities (reported **4**)

---

## Practical Implications (For Knowledge & Vibes)

1. **Security deserves specialized checks.** Don’t rely solely on “general code quality”; add explicit security verification beads for high-risk work.
2. **Blend static tools + LLM reasoning.** Use UBS/typecheck/lint as the baseline, then use LLM review to interpret and prioritize findings.
3. **Make security a gate in higher rigor tiers.** For “enterprise/regulatory” North Stars, security scanning + threat review should be mandatory before release.

---

## Caveats

- IRIS is a research system; replicate the *principle* (analysis + LLM) with your available tools (UBS, linters, SAST) rather than the exact implementation.

