---
type: method
steps:
  - Pick a small model with short pretraining runs
  - Change one thing in the code
  - Re-run and compare the same metrics
  - Keep a change only if it works at every scale
sources: ["[[github-2026-07-03-nanochat-readme]]", "[[github-2026-01-07-nanochat-miniseries-v1]]", "[[github-2026-01-31-nanochat-beating-gpt-2]]"]
aliases: [d12 iteration loop]
---
# Quick experiment loop
How he iterates on nanochat research changes ([[github-2026-07-03-nanochat-readme]] §Research).

## Steps
1. **Small model.** His favourite scale for quick experiments is a 12-layer, GPT-1-sized model, with pretraining runs of about five minutes on the multi-GPU node used in the README ([[github-2026-07-03-nanochat-readme]] §Research).
2. **One change.** He changes something in the code and re-runs the d12 (or d16) ([[github-2026-07-03-nanochat-readme]] §Research).
3. **Same plots.** He judges a run by validation bits-per-byte against step, time and FLOPs, the CORE score, and VRAM, MFU and throughput ([[github-2026-07-03-nanochat-readme]] §Research).
4. **Must generalise.** Candidate changes have to work for all depth settings ([[github-2026-07-03-nanochat-readme]] §Research).

On 2026-01-07 he calls d12 "my favorite model (it's the size of GPT-1!)", 12 layers, currently about 6 minutes to train (measured, approximate); the same post's table gives 7.8 minutes for d12 at a ratio of 8, which the prose may not refer to, and the two are not reconciled ([[github-2026-01-07-nanochat-miniseries-v1]] §intro (Miniseries v1), §Details (Miniseries v1 CORE scores)). **Note:** the README's "about five minutes" is a different code state; each figure is given with its date ([[github-2026-07-03-nanochat-readme]] §Research; [[github-2026-01-07-nanochat-miniseries-v1]] §intro (Miniseries v1)).

On 2026-01-31 he says much of his iteration is at a smaller scale, a d12 that trains in "only ~5 minutes" or a d16, and that "many (but not all!) ideas that work there transfer to the bigger models" ([[github-2026-01-31-nanochat-beating-gpt-2]] §Reproduce). The same post's 320-experiment sweep found a value optimal at d20 and drew the lesson that small-scale tuning does not transfer; see [[small-scale-tuning-does-not-always-transfer]] ([[github-2026-01-31-nanochat-beating-gpt-2]] §What Worked). **Note:** step 4 asks that changes work at every depth ([[github-2026-07-03-nanochat-readme]] §Research); this post qualifies how far small-scale results reach ([[github-2026-01-31-nanochat-beating-gpt-2]] §What Worked, §Reproduce).

## Seen in
- [[nanochat]]
