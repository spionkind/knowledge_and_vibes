# Test-Driven Development (TDD) for Code Generation

**Paper:** Test-Driven Development for Code Generation  
**URL:** https://arxiv.org/abs/2402.13521  
**Date:** Feb 2024 (rev Jun 2024)  
**Venue:** arXiv preprint

---

## The Core Idea

Giving an LLM **tests alongside the problem statement** improves correctness, and adding a remediation loop using test failures improves it further.

The paper operationalizes TDD for LLMs via a framework (TGen):
- generate code with tests in context
- run tests
- feed failures back for revision (bounded iterations)

---

## Reported Results (Headlines)

The paper reports consistent improvements across benchmarks when tests are included:
- On MBPP and HumanEval, supplying tests increases solve rates (the v2 summary reports **+12.0%** MBPP and **+8.5%** HumanEval for GPT‑4 in their setup).
- Adding a remediation loop yields additional gains (reported **~+2.8%** MBPP, **~+3.0%** HumanEval).
- Test-informed solutions generalize better to private/unseen tests than solutions generated without tests.

---

## Why This Matters

This is direct evidence that for reliability:
> “Acceptance criteria as executable tests” is not optional — it measurably improves correctness and robustness.

It also supports “multi-session planning”: requirements become durable only when they’re testable.

---

## Critical Caveats

1. **Test quality matters:** weak or ambiguous tests can mislead.
2. **Benchmark focus:** primarily function-level tasks, not repo-scale edits.
3. **Iteration bounds matter:** unlimited loops can waste compute or drift.

---

## Relevance to Knowledge & Vibes

### Supports
- Your REQ/AC discipline: AC should become tests.
- Beads that explicitly include a test harness and a repair loop.

### Practical implication
For nontechnical operators, make “tests as the contract” the main decision surface: they can validate intent without judging code.

