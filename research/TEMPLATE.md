# Research Document Template

Use this template when adding new research papers to the library.

---

## File Naming

```
{number}-{short-descriptive-name}.md

Examples:
- 071-tool-use-patterns.md
- 072-context-caching.md
- 073-error-recovery.md
```

**Next available number:** Check the highest existing number and increment by 1.

---

## Template

Copy everything below this line:

---

# {Paper Title}

**Paper:** {Full paper title}
**URL:** {arxiv or publication URL}
**Date:** {Month Year}

---

## Summary

{2-3 sentence summary of the key contribution}

**Key finding:** {Single most important takeaway in bold}

---

## Core Concept

{Explain the main idea in 3-5 paragraphs}

### The Problem

{What problem does this research solve?}

### The Solution

{How does the paper solve it?}

### Key Innovation

{What's new compared to prior work?}

---

## Technical Details

{Include relevant diagrams, algorithms, or code examples}

```
{ASCII diagram if helpful}
```

### Key Techniques

| Technique | Description | When to Use |
|-----------|-------------|-------------|
| {name} | {what it does} | {when it's useful} |

---

## Performance Results

| Benchmark | Baseline | This Approach | Improvement |
|-----------|----------|---------------|-------------|
| {name} | {X%} | {Y%} | {+Z%} |

{Commentary on what the results mean}

---

## Practical Implications

### For Knowledge & Vibes

{How does this apply to our workflow?}

| Research Technique | K&V Application |
|--------------------|-----------------|
| {technique} | {how we use it} |

### Implementation Checklist

- [ ] {action item 1}
- [ ] {action item 2}
- [ ] {action item 3}

---

## Key Takeaways

1. **{takeaway 1}** — {explanation}
2. **{takeaway 2}** — {explanation}
3. **{takeaway 3}** — {explanation}

---

## Limitations

- {limitation 1}
- {limitation 2}
- {limitation 3}

---

## See Also

- `{related-doc-1}.md` — {why it's related}
- `{related-doc-2}.md` — {why it's related}

---

## Quality Checklist

Before submitting a research doc, verify:

- [ ] **Summary is concrete** — Numbers, not vague claims
- [ ] **Key finding is actionable** — Tells you what to do
- [ ] **Technical details included** — Diagrams, code, tables
- [ ] **Performance results present** — With comparison to baseline
- [ ] **K&V implications stated** — How it applies to our workflow
- [ ] **Takeaways are numbered** — 3-5 clear points
- [ ] **Limitations acknowledged** — Honest about constraints
- [ ] **See Also links work** — Related docs exist
- [ ] **No vague language** — "Significant" → "45% improvement"
- [ ] **Date is accurate** — Prefer 2024-2025 research

---

## Examples of Good vs Bad

### Bad Summary
> "This paper presents a novel approach to code generation that shows promising results."

### Good Summary
> "Research demonstrating that structured chain-of-thought prompting improves code generation by 9.7% on HumanEval. Uses program structures (SEQUENCE, BRANCH, LOOP) as reasoning steps instead of natural language."

### Bad Key Finding
> "The approach works better than baselines."

### Good Key Finding
> "60-80% of debugging capability is lost within 2-3 attempts. Hard stop at iteration 3 and decompose."

### Bad Takeaway
> "This is useful for code generation."

### Good Takeaway
> "**TDD-first is mandatory** — 45.97% pass@1 improvement when tests are written before implementation."
