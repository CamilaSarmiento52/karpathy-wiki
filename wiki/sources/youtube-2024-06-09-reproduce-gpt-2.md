---
type: source
raw_path: raw/youtube/l8pRSuU81PU.md
published: 2024-06-09
medium: youtube
summary: Four-hour lecture that writes GPT-2 (124M) from scratch in PyTorch, loads OpenAI's released weights to check it, speeds training about elevenfold on one A100, adopts GPT-3 optimisation settings, scales to eight GPUs with DDP, and trains on FineWeb-Edu until it beats the GPT-2 124M checkpoint on HellaSwag.
url: https://www.youtube.com/watch?v=l8pRSuU81PU
title: "Let's reproduce GPT-2 (124M)"
---
# Let's reproduce GPT-2 (124M)
Raw: [[raw/youtube/l8pRSuU81PU]] · Original: https://www.youtube.com/watch?v=l8pRSuU81PU

Many numbers in this lecture come from the GPT-2 and GPT-3 papers, OpenAI's released code,
or hardware datasheets; the pages that cite it say which numbers are the paper's and which
are his own run's.

## Summary
A 4-hour Zero to Hero lecture that reproduces the 124M-parameter GPT-2, which he says now
takes about an hour and about $10 of rented compute (@02:11, @02:45). He starts at the target:
he loads OpenAI's released weights through Hugging Face, writes his own GPT-2 class of under
100 lines that matches its parameter names, and checks that it generates coherent text
(@03:50, @12:50, @27:27, @40:59). He then trains from random weights, adding weight tying and
the GPT-2 initialisation (@1:06:20, @1:13:36), and speeds one training step from about 1,000 ms
to about 93 ms with TF32, bfloat16 autocast, torch.compile, flash attention and a vocabulary
padded to 50,304 (@1:36:41, @1:43:58, @1:48:29, @2:00:09, @2:09:10, @2:14:49). Because the
GPT-2 paper is vague, he takes AdamW betas, gradient clipping, a warmup-plus-cosine learning-rate
schedule, weight decay and a 0.5M-token batch from the GPT-3 paper, simulating the batch with
gradient accumulation and spreading it over eight GPUs with distributed data parallel
(@2:15:20, @2:16:28, @2:21:02, @2:28:53, @2:36:15, @2:46:53). He trains on a 10B-token sample of
FineWeb-Edu, checks validation loss and HellaSwag, and reports beating the GPT-2 124M
checkpoint after 10B tokens and nearly matching GPT-3 124M after an overnight 40B-token run
(@3:12:45, @3:28:13, @3:44:15, @3:49:15). He ends with open issues and points to llm.c and the
build-nanogpt repo (@3:56:27, @4:00:28).

## Key points
- GPT-2 is a decoder-only Transformer with pre-norm LayerNorm, a final LayerNorm, GELU and a clean residual stream; attention is the reduce, the MLP the map → [[transformer-architecture]], [[activation-functions]], [[attention-is-a-communication-mechanism]]
- His whole GPT-2 class is under 100 lines → [[gpt-is-not-a-complicated-model]]
- Learned position embeddings recover sinusoid-like structure; token embedding and output head share one matrix (weight tying) → [[embeddings]]
- GPT-2's initialisation from OpenAI's code (std 0.02) and the GPT-2 paper's 1/√N residual scaling → [[weight-initialization]]
- The GPT-2 vocabulary, tiktoken, and uint16 token shards → [[tokenization]]
- PyTorch details: device handling, synchronize for timing, autocast, DDP, torch.compile breaking sampling → [[pytorch]], [[pytorch-documentation-is-unreliable]]
- Flattening logits for cross-entropy; mean reduction and gradient accumulation → [[loss-functions]]
- The speed-up sequence: TF32, bfloat16 autocast, torch.compile, flash attention, nice numbers, fused AdamW, DDP → [[compute-efficiency]], [[memory-access-not-flops-limits-training-speed]]
- AdamW settings, gradient clipping, warmup and cosine decay, weight decay and gradient accumulation from the GPT-3 paper → [[gradient-descent]], [[regularization]], [[inherited-gpt-3-hyperparameters-look-conservative]]
- Top-k sampling and a mismatch with the Hugging Face pipeline → [[sampling-from-language-models]], [[verify-against-a-reference-implementation]]
- With near-infinite data, train and validation loss stay close → [[overfitting-and-generalization]]
- Expected loss at initialisation, overfitting one batch, watching the gradient norm and validation loss → [[training-diagnostics]], [[diagnose-under-or-overfitting]]
- WebText, Common Crawl, data mixtures and FineWeb-Edu; pretraining alone dreams documents, SFT swaps the dataset → [[pretraining-and-finetuning]], [[pretraining-gives-a-document-completer]]
- HellaSwag as a smooth, early-signal eval for small models → [[llm-evaluation]]
- Beats GPT-2 124M on 10B tokens; nearly GPT-3 124M after 40B → [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- His working method for reproducing a released model → [[reproduce-a-published-model]]
- Commit-by-commit build, Jupyter in VS Code, a toy notebook for debugging → [[spelled-out-build-from-scratch]], [[small-hackable-educational-code]], [[prototype-in-jupyter-then-repo]]
- What it builds toward, and the C/CUDA parallel implementation → [[build-nanogpt]], [[nanogpt]], [[llm-c]], [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]

## Fed pages
- [[transformer-architecture]]
- [[activation-functions]]
- [[embeddings]]
- [[weight-initialization]]
- [[tokenization]]
- [[pytorch]]
- [[loss-functions]]
- [[gradient-descent]]
- [[regularization]]
- [[overfitting-and-generalization]]
- [[sampling-from-language-models]]
- [[pretraining-and-finetuning]]
- [[compute-efficiency]]
- [[llm-evaluation]]
- [[training-diagnostics]]
- [[diagnose-under-or-overfitting]]
- [[small-hackable-educational-code]]
- [[spelled-out-build-from-scratch]]
- [[prototype-in-jupyter-then-repo]]
- [[reproduce-a-published-model]]
- [[verify-against-a-reference-implementation]]
- [[nanogpt]]
- [[llm-c]]
- [[memory-access-not-flops-limits-training-speed]]
- [[inherited-gpt-3-hyperparameters-look-conservative]]
- [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- [[pretraining-gives-a-document-completer]]
- [[gpt-is-not-a-complicated-model]]
- [[pytorch-documentation-is-unreliable]]
- [[attention-is-a-communication-mechanism]]
- [[do-not-decay-the-learning-rate-to-zero]]
- [[build-nanogpt]]
- [[how-he-explains]]
- [[build-it-yourself-to-understand-it]]
- [[predict-the-number-before-you-run]]
- [[report-a-comparison-with-its-setting-and-caveats]]
