# Digest: Let's reproduce GPT-2 (1.6B): one 8XH100 node, 24 hours, $672, in llm.c
- raw: raw/github/karpathy__llm.c__discussion-677.md · published: 2024-07-11 · medium: github · words: 4283
- source slug: github-2024-07-11-llmc-gpt-2-1-6b

## Source page
```
---
type: source
raw_path: raw/github/karpathy__llm.c__discussion-677.md
published: 2024-07-11
medium: github
summary: "His walkthrough of reproducing the full 1558M GPT-2 in llm.c on one 8×H100 node in 24 hours for $672: the launch recipe and flags, how he reads the evals against OpenAI's GPT-2 and GPT-3, why he finds the C/CUDA code beautiful, a comparison with PyTorch, and a 420B-token run that beat both on HellaSwag before going unstable."
url: https://github.com/karpathy/llm.c/discussions/677
title: "Let's reproduce GPT-2 (1.6B): one 8XH100 node, 24 hours, $672, in llm.c"
---
# Let's reproduce GPT-2 (1.6B): one 8XH100 node, 24 hours, $672, in llm.c
Raw: [[raw/github/karpathy__llm.c__discussion-677]] · Original: https://github.com/karpathy/llm.c/discussions/677

## Summary
He reproduces the full 1558M GPT-2 of OpenAI's February 2019 release in llm.c, about 5,000 lines of C/CUDA with no Python or PyTorch, on one 8×H100 node in 24 hours for $672, crediting five years of better GPUs, software and data such as FineWeb-Edu; he flags that llm.c is not yet perfectly tuned or stable and its evals are not comprehensive (§intro). The run takes 32,000 steps of about 1M tokens, 33.6B tokens in all, at about 50% MFU; its validation loss passes OpenAI's GPT-2 by step ~5,000, which he calls unfair because of the data shift, and its HellaSwag crosses GPT-2 around step 25K, possibly because of data quality (§intro). He explains each flag, mostly GPT-3-paper hyperparameters except a tripled learning rate, a memory guide, and why he finds the code beautiful: minimal C/CUDA, fast to compile, constant memory, bitwise deterministic, just below 50% MFU (§intro). Against a comparable PyTorch run he measures 57GB against about 80GB of memory and about 19% faster steps, while saying the PyTorch script may not be fully tuned (§intro). A 420B-token run beat GPT-2 and GPT-3 of its size on HellaSwag, reaching about 61%, then went unstable after step ~330,000, which he puts down to not yet being careful enough about initialisation, activation ranges and stability (§intro).

## Key points
- Full 1558M GPT-2: 8×H100, 24 h, $672, ~5,000 LOC, flags, multi-node, model export, FAQ, roadmap and goal → [[llm-c]]
- Val loss vs OpenAI's GPT-2 is unfair; HellaSwag as a smooth early-signal eval; even HellaSwag misses multilingual, math, code; evals are hard at GPT-2 capability → [[llm-evaluation]]
- Crosses GPT-2 on HellaSwag around 25K steps, earlier than expected; 400B run reaches ~61% → [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- 6e-4 instead of the GPT-3 paper's 2e-4; GPT-3 hyperparameters look suboptimal → [[gpt-3-paper-hyperparameters-look-suboptimal]], [[gradient-descent]]
- Decay to 10% (`-q 0.1`), following the GPT-3 paper → [[do-not-decay-the-learning-rate-to-zero]]
- Neural net training is one while loop of simple arithmetic and should not be that complicated → [[neural-net-training-should-not-be-complicated]], [[small-hackable-educational-code]]
- 57GB vs ~80GB, ~19% faster than a PyTorch run, with caveats → [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]], [[benchmark-against-pytorch]]
- Memory guide (micro-batch, recompute, fp32 master weights, sequence length), MFU, multi-node → [[gpu-training-efficiency]]
- Loss spikes, skipped updates, a 420B-token run that explodes → [[llm-c-was-not-yet-careful-enough-about-training-stability]], [[training-diagnostics]]
- Resume flag and bitwise determinism; constant memory footprint → [[keep-long-training-runs-alive]]
- 33.6B tokens in 24 h; ~30 min estimate on 512 GPUs → [[training-compute-budget]]
- GPT-3 is essentially GPT-2's architecture with context 2048 → [[transformer-architecture]]
- Pretraining only; SFT and RLHF on the roadmap; finetuning OpenAI's model adapts quickly to new data → [[pretraining-and-finetuning]]
- PyTorch script as a testing reference, not an implementation → [[pytorch]]

## Fed pages
- [[llm-c]]
- [[llm-evaluation]]
- [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- [[gpt-3-paper-hyperparameters-look-suboptimal]]
- [[gradient-descent]]
- [[do-not-decay-the-learning-rate-to-zero]]
- [[neural-net-training-should-not-be-complicated]]
- [[small-hackable-educational-code]]
- [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- [[benchmark-against-pytorch]]
- [[gpu-training-efficiency]]
- [[llm-c-was-not-yet-careful-enough-about-training-stability]]
- [[training-diagnostics]]
- [[keep-long-training-runs-alive]]
- [[training-compute-budget]]
- [[transformer-architecture]]
- [[pretraining-and-finetuning]]
- [[pytorch]]
```

## Candidates
### artifact: llm-c
- existing: no
- statements:
  - llm.c reproduces the full 1558M GPT-2 directly in C/CUDA, about 5,000 lines, without Python or a library like PyTorch/JAX or huggingface/transformers (§intro).
  - In 2019 training GPT-2 was a team project and a big run; about five years later, thanks to H100s, CUDA/cuBLAS/cuDNN/FlashAttention and data such as FineWeb-Edu, one 8×H100 node does it in 24 hours for $672 (§intro). [his result]
  - Caveats he states: not perfectly tuned, not sufficiently stabilised (occasional loss spikes and bad activation ranges), evals not comprehensive (§intro).
  - The unicorn prompt from OpenAI's GPT-2 post gives a fairly coherent completion that he judges qualitatively around GPT-2's level; 20 side-by-side samples are linked (§intro). [qualitative judgement]
  - One GPU gives the same GPT-2 in about 8 days instead of 1; 16 GPUs multi-node in about 12 hours; setup takes about a minute from blank box to stepping (§intro). [estimates]
  - Layout: `train_gpt2.cu` holds the model and training loop (`cloc` 1353 LOC at the time; he also says ~2,000), importing 23 helper files in `llmc` totalling 3170 LOC (§intro).
  - Multi-node: the most GPUs he has seen used is ~500; his own largest run was 16×H100 across two nodes on Lambda's 1-click clusters; on a 512-GPU cluster at $2,300/hour GPT-2 might train in ~30 minutes with a larger batch (~8M) and some tuning, untried (§intro). [estimate]
  - Final model on S3 and Hugging Face; longer runs of 100K steps (HellaSwag 57.7) and 330K steps (62.7) also uploaded (§intro). [his results]
  - Export to Hugging Face format enables the Eleuther eval harness and HF sampling (§intro).
  - FAQ: sampling in llm.c is inefficient and hacky, use the HF export; no chat (pretraining only); fp8 work in progress; CUDA only, with an actively maintained AMD fork by @anthonix (§intro).
  - Core contributors: @ngc92, @ademeure, @gordicaleksa, @rosslwheeler; Lambda sponsors the GPUs; Nvidia and Ubicloud provide CI runners (§intro).
  - Roadmap: tune GPT-2 hyperparameters; training and scaling stability (optimisers, schedulers, clipping, norming, muP); fp8; inference with a KV cache; SFT and RLHF; multimodal (VQVAE); Llama/Gemma support (§intro).
  - Goal: a simple, minimal, clean training stack for a full-featured LLM agent in direct C/CUDA, plus companion educational materials to bring many people up to speed (§intro).
- status note: still active and expanding in July 2024 per this roadmap.

### topic: llm-evaluation
- existing: no
- statements:
  - OpenAI's GPT-2 scores 2.83 on FineWeb-Edu validation loss, and his run passes it by about step 5,000, but he calls the comparison unfair because GPT-2 trained on the unreleased WebText; finetuning OpenAI's model for 1,000 steps at LR 1e-4 drops its loss to 2.61 (§intro). [2.83 and 2.61 are his measurements of OpenAI's model]
  - He uses validation loss as a sanity check; for the actual comparison he wants fixed third-party evals (§intro).
  - HellaSwag: simple common-sense scenarios where the model picks the right continuation; well-behaved, smooth, common, often cited, and gives early signal (§intro).
  - Even HellaSwag is not an ideal single comparison: it tests simple English and common sense, not multilingual, math or code; WebText may have weighted those more and they may have taken capacity, which cannot be known (§intro).
  - Good evals are harder at GPT-2's capability: such models do not understand multiple choice and their samples are not good enough to beat chance on math or code evals (§intro).
  - `dev/eval` has instructions for the Eleuther harness and the HF Open LLM Leaderboard evals (§intro).

### claim: his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag
- existing: no
- confidence: stated
- quote (this file): "This model dramatically beats GPT-2 and GPT-3 of its size on HellaSwag" (§intro)
- statements:
  - The 1558M run crosses GPT-2 on HellaSwag around step 25K, earlier than GPT-2, which is estimated to have trained on ~100B tokens; he says this possibly has to do with data quality, as in the 124M run (§intro). [crossing point is his result; GPT-2's ~100B is an estimate]
  - The green comparison line is GPT-3 of the same size, nearly the same architecture, trained on 300B tokens, about 10X his run (§intro). [comparison]
  - The 420B-token run reaches about 61% HellaSwag, dramatically beating GPT-2 and GPT-3 of its size, before going unstable (§intro). [his result]
- relation to existing claims: none. Internal to the batch: same claim across 481, 580 and 677, with his uncertainty about why stated in 580 and 677.

### claim: gpt-3-paper-hyperparameters-look-suboptimal
- existing: no
- title: He finds the GPT-3 paper's hyperparameters appear quite suboptimal for GPT-2 training
- confidence: stated
- stated_on: 2024-07-11
- quote: "the hyperparameters cited by OpenAI in the GPT-3 paper appear to be quite suboptimal" (§intro)
- context: he follows the GPT-3 paper in most settings because GPT-2's paper gave very little detail (§intro); the GPT-3 paper says 2e-4 for this size, he tripled it to 6e-4 and it seems to train faster without issues, though not tuned carefully (§intro); in "Coming up" he credits @Yuchenj_UW on X with finding that 3X the learning rate trains faster with no apparent downsides, and expects more low-hanging fruit (§intro).
- attribution: the 3X-LR finding is credited to another person; his own evidence is his run "seems to" train faster. Keep the title at "appear".
- relation to existing claims: none.

### claim: do-not-decay-the-learning-rate-to-zero
- existing: no (proposed in digest 580)
- statements:
  - The 1.6B run uses `-q 0.1`, decaying to 10% of max LR, following the GPT-3 paper (§intro).
- relation: follows through on the 580 reflection; supports evidence for the claim, not a new claim.

### topic: gradient-descent
- existing: yes
- statements:
  - Total batch 2^20 ≈ 1M tokens from the GPT-3 table; with 8 GPUs × 16 × 1024 = 131,072 tokens per micro-step the code does 8 forward-backward passes per update (§intro).
  - Cosine schedule (default), max LR 6e-4, decay to 10%, 700-step warmup, weight decay 0.1 on 2-D weights only, 32,000 steps chosen to fit 24 hours (§intro).
  - He skips updates on instantaneous instability with `-sl 5.0 -sg 5.0`, which helps mitigate and defer problems (§intro).

### claim: neural-net-training-should-not-be-complicated
- existing: no
- title: Neural net training is one loop of simple arithmetic and should not be that complicated
- confidence: stated
- stated_on: 2024-07-11
- quote: "Neural net training is just one while loop of the same, simple arithmetic operations" (§intro); also "it really shouldn't be that complicated." (§intro)
- context: in the Code paragraph, where he says, while admitting bias, that llm.c is quite beautiful: basic CUDA dependencies only, direct minimal readable C/CUDA, mostly C not C++ to stay simple, the arithmetic is +, -, *, / on a single float array (§intro).
- relation to existing claims:
  - **supports** [[gpt-is-not-a-complicated-model]]: minGPT's README says GPT is not complicated and the complexity is batching for efficiency ([[github-2023-01-08-mingpt-readme]] §intro); here he says training as a whole should not be complicated ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro). Both can hold; this one broadens from the model to the training loop, so `extends` is also defensible; pick `supports` as the weaker link unless merge wants a timeline.
  - **supports** [[micrograd-is-all-you-need-everything-else-is-efficiency]]: the micrograd lecture says micrograd is what you need to train networks and the rest is efficiency ([[youtube-2022-08-16-micrograd]] @06:30); llm.c's "simple arithmetic on a float array" is the same view at production scale. Both can hold.

### method: small-hackable-educational-code
- existing: yes
- statements:
  - His list of why llm.c is beautiful: only basic CUDA dependencies; direct, minimal, readable C/CUDA in about 5,000 lines; mostly C, not C++, to keep it simple; compiles and runs in seconds so you step more and wait less; allocates all GPU memory once with a constant footprint; bitwise deterministic; efficient at just under 50% MFU (§intro).
  - The goal pairs the minimal stack with companion educational materials (§intro).
- relation: extends the method beyond one-file PyTorch repos to a ~5,000-line C/CUDA project that adds efficiency as a stated virtue; consistent with the existing "teeth" step from minGPT.

### claim: llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements
- existing: no
- statements:
  - In a comparable 1.6B run, PyTorch nightly (vocab padded to 50304) used ~80GB against llm.c's 57GB, a 29% improvement, and stepped at about 3386 ms against 2750 ms, llm.c ~19% faster (§intro). [his measurement]
  - Known sources of the gain include the fused classifier that kicks off the backward pass, which he says torch.compile does not do as far as he knows (§intro).
  - He does not have full confidence the PyTorch script is maximally tuned and shows the comparison so others can check and help tune (§intro).
- quote option: "Certainly I feel biased but llm.c is quite beautiful" belongs to the code claim, not this one; no clean under-15-word speed quote here. Use 344's or leave the claim quote to merge.

### method: benchmark-against-pytorch
- existing: no
- statements:
  - He gives the full comparable `torchrun` command, says where the PyTorch loop differs (e.g. the dataloader does not permute shards), and notes the vocab hack applied to PyTorch (§intro).
  - He reports memory and step time, names known causes of the gap, and says the PyTorch side may not be maximally tuned, inviting others to check (§intro).

### topic: gpu-training-efficiency
- existing: no
- statements:
  - MFU around 50%, "quite efficient" (§intro). [his measurement; first log lines show 42.6–47.5% bf16 MFU]
  - Memory guide for GPUs under 80GB: first lower the micro-batch in powers of two; then recompute (`-r 1` very slightly slower with a huge saving, `-r 2` also recomputes layernorms); then `-w 0` to drop the fp32 master weights, which has seemed fine empirically, likely thanks to stochastic rounding; lastly shorten the sequence, which makes the model worse (§intro).
  - Memory matters because it lets you raise the batch size, which goes a bit faster (§intro).
  - Recompute trades compute for memory: recomputing GELU in backward avoids caching it (§intro).

### claim: llm-c-was-not-yet-careful-enough-about-training-stability
- existing: no
- title: He judged llm.c not yet careful enough about initialisation, activation ranges and stability for long runs
- confidence: stated
- stated_on: 2024-07-11
- quote: "but sadly becomes unstable there on and explodes" (§intro) (describes the run; the judgement sentence is longer than 15 words)
- context: the 420B-token run (more than GPT-3's 300B for this size) looked great until about step 330,000, then became unstable and exploded; smaller spikes along the way were mitigated by skipping updates; he thinks deeper issues gradually drift the model into instability, especially for larger models and long training, and asks for ideas (§intro). Also the intro caveat: loss spikes and bad activation ranges now and then (§intro).
- topic: [[training-diagnostics]] or [[weight-initialization]]
- relation to existing claims: [[modern-innovations-make-precise-initialization-less-important]] (2022) says exact init has become less important, while also saying the field has not solved initialisation ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @36:26, @1:54:48). Both can hold (smaller nets vs long large runs), so **not** `contradicts`. A **Note:** connecting the two is safest; `extends` is arguable but would require a timeline. Recommend Note only.

### method: training-diagnostics
- existing: yes
- statements:
  - In the log he expects the gradient norm to settle around 0.1–1 as the learning rate warms up (§intro).
  - The validation loss serves him as a sanity check rather than the comparison (§intro).
  - Loss spikes and bad activation ranges are his signs of instability; the code detects simple instantaneous instability and skips the update (§intro).

### method: keep-long-training-runs-alive (optional)
- existing: no (proposed in digest 580)
- statements:
  - `-y 1` turns on resume: if training crashes or hangs, CTRL+C and re-run the same command and it resumes; because llm.c is bitwise-deterministic the result is identical to an uninterrupted run (§intro).
  - llm.c allocates all GPU memory at the start with a constant footprint, so once stepping starts it will not run out of memory (§intro).
  - Checkpoints every 2,000 steps (`-n 2000`) (§intro).

### topic: training-compute-budget (optional)
- existing: no
- statements:
  - 32,000 steps × 1,048,576 tokens = 33.6B tokens, about 2.75 s per step, about 24 hours on 8×H100, $672 (§intro). [his result]
  - The 420B-token run is more than GPT-3's 300B for this size (§intro).

### topic: transformer-architecture
- existing: yes
- statements:
  - GPT-3 of the same size is pretty much GPT-2's architecture with minor differences (context 1024 → 2048) but trained for 300B tokens (§intro).
  - GPT-2's release had weights but few details, GPT-3's had details but no weights, so he follows GPT-3's hyperparameters (§intro).
  - The 1558M model is `-e "d48"`, depth 48, 1,557,686,400 parameters per the log (§intro).

### topic: pretraining-and-finetuning
- existing: yes
- statements:
  - llm.c is pretraining only; you cannot chat with it (§intro).
  - Finetuning OpenAI's GPT-2 for 1,000 steps at LR 1e-4 quickly adapts it to the new data distribution (§intro).
  - SFT and RLHF finetuning are on the roadmap (§intro).

### topic: pytorch
- existing: yes
- statements:
  - The PyTorch `train_gpt2.py` is meant as a testing reference, not an actual implementation, so its loop differs in places (§intro).

## Quotes
- "Certainly I feel biased but llm.c is quite beautiful" (§intro)
- "Neural net training is just one while loop of the same, simple arithmetic operations" (§intro)
- "it really shouldn't be that complicated." (§intro)
- "We try to be mostly C, not C++ to keep it simple." (§intro)
- "I like to look at the validation loss as a sanity check" (§intro)
- "good evals are harder at low model capability like GPT-2" (§intro)
- "This model dramatically beats GPT-2 and GPT-3 of its size on HellaSwag" (§intro)
- "but sadly becomes unstable there on and explodes" (§intro)
- "the hyperparameters cited by OpenAI in the GPT-3 paper appear to be quite suboptimal" (§intro)
- "The model is fairly coherent and qualitatively somewhere around the level of GPT-2." (§intro)
- "llm.c is bitwise-deterministic, so you'll get the identical result as if you didn't crash." (§intro)
- "This wasn't tuned very carefully yet." (§intro)
- "The downsides of unemployment." (§intro) — a joke about his own multi-node use; quote only with that context

## Notes for merge
- No markdown headings: bold labels Unicorns, Training, Evals, Args guide, Memory guide, Code, Multi-node training, PyTorch comparison, The final model, Model export, 400B token run, FAQ, GPT-2 (124M), Authors, Coming up. All `§intro`; append the label for precision.
- **Measured vs comparison vs estimate.** Measured (his): 24 h, $672, ~2.75 s/step, ~50% MFU, 33.6B tokens, HellaSwag crossover ~25K steps, 57GB vs ~80GB, 2750 vs 3386 ms (~19%), 100K-step HellaSwag 57.7, 330K-step 62.7, 420B run ~61% before instability, OpenAI GPT-2 val loss 2.83 and 2.61 after finetuning. Comparisons: GPT-2 trained on ~100B tokens (an estimate he cites), GPT-3 on 300B, GPT-3 paper LR 2e-4. Estimates: 8 days on 1 GPU, 12 h on 16 GPUs, ~30 min on 512 GPUs at $2,300/h.
- Odd numbers: the 420B run's HellaSwag is "~61%", while the 330K-step uploaded model is listed at 62.7. Both are in the raw; do not reconcile. The `-u 700` bullet says "at total batch size 0.5M is 350M tokens", copied from the 124M post although this run's batch is 1M; flag, do not repeat. The model-export example path says `log_gpt2_128M` (likely a typo in the raw). LOC: "~5,000 lines" overall and "~2,000 LOC" for `train_gpt2.cu`, but `cloc` reports 1353 for that file; cite the cloc figures if precision matters.
- Unicorn completion and sample text are model output, not his words.
- The 3X learning-rate finding is credited to @Yuchenj_UW on X; his own statement is that tripling "seems to" work.
- "The downsides of unemployment" is a self-deprecating aside, not a position.
- The GPT-2 (124M) paragraph links back to Discussion 481. It does not mention the June 2024 lecture `youtube-2024-06-09-reproduce-gpt-2`; any link between the lecture's 124M reproduction and this post is a merge **Note:** once the lecture source page exists.
- nanoGPT is not mentioned.
- No replies by other people in the raw file.
