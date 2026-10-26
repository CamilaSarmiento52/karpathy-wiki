# Digest: autoresearch README
- raw: raw/github/karpathy__autoresearch.md · published: 2026-03-21 · medium: github · words: 1223 (frontmatter) · commit: e6d79c1
- source slug: github-2026-03-21-autoresearch-readme

Location scheme: `§intro` (text under `# autoresearch`, before `## How it works`, including
the italic opening paragraph), then `§How it works`, `§Quick start`, `§Running the agent`,
`§Project structure`, `§Design choices`, `§Platform support`, `§Notable forks`, `§License`.

Number tags used below: **[setting]** a value of the repo's design or defaults; **[estimate]**
his arithmetic or approximate expectation, not a measured result; **[suggestion]** a value
he recommends trying; **[fiction]** a number inside the italic opening, which is a joke about
the future (see Notes). No result in this README is a measurement.

## Source page
```
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

Dated by the README's commit `e6d79c1`. The italic opening paragraph is a signed joke set in
an imagined future, not a set of claims.

## Summary
The idea is to give an AI agent a small but real LLM training setup and let it experiment
overnight: it edits the code, trains for five minutes, checks whether the result improved,
keeps or discards the change, and repeats (§intro). The training code is a simplified,
single-GPU version of nanochat, and the human's job moves from editing Python to editing
`program.md`, the Markdown instructions for the agent (§intro, §How it works). Three files
matter: a fixed `prepare.py`, the `train.py` the agent edits, and the `program.md` the human
edits; the metric is validation bits per byte under a fixed 5-minute budget (§How it works).
He explains the design choices, one file to modify, a fixed time budget and no dependencies
beyond PyTorch and a few small packages, with their trade-offs (§Design choices). He gives
advice for forks on smaller machines and lists four (§Platform support, §Notable forks).

## Key points
- What autoresearch is, its three files, the 5-minute budget and val_bpb → [[autoresearch]]
- A simplified single-GPU nanochat as the training code → [[nanochat]]
- The keep-or-discard loop run by an agent overnight → [[quick-experiment-loop]]
- program.md as a "super lightweight skill"; the README written for agents to read → [[building-for-agents]]
- The human programs Markdown, not Python → [[english-is-the-new-programming-language]]
- One file to modify, small, self-contained, reviewable diffs → [[small-hackable-educational-code]]
- Low-entropy TinyStories data for small machines → [[small-llms-can-be-strong-in-narrow-domains]]

## Fed pages
- [[autoresearch]]
- [[nanochat]]
- [[quick-experiment-loop]]
- [[building-for-agents]]
- [[english-is-the-new-programming-language]]
- [[small-hackable-educational-code]]
- [[small-llms-can-be-strong-in-narrow-domains]]
```

## Candidates

### artifact: autoresearch
- existing: no (new; slug given in the prompt)
- repo_url: https://github.com/karpathy/autoresearch · language: Python · status: active (the README gives no status; merge decides) · license MIT (§License)
- aliases: autoresearch
- statements:
  - The idea: give an AI agent a small but real LLM training setup and let it experiment autonomously overnight; it modifies the code, trains for 5 minutes, checks if the result improved, keeps or discards, and repeats, and you wake to a log of experiments and, hopefully, a better model (§intro). [5 min: setting]
  - The training code is a simplified single-GPU implementation of [[nanochat]] (§intro).
  - The core idea, he says, is that the researcher does not touch the Python files; instead they program the `program.md` Markdown files that give the agents context and set up an autonomous research org (§intro).
  - The default `program.md` is deliberately a bare-bones baseline; he says it is obvious how one would iterate on it to find the "research org code" that makes research progress fastest, and how one would add more agents (§intro).
  - Three files matter: `prepare.py` (fixed constants, one-time data prep that downloads data and trains a BPE tokenizer, and runtime utilities; not modified); `train.py` (the full GPT model, the Muon + AdamW optimizer and the training loop; everything is fair game; edited by the agent); `program.md` (baseline instructions for one agent; edited by the human) (§How it works).
  - Training runs for a fixed 5-minute wall-clock budget, excluding startup and compilation, whatever the compute (§How it works). [setting]
  - The metric is val_bpb, validation bits per byte: lower is better, and vocab-size-independent so architectural changes are compared fairly (§How it works).
  - Requirements: one NVIDIA GPU (tested on H100), Python 3.10+, and uv; data prep is a one-time ~2 minutes and a manual training run ~5 minutes (§Quick start). [~2 min, ~5 min: estimate]
  - To run it, start Claude, Codex "or whatever you want" in the repo "(and disable all permissions)", and prompt it to look at `program.md` and kick off an experiment (§Running the agent). See Notes on the wording.
  - He calls `program.md` essentially a super lightweight "skill" (§Running the agent).
  - Design choices: a single file to modify, which keeps scope manageable and diffs reviewable; a fixed time budget; self-contained, with no distributed training or complex configs (§Design choices).
  - The fixed budget gives approx 12 experiments per hour and approx 100 overnight (§Design choices). [estimate]
  - Two upsides of the fixed budget, he says: experiments are directly comparable whatever the agent changes (model size, batch size, architecture), and autoresearch finds the most optimal model for your platform in that budget; the downside is that results are not comparable with other people's on other platforms (§Design choices).
  - It needs one NVIDIA GPU; other platforms are possible in principle but would bloat the code, and he is not sure he wants to take that on personally now; he points to the parent nanochat repo and to forks (§Platform support). Four forks are listed: two for macOS, one for Windows RTX, one for AMD (§Notable forks).
  - Advice for smaller machines: a lower-entropy dataset such as TinyStories (GPT-4-generated short stories), a smaller `vocab_size` (from 8192 to 4096, 2048, 1024 or bytes), a much lower `MAX_SEQ_LEN` (down to 256) with a slightly larger `DEVICE_BATCH_SIZE`, fewer `EVAL_TOKENS`, a lower `DEPTH` (default 8, e.g. 4), `WINDOW_PATTERN` "L" instead of "SSSL", and a much lower `TOTAL_BATCH_SIZE` kept to powers of 2, e.g. 2**14 (§Platform support). [8192, DEPTH 8, SSSL: setting; the rest: suggestion]
  - He suggests asking your favourite coding agent for help and pasting it the guide and the full source (§Platform support).
- relation: none to claims.

### artifact (existing): nanochat
- existing: yes
- statements:
  - autoresearch's training code is a simplified single-GPU implementation of nanochat (§intro).
  - He sends people who need other platforms to the full parent nanochat repo, which has wider platform support, such as a Flash Attention 3 kernels fallback, generic device support and autodetection (§Platform support).
- add [[autoresearch]] to `## Related`.

### method (existing): quick-experiment-loop
- existing: yes
- statements:
  - In autoresearch the loop is handed to an agent: modify `train.py`, train for 5 minutes, check whether val_bpb improved, keep or discard, repeat (§intro, §How it works).
  - The fixed budget makes runs directly comparable whatever the agent changes, at the cost of comparability across platforms (§Design choices).
  - One file to edit keeps the diffs reviewable (§Design choices).
- **Note for merge:** the page's existing steps (d12, ~5-minute runs, one change, same plots) come from the README dated 2026-07-03 ([[github-2026-07-03-nanochat-readme]] §Research). Both describe short runs of about five minutes; write them with their dates, no order. Suggest one section "Run by an agent (autoresearch)" fed by this README, [[x-2026-03-09-autoresearch-tuning-nanochat]] and, only for what the agent reported, [[github-2026-03-08-autoresearch-session-report]]. Possible extra step for `steps`: "Fix the time budget so runs compare". Optional.

### topic (existing): building-for-agents
- existing: yes
- statements:
  - He calls `program.md` essentially a super lightweight "skill": the instructions the human writes for the agent (§Running the agent, §How it works).
  - The README speaks to agents as readers: people can "have their agents reference" the parent nanochat repo, and he suggests pasting the small-machine guide and the full source into a coding agent (§Platform support).
- relation: topic text, no claim link. **Note:** the gist [[github-2026-04-04-llm-wiki-gist]] is another document written to be pasted to an agent; merge may connect the two with a Note.

### claim (existing): english-is-the-new-programming-language
- existing: yes (2025-06-19)
- statement: the core idea is that you are not touching the Python files as a researcher normally would, but "programming" the `program.md` Markdown files that give the agents context (§intro).
- relation: **supports**, weakly. In 2025 he says we are now programming computers in English ([[youtube-2025-06-19-software-is-changing]] @04:23); here the human's programming work is writing Markdown instructions for agents instead of Python (§intro). The README does not say "English" or "Software 3.0"; it is an example, not a restatement. If merge finds `supports` too strong, use a **Note:** on [[software-3-0]] instead and drop it from Fed pages.

### method (existing): small-hackable-educational-code
- existing: yes
- statements:
  - The repo is deliberately kept small, with three files that matter (§How it works).
  - Only `train.py` is modified, to keep scope manageable and diffs reviewable; no external dependencies beyond PyTorch and a few small packages, no distributed training, no complex configs: "One GPU, one file, one metric." (§Design choices)
  - He declines extra platform support because it would bloat the code (§Platform support).
- relation: method update; the reason here is reviewable agent diffs, not education. Say so; do not call autoresearch educational code.

### claim (existing): small-llms-can-be-strong-in-narrow-domains
- existing: yes (2024-05-29)
- statement: for small computers he recommends a much lower-entropy dataset such as TinyStories, because with data narrower in scope you will see reasonable results with much smaller models (§Platform support).
- relation: **supports.** In 2024 he says very small LLMs can be surprisingly strong if the domain is narrow enough, citing TinyStories ([[github-2024-05-29-llama2c-readme]] §intro); here the same dataset and reasoning appear as practical advice (§Platform support). His wording here is "reasonable results", weaker than "surprisingly strong"; keep that difference.

### topic (existing): partial-autonomy-apps — context only
- **Note** candidate, not a fed page: the YC talk's autonomy slider and "keep the AI on the leash" ([[youtube-2025-06-19-software-is-changing]] @20:29, @22:43) versus a setup in which the agent runs overnight on its own and the human reviews a log in the morning (§intro), with reviewable diffs kept as a design goal (§Design choices). A connection for merge to write or skip; he does not mention the slider here.

## Quotes
- "let it experiment autonomously overnight" (§intro)
- "you are programming the `program.md` Markdown files that provide context to the AI agents" (§intro)
- "This repo is the story of how it all began." (§intro) — the last line of the italic joke; see Notes
- "The `program.md` file is essentially a super lightweight "skill"." (§Running the agent)
- "(and disable all permissions)" (§Running the agent)
- "This keeps the scope manageable and diffs reviewable." (§Design choices)
- "approx 100 experiments while you sleep" (§Design choices)
- "autoresearch will find the most optimal model for your platform in that time budget" (§Design choices)
- "your runs (and results) become not comparable to other people" (§Design choices)
- "One GPU, one file, one metric." (§Design choices)
- "I'm not 100% sure that I want to take this on personally right now." (§Platform support)

## Notes for merge
- **The italic opening (§intro) is fiction.** Signed "-@karpathy, March 2026", it describes a future where research is done by autonomous agent swarms in "compute cluster megastructures" and the code is in its "10,205th generation" [fiction], beyond human comprehension. It is a joke set in an imagined future, not a prediction he states. Do not cite it for any claim about the future of research; if used at all, describe it as a joke opening. The X post [[x-2026-03-09-autoresearch-tuning-nanochat]] is where he makes his actual prediction.
- **"(and disable all permissions)"** is ambiguous on its face: most likely he means turning off the agent's permission prompts so it runs unattended, but the README does not say which. Quote it rather than paraphrase.
- The README links two X posts for context: `2029701092347630069` (in raw/, not in this batch) and `2031135152349524125` = [[x-2026-03-09-autoresearch-tuning-nanochat]] (§intro).
- The "Dummy's Guide" link (§How it works) is someone else's post (hooeem); he says it "looks pretty good". Not a source.
- Window pattern defaults: "SSSL" here (§Platform support); the agent-written session report finds "SSSSL" ([[github-2026-03-08-autoresearch-session-report]] §Highlights). Different code states; no conflict.
- `DEPTH` default 8 "here" (§Platform support), against nanochat's d12/d20 language elsewhere; it is this repo's own default.
- Platform-support recommendations end "hard to tell" (on the batch size) and "Try it." (on the window): keep them hedged.
