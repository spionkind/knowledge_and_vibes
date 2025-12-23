# APPATCH (Automated Vulnerability Patching via Adaptive Prompting)

**Paper:** APPATCH: Automated Adaptive Prompting Large Language Models for Real-World Software Vulnerability Patching  
**URL:** https://arxiv.org/html/2408.13597v1  
**Date:** Aug 2024  
**Venue:** arXiv preprint

---

## The Core Idea

Vulnerability patching is harder than “bug fix” because you often don’t have:
- a reproducer exploit
- a good test suite

APPATCH (also referred to in some summaries as “LLMPatch”) aims to patch vulnerabilities by combining:
- program analysis to shrink context
- adaptive few-shot prompting based on root cause similarity
- multi-faceted validation to reduce hallucinated “fixes”

---

## Key Techniques

1. **Semantics-aware scoping**
   - Use program dependence / slicing to extract a “vulnerability semantics” slice (keep only the code that matters)

2. **Exemplar mining**
   - Build a pool of exemplars containing (root cause analysis → fix strategy → ground-truth patch)

3. **Dynamic adaptive prompting**
   - For a new vuln: infer root cause → select similar exemplars → generate patch with CoT guidance

4. **Multi-faceted validation**
   - Use multiple checks (and sometimes multiple LLMs) to filter candidates for correctness + behavioral preservation

---

## Reported Results (Headlines)

The paper reports large improvements over baseline prompting and some non-LLM patching baselines, including:
- Significant F1 improvements on correctness-style metrics
- Strong performance on “zero-day” vulnerabilities (reported patching **7/11** in one evaluation setting)

---

## Why This Matters

It demonstrates a general recipe for safety-critical coding tasks:
> Don’t just “ask for a patch”. Constrain context with analysis, guide with root-cause-matched exemplars, then validate aggressively.

---

## Critical Caveats

1. **Validation without tests is hard:** semantic equivalence checks are partial.
2. **Program analysis dependency:** slicing/PDG tooling must be correct and language-specific.
3. **LLM-based validation can collude:** multiple LLMs are not independent oracles.

---

## Relevance to Knowledge & Vibes

### Supports
- Your evidence-standard calibration: claims should be backed by executable checks or strong analysis artifacts.
- “North star” rigor: safety/security contexts require different rigor than hobby projects.

### Practical implication
For high-stakes projects, add explicit “analysis + validation” beads (not optional) before shipping changes.

