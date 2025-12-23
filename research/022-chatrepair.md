# ChatRepair (Conversation-Driven Program Repair)

**Paper:** Automated Program Repair via Conversation: Fixing 162 out of 337 Bugs for $0.42 Each using ChatGPT  
**URL:** https://lingming.cs.illinois.edu/publications/issta2024.pdf  
**Date:** ISSTA 2024  
**Venue:** ISSTA 2024

---

## The Core Idea

Most LLM-based APR is “generate-and-validate” with independent samples.

ChatRepair treats APR as a **conversation**:
- Generate a patch
- Run tests
- Feed back failure info + the incorrect patch
- Ask for a revised patch (so the model “learns” from the failure)

And when it finds a plausible patch, it asks for *variations* of the successful patch to search locally around success.

---

## What Information It Uses That Matters

ChatRepair explicitly includes bug-exposing test info:
- failing test name
- failing line / stack trace
- error message

This is often omitted in simpler prompting baselines.

---

## Reported Results (Headlines)

On Defects4J, the paper reports:
- **162** correct fixes out of **337** bugs
- Estimated cost of about **$0.42 per fix** (in their ChatGPT pricing setup)

---

## Why This Matters

It provides evidence for a workflow principle you already believe:
> Multi-step interaction with feedback beats one-shot generation.

And it suggests that “reflection” is most useful when grounded in **concrete execution signals**, not abstract self-critique.

---

## Critical Caveats

1. **Tests define correctness:** passing tests can still be wrong (plausible vs correct patch problem).
2. **Repair scope:** many APR benchmarks are single-function; repo-level issue resolution is harder.
3. **Pricing/results can drift:** costs depend on model version + prompt length.

---

## Relevance to Knowledge & Vibes

### Supports
- Treating calibration as “post-execution”: after a phase, run checks, then revise.
- Encoding “failure → patch revision” loops as first-class beads.

### Practical implication
In your system, make “test feedback ingestion” a standard artifact:
- What failed, where, and what changed in response?

