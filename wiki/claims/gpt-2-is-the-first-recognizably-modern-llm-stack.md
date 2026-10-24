---
type: claim
stated_on: 2024-05-28
confidence: stated
sources: ["[[github-2024-05-28-llmc-gpt-2-124m]]", "[[youtube-2025-02-05-deep-dive-into-llms]]"]
topic: "[[transformer-architecture]]"
---
# GPT-2 was the first time the modern LLM stack came together in recognisable form
> "GPT-2 is the grand-daddy of LLMs" — [[github-2024-05-28-llmc-gpt-2-124m]] §intro

## Context
In the FAQ of his llm.c GPT-2 (124M) walkthrough, asked why he cares so much about GPT-2, he answers that it was the first time the modern LLM stack came together in a recognisably modern form, and that OpenAI released its parameters ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (FAQ)). He adds that GPT-3 changed little about the model, he thinks only the context size from 1024 to 2048; that GPT-4's details were never published; and that many other LLMs still strongly resemble GPT-2 despite its 2019 date, with Llama 3, from the architecture perspective, differing by a change of non-linearity in the MLP and the addition of RoPE relative positional encoding ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (FAQ)). This is the reason llm.c targets GPT-2 ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (FAQ)).

In the Deep Dive lecture, published 2025-02-05, he says he likes GPT-2 because it is the first time a recognizably modern stack came together, and that everything in it is recognizable today, only bigger: 1.6 billion parameters, a context of 1,024 tokens and about 100 billion training tokens ([[youtube-2025-02-05-deep-dive-into-llms]] @31:19, @31:52, @32:28, @33:01).
