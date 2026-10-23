---
type: topic
aliases: [Pretraining, finetuning, RLHF, ChatGPT training stages, pretraining vs finetuning, alignment stage, fine-tuning]
first_seen: 2023-01-17
last_updated: 2023-01-17
sources: ["[[youtube-2023-01-17-gpt-from-scratch]]"]
related: ["[[rlvr]]", "[[nanogpt]]", "[[transformer-architecture]]", "[[tokenization]]"]
---
# Pretraining and finetuning
Training ChatGPT, as he describes it in January 2023, has roughly two stages: pretraining, which trains a decoder-only Transformer on a large chunk of the internet to babble text, and finetuning, which aligns the result into an assistant ([[youtube-2023-01-17-gpt-from-scratch]] @1:48:42, @1:49:14, @1:52:36).

## What he says
Pretraining is very similar to the lecture's tiny baby pretraining step ([[youtube-2023-01-17-gpt-from-scratch]] @1:48:42, @1:49:14). His Shakespeare model has about 10 million parameters trained on about 1 million characters, roughly 300,000 tokens in OpenAI's vocabulary ([[youtube-2023-01-17-gpt-from-scratch]] @1:49:14, @1:49:47). GPT-3's largest model has 175 billion parameters trained on 300 billion tokens, about a millionfold more data, and that is not even large by today's standards; training at that scale is a massive infrastructure challenge with thousands of GPUs ([[youtube-2023-01-17-gpt-from-scratch]] @1:50:22, @1:50:56). He says GPT-3's architecture is nearly identical to what the lecture implemented, and its hyperparameters (layers, n_embd, heads, head size, batch size, learning rate) should be recognisable ([[youtube-2023-01-17-gpt-from-scratch]] @1:50:22, @1:50:56). Models like GPT-3 are between 10,000 and 1 million times bigger depending on how you count ([[youtube-2023-01-17-gpt-from-scratch]] @1:55:22).

After pretraining you get a document completer that babbles internet, may answer questions with more questions, and is unaligned ([[youtube-2023-01-17-gpt-from-scratch]] @1:51:29, @1:52:02). The finetuning stage aligns it to be an assistant in roughly three steps: supervised finetuning on question-answer documents, perhaps thousands of examples; raters ranking responses to train a reward model; and PPO, a policy-gradient reinforcement-learning optimiser, finetuning the sampling policy to score high reward ([[youtube-2023-01-17-gpt-from-scratch]] @1:52:36, @1:53:08, @1:53:43). Very large models are very sample efficient during finetuning ([[youtube-2023-01-17-gpt-from-scratch]] @1:53:08). Much of this data is internal to OpenAI and much harder to replicate; nanoGPT focuses on pretraining ([[youtube-2023-01-17-gpt-from-scratch]] @1:54:16). Anything that is not a plain document completer, such as task performance, alignment or sentiment, requires further finetuning stages, simple supervised or RLHF-style ([[youtube-2023-01-17-gpt-from-scratch]] @1:55:22, @1:55:55).

## Claims
- [[pretraining-gives-a-document-completer]]

## Related
- [[rlvr]] — **Note:** the lecture describes the 2023 recipe of pretraining, supervised finetuning and RLHF; his 2025 review names RLVR as a different, later training stage. The pages are linked here as related only, not as evidence for each other.
- [[nanogpt]] — the pretraining-stage repo
- [[transformer-architecture]] — what both stages train
- [[tokenization]] — why 1 million characters is about 300,000 tokens
