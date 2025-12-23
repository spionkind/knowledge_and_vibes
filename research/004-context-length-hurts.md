# Context Length Alone Hurts

**Paper:** Context Length Alone Hurts LLM Performance Despite Perfect Retrieval
**URL:** https://arxiv.org/abs/2510.05381
**Date:** October 2025

---

## Summary

LLM performance degrades with longer inputs even when the model can perfectly retrieve all relevant information. This happens even when irrelevant tokens are replaced with whitespace or completely masked.

**Methodology:** Split short problems into evidence + question, insert distractors between them, measure if solving (not just retrieval) works.

**Results with essay distraction (0-30K tokens):**

| Model | Task | Degradation |
|-------|------|-------------|
| Llama3 8B | HumanEval (code) | 47.6% drop |
| Llama3 8B | VarSum (synthetic) | 85% drop |
| Mistral 7B | GSM8K (math) | 34.2% drop |

**With whitespace only:**

| Model | Task | Degradation |
|-------|------|-------------|
| Llama3 8B | VarSum | 48% drop at 30K |
| Mistral 7B | GSM8K | 30% drop at 30K |

**With complete masking (zero distraction):**

Still 21-50% drops. Even when the model can only attend to relevant tokens.

**Mitigation - "Retrieve Then Solve":**
1. Model recites relevant evidence from long context
2. Then solves using only that short output
3. Result: 35.5% → 66.7% on GSM8K at 26K tokens

---

## Practical Implications

1. **Keep relevant context together** - Don't scatter critical info across long documents
2. **Retrieval + short-context solving works** - Your cm/cass approach is validated
3. **Task type matters:**
   - Synthetic tasks (VarSum): 85% drop
   - Real code (HumanEval): 47.6% drop
   - Math (GSM8K): 34% drop
4. **Model size matters** - Closed-source models (GPT-4o, Claude) showed smaller degradation
5. **The 85% number is worst-case** - That's a small model on a synthetic task

**For your system:**
- Phase chunking is the right pattern
- Don't mandate specific line limits based on this paper
- The "recite then solve" pattern is interesting for calibration
- Frontier models (what you likely use) are less affected
