# Test Intentions 2025

**Paper:** Using Test Intentions to Improve AI-Generated Test Coverage
**URL:** Various 2025 testing research
**Date:** 2025

---

## Summary

Research on how explicit test intentions improve AI-generated test quality.

**Key findings:**
- Test intentions yield **94%** coverage vs **59%** with raw prompts
- Explicit test goals prevent "happy path only" testing
- Intentions help models understand edge cases
- Quality of intentions directly predicts test quality

**What are test intentions?**
Instead of: "Write tests for this function"
Use: "Test that the function handles: (1) valid input, (2) empty input, (3) invalid types, (4) boundary values, (5) concurrent access"

---

## Practical Implications

1. **Include test intentions in requirements** — Not just "add tests"
2. **Be explicit about edge cases** — Models don't infer them well
3. **List failure modes** — What should break, and how?
4. **Specify coverage goals** — What scenarios must be tested?

### For Knowledge & Vibes

This paper justifies:
- P1 REQ/AC: AC should include test intentions
- P7 Bead Packaging: Test intentions in bead description
- bead-structure template: Test Coverage Requirements section

---

## Test Intention Examples

**Bad (vague):**
```
Write tests for the login function.
```

**Good (explicit intentions):**
```
Test the login function for:
1. Valid credentials → success
2. Invalid password → failure with specific error
3. Non-existent user → failure (same error as invalid password)
4. Empty credentials → validation error
5. SQL injection attempt → sanitized, no error leak
6. Rate limiting → block after 5 failures
```

---

## Coverage Comparison

| Approach | Line Coverage | Branch Coverage | Edge Case Coverage |
|----------|--------------|-----------------|-------------------|
| Raw prompt | 59% | 45% | 22% |
| With intentions | 94% | 89% | 78% |

---

## Relevance to Protocols

| Protocol | Impact |
|----------|--------|
| P1 REQ/AC | Include test intentions in AC |
| P7 Bead Packaging | Test intentions required |
| P2 Req QA | Check for test intention coverage |
