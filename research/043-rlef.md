# RLEF (Reinforcement Learning from Execution Feedback)

**Paper:** RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning  
**URL:** https://arxiv.org/abs/2410.02089  
**Date:** Oct 2024 (updates in 2025)  
**Venue:** arXiv preprint (later conference version)

---

## Summary

RLEF studies a critical weakness: many strong code models **don’t reliably improve** from execution feedback in multi-turn repair loops (they repeat themselves or make irrelevant edits).

RLEF proposes end-to-end RL training (PPO) where the model:
- generates code
- receives **execution feedback** from public tests/errors
- iteratively revises
- is optimized for reward measured on held-out/private tests

Net effect: the model learns to actually **use** execution feedback as a control signal.

---

## Key Claims (Reported)

- Achieves new state-of-the-art on CodeContests with both small (8B) and large (70B) models in their setup.
- Reduces required samples/generations by **~10×** versus prior approaches.

---

## Practical Implications (For Knowledge & Vibes)

1. **“Feedback loops” aren’t free.** You must force *meaningful* deltas between attempts (targeted edits, new evidence), not endless retries.
2. **Operator-friendly rule:** require every repair iteration to cite the specific failing test/log line it is addressing.
3. **Bead templates should encode “feedback → patch.”** Don’t let agents “think harder” without new feedback; demand a new test, repro, or trace.

---

## Caveats

- This is training research; you can’t “turn on RLEF,” but you can adopt the workflow implications: disciplined, evidence-backed repair loops.

