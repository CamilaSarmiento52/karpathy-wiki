---
type: claim
stated_on: 2023-01-17
confidence: stated
sources: ["[[youtube-2023-01-17-gpt-from-scratch]]"]
topic: "[[pretraining-and-finetuning]]"
---
# Pretraining alone gives a document completer, not an assistant
> "you get a document completer" — [[youtube-2023-01-17-gpt-from-scratch]] @1:51:29

## Context
After the pretraining stage, he says, you do not get something that answers your questions: it will complete whatever a similar internet document would, so a question may be answered with more questions, and the behaviour is undefined and unaligned ([[youtube-2023-01-17-gpt-from-scratch]] @1:51:29, @1:52:02). It babbles, but not Shakespeare; it babbles internet ([[youtube-2023-01-17-gpt-from-scratch]] @1:51:29). The finetuning stage, supervised examples, a reward model and PPO, is what aligns it into an assistant ([[youtube-2023-01-17-gpt-from-scratch]] @1:52:36, @1:53:08, @1:53:43). GPT-3 is architecturally nearly identical to the lecture model but 10,000 to 1 million times bigger, and the finetuning stage is much harder to replicate because much of the data is internal to OpenAI; nanoGPT focuses on pretraining ([[youtube-2023-01-17-gpt-from-scratch]] @1:50:56, @1:54:16, @1:55:22).

## Related claims
- **Note:** no earlier claim in the wiki covers the training stages; his 2025 account of RLVR as a new stage is on [[rlvr]], linked from [[pretraining-and-finetuning]] as related only ([[youtube-2023-01-17-gpt-from-scratch]] @1:55:22).
