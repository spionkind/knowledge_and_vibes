# Lita: Lightweight Agents for Agentic Coding 2025

**Paper:** Lita: Light Agent Uncovers the Agentic Coding Capabilities of LLMs
**URL:** https://arxiv.org/abs/2509.25873
**Date:** September 2025

---

## Summary

Research introducing **Lita (Lite Agent)**, a minimalist agent framework designed to evaluate the true coding capabilities of LLMs without complex hand-crafted workflows.

**Key insight:** Complex agent scaffolding often obscures the underlying model's capabilities. Simpler agents can reveal what the model actually knows vs. what the scaffolding provides.

---

## Core Philosophy

| Principle | Description |
|-----------|-------------|
| **Minimal scaffolding** | Reduce hand-crafted workflows to minimum |
| **Model capability focus** | Isolate what the LLM can do vs. what tooling adds |
| **Prompt tuning independence** | Avoid over-reliance on specific prompt patterns |
| **Bias elimination** | Remove hidden biases from complex pipelines |

---

## Findings

### Simple vs. Complex Agents

```
Complex Agent Pipeline:
├── Planner Agent
├── Executor Agent
├── Reviewer Agent
├── Test Runner
├── Error Analyzer
└── Repair Agent
    = Many moving parts, hard to attribute success

Lite Agent:
├── Single LLM
├── Minimal tools (read, write, execute)
└── Clear feedback loop
    = Direct attribution of capability
```

**Surprising result:** On many benchmarks, the gap between complex multi-agent systems and minimal agents is smaller than expected when using capable base models.

### Implications for Agent Design

1. **Start simple** — Complex orchestration should be justified by measurable gains
2. **Attribute carefully** — Know what's model capability vs. scaffolding
3. **Test both** — Compare complex pipeline against minimal baseline
4. **Avoid premature optimization** — Don't add agents until simple approach fails

---

## Practical Implications

### For Knowledge & Vibes

This validates our ADaPT pattern:
- **Start coarse** — Don't over-decompose upfront
- **Add complexity only when needed** — Decompose when execution fails
- **Simple pipelines beat complex ones** — Aligns with Agentless research (011)

### When to Add Complexity

| Add Agent Complexity When... | Don't Add When... |
|------------------------------|-------------------|
| Simple approach fails after 3 tries | "Might be useful" |
| Specific bottleneck identified | General optimization |
| Measurable improvement expected | Theoretical benefit |
| Clear attribution possible | Black box improvement |

---

## Contrast with Multi-Agent Systems

| Aspect | Lite Agent | Multi-Agent |
|--------|------------|-------------|
| Debugging | Easy | Hard |
| Attribution | Clear | Obscured |
| Overhead | Low | High |
| Ceiling | Model-limited | Can exceed model |
| Best for | Baseline, simple tasks | Complex coordination |

**Takeaway:** Use multi-agent when you have evidence it helps, not by default.

---

## Relevance to Protocols

| Protocol | Impact |
|----------|--------|
| ADaPT Pattern | Validates "start coarse" approach |
| Execution agents | Consider minimal agent first |
| Debugging | Simpler agents easier to debug |
| Calibration | Attribute failures to model vs. scaffolding |

---

## See Also

- `011-agentless.md` — Simple pipelines outperform complex agents
- `038-adapt.md` — Adaptive decomposition
- `056-multi-agent-orchestrator.md` — When multi-agent is warranted
