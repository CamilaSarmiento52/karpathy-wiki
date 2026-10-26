# Digest: GPT-2 (774M) reproduced
- raw: raw/github/karpathy__llm.c__discussion-580.md · published: 2024-06-12 · medium: github · words: 515
- source slug: github-2024-06-12-llmc-gpt-2-774m

## Source page
```
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

## Summary
He trained GPT-2 (774M) for about six days on his 8×A100 80GB node, 150B tokens or 1.5 epochs of the 100B FineWeb sample, and it finished without major incidents (§intro). As with the previous run, the model somewhat unexpectedly outperforms GPT-2 and GPT-3 quickly; he is not sure whether that comes from the evaluations, from weaknesses they do not test such as multilingual, math or code, or possibly FineWeb's quality (§intro). The config estimates about 7e20 FLOPs by 6ND, 286,102 steps of 524,288 tokens at ~1.7 s each, about 135 hours and $2,000, ten times the 124M on both counts (§intro). Because runs sometimes hang on an MPI error, he ran a watcher script that interrupts the training session when its log stops updating (§intro). His reflections: run a wider eval suite on a Hugging Face conversion before the next big run, decay the learning rate only to 10% as in the GPT-3 paper rather than to zero, and worry about a downward kink in validation loss at the epoch boundary that may mean train and validation overlap (§intro).

## Key points
- 774M run: ~6 days, 150B tokens, 8×A100, checkpoints on S3 and Hugging Face, next step the 1.6B → [[llm-c]]
- Outperforms GPT-2 and GPT-3 "somewhat unexpectedly"; unsure why → [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- Plans a wider eval suite; possible train/val overlap in FineWeb → [[llm-evaluation]]
- "We shouldn't decay the LR to 0%" → [[do-not-decay-the-learning-rate-to-zero]], [[gradient-descent]]
- The epoch-boundary kink in validation loss as a warning sign → [[training-diagnostics]]
- Watcher script that restarts a hung run from its log → [[keep-long-training-runs-alive]]
- 6ND ≈ 7e20, 10X compute and cost over 124M → [[training-compute-budget]]

## Fed pages
- [[llm-c]]
- [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- [[llm-evaluation]]
- [[do-not-decay-the-learning-rate-to-zero]]
- [[gradient-descent]]
- [[training-diagnostics]]
- [[keep-long-training-runs-alive]]
- [[training-compute-budget]]
```

## Candidates
### artifact: llm-c
- existing: no
- statements:
  - GPT-2 (774M) ran for about six days on his 8×A100 80GB node, 150B tokens (1.5 epochs of the 100B FineWeb sample), finishing without major issues (§intro). [his result]
  - Launch script `scripts/run_gpt2_774M.sh`; final log and checkpoint on S3; a Hugging Face upload by another user, `mdouglas` (§intro).
  - Next: figure out the evals, then launch "the GPT-2", 1558M, on a bigger node so it does not take half a month, and use the occasion to merge multi-GPU PRs (§intro).

### claim: his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag
- existing: no (first proposed in digest 481)
- confidence: stated
- quote: "we somewhat unexpectedly outperform both GPT-2 and GPT-3 very quickly" (§intro)
- statements:
  - As with the previous run, the 774M somewhat unexpectedly outperforms both GPT-2 and GPT-3 very quickly (§intro). [his result; the chart is an image, so the eval behind "outperform" is not named in the text]
  - He is not sure why: it could be the evaluations, or the model could be much worse on multilingual, math or code, or possibly FineWeb's quality (§intro).
  - He is very curious why it does better than expected and will run a wider suite of evals on a Hugging Face conversion before the next big run (§intro).
- note for the title: keep "on HellaSwag" only if merge cites 481/677 for the eval; this file alone says "outperform" without naming the benchmark.

### topic: llm-evaluation
- existing: no
- statements:
  - Before the next big run he plans to convert the checkpoint to Hugging Face format and run a wider, bigger suite of evals (§intro).
  - A downward kink in validation loss exactly at the one-epoch boundary makes him nervous that FineWeb's validation and training sets overlap more than expected (§intro).

### claim: do-not-decay-the-learning-rate-to-zero
- existing: no
- title: He concluded the llm.c runs should not decay the learning rate to zero
- confidence: stated
- stated_on: 2024-06-12
- quote: "We shouldn't decay the LR to 0%." (§intro)
- context: at the tail end of the 774M optimisation the run was going way too slow; for future runs he will probably follow the GPT-3 paper and decay to 10%, `-q 0.1` instead of `-q 0.0` (§intro).
- relation to existing claims: none in the wiki. Within this batch it revises his own 124M setting (`-q 0.0`, decay to 0, [[github-2024-05-28-llmc-gpt-2-124m]] §intro), and the 1.6B run follows through with `-q 0.1` ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro). This is a change of practice inside one project, not an earlier claim being contradicted; no prior claim page exists, so no `extends`/`contradicts` link. Merge could note it on [[gradient-descent]].

### topic: gradient-descent
- existing: yes
- statements:
  - After the 774M run he judged that decaying the LR to 0% made the end of training too slow and planned to decay to 10% of max as in the GPT-3 paper (§intro).

### method: training-diagnostics
- existing: yes
- statements:
  - He reads a downward kink in validation loss at exactly the epoch boundary as a sign of possible train/validation overlap (§intro).
  - He reads the tail of the loss curve to judge the LR schedule: too slow at the end means the decay went too low (§intro).

### method: keep-long-training-runs-alive (optional; merge may fold into [[llm-c]] or [[training-diagnostics]])
- existing: no
- aliases: [watcher script, resume training, babysitting a run]
- proposed steps: Run training in a named screen session · Watch the log file's modification time · Interrupt the session when the log stalls · Let the run resume from its last checkpoint · Exit when the DONE file appears
- statements:
  - Runs sometimes stall on a weird MPI error, so he ran `watcher.sh` in a second screen session: if `main.log` is not written for more than two minutes it sends CTRL+C to the `train` session, checks every two minutes, and exits when the final DONE file exists (§intro).
- note: the script relies on the training script restarting and resuming; 677 describes the `-y 1` resume flag and bitwise determinism that make this safe.

### topic: training-compute-budget (optional)
- existing: no
- statements:
  - 774M on 150B tokens: 6 × 774e6 × 150e9 ≈ 7e20, ten times the 350M; 286,102 steps of 524,288 tokens at ~1.7 s/step on 8×A100 80GB SXM at $14/hour ≈ 135 hours ≈ 5.6 days ≈ $2,000, ten times the 124M (§intro). [estimates written in the config comment before the run; the reported actual run was "~6 days"]

## Quotes
- "we somewhat unexpectedly outperform both GPT-2 and GPT-3 very quickly" (§intro)
- "I am very curious why we are performing better than expected" (§intro)
- "We shouldn't decay the LR to 0%." (§intro)
- "at the tail end of the optimization we are going way too slow" (§intro)
- "an unnerving downward "kink" in the validation loss" (§intro)
- "Sometimes the training run stalls and hangs with a weird MPI error" (§intro)

## Notes for merge
- No markdown headings: bold labels Reflections, s3 paths, huggingface paths, Next up. All `§intro`.
- Numbers: "~6 days", 150B tokens, 1.5 epochs are his reported result. The 7e20, 286,102 steps, 1.7 s/iter, 135 h, 5.6 days and $2,000 are the planning arithmetic in the config comment. "(10X 350M)" and "(10X 124M)" are his comparisons with his own earlier runs.
- The watcher script's comment says "1 minute" while its threshold is 120 s and the echo says 2 minutes; paraphrase as "about two minutes".
- The "outperform GPT-2 and GPT-3" chart is an image; the text does not name HellaSwag here. The eval named in 481 and 677 is HellaSwag.
- The Hugging Face upload is by another user (`mdouglas`), credited by him.
- **Lecture:** published three days after `youtube-2024-06-09-reproduce-gpt-2`, but does not mention it. No Note needed from this file.
- No replies by other people in the raw file.
