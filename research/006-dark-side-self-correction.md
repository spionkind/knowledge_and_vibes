# Dark Side of LLM Self-Correction

**Paper:** Understanding the Dark Side of LLMs' Intrinsic Self-Correction
**URL:** https://arxiv.org/abs/2412.14959
**Date:** December 2024

---

## Summary

**Intrinsic self-correction** = asking an LLM to improve its response without any external feedback. This often makes things worse.

**Three failure modes:**

1. **Answer Wavering:** LLMs flip-flop on answers across rounds. Llama-3.1-8B overturned 58.8% of correct answers.

2. **Prompt Bias:** The refinement prompt ("Are you sure?") gets over-weighted vs the original question. Recency bias.

3. **Cognitive Biases:** Overthinking, cognitive overload with long contexts, perfectionism that breaks working code.

**Tasks tested:** BoolQ, AlfWorld, HotPotQA, HumanEval (code)

**Models tested:** ChatGPT (o1, 4o, 3.5-turbo), Llama (2-7B, 3-8B, 3.1-8B), DeepSeek (V3, R1)

**Mitigations:**
- **Question repeating:** Append original question after refinement prompt (+3.2-4.9%)
- **Supervised fine-tuning:** Train on correct→incorrect→correct examples. Cost: $0.004, 3 minutes. Near-zero error rates.

---

## Practical Implications

1. **Don't ask "are you sure?" without new information** - This is the problematic pattern
2. **External feedback is NOT this problem:**
   - Test results: "Your code fails with X" - fine
   - Other agent input: "I found issue Y" - fine
   - Docs: "The API changed" - fine
3. **Restate the original goal when asking for revisions** - The "question repeating" mitigation

**What IS intrinsic self-correction:**
- "Check your code again" (no new info)
- "Please reconsider" (no new info)
- "Double-check your answer" (no new info)

**What is NOT intrinsic self-correction:**
- "Your code fails test X with error Y" (external feedback)
- "Agent B found issue Z" (new information)
- "The docs say..." (grounding)

**For your system:** Calibration with evidence requirements is fine. The problem is asking for reconsideration without giving new information to consider.
