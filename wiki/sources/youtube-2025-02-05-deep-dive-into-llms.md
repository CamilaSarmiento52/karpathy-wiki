---
type: source
raw_path: raw/youtube/7xTGNNLPyMI.md
published: 2025-02-05
medium: youtube
summary: "A 3.5-hour general-audience walk through the whole ChatGPT pipeline: FineWeb data, tokenization, pretraining a base model, SFT on labeler conversations, LLM psychology (hallucination, self-knowledge, tokens to think, Swiss-cheese capabilities), RL and thinking models such as DeepSeek-R1, and why RLHF is not real RL."
url: https://www.youtube.com/watch?v=7xTGNNLPyMI
title: "Deep Dive into LLMs like ChatGPT"
---
# Deep Dive into LLMs like ChatGPT
Raw: [[raw/youtube/7xTGNNLPyMI]] · Original: https://www.youtube.com/watch?v=7xTGNNLPyMI

## Summary
A comprehensive general-audience lecture on what sits behind the ChatGPT text box, aimed at giving mental models for a tool that is good at some things, bad at others and has sharp edges (@00:00, @00:34). Pretraining starts from filtered web text such as FineWeb (about 44 TB, 15 trillion tokens), tokenized with byte-pair encoding, and trains a Transformer to predict the next token; the result is a base model, an internet-document simulator and lossy compression of the internet (@02:14, @10:38, @14:40, @43:04, @49:59). Post-training swaps the data for conversations written by human labelers under labeling instructions, so the assistant is a statistical simulation of a labeler; he then covers the "LLM psychology" this produces: hallucination and its two mitigations, missing self-knowledge, needing tokens to think, and tokenization-driven failures at counting and spelling (@1:02:42, @1:18:17, @1:20:31, @1:26:02, @1:32:43, @1:41:37, @1:57:46, @2:01:07). The third stage is reinforcement learning on practice problems with known answers, where models like DeepSeek-R1 and OpenAI's o-series discover chains of thought themselves; he compares this to AlphaGo and Move 37, and says RLHF, whose learned reward model gets gamed, is not RL in that sense (@2:13:19, @2:28:46, @2:32:04, @2:42:07, @2:45:26, @3:04:50). He closes with the Swiss cheese model of capabilities, advice to use LLMs as tools and check their work, and expected developments: multimodality, supervised agents, computer use and test-time learning (@3:08:39, @3:09:14, @3:09:48, @3:11:26, @3:13:05).

## Key points
- FineWeb-style filtering of Common Crawl into ~44 TB / 15T tokens; pretraining predicts the next token in windows of tokens → [[pretraining-and-finetuning]]
- Bits to bytes to BPE; GPT-4 uses 100,277 tokens; models see tokens, not characters → [[tokenization]], [[a-lot-of-llm-oddness-traces-back-to-tokenization]], [[tokenization-free-modeling-would-be-amazing-but-is-unproven]]
- Inference flips a biased coin per token; outputs are stochastic remixes of the training data → [[sampling-from-language-models]]
- The Transformer is a fixed, stateless mathematical expression; its neurons are far simpler than biological ones → [[transformer-architecture]]
- GPT-2 was the first recognizably modern stack; his llm.c reproduction cost about $600 against an estimated $40,000 in 2019 → [[gpt-2-is-the-first-recognizably-modern-llm-stack]], [[llm-c]], [[compute-efficiency]]
- GPU demand and the Nvidia gold rush come from bigger networks on more tokens → [[scaling-laws]]
- A base model is an internet text token simulator; a release is code plus parameters → [[pretraining-gives-a-document-completer]], [[an-llm-is-just-two-files]]
- The parameters are a lossy compression of the internet; knowledge is a vague recollection, context is working memory → [[pretraining-is-lossy-compression-of-the-internet]], [[parameters-are-vague-recollection-context-is-working-memory]]
- Few-shot prompts and a fake conversation page can make a base model useful → [[prompting-llms]]
- An assistant's answer is a simulation of a human data labeler following labeling instructions → [[chatgpt-answers-simulate-a-human-data-labeler]], [[llms-want-to-imitate-not-succeed]], [[pretraining-and-finetuning]]
- Hallucination comes from imitating confident answers; mitigations are "I don't know" training data and web search → [[llm-hallucinations]], [[hallucinations-come-from-imitating-confident-answers]], [[llm-tool-use]]
- Models need tokens to think; use code for arithmetic, counting and spelling → [[transformers-need-tokens-to-think]], [[llm-tool-use]]
- Swiss cheese capabilities: Olympiad problems solved, 9.11 vs 9.9 failed → [[jagged-intelligence]]
- RL on practice problems lets models discover their own chains of thought; DeepSeek-R1, o1/o3 are thinking models → [[rlvr]], [[rl-lets-models-discover-their-own-thinking-strategies]], [[system-1-and-system-2-thinking]], [[self-improvement-may-be-possible-in-narrow-domains]], [[llms-currently-only-have-a-system-1]], [[llm-self-improvement-over-time]]
- AlphaGo and Move 37 show RL is not capped by human performance; LLMs show only hints so far → [[llm-self-improvement]]
- RLHF trains against a gameable reward model, so it is "not real RL"; it still helps, perhaps via the discriminator-generator gap → [[rlhf-is-not-real-rl]], [[rlhf-works-better-because-comparing-is-easier-than-generating]]
- Use LLMs as tools, check their work, own the result; agents will need supervision → [[use-llms-as-tools-and-check-their-work]], [[use-llms-as-copilots-with-human-oversight]]
- Longer context windows alone will not scale to long multimodal tasks; test-time learning needs new ideas → [[longer-context-windows-alone-will-not-scale-to-long-multimodal-tasks]]
- LM Arena has become a bit gamed; DeepSeek's MIT-licensed open weights near the top → [[llm-evaluation]], [[ai-ecosystem]]

## Fed pages
- [[pretraining-and-finetuning]]
- [[tokenization]]
- [[sampling-from-language-models]]
- [[transformer-architecture]]
- [[compute-efficiency]]
- [[scaling-laws]]
- [[prompting-llms]]
- [[llm-tool-use]]
- [[llm-hallucinations]]
- [[jagged-intelligence]]
- [[rlvr]]
- [[llm-self-improvement]]
- [[system-1-and-system-2-thinking]]
- [[llm-evaluation]]
- [[ai-ecosystem]]
- [[llm-c]]
- [[pretraining-gives-a-document-completer]]
- [[pretraining-is-lossy-compression-of-the-internet]]
- [[an-llm-is-just-two-files]]
- [[gpt-2-is-the-first-recognizably-modern-llm-stack]]
- [[transformers-need-tokens-to-think]]
- [[a-lot-of-llm-oddness-traces-back-to-tokenization]]
- [[tokenization-free-modeling-would-be-amazing-but-is-unproven]]
- [[rlhf-works-better-because-comparing-is-easier-than-generating]]
- [[llms-want-to-imitate-not-succeed]]
- [[use-llms-as-copilots-with-human-oversight]]
- [[self-improvement-may-be-possible-in-narrow-domains]]
- [[llms-currently-only-have-a-system-1]]
- [[chatgpt-answers-simulate-a-human-data-labeler]]
- [[hallucinations-come-from-imitating-confident-answers]]
- [[parameters-are-vague-recollection-context-is-working-memory]]
- [[rl-lets-models-discover-their-own-thinking-strategies]]
- [[rlhf-is-not-real-rl]]
- [[use-llms-as-tools-and-check-their-work]]
- [[longer-context-windows-alone-will-not-scale-to-long-multimodal-tasks]]
- [[llm-self-improvement-over-time]]
