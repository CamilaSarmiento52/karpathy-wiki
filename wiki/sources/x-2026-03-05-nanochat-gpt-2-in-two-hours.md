---
type: source
raw_path: raw/x/2029701092347630069.md
published: 2026-03-05
medium: x
summary: "His post that nanochat now trains a GPT-2 capability model in 2 hours on one 8×H100 node, mostly thanks to switching the data to NVIDIA ClimbMix, and that he now has AI agents iterating on nanochat automatically, whose 110 changes in about 12 hours lowered a d12's validation loss."
url: https://x.com/karpathy/status/2029701092347630069
title: nanochat now trains GPT-2 capability model in just 2 hours on a single 8XH100…
---
# nanochat now trains GPT-2 capability model in just 2 hours on a single 8XH100…
Raw: [[raw/x/2029701092347630069]] · Original: https://x.com/karpathy/status/2029701092347630069

One post, two paragraphs, so no locations are given. The 110 changes and the d12 loss drop are the agents' results, which he reports; they are not changes he made himself.

## Summary
He says nanochat now trains a GPT-2 capability model in 2 hours on one 8×H100 node, "down from ~3 hours 1 month ago" in his words, which brings it closer to interactive. Tuning and features such as fp8 contributed, but the biggest difference was switching the dataset from FineWeb-edu to NVIDIA's ClimbMix; Olmo, FineWeb and DCLM had all led to regressions, and ClimbMix worked so well out of the box that he is slightly suspicious of goodharting, though the paper reads as about okay to him. He also has AI agents iterating on nanochat automatically: on a feature branch an agent tries ideas, merges those that work and iterates, and the agents' 110 changes over about 12 hours took a d12's validation loss from 0.862415 to 0.858039 at no cost to wall-clock time, as he reports them. Over about two weeks, he says, he has iterated more on this agent "meta-setup" than on nanochat itself.

## Key points
- GPT-2 capability in 2 hours; "down from ~3 hours 1 month ago" → [[nanochat]]
- ClimbMix beat FineWeb-edu, Olmo, FineWeb and DCLM → [[pretraining-and-finetuning]]
- Slightly suspicious of goodharting → [[llm-evaluation]]
- fp8 among the features → [[compute-efficiency]]
- Agents iterate on nanochat: branch, try, merge, iterate; the agents' 110 changes and the d12 loss → [[quick-experiment-loop]], [[llm-agents-over-time]]
- Tuning the agent flows more than the repo → [[ai-assisted-coding-loop]]

## Fed pages
- [[nanochat]]
- [[pretraining-and-finetuning]]
- [[llm-evaluation]]
- [[compute-efficiency]]
- [[quick-experiment-loop]]
- [[llm-agents-over-time]]
- [[ai-assisted-coding-loop]]
- [[autoresearch]]
