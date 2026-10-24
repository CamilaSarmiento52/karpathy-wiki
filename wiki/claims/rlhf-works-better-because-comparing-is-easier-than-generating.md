---
type: claim
stated_on: 2023-05-25
confidence: stated
sources: ["[[talk-2023-05-25-state-of-gpt]]"]
topic: "[[pretraining-and-finetuning]]"
---
# RLHF models are preferred over SFT models, and he offers the ease of comparing over generating as one possible reason
> "Judging which one of these is good is a much easier task." — [[talk-2023-05-25-state-of-gpt]] @18:21

## Context
He reports the InstructGPT paper's finding that humans prefer outputs of RLHF (PPO) models over SFT models, and both over a prompted base model; he calls this the not-very-exciting answer that it works better ([[talk-2023-05-25-state-of-gpt]] @17:16). He says the community has not agreed on a single answer for why, and offers one reason potentially: the asymmetry between how easy it is computationally to compare versus generate ([[talk-2023-05-25-state-of-gpt]] @17:16, @17:49). His example is a contractor who may not be able to write a good haiku about paper clips but can judge which of several haikus is better, so comparisons leverage human judgment to make a slightly better model ([[talk-2023-05-25-state-of-gpt]] @17:49, @18:21). Later in the talk he says RLHF works a bit better than SFT if you can get it to work ([[talk-2023-05-25-state-of-gpt]] @38:51).

## Related claims
- **Note:** the 2025 [[rlvr]] page says the pre-2025 recipe was pretraining, SFT and RLHF; that is background, not support ([[talk-2023-05-25-state-of-gpt]] @16:43).
