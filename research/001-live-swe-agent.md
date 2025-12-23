# Live-SWE-agent

**Paper:** Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?
**URL:** https://arxiv.org/abs/2511.13646
**Date:** November 2025

---

## Summary

Live-SWE-agent achieves 77.4% on SWE-bench Verified by allowing agents to **create custom tools (scripts)** during problem-solving. The agent starts with minimal capabilities (bash only) and writes helper scripts as needed.

**What "self-evolution" actually means:**
- Agent writes Python/bash scripts to help with current task
- Scripts include: file editors, search utilities, language-specific analyzers
- Tools are NOT carried forward between tasks
- The underlying agent loop stays completely fixed

**Key results:**
| Benchmark | Score |
|-----------|-------|
| SWE-bench Verified | 77.4% |
| SWE-Bench Pro | 45.8% |

**Ablation (50-problem subset):**
| Condition | Solve Rate |
|-----------|------------|
| Full system | 76.0% |
| Without tool creation | 62.0% |
| Without reflection | 64.0% |

---

## Practical Implications

1. **Don't over-constrain agent tooling** - Let agents create helper scripts during implementation
2. **The core workflow can remain fixed** - The paper keeps the agentic loop unchanged; only tools are dynamic
3. **Requires capable models** - Weaker models (GPT-5-Nano) entered infinite loops and performed worse
4. **Reflection prompts help** - Asking "would creating a tool help?" improved performance

**For your system:** Phase templates and planning structure are unrelated to this finding. The paper is about runtime tool creation, not planning artifacts.
