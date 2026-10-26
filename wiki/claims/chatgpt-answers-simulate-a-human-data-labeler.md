---
type: claim
stated_on: 2025-02-05
confidence: stated
sources: ["[[youtube-2025-02-05-deep-dive-into-llms]]"]
context: ["[[talk-2023-05-25-state-of-gpt]]"]
topic: "[[pretraining-and-finetuning]]"
supports: ["[[llms-want-to-imitate-not-succeed]]"]
---
# An assistant's answer is, roughly, a statistical simulation of a human data labeler following the company's labeling instructions
> "you're not talking to a magical AI you're talking to an average labeler" — [[youtube-2025-02-05-deep-dive-into-llms]] @1:18:17

## Context
Explaining post-training, he says the assistant's answer is statistically aligned with a training set seeded by humans following labeling instructions ([[youtube-2025-02-05-deep-dive-into-llms]] @1:16:35, @1:17:10). The labelers are often educated experts, so it is like asking an instantaneous simulation of a fairly skilled person of the kind hired to build these datasets ([[youtube-2025-02-05-deep-dive-into-llms]] @1:17:43, @1:18:17). If the query is in the post-training data the answer will resemble what the labeler wrote; otherwise it is more emergent, combining knowledge from pretraining with the style of post-training ([[youtube-2025-02-05-deep-dive-into-llms]] @1:18:52, @1:19:25, @1:19:59).

In his closing recap he calls what comes back a neural-network simulation of a data labeler at OpenAI, a lossy one limited to a fixed amount of compute per token ([[youtube-2025-02-05-deep-dive-into-llms]] @3:24:12, @3:24:47, @3:25:20). Thinking models change this, he says: their output is not just imitation of a labeler but comes from reinforcement learning ([[youtube-2025-02-05-deep-dive-into-llms]] @3:27:03, @3:28:11).

## Related claims
- Supports [[llms-want-to-imitate-not-succeed]]: in State of GPT (published 2023-05-25) the model imitates everything in its training data ([[talk-2023-05-25-state-of-gpt]] @30:02); in the 2025-02-05 lecture the assistant imitates the labelers who wrote its post-training data ([[youtube-2025-02-05-deep-dive-into-llms]] @1:16:35). The 2025 lecture does not repeat the advice to ask for a strong solution, so the support covers imitation only.
- **Note:** the exception he makes for thinking models is the subject of [[rl-lets-models-discover-their-own-thinking-strategies]] ([[youtube-2025-02-05-deep-dive-into-llms]] @3:27:03).
