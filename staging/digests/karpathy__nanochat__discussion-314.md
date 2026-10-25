# Digest: d34 model (~$2,500)
- raw: raw/github/karpathy__nanochat__discussion-314.md · published: 2025-11-20 · medium: github · words: 556 (frontmatter)
- source slug: github-2025-11-20-nanochat-d34-model

Number tags: **[measured]** his reported result from a run; **[target]** a goal for a run not
reported; **[comparison]** someone else's figure or a baseline he compares against, including
his own earlier runs when cited only as a yardstick; **[setting]** a configuration value he
chose; **[estimate]** an approximation or a calculated (not observed) figure.

The post has no headings: everything is `§intro`. The raw file is his post only.

## Source page
```
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

The post has no headings; it is cited `§intro`.

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
```

## Candidates

### artifact: nanochat
- existing: yes
- statements:
  - He trained d34 and uploaded it to Hugging Face as `karpathy/nanochat-d34` (§intro).
  - It was pretrained with `--depth=34 --device_batch_size=4 --target_param_data_ratio=40` on an 8×H100 node, running about 100 hours, about 4 days, for about $2,500 (§intro). [depth, batch, ratio: setting; ~100 h / ~4 days: measured, approximate; ~$2,500: estimate, his rounded cost (≈100 h × $24/h is $2,400; he does not give the rate here)]
  - The d34 is now deployed on nanochat.karpathy.ai (§intro).
  - For comparison he calls d32 a "$1000 run" (§intro). [comparison; cost estimate of his earlier run, no time given]
- **Cost/time series (for a possible timeline; do not order):** this source gives the cost of a model far past GPT-2 on CORE (0.3382 vs 0.25), not a time-to-GPT-2 figure. Record as "2025-11-20: d34, ~100 h, ~$2,500, CORE 0.3382; d32 $1000, CORE 0.3168".

### topic: scaling-laws
- existing: yes
- statements:
  - d34 is "2X longtrained" compared to Chinchilla: the param:token ratio is overridden from 20 up to 40, so it is trained longer than compute optimal to squeeze more capability into a smaller package (§intro). [20: comparison (Chinchilla); 40: setting]
  - Printed stats: 88,683,315,200 training tokens, 169,150 iterations, 524,288 tokens per batch, max sequence length 2048 (§intro). [settings, derived by the script from the ratio]
- relation: none to a claim page. **Note:** the 2026-01-07 miniseries post fits nanochat's own compute-optimal ratio at about 8 and says earlier models used Chinchilla's 20 ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws), §Details (Miniseries v1 CORE scores)). Give each with its date; this post's "compute optimal" means Chinchilla's 20.

### topic: llm-evaluation
- existing: yes
- statements:
  - d34 base: CORE 0.3382, minimum and final validation bpb 0.7045 (§intro). [measured]
  - Comparison COREs he gives: d32 0.3168, d20 "speedrun" 0.22, GPT-2 0.25 (§intro). [d32, d20: comparison (his earlier runs); GPT-2 0.25: comparison, rounded]
  - d34 MID → SFT: ARC-Challenge 0.5333 → 0.5435, ARC-Easy 0.7071 → 0.7365, GSM8K 0.1137 → 0.1296, HumanEval 0.1159 → 0.0488, MMLU 0.4297 → 0.4311, ChatCORE 0.4087 → 0.4100 (§intro). [measured]
  - d32 MID → SFT (→ RL): ARC-Challenge 0.4787 → 0.4991, ARC-Easy 0.6233 → 0.6797, GSM8K 0.1099 → 0.1274 → 0.1994 (RL), HumanEval 0.1098 → 0.1280, MMLU 0.3896 → 0.4049, ChatCORE 0.2417 → 0.2734 (§intro). [comparison, his earlier run]
  - ChatCORE "lifted quite a lot", 0.27 → 0.41, d32 to d34 (§intro). [measured]
  - HumanEval "stubbornly plunged" during SFT, which he attributes mostly to noise and expects tuning could recover; he expected more GSM8K lift, midtraining gave good lift but SFT "botches it a bit again", possibly not tuned well (§intro).
- relation: none. **Note:** GPT-2 is 0.25 here; other nanochat sources give 0.26 (GPT-2 xl, launch post), 0.257 (GPT-2 XL, 2026-01-07) and 0.256525 (2026-01-31, README). Rounding of the same figure, likely; merge should not reconcile beyond saying so.

### topic: compute-efficiency
- existing: yes
- statements (all printed by the training script, so measured or calculated by it):
  - 2,217,082,880 parameters; 1.426509e10 FLOPs per token; total training FLOPs 1.265075e21 (§intro). [params: measured (counted); FLOPs: estimate (formula)]
  - MFU 47.40%; peak memory 69,811.85 MiB; DDP world size 8 (§intro). [measured]
  - `--device_batch_size=4`, against the default per-GPU batch, to fit the larger model (§intro). [setting]

### method: training-diagnostics
- existing: yes
- statements:
  - In the wandb plots (d32 brown, d34 blue, the resumed 5% green) he notes d34 trained fairly stably except a tiny early bump that recovered quickly (§intro).
  - Training crashed in the last 5% with a cryptic NCCL error; he used the new optimisation-resumption logic to resume from that point, which "worked perfect" (§intro).
- note: run-level reading of loss curves; same kind as the launch post's statements on this method.

### topic: pretraining-and-finetuning
- existing: yes
- statement: on d34, SFT barely moves ChatCORE (0.4087 → 0.4100) and lowers HumanEval, and he expects better tuning could recover it (§intro). [measured]

## Quotes
- "the model was trained longer that is compute optimal" (§intro)
- "just to squeeze a bit more capability into a bit smaller package" (§intro)
- "fairly stable except for a tiny bump that recovered quickly near the beginning" (§intro)
- "the training crashed for the last 5% with some cryptic NCCL error" (§intro)
- "So our ChatCORE lifted quite a lot, from 0.27 -> 0.41." (§intro)
- "HumanEval stubbornly plunged during SFT, which I attribute mostly to noise" (§intro)
- "Possibly not tuned super well." (§intro)

All grep-checked (one match each, under 15 words).

## Notes for merge
- "trained longer that is compute optimal" is his typo for "than"; quote as is or paraphrase.
- The ~$2,500 is in the title and body with a tilde; he does not state the hourly rate here. Tag as his approximate cost, not an invoice.
- d32 is cited only as a comparison ("$1000 run"); no d32 training time or date is given. The d32 was first mentioned in the 2025-10-24 strawberry guide as the model he taught to count letters.
- d34 has no RL column; d32 has RL only for GSM8K (0.1994).
- The two images (wandb curves, live demo screenshot) are not described beyond his bullets; do not invent curve details.
- No headings, no replies.
