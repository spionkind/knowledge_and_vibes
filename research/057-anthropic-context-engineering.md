# Anthropic Context Engineering 2025

**Paper:** Context Engineering for Claude: Best Practices from Anthropic
**URL:** https://www.anthropic.com/engineering/context-engineering (2025)
**Date:** 2025

---

## Summary

Anthropic's official guidance on context engineering for Claude models.

**Key principle:**
> "The goal is to find the smallest set of high-signal tokens that enables correct behavior."

**Key findings:**
- More context is not better — quality over quantity
- Position matters — critical info at boundaries
- Retrieval + short context beats long context
- Tool design affects context efficiency

---

## Practical Implications

1. **Minimize context** — Only include what's necessary
2. **Maximize signal** — Every token should earn its place
3. **Position strategically** — Critical info at start/end
4. **Use tools wisely** — Tools can reduce context needs

### For Knowledge & Vibes

This paper supports:
- P6 Phase Chunking — Short context, lossless
- P3 Grounding — Selective retrieval, not context stuffing
- Tool design principles — Warp-Grep, cass, Exa

---

## Context Engineering Principles

### 1. Smallest Effective Context
Don't include "just in case" — include only what's needed for the current task.

### 2. High-Signal Tokens
Prioritize:
- Direct instructions
- Relevant code snippets
- Specific examples
- Constraints and requirements

Deprioritize:
- Background context
- Historical discussion
- Tangential information

### 3. Strategic Positioning
- **Start**: Most critical instructions
- **End**: Current task context
- **Middle**: Supporting information (but minimize)

### 4. Tool Integration
Tools can:
- Retrieve context on-demand (better than pre-loading)
- Reduce token count (85% reduction with Tool Search Tool)
- Provide fresh information (vs stale context)

---

## Anti-Patterns

| Don't | Why | Do Instead |
|-------|-----|------------|
| Stuff full context | Quality degrades | Selective retrieval |
| Include "just in case" | Noise hurts signal | Include only needed |
| Put critical info in middle | Lost-in-middle effect | Position at boundaries |
| Static context | Gets stale | Dynamic retrieval |

---

## Relevance to Protocols

| Protocol | Impact |
|----------|--------|
| P6 Phase Chunking | Short context justified |
| P3 Grounding | Retrieval patterns |
| Tool design | Minimize context via tools |
