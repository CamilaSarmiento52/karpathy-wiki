---
type: claim
stated_on: 2023-01-17
confidence: stated
sources: ["[[youtube-2023-01-17-gpt-from-scratch]]", "[[talk-2023-05-25-state-of-gpt]]", "[[youtube-2023-11-23-intro-to-llms]]", "[[youtube-2024-06-09-reproduce-gpt-2]]", "[[github-2024-06-17-build-nanogpt-readme]]"]
topic: "[[pretraining-and-finetuning]]"
---
# Pretraining alone gives a document completer, not an assistant
> "you get a document completer" — [[youtube-2023-01-17-gpt-from-scratch]] @1:51:29

## Context
After the pretraining stage, he says, you do not get something that answers your questions: it will complete whatever a similar internet document would, so a question may be answered with more questions, and the behaviour is undefined and unaligned ([[youtube-2023-01-17-gpt-from-scratch]] @1:51:29, @1:52:02). It babbles, but not Shakespeare; it babbles internet ([[youtube-2023-01-17-gpt-from-scratch]] @1:51:29). The finetuning stage, supervised examples, a reward model and PPO, is what aligns it into an assistant ([[youtube-2023-01-17-gpt-from-scratch]] @1:52:36, @1:53:08, @1:53:43). GPT-3 is architecturally nearly identical to the lecture model but 10,000 to 1 million times bigger, and the finetuning stage is much harder to replicate because much of the data is internal to OpenAI; nanoGPT focuses on pretraining ([[youtube-2023-01-17-gpt-from-scratch]] @1:50:56, @1:54:16, @1:55:22).

Four months later, in State of GPT, he says the same of base models: they are not assistants, they want to complete documents, so a request may be answered with more questions ([[talk-2023-05-25-state-of-gpt]] @10:05, @10:36). Asked for a poem, a base model does better if prompted as the start of a document such as "here's a poem about bread and cheese" ([[talk-2023-05-25-state-of-gpt]] @10:36). Few-shot prompts trick a base model into doing tasks by making it believe it is imitating a document ([[talk-2023-05-25-state-of-gpt]] @08:56, @09:31).

In November 2023 he says the Llama 2 base model is not directly usable: given questions it gives more questions, because it is just an internet document sampler ([[youtube-2023-11-23-intro-to-llms]] @20:30).

In the GPT-2 lecture, published 2024-06-09, he says everything he built is only pretraining: the model dreams documents and you cannot talk to it like ChatGPT, until supervised finetuning on conversations ([[youtube-2024-06-09-reproduce-gpt-2]] @3:55:21, @3:55:54).

The build-nanogpt README, dated 2024-06-17, says GPT-2 and GPT-3 are simple language models trained on internet documents and all they do is "dream" internet documents, so you cannot talk to them as you can to ChatGPT ([[github-2024-06-17-build-nanogpt-readme]] §intro).

## Related claims
- **Note:** no earlier claim in the wiki covers the training stages; his 2025 account of RLVR as a new stage is on [[rlvr]], linked from [[pretraining-and-finetuning]] as related only ([[youtube-2023-01-17-gpt-from-scratch]] @1:55:22).
