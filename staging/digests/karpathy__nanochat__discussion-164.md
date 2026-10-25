# Digest: Guide: counting r in strawberry (and how to add abilities generally)
- raw: raw/github/karpathy__nanochat__discussion-164.md · published: 2025-10-24 · medium: github · words: 1688 (frontmatter)
- source slug: github-2025-10-24-nanochat-strawberry-guide

Number tags used below (same legend as the launch-post digest): **[measured]** his reported result
from a run; **[target]** a goal or recommendation for a run not reported; **[comparison]** someone
else's figure or a baseline; **[setting]** a configuration value he chose; **[estimate]**
arithmetic or approximation before or instead of measuring. This post has very few numbers.

Headings (exact, all `####` in the raw): `§intro`, `§Entropy`, `§Reasoning structure`, `§Spelling`,
`§Counting`, `§Summary`. The raw file is his post only; no replies by others are included.

## Source page
```
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

The text before the first heading is cited `§intro`.

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
```

## Candidates

### artifact: nanochat
- existing: yes (`wiki/artifacts/nanochat.md`, built from the 2025-10-13 launch Discussion and the 2026-07-03 README)
- statements:
  - He wanted to teach nanochat d32 to count the letter r in strawberry, as a cute example of how any arbitrary computing capability can be added to nanochat (§intro). [d32: setting, the model he taught]
  - The work lives in a new task under `tasks/`, `SpellingBee`, with a second task `SimpleSpelling`, introduced in commit 8892470 (§intro, §Spelling, §Summary).
  - The d32 deployed on nanochat.karpathy.ai can count letters now, he says (§Summary).
- **Note:** this is the first wiki source naming a d32 model or the live demo site; the page does not yet mention either.

### method: teach-a-capability-with-synthetic-tasks
- existing: no (checked `wiki/index/methods.md`: no method on adding abilities or synthetic data; closest are [[quick-experiment-loop]] and [[spelled-out-build-from-scratch]], neither fits)
- aliases: add a capability to nanochat, SpellingBee, synthetic task, data engine
- proposed steps (each from this source):
  1. Write a task that generates synthetic conversations of the problem with the correct answer attached, to be imitated in midtraining and SFT (§intro).
  2. Randomise the user prompt from many templates, including other languages, as data augmentation (§Entropy).
  3. Write the answer as a reasoning schema: a manual attempt, then a check with the Python tool (§Reasoning structure).
  4. Format the answer around the tokenizer so each piece is a clean token (§Spelling).
  5. Break the problem into all its implicit steps, with explicit intermediate state such as a running count (§Counting).
  6. Add a simpler sub-task for the part the model gets wrong and mix it in (§Spelling).
  7. Improve later with mistakes and recoveries, RL, more entropy, varied position in a conversation, and a data engine of hard cases (§Reasoning structure, §Summary).
- statements:
  - Adding a capability is done as usual through synthetic data generation during midtraining and SFT; every conversation is two turns: the user asks, nanochat answers in the set style (§intro). [2 turns: setting]
  - The prompts are "fudged" randomly for diversity, with a few other languages at the bottom of the template list so the task is triggered even when asked in another language; he calls this important data augmentation (§Entropy).
  - Playing with early versions, he noticed the model often got the spelling wrong, so he added `SimpleSpelling`, which only asks the model to spell, a very token-efficient way to learn the spelling task, mixed into training so the harder part gets more loss (§Spelling).
  - Possible improvements: simulate the task deeper in a conversation, add more entropy to both user and assistant messages, simulate mistakes in SFT, finetune with RL, or run a round of "data engine" that finds words nanochat cannot spell and mixes them into `SimpleSpelling` (§Summary).
- relation: none to a claim page; see the two claim relations below.

### topic: tokenization
- existing: yes (last_updated 2025-10-13)
- statements:
  - "pollocks" is two tokens to nanochat's tokenizer, `poll` and `ocks`; with a leading space it is ` poll` and `ocks`, and ` poll` has a different id from `poll` (§Spelling). [ids 47947, 3635, 2478: measured, printed by the tokenizer]
  - He wraps the word in single quotes because the tokenizer's regex guarantees a token boundary at `'`, and avoids a space after ":" while commas force boundaries, so the spelled-out word comes out as single letters without spaces (§Spelling).
  - Even restating the user's query is computational work for the LLM because of tokenization (§Spelling).
  - Bigger models can do more mental arithmetic per token and probably place " pollocks" and "pollocks" near each other in a latent space, he says; smaller models care more, so obsessively scrutinising the tokenization makes tasks much easier for them (§Counting).
  - One spelling example in his own training data had a stray space after ":" by mistake, which he says was fine "because of the magic of neural networks" (§Spelling).

### claim (existing): a-lot-of-llm-oddness-traces-back-to-tokenization
- existing: yes (2024-02-20; the 2025-02-05 Deep Dive already cites strawberry counting there)
- **Does the guide link to it? Yes, in substance:** its §Summary asks why the strawberry prompt is so hard for an LLM and gives three reasons, the first two tokenization: whitespace makes the model translate tokens with and without a space, and it has to break tokens into individual characters; the third is comparing and counting (§Summary). The guide does not use the word "oddness" or cite the lecture; the link is the merge's, on the shared idea.
- relation: **supports.** The 2024 claim lists spelling and simple string processing among tokenization-caused failures ([[youtube-2024-02-20-gpt-tokenizer]] @04:27), and the Deep Dive gives strawberry counting as not seeing characters plus not being good at counting ([[youtube-2025-02-05-deep-dive-into-llms]] @2:03:51). This source builds a fix around the same diagnosis (§Spelling, §Summary). Add as a `sources` entry with a dated paragraph.

### claim (existing): transformers-need-tokens-to-think
- existing: yes (2023-05-25)
- statements:
  - Smaller models gain from breaking the problem into all its implicit calculations spread across the tokens, so no single token carries too much computation, since "it only has so many layers per token!" (§Counting).
  - Forced to answer in a single token, even a state-of-the-art LLM must solve all of this in one forward pass, which he calls really hard; reasoning models break the task over many tokens and attend back to that work like memory registers of a partial solution (§Summary).
  - The explicit running counter lets the model attend back to the latest count and just add one (§Counting).
- relation: **supports**: same mechanism, finite compute per token, so spread the reasoning ([[talk-2023-05-25-state-of-gpt]] @22:45, @24:27; §Counting, §Summary). Here he applies it to how training answers are written, as the Deep Dive did for labels ([[youtube-2025-02-05-deep-dive-into-llms]] @1:51:07).

### claim (existing): synthetic-data-is-the-future-if-you-keep-its-entropy
- existing: yes (2024-09-05)
- statement: under a heading he calls "Entropy", he randomises user prompts for diversity so the skill is evoked however the user asks, and lists more entropy in both user and assistant messages as an improvement (§Entropy, §Summary).
- relation: **supports**, at the level of practice: the 2024 claim says synthetic data needs its entropy kept ([[talk-2024-09-05-no-priors-ep-80]] @18:38); here his own synthetic task adds entropy on purpose (§Entropy). He does not mention collapse here; do not say he does.

### claim (existing): rl-lets-models-discover-their-own-thinking-strategies
- existing: yes (2025-02-05)
- statements:
  - The reasoning in the answers is "fully fake and cooked up" for now, because every synthetic instance is clean and the manual count and the Python check always agree (§Reasoning structure).
  - He sees two ways to make it real: simulate small mistakes and show recoveries, possibly with a Yes/No check token acting as a classifier, which he says imitation learning can teach; or, more principled, RL on the task as already done for GSM8K, where nanochat practises, makes its own mistakes and learns to recover (§Reasoning structure).
  - In practice you usually want both: reasoning shown in SFT as a "prior", then RL to string it together for reward (§Reasoning structure).
- relation: **supports.** The 2025-02-05 claim says imitation is useful to initialise, and the model must find what works for it through RL ([[youtube-2025-02-05-deep-dive-into-llms]] @2:19:55); here SFT gives the prior and RL takes over (§Reasoning structure). Not `extends`: nothing broader is said.

### topic: pretraining-and-finetuning
- existing: yes
- statement: new abilities go in through synthetic data in midtraining and SFT, which nanochat then imitates (§intro); the guide describes SFT examples of reasoning as the "prior" that RL can later build on (§Reasoning structure).

### topic: llm-tool-use
- existing: yes
- statement: the answer double-checks the manual count with the Python interpreter tool, written as `<<'pollocks'.count('o')=2>>` in the example (§intro, §Reasoning structure).

### topic: rlvr
- existing: yes
- statement: RL on the letter-counting task, as nanochat already does on GSM8K, is in his words the significantly more principled way to make the reasoning real (§Reasoning structure). He does not run it in this post. He does not use the term RLVR.

## Quotes
- "how one can add any arbitrary computing capability to nanochat" (§intro)
- "As usual this is done through synthetic data generation during midtraining and SFT." (§intro)
- "Doing this is important as a data augmentation" (§Entropy)
- "At this time, this is all just smoke and mirrors" (§Reasoning structure)
- "we are habituating the neural network to thinking in this manner" (§Reasoning structure)
- "In practice, you usually want a bit of both!" (§Reasoning structure)
- "the LLM is already doing computational work under the hood because of tokenization" (§Spelling)
- "a very token-efficient way to get the neural net to learn the spelling task" (§Spelling)
- "it's okay because of the magic of neural networks" (§Spelling)
- "by obsessively scrutinizing the tokenization, you can make tasks a lot easier for them" (§Counting)
- "it only has so many layers per token!" (§Counting)
- "Tokenization makes whitespace annoying" (§Summary)
- "Reasoning models break up the task over many tokens, simplifying each forward pass substantially." (§Summary)

All grep-checked against the raw (one match each, all under 15 words).

## Notes for merge
- **Strawberry ↔ tokenization claim:** the post does not name or link [[a-lot-of-llm-oddness-traces-back-to-tokenization]] or the tokenizer lecture; the connection is by content (§Summary's first two reasons). Set it as this source supporting the claim, not as a citation he made.
- The worked example in the post is "pollocks" and "o", not strawberry; strawberry appears only in the title, §intro and §Summary.
- "kind schema" (§Reasoning structure) and "practiec" (§Summary) are his typos.
- The quoted user templates and the example conversation are generated data, not his statements; do not quote them as him.
- d32 is not described here (size, cost); the 2025-11-20 d34 post calls d32 a "$1000 run" with CORE 0.3168. Do not import those numbers into this source's statements.
- He says bigger models "probably" place the two pollocks tokens nearby; keep the hedge.
- The "data engine" phrase is in quotes in the raw; it is a name he uses, not explained further here.
