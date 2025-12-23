# Evidence Map

This document traces each protocol back to the research that justifies it. Use this when you want to understand *why* a protocol exists.

> We don't just "do what feels right." We adopt workflow moves that are supported by the literature, and we encode them as gates/protocols.

---

## How to Read This

| Column | Meaning |
|--------|---------|
| **Protocol** | The protocol ID from `PROTOCOLS.md` |
| **Failure mode** | What goes wrong if you skip this protocol |
| **Evidence** | Research papers that support this protocol |
| **Confidence** | How directly the research applies |

---

## Protocol → Research Mapping

| Protocol | Primary failure mode addressed | Evidence in this repo | Confidence note |
|---------|--------------------------------|------------------------|-----------------|
| P0 North Star | drift / unscoped work | RE leverage: `research/034-llms-in-re-guideline.md`, `research/036-requirements-qa-iso-29148.md` | Indirect evidence; principle is classic SE + operator control |
| P1 REQ/AC | "correct" undefined / unverifiable | `research/033-requirements-to-code.md`, `research/037-requirements-to-code-practices.md` | Strong in SE practice; LLM-specific evidence supports artifact chains |
| P2 Req QA | ambiguity → rework | `research/036-requirements-qa-iso-29148.md`, `research/034-llms-in-re-guideline.md` | Direct evidence (LLM assists QA effectively) |
| P3 Grounding | API hallucination / outdated patterns | `research/008-api-hallucination.md`, `research/017-context-retrieval-repo-editing.md`, `research/012-autocoderover.md` | Direct evidence (hallucination, retrieval tradeoffs) |
| P4 Decision search | premature convergence | `research/019-plansearch.md`, `research/020-codetree.md`, `research/042-rankef.md` | Strong for code-gen; needs careful transfer to repo work |
| P5 Spikes | unknown unknowns | `research/014-codeplan.md`, `research/031-alphacodium.md` | Good support for "evidence first" + adaptive planning |
| P6 Phase chunking | long-context omission | `research/004-context-length-hurts.md`, `research/005-lost-in-middle-code.md` | Strong evidence |
| P7 Bead packaging (TDD-first) | vague tasks → vague output; low pass rate | `research/037-requirements-to-code-practices.md`, `research/011-agentless.md`, `research/054-tdd-ai-code-gen.md` | Strong practitioner support; TDD yields 45.97% improvement |
| P8 Adaptive decomposition | rigid task trees | `research/038-adapt.md`, `research/039-tdag.md` | Evidence from tool/planning domains; principle transfers |
| P9 Exec loop (3-iteration cap) | "think harder" / security degradation | `research/022-chatrepair.md`, `research/045-repairagent.md`, `research/046-d4c.md`, `research/043-rlef.md`, `research/053-feedback-loop-security.md` | Strong evidence; security degrades with unlimited iterations |
| P10 Calibration | drift compounding / debate noise | `research/003-debate-or-vote.md`, `research/041-debatecoder.md`, `research/019-plansearch.md`, `research/020-codetree.md` | Evidence supports selection + test-mediated dispute resolution |
| P11 Traceability | local optimization / missing coverage | `research/014-codeplan.md`, `research/021-swe-bench-plus.md` | Indirect: traceability is classic SE; maps well to agent failure modes |
| P12 Release readiness | benchmark overconfidence / drift | `research/028-swe-bench-live.md`, `research/029-swe-rebench.md`, `research/047-humaneval-pro.md`, `research/044-iris.md`, `research/050-swe-bench-pro.md` | Strong "reality check" evidence; best models solve only ~23% |
| **P13 Security Gate** | ~40% vulnerability rate in LLM code | `research/052-llm-security-vulnerabilities.md`, `research/053-feedback-loop-security.md`, `research/044-iris.md` | **2025 update:** Direct evidence; mandatory `ubs` gate |
| **P14 Human Verification** | AI slows experts on unfamiliar code | `research/051-metr-rct.md`, `research/050-swe-bench-pro.md` | **2025 update:** 19% slowdown without human verification |

---

## What's intentionally *not* claimed

- That multi-agent "debate" is inherently good: it isn't unless grounded in evidence and selection (`research/003-debate-or-vote.md`).
- That long context alone solves planning: it can worsen omission (`research/004-context-length-hurts.md`, `research/005-lost-in-middle-code.md`).
- That high benchmark scores guarantee production robustness: they don't (`research/021-swe-bench-plus.md`, `research/028-swe-bench-live.md`).

### 2025 Reality Checks (Critical Updates)

- **That AI assistance always improves productivity:** It doesn't for experienced devs on unfamiliar code—19% slower (`research/051-metr-rct.md`).
- **That best models are highly reliable:** They solve only ~23% of realistic tasks (`research/050-swe-bench-pro.md`).
- **That more iterations improve code:** Security degrades with repeated self-correction (`research/053-feedback-loop-security.md`).
- **That LLM code is reasonably safe:** ~40% has vulnerabilities; security scanning is mandatory (`research/052-llm-security-vulnerabilities.md`).
- **That TDD is optional:** It yields 45.97% pass@1 improvement; tests must be written first (`research/054-tdd-ai-code-gen.md`).

