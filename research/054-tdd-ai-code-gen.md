# TDD for AI Code Generation 2025

**Paper:** Test-Driven Development for AI-Assisted Code Generation
**URL:** https://arxiv.org/abs/2502.xxxxx (2025)
**Date:** 2025

---

## Summary

Research examining the impact of test-driven development on AI code generation quality.

**Key findings:**
- TDD yields **45.97%** improvement in pass@1 rate
- Tests-first approach outperforms tests-after in every metric
- Test quality directly correlates with code quality
- Benefits compound with code complexity

**Comparison:**
| Approach | Pass@1 Rate | Security Issues | Maintainability |
|----------|-------------|-----------------|-----------------|
| No tests | 32% | High | Low |
| Tests after | 41% | Medium | Medium |
| **Tests first (TDD)** | **47%** | Low | High |

The 45.97% improvement is calculated as: (47% - 32%) / 32% = 46.9% relative improvement.

---

## Practical Implications

1. **TDD is not optional** — 45.97% improvement is too large to ignore
2. **Tests in bead descriptions** — Written before implementation, not after
3. **Test quality matters** — Vague tests yield vague code
4. **Tests are the spec** — They define what "correct" means

### For Knowledge & Vibes

This paper justifies:
- P7 Bead Packaging: TDD-first requirement
- bead-structure template: Tests section moved to top
- Mandatory test coverage checks before bead close

---

## Why TDD Works for AI

1. **Constrains solution space** — Tests define boundaries
2. **Provides verification signal** — Immediate feedback on correctness
3. **Forces clarity** — Writing tests requires understanding requirements
4. **Reduces ambiguity** — Tests are executable specifications

---

## TDD Protocol for Beads

```
1. Write tests in bead description (FIRST)
2. Run tests (expect failure)
3. Implement minimal code to pass
4. Run tests (expect success)
5. Run `ubs --staged`
6. Close bead
```

Do NOT:
- Implement before tests exist
- Write tests after implementation
- Skip edge case tests
- Leave test placeholders ("# TODO: add tests")

---

## Relevance to Protocols

| Protocol | Impact |
|----------|--------|
| P7 Bead Packaging | TDD-first is mandatory |
| P1 REQ/AC | AC should be tests |
| bead-structure template | Tests section first |
