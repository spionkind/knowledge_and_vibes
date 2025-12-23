# Agentless (Demystifying SWE Agents)

**Paper:** Agentless: Demystifying LLM-based Software Engineering Agents  
**URL:** https://arxiv.org/html/2407.01489v2  
**Date:** July 2024  
**Venue:** arXiv preprint

---

## The Core Idea

You can get strong SWE-bench performance **without** a complex tool-using autonomous agent.

Agentless proposes a simple, interpretable pipeline:
1. **Localization** (hierarchical narrowing: files → symbols → edit locations)
2. **Repair** (generate patches in a constrained diff format)
3. **Patch validation / selection** (filter + rerank using tests, including LLM-generated repro tests)

The LLM does not decide open-ended actions; the scaffold is fixed.

---

## Why “Agentless” Works

Agentless attacks the two biggest failure modes in repo repair:
- **Wrong place:** models patch the wrong file/function
- **Wrong patch format / low patch quality:** models generate fragile edits that don’t apply or break tests

It uses hierarchical localization and a constrained Search/Replace diff representation to reduce “patch application” failures and keep edits focused.

---

## Reported Results (Headlines)

The paper reports that Agentless:
- Achieves among the best results on **SWE-bench Lite** for open-source-ish scaffolds, with low cost per issue (reported on the order of **<$1** per issue in their setup).
- Performs competitively on stricter filtered variants (they also construct stricter Lite subsets to remove problematic instances).

(Exact numbers depend on benchmark split + model choice; the central point is that a fixed pipeline can beat many “agentic” scaffolds.)

---

## Key Method Details Worth Copying

- **Hierarchical localization** (file-level + symbol-level + edit-span selection) reduces wasted patch attempts.
- **Multiple candidate patches** + filtering is better than betting everything on one “beautiful patch”.
- **Reproducer tests** as a validation signal can be more discriminative than weak existing test suites.

---

## Critical Caveats

1. **Scaffold still matters:** “agentless” doesn’t mean “no engineering” — it’s a carefully designed pipeline.
2. **Validation is only as good as tests:** if tests are weak, passing can still be wrong.
3. **Benchmark artifacts:** the paper itself argues many SWE-bench Lite tasks are problematic (solution leakage, underspecification), which can inflate apparent success.

---

## Relevance to Knowledge & Vibes

### Supports
- Your instinct to standardize workflows with **coarse heuristic guardrails** (fixed phases) rather than open-ended roleplay.
- Emphasis on **localization-first** before editing.
- Multi-candidate patching + selection (don’t over-trust a single “plan”).

### Tension with
- Very heavy multi-agent orchestration for every issue: Agentless suggests many wins come from *pipeline design* and *validation*, not debate.

