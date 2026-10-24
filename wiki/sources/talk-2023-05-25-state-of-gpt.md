---
type: source
raw_path: raw/talks/bZQun8Y4L2A.md
published: 2023-05-25
medium: talk
summary: "Microsoft Build 2023 talk in two halves: the four-stage recipe for training GPT assistants (pretraining, supervised finetuning, reward modeling, RL), then how to use them: prompting around their cognitive differences from people, tools and retrieval, finetuning, and low-stakes, human-overseen use."
url: https://www.youtube.com/watch?v=bZQun8Y4L2A
title: "State of GPT | BRK216HFS"
---
# State of GPT
Raw: [[raw/talks/bZQun8Y4L2A]] · Original: https://www.youtube.com/watch?v=bZQun8Y4L2A

Only the announcer's introduction at @00:00 is another speaker. From @40:31 to the end he reads aloud an address GPT-4 wrote for the audience; those words are GPT-4's, not his, and the wiki does not quote or attribute them.

## Summary
He splits the talk into how GPT assistants are trained and how to use them well (@00:35). The training recipe has four serial stages, pretraining, supervised finetuning, reward modeling and reinforcement learning, with pretraining taking about 99 percent of the compute and the other three needing few GPUs for hours or days (@00:35, @01:07, @01:41). Base models complete documents rather than answer questions; SFT swaps in tens of thousands of contractor-written prompt and response pairs, and RLHF adds a reward model trained on rankings and RL that weights the language-modeling loss by reward (@10:36, @11:43, @13:23, @15:35). In the second half he argues that LLMs differ cognitively from people, spending equal compute per token with no inner monologue or self-check, and that prompting largely makes up for that difference: spread reasoning over tokens, sample several times, ask the model to check itself, ask for good performance, give it tools and retrieved context (@22:13, @23:22, @24:27, @25:32, @30:02, @32:15, @32:48). He recommends getting top performance first with GPT-4 and detailed prompts, then optimising cost, treating finetuning (and especially RLHF) as slower and harder (@37:12, @38:17, @38:51). Given current limitations he recommends low-stakes uses, always with human oversight, as copilots rather than autonomous agents (@39:24, @39:57).

## Key points
- Four serial stages, each with its own dataset, objective and resulting model; pretraining is about 99 percent of compute → [[pretraining-and-finetuning]]
- Tokenization is a lossless translation of text to integers, typically by byte pair encoding; vocabularies are a couple of tens of thousands of tokens → [[tokenization]]
- LLaMA 65B beats GPT-3 175B because it trained on far more tokens; parameter count alone is not a guide to power → [[pretraining-and-finetuning]]
- Base models want to complete documents, not answer; few-shot documents can trick them into tasks or even into acting as assistants, unreliably → [[pretraining-gives-a-document-completer]]
- Base, SFT and RLHF models are distinct; ChatGPT is RLHF, Vicuna-13B is SFT → [[pretraining-and-finetuning]]
- RLHF works better than SFT in human comparisons; his offered reason is that comparing is easier than generating → [[rlhf-works-better-because-comparing-is-easier-than-generating]]
- RLHF models lose entropy, so he still uses base models to generate more things like a list → [[pretraining-and-finetuning]]
- Transformers spend the same compute on every token and cannot think much per token, so reasoning must be spread across tokens → [[transformers-need-tokens-to-think]]
- Prompting largely makes up for the cognitive differences between human brains and LLMs: chain of thought, self-consistency, asking it to check → [[prompting-llms]]
- Many of these techniques recreate System 2 on top of System 1 token sampling; Tree of Thought adds Python glue code → [[system-1-and-system-2-thinking]]
- LLMs imitate the whole quality range of their data, so ask for a strong solution → [[llms-want-to-imitate-not-succeed]]
- Give LLMs tools and tell them what they are bad at; fill the context window with retrieved documents → [[llm-tool-use]]
- His default recommendations: GPT-4 with detailed prompts, few-shot examples, tools, chains; finetune only after prompting is squeezed; then cut cost → [[prompting-llms]]
- Use LLMs in low-stakes applications with human oversight, as copilots rather than autonomous agents; AutoGPT does not work well yet → [[use-llms-as-copilots-with-human-oversight]], [[this-is-the-decade-of-agents]]
- The copilot stance is background for his later autonomy-slider framing → [[partial-autonomy-apps]]
- Parameter count alone is no guide to power; LLaMA 65B trained on more tokens → [[scaling-laws]]
- Prompt injection, jailbreaks and data poisoning among the limitations → [[llm-security]]
- No self-knowledge and no reflection, but vast knowledge and a perfect working memory, before he called this jagged → [[jagged-intelligence]]

## Fed pages
- [[pretraining-and-finetuning]]
- [[tokenization]]
- [[pretraining-gives-a-document-completer]]
- [[rlhf-works-better-because-comparing-is-easier-than-generating]]
- [[transformers-need-tokens-to-think]]
- [[prompting-llms]]
- [[system-1-and-system-2-thinking]]
- [[llms-want-to-imitate-not-succeed]]
- [[llm-tool-use]]
- [[use-llms-as-copilots-with-human-oversight]]
- [[this-is-the-decade-of-agents]]
- [[partial-autonomy-apps]]
- [[jagged-intelligence]]
- [[scaling-laws]]
- [[llm-security]]
- [[llms-currently-only-have-a-system-1]]
- [[make-it-work-then-make-it-cheap]]
- [[llm-agents-over-time]]
