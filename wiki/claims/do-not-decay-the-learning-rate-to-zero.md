---
type: claim
stated_on: 2024-06-12
confidence: stated
sources: ["[[github-2024-06-12-llmc-gpt-2-774m]]", "[[github-2024-07-11-llmc-gpt-2-1-6b]]"]
context: ["[[github-2024-05-28-llmc-gpt-2-124m]]", "[[youtube-2024-06-09-reproduce-gpt-2]]", "[[github-2025-10-13-nanochat-discussion-introducing]]"]
topic: "[[gradient-descent]]"
---
# He concluded the llm.c runs should not decay the learning rate to zero
> "We shouldn't decay the LR to 0%." — [[github-2024-06-12-llmc-gpt-2-774m]] §intro

## Context
**2024-06-12, after the 774M run.** At the tail end of the GPT-2 (774M) optimisation, he says, the run was going way too slow, so for future runs he will probably follow the GPT-3 paper and decay only to 10%, `-q 0.1` instead of `-q 0.0` ([[github-2024-06-12-llmc-gpt-2-774m]] §intro (Reflections)). It is one of three reflections after the run, beside a wider eval suite and a worrying validation-loss kink ([[github-2024-06-12-llmc-gpt-2-774m]] §intro (Reflections)).

**His practice in llm.c, dated.** On 2024-05-28 the GPT-2 (124M) run decays the learning rate to 0 over training ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (Args guide)). On 2024-06-12 he writes that they should not decay to 0% ([[github-2024-06-12-llmc-gpt-2-774m]] §intro (Reflections)). On 2024-07-11 the 1.6B run uses `-q 0.1`, decaying to 10% of the maximum learning rate over training, following the GPT-3 paper ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Args guide)). This is a change of practice inside one project, stated by him as a lesson from the 774M run ([[github-2024-06-12-llmc-gpt-2-774m]] §intro (Reflections); [[github-2024-05-28-llmc-gpt-2-124m]] §intro (Args guide)). **Note:** no earlier claim page said to decay to zero, so no `contradicts` or `extends` is set.

**Note:** the PyTorch run in the GPT-2 lecture, published 2024-06-09, already decayed to 10% at its last step, following the GPT-3 paper; the lecture mentions a zero minimum only on the schedule plot it starts from, and does not argue for or against decaying to zero ([[youtube-2024-06-09-reproduce-gpt-2]] @2:21:02, @2:24:59; [[github-2024-06-12-llmc-gpt-2-774m]] §intro (Reflections)).

**Note:** in nanochat's launch post, dated 2025-10-13, the default learning-rate multiplier `lrm` ramps linearly down to 0 near the end of training (setting) ([[github-2025-10-13-nanochat-discussion-introducing]] §Pretraining). This claim is scoped to the llm.c runs, and nanochat is a different project with a different optimiser setup (Muon for the matrices, AdamW for the embeddings); he gives no reason or opinion on the schedule there, so this is not a contradiction or a change of mind ([[github-2025-10-13-nanochat-discussion-introducing]] §Pretraining; [[github-2024-06-12-llmc-gpt-2-774m]] §intro (Reflections)).

## Related claims
- **Note:** [[inherited-gpt-3-hyperparameters-look-conservative]] is about the GPT-3 settings being too cautious; here he returns to one of them, the 10% floor, after his own run went too slow at zero ([[github-2024-06-12-llmc-gpt-2-774m]] §intro (Reflections); [[youtube-2024-06-09-reproduce-gpt-2]] @3:51:29).
