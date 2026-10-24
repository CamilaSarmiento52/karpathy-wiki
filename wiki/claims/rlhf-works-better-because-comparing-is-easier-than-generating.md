---
type: claim
stated_on: 2023-05-25
confidence: stated
sources: ["[[talk-2023-05-25-state-of-gpt]]", "[[youtube-2025-02-05-deep-dive-into-llms]]"]
topic: "[[pretraining-and-finetuning]]"
---
# RLHF models are preferred over SFT models, and he offers the ease of comparing over generating as one possible reason
> "Judging which one of these is good is a much easier task." — [[talk-2023-05-25-state-of-gpt]] @18:21

## Context
He reports the InstructGPT paper's finding that humans prefer outputs of RLHF (PPO) models over SFT models, and both over a prompted base model; he calls this the not-very-exciting answer that it works better ([[talk-2023-05-25-state-of-gpt]] @17:16). He says the community has not agreed on a single answer for why, and offers one reason potentially: the asymmetry between how easy it is computationally to compare versus generate ([[talk-2023-05-25-state-of-gpt]] @17:16, @17:49). His example is a contractor who may not be able to write a good haiku about paper clips but can judge which of several haikus is better, so comparisons leverage human judgment to make a slightly better model ([[talk-2023-05-25-state-of-gpt]] @17:49, @18:21). Later in the talk he says RLHF works a bit better than SFT if you can get it to work ([[talk-2023-05-25-state-of-gpt]] @38:51).

In the Deep Dive lecture, published 2025-02-05, he says the same with the same hedge: done correctly, RLHF gives slightly better models, why is not clear, and his best guess is "the discriminator generator Gap", since ordering five poems is far easier for a labeler than writing the ideal one ([[youtube-2025-02-05-deep-dive-into-llms]] @2:58:09, @2:58:41, @2:59:15, @2:59:49). Humans order rollouts rather than score them because ordering is easier ([[youtube-2025-02-05-deep-dive-into-llms]] @2:54:19).

## Related claims
- **Note:** the 2025 [[rlvr]] page says the pre-2025 recipe was pretraining, SFT and RLHF; that is background, not support ([[talk-2023-05-25-state-of-gpt]] @16:43).
- **Note:** compatible with [[rlhf-is-not-real-rl]]: in the same 2025-02-05 lecture he says RLHF helps a little and is not RL in the full sense ([[youtube-2025-02-05-deep-dive-into-llms]] @2:58:09, @3:06:27).
