---
type: method
steps:
  - Pick a small model with short pretraining runs
  - Change one thing in the code
  - Re-run and compare the same metrics
  - Keep a change only if it works at every scale
sources: ["[[github-2026-07-03-nanochat-readme]]", "[[github-2026-01-07-nanochat-miniseries-v1]]", "[[github-2026-01-31-nanochat-beating-gpt-2]]", "[[x-2026-03-05-nanochat-gpt-2-in-two-hours]]", "[[x-2026-03-09-autoresearch-tuning-nanochat]]", "[[github-2026-03-21-autoresearch-readme]]"]
aliases: [d12 iteration loop]
---
# Quick experiment loop
How he iterates on nanochat research changes ([[github-2026-07-03-nanochat-readme]] §Research).

## Steps
1. **Small model.** His favourite scale for quick experiments is a 12-layer, GPT-1-sized model, with pretraining runs of about five minutes on the multi-GPU node used in the README ([[github-2026-07-03-nanochat-readme]] §Research).
2. **One change.** He changes something in the code and re-runs the d12 (or d16) ([[github-2026-07-03-nanochat-readme]] §Research).
3. **Same plots.** He judges a run by validation bits-per-byte against step, time and FLOPs, the CORE score, and VRAM, MFU and throughput ([[github-2026-07-03-nanochat-readme]] §Research).
4. **Must generalise.** Candidate changes have to work for all depth settings ([[github-2026-07-03-nanochat-readme]] §Research).

On 2026-01-07 he calls d12 "my favorite model (it's the size of GPT-1!)", 12 layers, currently about 6 minutes to train (measured, approximate); the same post's table gives 7.8 minutes for d12 at a ratio of 8, which the prose may not refer to, and the two are not reconciled ([[github-2026-01-07-nanochat-miniseries-v1]] §intro (Miniseries v1), §Details (Miniseries v1 CORE scores)). **Note:** the README's "~5 min pretraining runs" is a different code state; each figure is given with its date ([[github-2026-07-03-nanochat-readme]] §Research; [[github-2026-01-07-nanochat-miniseries-v1]] §intro (Miniseries v1)).

On 2026-01-31 he says much of his iteration is at a smaller scale, a d12 that trains in "only ~5 minutes" or a d16, and that "many (but not all!) ideas that work there transfer to the bigger models" ([[github-2026-01-31-nanochat-beating-gpt-2]] §Reproduce). The same post's 320-experiment sweep found a value optimal at d20 and drew the lesson that small-scale tuning does not transfer; see [[small-scale-tuning-does-not-always-transfer]] ([[github-2026-01-31-nanochat-beating-gpt-2]] §What Worked). **Note:** step 4 asks that changes work at every depth ([[github-2026-07-03-nanochat-readme]] §Research); this post qualifies how far small-scale results reach ([[github-2026-01-31-nanochat-beating-gpt-2]] §What Worked, §Reproduce).

**Run by agents (X post, 2026-03-05).** He now has AI agents iterating on nanochat automatically: the agent works on a feature branch, "tries out ideas, merges them when they work and iterates" ([[x-2026-03-05-nanochat-gpt-2-in-two-hours]]). As the agents' output, he reports 110 changes over about 12 hours that took a d12's validation loss from 0.862415 to 0.858039 at no cost to wall-clock time; these are results of the agents' run, not changes he made, and the figures are for a d12, not the GPT-2-capability model ([[x-2026-03-05-nanochat-gpt-2-in-two-hours]]). **Note:** the post does not call this loop by name; the steps above are unchanged ([[x-2026-03-05-nanochat-gpt-2-in-two-hours]]).
**His manual loop, and the agent running it (X post, 2026-03-09).** He describes the loop he has run by hand daily for two decades, "the bread and butter of what I do": come up with ideas, implement them, check whether validation loss improves, come up with new ideas from that, read papers for inspiration ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1). With [[autoresearch]] the agent did this whole workflow end to end and by itself, planning the next experiments from the sequence of earlier results, a first for him ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1). He checked that changes found at depth=12 transfer to depth=24 ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1). **Note:** that check matches step 4, that changes must work at every depth ([[github-2026-07-03-nanochat-readme]] §Research; [[x-2026-03-09-autoresearch-tuning-nanochat]] #1). For scale he pictures tuning small models and promoting the most promising ideas to increasingly larger ones ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1).

**The autoresearch README (2026-03-21).** In [[autoresearch]] the loop is handed to an agent: it modifies `train.py`, trains for a fixed 5 minutes, checks whether val_bpb improved, keeps or discards the change and repeats, overnight ([[github-2026-03-21-autoresearch-readme]] §intro, §How it works). The fixed budget makes runs directly comparable whatever the agent changes, at the cost of comparability with other people's platforms, and editing one file keeps the diffs reviewable ([[github-2026-03-21-autoresearch-readme]] §Design choices). **Note:** the steps above, from the nanochat README dated 2026-07-03, also use runs of about five minutes; each is given with its date ([[github-2026-07-03-nanochat-readme]] §Research; [[github-2026-03-21-autoresearch-readme]] §How it works).

## Seen in
- [[nanochat]]
- [[autoresearch]]
