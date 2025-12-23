# Coeditor (Repo-level Diffs for Code Auto-Editing)

**Paper:** Coeditor: Leveraging Repo-level Diffs for Code Auto-editing  
**URL:** https://arxiv.org/html/2305.18584v2  
**Date:** May 2023 (arXiv); ICLR 2024  
**Venue:** ICLR 2024

---

## The Core Idea

Most “code LLM” work is about generating new code. Real development is mostly **editing** existing code.

Coeditor trains a model to predict edits conditioned on:
- The current code region
- **Recent repo-level diffs** (what changed elsewhere in the codebase)

This targets multi-round workflows: after a user changes some lines, the assistant predicts follow-up edits needed elsewhere.

---

## Key Technique

1. Represent changes as a **line-diff format** and cast editing as span-infilling.
2. Pull lightweight static-analysis context (e.g., signatures, variable usage) to enrich prompts.
3. Use **block-sparse attention** so the model can attend to many diff blocks without quadratic cost.

---

## Dataset Contribution

They introduce **PyCommits**: commit-history-based code editing data from ~1,650 Python repos.

This dataset matters because it’s closer to “what IDE copilots do” than single-file generation datasets.

---

## Reported Results (Headlines)

The paper reports that a relatively small model (~220M) can:
- Reach ~**60% exact match** on a simplified single-edit task (substantially above strong baselines in their setup)
- In multi-round settings, automate a large fraction of changed lines and reduce keystrokes materially (reported ~**28.6%** keystroke savings and ~**46.7%** of changed lines automated in their study)

---

## Why This Matters

It’s strong evidence that:
- “Repo awareness” can be expressed as **diff context**, not only as retrieving the entire repository.
- A good editing assistant should be optimized for *edit continuation*, not just “write function”.

---

## Critical Caveats

1. **Exact-match is a harsh metric:** “semantically correct but formatted differently” can count as wrong.
2. **Python-centric dataset:** generalization across languages/repos is not guaranteed.
3. **Not an SWE-bench agent:** this is more about interactive IDE editing than autonomous issue resolution.

---

## Relevance to Knowledge & Vibes

### Supports
- Treating “what changed so far” as first-class context for agents (temporal context).
- Capturing diffs as artifacts in calibration (“here’s the delta; what should happen next?”).

### Practical implication
When agents work in parallel, having a canonical “diff summary” artifact reduces cross-agent confusion and duplicated effort.

