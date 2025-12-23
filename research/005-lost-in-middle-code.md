# Lost-in-Middle for Code

**Paper:** Sense and Sensitivity: Examining the Influence of Semantic Recall on Long Context Code Reasoning
**URL:** https://arxiv.org/abs/2505.13353
**Date:** May 2025

---

## Summary

There's a "lost-in-the-middle" effect for code, but the severity depends on whether you're testing **lexical recall** (can you reproduce the code?) vs **semantic recall** (do you understand what it does?).

**Methodology:** Embed target function within 20-80 distractor functions, vary position, measure performance.

**Lexical recall (reproducing code):**

| Condition | Performance |
|-----------|-------------|
| Function-level | High accuracy across positions |
| Line-level, 20 distractors | 16% drop |
| Line-level, 80 distractors | 36% drop |

**Semantic recall (understanding code):**

| Model | Task | Drop |
|-------|------|------|
| Qwen 2.5 7B | CruxEval Input | 79.55% |
| Llama 3.1 8B | CruxEval Input | 46.67% |
| Small models | SemTrace | 94% (near-zero accuracy) |

**The 94% number:** This is on SemTrace, a synthetic task with randomized arithmetic where guessing is impossible. Real code reasoning (CruxEval) shows 30-50% drops.

**Key finding:** Lexical and semantic recall are independent. Some models are great at reproducing code but bad at understanding it (Gemma 3 27B). Others are the opposite.

---

## Practical Implications

1. **Position matters for reasoning** - Put critical code at start or end, not middle
2. **Function-level retrieval is fine** - Models can find and reproduce functions
3. **Semantic understanding suffers more** - Planning/reasoning tasks are more affected than retrieval
4. **The 94% is worst-case** - That's on a deliberately hard synthetic task
5. **Larger models more stable** - GPT 4.1 showed more resilience

**For your system:**
- Keep related context together (already doing this)
- Put important information at section boundaries
- The problem is mid-context positioning, not just total length
- Semantic tasks (planning, reasoning) need more care than retrieval
