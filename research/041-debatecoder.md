# DebateCoder (Test‑Case‑Driven Debate for Code Generation)

**Paper:** DebateCoder: Towards Collective Intelligence of LLMs via Test Case Driven LLM Debate for Code Generation  
**URL:** https://aclanthology.org/2025.acl-long.589/  
**Date:** 2025  
**Venue:** ACL 2025 (Long)

---

## Summary

DebateCoder replaces “argue in text” with **debate via executable evidence**:
- two models generate candidate solutions
- they **generate adversarial test cases** to break each other’s code
- code is refined using **test execution outcomes**, not rhetoric
- convergence is judged by test outcomes (no third-party “judge” model required)

It’s an evidence-first multi-agent pattern: **tests are the medium of disagreement**.

---

## Key Claim (Reported)

DebateCoder reports improved performance on competitive programming benchmarks (APPS, CodeContests) over baselines like self-play and generic multi-agent debate, and stabilizes in a small number of debate epochs.

---

## Practical Implications (For Knowledge & Vibes)

1. **Upgrade calibration challenges:** when agents disagree, require *either* a doc/code citation *or* a test case that distinguishes the alternatives.
2. **Make adversarial tests a standard move:** if a bead looks “done,” another agent should try to break it by generating edge-case tests tied to AC.
3. **Eliminate rhetorical debate:** for implementation disputes, move quickly to “write the test that proves you right.”

---

## Caveats

- Most benchmarks are self-contained; for repo work, “adversarial tests” often means strengthening the test suite around interfaces and invariants.

