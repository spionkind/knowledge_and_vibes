# METR Randomized Controlled Trial 2025

**Paper:** Measuring the Impact of AI Coding Assistants on Developer Productivity: A Randomized Controlled Trial
**URL:** https://metr.org/blog/2025-01-rct-results/ (2025)
**Date:** January 2025

---

## Summary

METR conducted a rigorous RCT measuring how AI coding assistants affect developer productivity on real tasks.

**Key findings:**
- Experienced developers were **19% slower** with AI assistants on unfamiliar codebases
- AI helped most when developers already understood the domain
- Productivity gains only appeared in familiar contexts

**Why experienced devs are slower:**
1. Time spent reviewing/validating AI output
2. Debugging AI-introduced issues
3. Cognitive overhead of context-switching between own thinking and AI suggestions
4. False confidence leading to less careful verification

---

## Practical Implications

1. **AI is not a universal productivity boost** — Context matters enormously
2. **Domain familiarity is key** — AI helps amplify existing knowledge, not replace it
3. **Verification overhead is real** — Time saved generating is lost verifying
4. **Human checkpoints are essential** — Especially for unfamiliar domains

### For Knowledge & Vibes

This paper justifies:
- P14 Human Verification Gate — Operator must understand what the code does
- Reality check in philosophy — Don't assume AI improves outcomes automatically
- Emphasis on grounding — Unfamiliar domains require extra verification

---

## The Counterintuitive Finding

> "AI coding assistants showed negative productivity impact for experienced developers working on unfamiliar codebases. The intuition that 'AI helps everyone' is not supported by evidence."

This contradicts popular narratives about AI productivity gains.

---

## When AI Helps vs Hurts

| Context | Impact |
|---------|--------|
| Familiar domain, routine tasks | Positive (modest gains) |
| Familiar domain, novel problems | Mixed |
| Unfamiliar domain, any task | **Negative (19% slower)** |
| Critical/security code | Requires extra verification overhead |

---

## Relevance to Protocols

| Protocol | Impact |
|----------|--------|
| P14 Human Verification | Primary justification |
| P13 Security Gate | Extra verification for unfamiliar code |
| P3 Grounding | Essential for unfamiliar domains |
