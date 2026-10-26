---
type: source
raw_path: raw/github/karpathy__nanochat__discussion-314.md
published: 2025-11-20
medium: github
summary: "His report on nanochat d34, a 2.2B-parameter model trained 2X past Chinchilla on one 8×H100 node for about 100 hours and $2,500, reaching CORE 0.3382 and ChatCORE 0.41 against d32's 0.3168 and 0.27, uploaded to Hugging Face and deployed on nanochat.karpathy.ai."
url: https://github.com/karpathy/nanochat/discussions/314
title: "d34 model (~$2,500)"
---
# d34 model (~$2,500)
Raw: [[raw/github/karpathy__nanochat__discussion-314]] · Original: https://github.com/karpathy/nanochat/discussions/314

The post has no headings; it is cited `§intro`. The raw file is his post only. Number tags as on [[github-2025-10-13-nanochat-discussion-introducing]]: measured, target, comparison, setting, estimate.

## Summary
He trained nanochat d34 and uploaded it to Hugging Face: about 100 hours on one 8×H100 node for about $2,500, with the tokens-to-parameters ratio raised from Chinchilla's 20 to 40 so a smaller model gets more capability than compute-optimal training would give (§intro). The base model has about 2.2B parameters and reaches validation bpb 0.7045 and CORE 0.3382, against 0.3168 for d32, 0.22 for the d20 speedrun and 0.25 for GPT-2 (§intro). Training was stable apart from a small early bump; an NCCL crash in the last 5% was resumed with new resumption logic (§intro). After midtraining and SFT, ChatCORE rose from d32's 0.27 to 0.41, while HumanEval fell during SFT, which he puts mostly down to noise, and GSM8K gained less than he expected (§intro). The model is live on nanochat.karpathy.ai (§intro).

## Key points
- d34: command, ~100 h, ~$2,500, Hugging Face upload, live demo → [[nanochat]]
- 2X longer than Chinchilla, ratio 40 instead of 20 → [[scaling-laws]]
- CORE 0.3382 vs d32, d20 and GPT-2; mid/SFT table, ChatCORE 0.27 → 0.41 → [[llm-evaluation]]
- 2.2B params, 1.43e10 FLOPs/token, MFU 47.4%, 1.27e21 total FLOPs → [[compute-efficiency]]
- Stable curve with a recovered bump; crash resumed from checkpoint → [[training-diagnostics]]
- HumanEval drop in SFT, GSM8K under-lift: not tuned super well → [[pretraining-and-finetuning]]

## Fed pages
- [[nanochat]]
- [[scaling-laws]]
- [[llm-evaluation]]
- [[compute-efficiency]]
- [[training-diagnostics]]
- [[pretraining-and-finetuning]]
