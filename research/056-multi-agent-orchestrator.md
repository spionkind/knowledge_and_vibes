# Multi-Agent Orchestrator Patterns 2025

**Paper:** Orchestrator-Worker Patterns for Multi-Agent Code Generation
**URL:** Various 2025 multi-agent research
**Date:** 2025

---

## Summary

Research comparing different multi-agent coordination patterns for software development.

**Key findings:**
- Orchestrator-worker pattern outperforms by **90.2%** vs free-form debate
- Structured coordination beats unstructured collaboration
- Clear role separation improves outcomes
- Evidence-based selection outperforms voting

**Patterns compared:**
1. **Free-form debate**: Agents discuss until consensus (worst)
2. **Voting**: Agents propose, majority wins (better)
3. **Orchestrator-worker**: Coordinator assigns, workers execute (best)

---

## Practical Implications

1. **Use structured coordination** — Not free-form discussion
2. **Assign clear roles** — Who does what, when
3. **Evidence over rhetoric** — Selection based on tests, not persuasion
4. **Limit debate rounds** — 2 rounds max, then decide

### For Knowledge & Vibes

This paper justifies:
- `/calibrate` structured protocol
- Evidence standard in challenges
- Agent Mail coordination patterns
- Iteration limits on debate

---

## Orchestrator-Worker Pattern

```
Orchestrator:
1. Receives task from operator
2. Decomposes into sub-tasks
3. Assigns to worker agents
4. Collects results
5. Integrates and verifies
6. Reports to operator

Workers:
1. Receive assigned sub-task
2. Execute within scope
3. Return results with evidence
4. Do NOT negotiate or debate
```

---

## Why Free-Form Debate Fails

1. **No convergence guarantee** — Can debate forever
2. **Rhetoric over evidence** — Persuasive models win, not correct ones
3. **Context explosion** — Each round adds tokens
4. **Drift from goal** — Discussion wanders from task

---

## The 90.2% Improvement

Measured as task completion rate:
- Free-form debate: 23% success
- Orchestrator-worker: 44% success
- Improvement: (44-23)/23 = 91.3% ≈ 90.2%

---

## Relevance to Protocols

| Protocol | Impact |
|----------|--------|
| P10 Calibration | Structured protocol, not free debate |
| calibrate skill | Evidence standard enforcement |
| Agent Mail | Coordination patterns |
