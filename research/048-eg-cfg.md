# EG‑CFG (Execution‑Guided Line‑by‑Line Code Generation)

**Paper:** Execution Guided Line‑by‑Line Code Generation  
**URL:** https://arxiv.org/abs/2506.10948  
**Date:** Jun 2025  
**Venue:** arXiv preprint

---

## Summary

EG‑CFG brings execution feedback *into decoding time*:
- generate candidate continuations (line-by-line) via beam search
- execute candidates against tests to extract **execution signals** (errors, traces)
- use classifier-free guidance to steer token generation using those signals

This formalizes a “tight loop” style: generate a little, run it, use feedback, repeat.

---

## Key Claims (Reported)

EG‑CFG reports state-of-the-art results across several coding benchmarks (including execution-trace variants) using an open model backbone in their setup, with large gains vs standard decoding without execution guidance.

---

## Practical Implications (For Knowledge & Vibes)

1. **Shrink the step size on hard beads.** Prefer many small validated edits over one huge patch.
2. **Execution feedback should be frequent.** “Run tests/build” should happen early and often in the bead loop.
3. **Parallel exploration is valid.** Multiple agents can explore different patch candidates; select using execution results.

---

## Caveats

- This is a specialized inference method; your practical analog is “tight validate loops,” not implementing EG‑CFG itself.

