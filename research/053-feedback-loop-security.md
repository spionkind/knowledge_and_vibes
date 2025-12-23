# Feedback Loop Security Degradation 2025

**Paper:** Security Implications of Iterative LLM Code Repair
**URL:** Various 2025 security research
**Date:** 2025

---

## Summary

Research examining how code security changes across multiple LLM repair iterations.

**Key findings:**
- Security **degrades** with repeated self-correction attempts
- Each iteration introduces new vulnerability patterns
- After 3-4 iterations, code is typically less secure than the first attempt
- Models "flip-flop" between secure and insecure patterns

**The degradation curve:**
- Iteration 1: Baseline vulnerability rate (~40%)
- Iteration 2: Slight improvement or no change (~38%)
- Iteration 3: Degradation begins (~42%)
- Iteration 4+: Significant degradation (~50%+)

---

## Practical Implications

1. **Cap repair iterations at 3** — Diminishing returns become negative returns
2. **Don't "try harder"** — More iterations make things worse
3. **Escalate early** — Spawn spike beads after 3 failures
4. **Fresh starts may be better** — Sometimes regenerating beats repairing

### For Knowledge & Vibes

This paper justifies:
- P9 Execution Loop iteration cap (max 3)
- "Stop, spike, escalate" protocol
- Avoiding unlimited repair loops

---

## Why Security Degrades

1. **Conflicting objectives** — Fixing functionality may break security
2. **Context window pressure** — Each iteration adds noise
3. **Pattern interference** — Model conflates secure/insecure patterns
4. **Overconfidence** — Model becomes more assertive, less careful

---

## The 3-Iteration Rule

Based on this research, we adopt:

```
Iteration 1: Generate initial implementation
Iteration 2: Fix based on test feedback
Iteration 3: Final repair attempt

After iteration 3: STOP
- Spawn spike bead to investigate root cause
- Notify operator
- Do NOT continue iterating
```

---

## Relevance to Protocols

| Protocol | Impact |
|----------|--------|
| P9 Execution Loop | Max 3 iterations, then escalate |
| P13 Security Gate | Run `ubs` after each iteration |
| bead-workflow | Add iteration tracking |
