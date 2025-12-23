# SWE-Gym

**Paper:** Training Software Engineering Agents and Verifiers with SWE-Gym
**URL:** https://arxiv.org/abs/2412.21139
**Date:** December 2024

---

## Summary

SWE-Gym is the first environment for **training** (not just evaluating) software engineering agents. It provides 2,438 real Python tasks with executable environments and unit tests.

**Components:**
- SWE-Gym: 2,438 tasks from 11 repos
- SWE-Gym Lite: 230 tasks for fast prototyping
- SWE-Gym Raw: 66,894 instances for future research

**Training methodology:** Rejection sampling fine-tuning on successful trajectories. Only trajectories that pass tests are kept.

**Results after training (Qwen-2.5 32B):**

| Benchmark | Before | After | Improvement |
|-----------|--------|-------|-------------|
| SWE-Bench Lite | 3.0% | 15.3% | +12.3% |
| SWE-Bench Verified | 7.0% | 20.6% | +13.6% |

**With verifier (inference-time scaling):**
- SWE-Bench Verified: 32.0% (new SOTA for open-weight)
- SWE-Bench Lite: 26.0%

**Repos included:** pandas, MONAI, moto, mypy, dask, dvc, conan, pydantic, hydra, bokeh, modin

---

## Practical Implications

1. **Training on real tasks works** - Substantial gains from fine-tuning on successful agent trajectories
2. **Verifiers help** - Training outcome-supervised reward models enables inference-time scaling
3. **Open-weight can compete** - 32% on SWE-Bench Verified rivals proprietary systems
4. **Self-improvement has limits** - Mixing on-policy/off-policy data caused performance drops
5. **Test-based verification is key** - All training uses test pass/fail as the reward signal

**Limitations noted:**
- 491 training trajectories (limited by compute, not tasks)
- Specialized workflow agents (MoatlessTools) showed limited improvement
- Gap between Pass@K and Best@K suggests room for better reward modeling

**For your system:** Validates test-based verification. The training success comes from only keeping trajectories that pass tests, supporting your emphasis on executable acceptance criteria.
