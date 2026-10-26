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

No markdown headings: bold labels (Unicorns, Training, Evals, Args guide, Memory guide, Code, Multi-node training, PyTorch comparison, The final model, Model export, 400B token run, FAQ, Authors, Coming up), cited as `§intro` with the label.

## Summary
He reproduces the full 1558M GPT-2 of OpenAI's February 2019 release in llm.c, about 5,000 lines of C/CUDA with no Python or PyTorch, on one 8×H100 node in 24 hours for $672, crediting five years of better GPUs, software and data such as FineWeb-Edu; he flags that llm.c is not yet perfectly tuned or stable and its evals are not comprehensive (§intro). The run takes 32,000 steps of about 1M tokens, 33.6B tokens in all, at about 50% MFU; its validation loss passes OpenAI's GPT-2 by step ~5,000, which he calls unfair because of the data shift, and its HellaSwag crosses GPT-2 around step 25K, possibly because of data quality (§intro (Training), §intro (Evals)). He explains each flag, mostly GPT-3-paper hyperparameters except a tripled learning rate, gives a memory guide, and says why he finds the code beautiful: minimal C/CUDA, fast to compile, constant memory, bitwise deterministic, just below 50% MFU (§intro (Args guide), §intro (Memory guide), §intro (Code)). Against a comparable PyTorch run he measures 57GB against about 80GB of memory and about 19% faster steps, while saying the PyTorch script may not be fully tuned (§intro (PyTorch comparison)). A 420B-token run beat GPT-2 and GPT-3 of its size on HellaSwag, reaching about 61%, then went unstable after step ~330,000, which he puts down to not yet being careful enough about initialisation, activation ranges and stability (§intro (400B token run)).

## Key points
- Full 1558M GPT-2: 8×H100, 24 h, $672, ~5,000 LOC, multi-node, model export, FAQ, roadmap and goal → [[llm-c]], [[reproduce-a-published-model]]
- Validation loss against OpenAI's GPT-2 is unfair; HellaSwag as a smooth early-signal eval that still misses multilingual, math and code → [[llm-evaluation]]
- Crosses GPT-2 on HellaSwag around 25K steps; the 420B-token run reaches ~61% → [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- 6e-4 instead of the GPT-3 paper's 2e-4; GPT-3 hyperparameters "appear to be quite suboptimal" → [[inherited-gpt-3-hyperparameters-look-conservative]], [[gradient-descent]]
- Decay to 10% (`-q 0.1`), following the GPT-3 paper → [[do-not-decay-the-learning-rate-to-zero]]
- Neural net training is one while loop of simple arithmetic and should not be that complicated → [[neural-net-training-should-not-be-complicated]], [[gpt-is-not-a-complicated-model]], [[small-hackable-educational-code]]
- 57GB vs ~80GB, ~19% faster than a PyTorch run, with caveats → [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]], [[verify-against-a-reference-implementation]]
- Memory guide, MFU, 33.6B tokens in 24 h, multi-node estimates → [[compute-efficiency]]
- Loss spikes, skipped updates, a 420B-token run that explodes; resume flag and bitwise determinism → [[llm-c-was-not-yet-careful-enough-about-training-stability]], [[training-diagnostics]]
- GPT-3 is essentially GPT-2's architecture with context 2048 → [[transformer-architecture]]
- Pretraining only; SFT and RLHF on the roadmap; finetuning OpenAI's model adapts quickly to new data → [[pretraining-and-finetuning]]
- The PyTorch script as a testing reference, not an implementation → [[pytorch]]

## Fed pages
- [[llm-c]]
- [[reproduce-a-published-model]]
- [[llm-evaluation]]
- [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- [[inherited-gpt-3-hyperparameters-look-conservative]]
- [[gradient-descent]]
- [[do-not-decay-the-learning-rate-to-zero]]
- [[neural-net-training-should-not-be-complicated]]
- [[gpt-is-not-a-complicated-model]]
- [[small-hackable-educational-code]]
- [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- [[verify-against-a-reference-implementation]]
- [[compute-efficiency]]
- [[llm-c-was-not-yet-careful-enough-about-training-stability]]
- [[training-diagnostics]]
- [[transformer-architecture]]
- [[pretraining-and-finetuning]]
- [[pytorch]]
- [[report-a-comparison-with-its-setting-and-caveats]]
