# Debate or Vote

**Paper:** Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?
**URL:** https://arxiv.org/abs/2508.17536
**Date:** August 2025

---

## Summary

The paper separates multi-agent debate (MAD) into two components: majority voting and inter-agent debate. Finding: **voting alone accounts for most performance gains**. In many cases, pure voting outperforms debate.

**Key results (Qwen2.5-7B, 7 benchmarks):**

| Method | Average Accuracy |
|--------|------------------|
| Single agent | 0.7205 |
| **Majority Voting** | **0.7691** |
| Debate T=2 | 0.7377 |
| Debate T=3 | 0.7112 |

More debate rounds made it **worse**.

**The theoretical finding:** Debate forms a "martingale" - a process where expected value doesn't change. Agents randomly influence each other; on average, it's neutral.

**What helps:**
- MAD-Conformist: Agents keep answers matching majority vote
- MAD-Follower: 30% chance agents adopt majority response
- These "biased" strategies break the random-walk property

---

## Practical Implications

1. **Voting is a strong baseline** - If you have multiple agents, majority vote is often enough
2. **Unstructured debate is neutral** - Random back-and-forth doesn't converge to truth
3. **Biased debate helps** - Lock in verified claims, weight toward evidence

**Important context:**
- Tasks tested were QA benchmarks (short answers, clear right/wrong)
- Agents were identical LLMs, not specialized roles
- No evidence grounding - agents argued from priors

**For your system:** Your calibration is different:
- Specialized agents with roles
- Evidence requirements
- Structured challenge/response
- Shared context (the plan)

The martingale result may not apply to evidence-grounded, structured debate. But do ensure challenges require evidence, not just opinions.
