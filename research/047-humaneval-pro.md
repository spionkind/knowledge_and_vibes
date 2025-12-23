# HumanEval Pro / MBPP Pro (Self‑Invoking Code Generation)

**Paper:** HumanEval Pro and MBPP Pro: Evaluating Large Language Models on Self‑invoking Code Generation  
**URL:** https://arxiv.org/abs/2412.21199  
**Date:** Dec 2024  
**Venue:** arXiv preprint (later ACL Findings)

---

## Summary

This paper introduces **self‑invoking code generation**: models must solve a base programming task and then use the generated solution as a tool to solve a related, harder task.

They generate harder “Pro” variants of popular benchmarks:
- HumanEval Pro
- MBPP Pro
- (and a Pro variant of a BigCodeBench subset)

This is a proxy for “progressive reasoning” during coding (build on prior work without drifting).

---

## Key Findings (Reported)

- Many models that score very highly on HumanEval/MBPP drop **~10–15% absolute** on the Pro variants.
- Instruction tuning offers only marginal gains on these tasks.
- Chain-of-thought style prompting can reduce common failure modes (assertion/name errors) and modestly improve Pro scores.

---

## Practical Implications (For Knowledge & Vibes)

1. **Don’t over-trust classic benchmarks.** High HumanEval doesn’t guarantee robustness on multi-step/reuse-heavy work.
2. **Treat “reuse” as a failure mode.** When agents build on prior code, enforce stronger invariants (tests/contracts) to prevent drift.
3. **Calibration between phases is justified.** Pro benchmarks are essentially “phase‑to‑phase reuse”; performance drops support adding strong between-phase checks.

---

## Caveats

- Still benchmarked code-gen tasks; repo integration adds additional failure modes (APIs, config, env).

