---
type: source
raw_path: raw/youtube/zjkBMFhNj_g.md
published: 2023-11-23
medium: youtube
summary: "A one-hour general-audience talk: an LLM as two files, pretraining as lossy compression of the internet, finetuning into an assistant, scaling laws, tool use, System 2 and self-improvement as open directions, the LLM as an operating-system kernel, and LLM security."
url: https://www.youtube.com/watch?v=zjkBMFhNj_g
title: "[1hr Talk] Intro to Large Language Models"
---
# [1hr Talk] Intro to Large Language Models
Raw: [[raw/youtube/zjkBMFhNj_g]] · Original: https://www.youtube.com/watch?v=zjkBMFhNj_g

## Summary
A re-recording, on his own channel, of a 30-minute intro talk he had given at an event run by Scale AI (@00:00, @03:18). He describes an LLM such as Llama 2 70B as two files, a 140 GB parameters file and about 500 lines of C that run it, and training as a lossy compression of roughly 10 TB of internet text into those parameters (@01:40, @02:13, @04:25, @05:30). He explains next-word prediction, why it forces the network to learn about the world, and why sampling from it "dreams" internet documents, then describes pretraining, finetuning on human-written Q&A, and an optional comparison-based RLHF stage (@07:43, @08:50, @14:21, @21:03, @22:09). The middle of the talk covers scaling laws, tool use (browser, calculator, Python, DALL-E) and multimodality, and research directions: System 2 thinking, AlphaGo-style self-improvement and customization (@25:28, @32:07, @33:12, @35:23, @38:14, @40:27). He ties these into the LLM as the kernel process of an emerging operating system, then closes with LLM security: jailbreaks, prompt injection and data poisoning (@42:06, @43:45, @45:59, @51:27, @56:28).

## Key points
- An LLM is two files, the parameters and a small program that runs them; inference is cheap, training is the expensive part → [[an-llm-is-just-two-files]], [[pretraining-and-finetuning]]
- Pretraining compresses about 10 TB of text into 140 GB of parameters, roughly 100x and lossy; next-word prediction forces the network to learn about the world → [[pretraining-is-lossy-compression-of-the-internet]], [[pretraining-and-finetuning]]
- Sampling dreams internet documents; you never know which parts are memorized or hallucinated → [[sampling-from-language-models]], [[pretraining-and-finetuning]]
- We know the architecture but not what the parameters do; treat LLMs as mostly inscrutable empirical artifacts → [[llms-are-mostly-inscrutable-empirical-artifacts]]
- The reversal curse and prompt injection, before he used the word jagged → [[jagged-intelligence]]
- Pretraining is about knowledge, finetuning about alignment; base models answer questions with more questions → [[pretraining-and-finetuning]], [[pretraining-gives-a-document-completer]]
- Stage three uses comparisons because comparing is easier than writing; OpenAI calls it RLHF → [[pretraining-and-finetuning]]
- Closed models currently work better; open models chase them → [[llms-as-operating-systems]]
- Performance is a smooth, predictable function of parameters and data, which drives the GPU gold rush → [[scaling-laws]], [[scaling-offers-a-guaranteed-path-to-better-models]]
- Tool use, multimodality and customization are axes of improvement → [[llm-tool-use]]
- LLMs currently have only System 1; the aim is to convert time into accuracy → [[system-1-and-system-2-thinking]], [[llms-currently-only-have-a-system-1]]
- Self-improvement lacks a general reward criterion but may work in narrow domains → [[llm-self-improvement]], [[self-improvement-may-be-possible-in-narrow-domains]]
- The LLM is the kernel process of an emerging OS; the context window is its RAM → [[llms-as-operating-systems]], [[llms-are-the-kernel-of-an-emerging-operating-system]]
- Jailbreaks, prompt injection and data poisoning are a new cat-and-mouse security field → [[llm-security]]

## Fed pages
- [[an-llm-is-just-two-files]]
- [[pretraining-and-finetuning]]
- [[pretraining-is-lossy-compression-of-the-internet]]
- [[sampling-from-language-models]]
- [[llms-are-mostly-inscrutable-empirical-artifacts]]
- [[jagged-intelligence]]
- [[pretraining-gives-a-document-completer]]
- [[llms-as-operating-systems]]
- [[scaling-laws]]
- [[scaling-offers-a-guaranteed-path-to-better-models]]
- [[llm-tool-use]]
- [[system-1-and-system-2-thinking]]
- [[llms-currently-only-have-a-system-1]]
- [[llm-self-improvement]]
- [[self-improvement-may-be-possible-in-narrow-domains]]
- [[llms-are-the-kernel-of-an-emerging-operating-system]]
- [[llm-security]]
