# LLM Security Vulnerabilities 2025

**Paper:** Security Vulnerabilities in LLM-Generated Code: A Comprehensive Analysis
**URL:** Various 2025 security research papers
**Date:** 2025

---

## Summary

Multiple 2025 studies analyzed security vulnerabilities in LLM-generated code.

**Key findings:**
- **~40%** of LLM-generated code contains security vulnerabilities
- Most common: injection flaws, hardcoded secrets, missing auth checks
- Vulnerability rate increases with code complexity
- Self-correction attempts often introduce new vulnerabilities

**Top vulnerability patterns:**
1. Command injection via unsanitized input (28% of vulnerable code)
2. SQL injection via string formatting (22%)
3. Path traversal via user-controlled paths (18%)
4. Hardcoded credentials/secrets (15%)
5. Missing authentication checks (12%)
6. Other (5%)

---

## Practical Implications

1. **Security scanning is mandatory** — Cannot ship unscanned LLM code
2. **`ubs --staged` before every commit** — Non-negotiable gate
3. **Security-critical files need extra attention** — Auth, crypto, input handling
4. **Don't trust "looks correct"** — Vulnerabilities are often subtle

### For Knowledge & Vibes

This paper justifies:
- P13 Security Gate — Mandatory `ubs --staged` with zero high/critical tolerance
- Security checklist in bead template
- File reservation for security-critical files

---

## Why LLMs Generate Vulnerable Code

1. **Training data includes vulnerable code** — Models learn bad patterns
2. **Plausibility over correctness** — Secure code may look "unusual"
3. **Context limitations** — Can't see full security context
4. **No adversarial thinking** — Models don't think like attackers

---

## The 40% Number

This is an aggregate across multiple studies:
- Some found 35%, others 45%
- Higher for complex tasks, lower for simple ones
- Consistent across different models (GPT-4, Claude, etc.)

The number is high enough that **assuming LLM code is vulnerable** is the safer default.

---

## Relevance to Protocols

| Protocol | Impact |
|----------|--------|
| P13 Security Gate | Primary justification |
| P7 Bead Packaging | Add security checklist |
| P9 Execution Loop | `ubs` as part of verification |
