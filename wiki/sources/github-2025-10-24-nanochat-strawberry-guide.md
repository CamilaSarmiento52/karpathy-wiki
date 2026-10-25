---
type: source
raw_path: raw/github/karpathy__nanochat__discussion-164.md
published: 2025-10-24
medium: github
summary: "His guide to teaching nanochat d32 to count letters in a word with synthetic SpellingBee and SimpleSpelling tasks in midtraining and SFT, designing the answer around the tokenizer so a small model never has to do too much work in one token."
url: https://github.com/karpathy/nanochat/discussions/164
title: "Guide: counting r in strawberry (and how to add abilities generally)"
---
# Guide: counting r in strawberry (and how to add abilities generally)
Raw: [[raw/github/karpathy__nanochat__discussion-164]] · Original: https://github.com/karpathy/nanochat/discussions/164

The text before the first heading is cited `§intro`. The raw file is his post only; the quoted user templates and the example conversations in it are generated data, not his statements.

## Summary
He uses counting the r's in "strawberry" as a worked example of adding any capability to nanochat: a new synthetic task, `SpellingBee`, generates two-turn conversations whose correct answers the model imitates during midtraining and SFT (§intro). User prompts are randomly varied, including other languages, so the skill is evoked however it is asked (§Entropy). The answer tries a manual approach and then checks with the Python tool; he calls this reasoning "smoke and mirrors" for now, a schema that simulated mistakes or RL could make real (§Reasoning structure). Every formatting choice is made with the tokenizer in mind: quotes and commas force token boundaries so the word is spelled into single letters, a simpler `SimpleSpelling` task drills spelling, and an explicit running count makes each step a small one (§Spelling, §Counting). The task is hard for an LLM because of whitespace in tokens, splitting tokens into characters and keeping a counter; reasoning spreads that work over many tokens, and the deployed d32 can now count letters (§Summary).

## Key points
- Add a capability by writing a synthetic task and mixing it into midtraining and SFT → [[teach-a-capability-with-synthetic-tasks]], [[pretraining-and-finetuning]]
- Randomised, multilingual prompts as data augmentation ("Entropy") → [[synthetic-data-is-the-future-if-you-keep-its-entropy]]
- Manual attempt, then a Python check → [[llm-tool-use]]
- Reasoning shown in SFT as a prior, RL to make it real → [[rlvr]], [[rl-lets-models-discover-their-own-thinking-strategies]]
- Token boundaries from quotes, commas and spaces; " poll" vs "poll" → [[tokenization]]
- Why counting letters is hard for an LLM → [[a-lot-of-llm-oddness-traces-back-to-tokenization]]
- Spread computation over tokens; small models have few layers per token → [[transformers-need-tokens-to-think]]
- d32 on nanochat.karpathy.ai can count letters → [[nanochat]]

## Fed pages
- [[nanochat]]
- [[teach-a-capability-with-synthetic-tasks]]
- [[tokenization]]
- [[a-lot-of-llm-oddness-traces-back-to-tokenization]]
- [[transformers-need-tokens-to-think]]
- [[synthetic-data-is-the-future-if-you-keep-its-entropy]]
- [[pretraining-and-finetuning]]
- [[llm-tool-use]]
- [[rlvr]]
- [[rl-lets-models-discover-their-own-thinking-strategies]]
