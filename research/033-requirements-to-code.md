# Requirements → Design → Tests → Code (Progressive Prompting)

**Paper:** Requirements are All You Need: From Requirements to Code with LLMs  
**URL:** https://arxiv.org/abs/2406.10101  
**Date:** Jun 2024  
**Venue:** arXiv preprint (also presented at RE 2024, RE@Next! track)

---

## The Core Idea

The highest-leverage input to LLM-based software development is **high-quality, structured requirements**.

This paper argues against “one-line requirement → code” and instead proposes **progressive prompting**:
1. Interpret requirements → extract functional needs
2. Produce an object-oriented design model
3. Generate unit tests
4. Generate code from the design + tests

This creates intermediate artifacts that humans can inspect before code is written.

---

## Why This Matters

This is one of the few papers that directly targets the “nontechnical operator” problem:
> If you can produce good requirements, you can push the LLM through a structured waterfall-like chain that yields design, tests, and code.

It supports your Plan Pack idea (REQ/AC/ADR/contracts/tests) as the right interface between human intent and agent execution.

---

## Critical Caveats

1. **Case-study scope:** demonstrated on a specific web project use case; generalization is plausible but not guaranteed.
2. **Still needs validation:** intermediate artifacts can still be wrong; tests remain the strongest arbiter.
3. **Waterfall risk:** must be paired with iterative feedback loops to avoid rigid early errors.

---

## Relevance to Knowledge & Vibes

### Supports
- “Requirements-first” planning for nontechnical users.
- Progressive artifact generation (REQ → model → tests → code) instead of roleplay.

### Practical implication
Add an explicit “requirements refinement + QA” stage before ideation and architecture lock-in.

