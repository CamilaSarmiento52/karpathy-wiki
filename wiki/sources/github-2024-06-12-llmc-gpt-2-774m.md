---
type: source
raw_path: raw/github/karpathy__llm.c__discussion-580.md
published: 2024-06-12
medium: github
summary: "His report on a six-day llm.c run of GPT-2 (774M) on 150B FineWeb tokens on one 8×A100 node: it outperformed GPT-2 and GPT-3 on his evals sooner than he expected, and he lists what he would change, from learning-rate decay to a suspected train/validation overlap."
url: https://github.com/karpathy/llm.c/discussions/580
title: GPT-2 (774M) reproduced
---
# GPT-2 (774M) reproduced
Raw: [[raw/github/karpathy__llm.c__discussion-580]] · Original: https://github.com/karpathy/llm.c/discussions/580

No markdown headings: bold labels (Reflections, s3 paths, huggingface paths, Next up), cited as `§intro` with the label where useful.

## Summary
He trained GPT-2 (774M) for about six days on his 8×A100 80GB node, 150B tokens or 1.5 epochs of the 100B FineWeb sample, and it finished without major incidents (§intro). As with the previous run, the model somewhat unexpectedly outperforms GPT-2 and GPT-3 quickly; he is not sure whether that comes from the evaluations, from weaknesses they do not test such as multilingual, math or code, or possibly FineWeb's quality (§intro). The config estimates about 7e20 FLOPs by 6ND, 286,102 steps of 524,288 tokens at ~1.7 s each, about 135 hours and $2,000, ten times the 124M on cost (§intro). Because runs sometimes hang on an MPI error, he ran a watcher script that interrupts the training session when its log stops updating (§intro). His reflections: run a wider eval suite on a Hugging Face conversion before the next big run, decay the learning rate only to 10% as in the GPT-3 paper rather than to zero, and worry about a downward kink in validation loss at the epoch boundary that may mean train and validation overlap (§intro (Reflections)).

## Key points
- 774M run: ~6 days, 150B tokens, 8×A100, checkpoints on S3 and Hugging Face, next the 1558M → [[llm-c]]
- Outperforms GPT-2 and GPT-3 "somewhat unexpectedly"; unsure why → [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- Plans a wider eval suite; possible train/validation overlap in FineWeb → [[llm-evaluation]]
- "We shouldn't decay the LR to 0%" → [[do-not-decay-the-learning-rate-to-zero]], [[gradient-descent]]
- The epoch-boundary kink and the slow tail as readings of the curve; a watcher script that restarts a hung run → [[training-diagnostics]]
- 6ND ≈ 7e20, ten times the 124M's cost → [[compute-efficiency]]

## Fed pages
- [[llm-c]]
- [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- [[llm-evaluation]]
- [[do-not-decay-the-learning-rate-to-zero]]
- [[gradient-descent]]
- [[training-diagnostics]]
- [[compute-efficiency]]
