# Planning-Driven Programming (LPW)

**Paper:** Planning-Driven Programming: A Large Language Model Programming Workflow
**URL:** https://arxiv.org/abs/2411.14503
**Date:** November 2024

---

## Summary

A two-phase workflow where the LLM first generates a step-by-step plan, verifies it against test cases, then generates code. The verified plan is also used to guide debugging when tests fail.

**The workflow:**
1. **Plan generation:** LLM creates numbered steps for solving the problem
2. **Plan verification:** LLM traces through the plan with test inputs to check if outputs match
3. **Code generation:** Generate code following the verified plan
4. **Debugging:** If tests fail, use the verified plan to identify where code diverges

**Key results (GPT-3.5):**

| Benchmark | LPW | Baseline | Improvement |
|-----------|-----|----------|-------------|
| HumanEval | 89.0% | 82.9% | +6.1% |
| MBPP | 76.0% | 72.4% | +3.6% |

**Harder benchmarks (GPT-4o):**

| Benchmark | LPW | Baseline | Improvement |
|-----------|-----|----------|-------------|
| CodeContests | 34.7% | 29.3% | +5.4% |
| APPS | 62.6% | 53.2% | +9.4% |

**Ablation - what matters:**

| Component Removed | Drop |
|-------------------|------|
| Plan verification | -3.0% |
| Code refinement loop | -9.1% |

The refinement loop (using the plan to debug) contributes more than initial verification.

---

## Practical Implications

1. **Plan-then-implement works** - Consistent 2-10% improvement over direct generation
2. **Verification helps but isn't magic** - Only 3% improvement from plan verification alone
3. **The real value is in debugging** - Having a verified plan to compare against when fixing code is the bigger win (9% improvement)
4. **Plan verification accuracy is 92.7%** - 7.3% of verifications are wrong, so don't treat it as ground truth
5. **Half of failures are planning failures** - If the LLM can't create a valid plan, nothing else helps

**For your system:** Supports having detailed phase docs. The bigger insight is that plans should be used for debugging, not just initial generation.
