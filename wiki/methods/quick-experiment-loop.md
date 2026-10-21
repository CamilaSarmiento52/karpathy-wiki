---
type: method
steps:
  - Pick a small model with short pretraining runs
  - Change one thing in the code
  - Re-run and compare the same metrics
  - Keep a change only if it works at every scale
sources: ["[[github-2026-07-03-nanochat-readme]]"]
aliases: [d12 iteration loop]
---
# Quick experiment loop
How he iterates on nanochat research changes ([[github-2026-07-03-nanochat-readme]] §Research).

## Steps
1. **Small model.** His favourite scale for quick experiments is a 12-layer, GPT-1-sized model, with pretraining runs of about five minutes on the multi-GPU node used in the README ([[github-2026-07-03-nanochat-readme]] §Research).
2. **One change.** He changes something in the code and re-runs the d12 (or d16) ([[github-2026-07-03-nanochat-readme]] §Research).
3. **Same plots.** He judges a run by validation bits-per-byte against step, time and FLOPs, the CORE score, and VRAM, MFU and throughput ([[github-2026-07-03-nanochat-readme]] §Research).
4. **Must generalise.** Candidate changes have to work for all depth settings ([[github-2026-07-03-nanochat-readme]] §Research).

## Seen in
- [[nanochat]]
