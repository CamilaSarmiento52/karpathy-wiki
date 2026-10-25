---
type: source
raw_path: raw/github/karpathy__nanochat__discussion-1.md
published: 2025-10-13
medium: github
summary: "His launch walkthrough of nanochat's speedrun on one 8×H100 node: a Rust BPE tokenizer, a d20 pretraining run that slightly beats GPT-2 large on CORE, midtraining, SFT and an optional GSM8K RL stage, about 3h51m and $92 up to SFT, with every stage's evals in a report card."
url: https://github.com/karpathy/nanochat/discussions/1
title: "Introducing nanochat: The best ChatGPT that $100 can buy."
---
# Introducing nanochat: The best ChatGPT that $100 can buy.
Raw: [[raw/github/karpathy__nanochat__discussion-1]] · Original: https://github.com/karpathy/nanochat/discussions/1

The text before the first heading is cited `§intro`. Numbers on wiki pages carry a tag:
measured (his reported result from a run), target (a goal or recommendation for a run not
reported), comparison (someone else's figure or a baseline), setting (a configuration value he
chose) or estimate (arithmetic done before or instead of measuring).

## Summary
He steps through `speedrun.sh`, which trains "the best ChatGPT that $100 can buy" on an 8×H100 node at about $24/hour (§intro, §Environment setup). He trains a 65,536-token byte-level BPE tokenizer with a new Rust implementation, because minbpe is too slow and Hugging Face tokenizers too bloated, and compares its compression with GPT-2's and GPT-4's (§Environment setup, §Train the tokenizer). Pretraining a 20-layer, ~560M-parameter model on ~11.2B FineWeb-EDU tokens, the Chinchilla ratio, takes about 3 hours and reaches a CORE score of 0.22, between GPT-2 large and GPT-2 xl (§Pretraining). Midtraining on conversations, multiple-choice and tool-use data, then SFT, give a chat model he evaluates on ARC, MMLU, GSM8K, HumanEval and his own ChatCORE; an optional, simplified GRPO stage hill-climbs GSM8K (§Midtraining, §Supervised Finetuning (SFT), §Reinforcement Learning (RL)). Up to SFT the run took 3h51m, about $92.4, summarised in an auto-generated report card, and `--depth` scales the whole recipe to bigger models (§Report card, §Your turn).

## Key points
- The launch post: speedrun.sh, d20, stages, report card, $100 budget → [[nanochat]]
- rustbpe for training, tiktoken for inference; 65,536 vocab; 4.8 chars/token; vs GPT-2 and GPT-4 → [[tokenization]], [[minbpe]], [[he-prefers-tiktoken-byte-level-bpe-to-sentencepiece]]
- Pretraining, midtraining, SFT and RL as four stages, each with what it adapts → [[pretraining-and-finetuning]]
- Pretraining compresses web text and gains world knowledge → [[pretraining-is-lossy-compression-of-the-internet]]
- Base model is a fancy autocomplete → [[pretraining-gives-a-document-completer]]
- CORE, bits per byte, ChatCORE; small models must be taught multiple choice in midtraining → [[llm-evaluation]]
- Simplified GRPO on GSM8K; RL sucks supervision bits through a straw → [[rlvr]], [[rl-sucks-supervision-bits-through-a-straw]], [[llm-self-improvement-over-time]]
- The learning-rate multiplier ramps to 0 at the end of training → [[do-not-decay-the-learning-rate-to-zero]]

## Fed pages
- [[rustbpe]]
- [[nanochat]]
- [[tokenization]]
- [[minbpe]]
- [[he-prefers-tiktoken-byte-level-bpe-to-sentencepiece]]
- [[pretraining-and-finetuning]]
- [[pretraining-is-lossy-compression-of-the-internet]]
- [[pretraining-gives-a-document-completer]]
- [[llm-evaluation]]
- [[rlvr]]
- [[rl-sucks-supervision-bits-through-a-straw]]
- [[do-not-decay-the-learning-rate-to-zero]]
- [[llm-self-improvement-over-time]]
- [[rl-is-terrible-but-better-than-imitation]]
