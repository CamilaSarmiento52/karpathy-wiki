---
type: source
raw_path: raw/github/karpathy__autoresearch.md
published: 2026-03-21
medium: github
summary: "README of autoresearch, a small single-GPU nanochat training setup in which an AI agent edits train.py, trains for a fixed five minutes, keeps or discards the change by val_bpb and repeats, while the human edits the agent's program.md instructions."
url: https://github.com/karpathy/autoresearch
title: autoresearch README
---
# autoresearch README
Raw: [[raw/github/karpathy__autoresearch]] · Original: https://github.com/karpathy/autoresearch

Dated by the README's commit `e6d79c1`. Locations: `§intro` (text under the title, before `## How it works`, including the italic opening), `§How it works`, `§Quick start`, `§Running the agent`, `§Design choices`, `§Platform support`, `§Notable forks`. The italic opening paragraph, signed "-@karpathy, March 2026", is a joke set in an imagined future where research is done by autonomous agent swarms; it is not a prediction and is not cited for one.

## Summary
The idea is to give an AI agent a small but real LLM training setup and let it experiment overnight: it edits the code, trains for five minutes, checks whether the result improved, keeps or discards the change, and repeats (§intro). The training code is a simplified, single-GPU version of nanochat, and the human's job moves from editing Python to editing `program.md`, the Markdown instructions for the agent (§intro, §How it works). Three files matter: a fixed `prepare.py`, the `train.py` the agent edits, and the `program.md` the human edits; the metric is validation bits per byte under a fixed 5-minute budget (§How it works). He explains the design choices, one file to modify, a fixed time budget and no dependencies beyond PyTorch and a few small packages, with their trade-offs (§Design choices). He gives advice for forks on smaller machines and lists four (§Platform support, §Notable forks).

## Key points
- What autoresearch is, its three files, the 5-minute budget and val_bpb; the italic opening is a joke → [[autoresearch]]
- A simplified single-GPU nanochat as the training code → [[nanochat]]
- The keep-or-discard loop run by an agent overnight → [[quick-experiment-loop]]
- program.md as a "super lightweight skill"; the README written for agents to read → [[building-for-agents]]
- One file to modify, so diffs stay reviewable → [[small-hackable-educational-code]]

## Fed pages
- [[autoresearch]]
- [[nanochat]]
- [[quick-experiment-loop]]
- [[building-for-agents]]
- [[small-hackable-educational-code]]
