---
type: source
raw_path: raw/github/karpathy__llm.c__discussion-481.md
published: 2024-05-28
medium: github
summary: "His walkthrough of training GPT-2 (124M) from scratch in llm.c on 10B FineWeb tokens in about 90 minutes and $20 on one 8×A100 node, with every flag explained, how to read the training log, how he evaluates against OpenAI's checkpoint, a 350M run, and an FAQ on why GPT-2."
url: https://github.com/karpathy/llm.c/discussions/481
title: Reproducing GPT-2 (124M) in llm.c in 90 minutes for $20
---
# Reproducing GPT-2 (124M) in llm.c in 90 minutes for $20
Raw: [[raw/github/karpathy__llm.c__discussion-481]] · Original: https://github.com/karpathy/llm.c/discussions/481

No markdown headings: bold-labelled paragraphs (Args guide, Training, Visualization, Tokenizer, Sampling, Code, 350M model, Coming up, FAQ, Acknowledgements), cited as `§intro` with the label where useful.

## Summary
He reproduces GPT-2 (124M), the smallest model OpenAI released in 2019, in llm.c (about 4,000 lines of C/CUDA): on one 8×A100 80GB node at up to ~60% model flops utilisation it takes about 90 minutes, about $20 at ~$14/hour, training on 10B tokens of FineWeb (§intro). His run beats OpenAI's checkpoint on FineWeb validation loss, which he says is not a fair comparison because GPT-2 was trained on different data, and reaches 29.9 on HellaSwag against GPT-2 (124M)'s 29.4 and the GPT-3 paper's 33.7 for a 124M model trained on 300B tokens (§intro). He gives the full setup and explains each flag, most following the GPT-3 paper because it is more detailed than GPT-2's, then explains how to read a log line: MFU, tokens per second, loss as perplexity, and gradient norm with clipping at 1.0 (§intro (Args guide), §intro (Training)). He covers tokenizer generation, very hacky sampling, the code's layout, and an overnight 350M run on 30B tokens for about $200 (§intro (Tokenizer), §intro (Sampling), §intro (Code), §intro (350M model)). The FAQ says the model is pretraining only, not chat, that llm.c is C/CUDA only, and that he cares about GPT-2 because it was the first recognisably modern LLM stack with released weights (§intro (FAQ)).

## Key points
- 124M in ~90 min / ~$20 on 8×A100, 350M in 14 h / ~$200, code layout, FAQ → [[llm-c]]
- The steps of the reproduction, from picking GPT-2 to scaling to 350M → [[reproduce-a-published-model]]
- FineWeb val vs HellaSwag, why val loss against OpenAI's checkpoint is unfair, HellaSwag favouring web-like data → [[llm-evaluation]]
- His 124M beats OpenAI's 124M on HellaSwag with 10B tokens → [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- Hyperparameters from the GPT-3 paper: 0.5M-token batch, LR 6e-4, 700-step warmup, decay to 0, weight decay 0.1 on 2-D weights, clipping at 1.0 → [[gradient-descent]]
- Reading a log line: loss as perplexity, gradient norm spikes, MFU → [[training-diagnostics]]
- exp(loss) as the number of tokens the model is effectively guessing among → [[loss-functions]]
- MFU, memory-bound training, GELU recompute, ZeRO-1, 6ND compute and cost → [[compute-efficiency]]
- GPT-2 as the grand-daddy of LLMs; GPT-3 and Llama 3 differences → [[gpt-2-is-the-first-recognizably-modern-llm-stack]], [[transformer-architecture]]
- Pretraining only, no chat finetuning; CPU users can finetune OpenAI's weights → [[pretraining-and-finetuning]]
- `train_gpt2.py` as a parallel reference for error checking, without full parity → [[pytorch]], [[verify-against-a-reference-implementation]]
- Started as 1,000 clean lines of C, now ~3,500 → [[small-hackable-educational-code]]

## Fed pages
- [[llm-c]]
- [[reproduce-a-published-model]]
- [[llm-evaluation]]
- [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- [[gradient-descent]]
- [[training-diagnostics]]
- [[loss-functions]]
- [[compute-efficiency]]
- [[gpt-2-is-the-first-recognizably-modern-llm-stack]]
- [[transformer-architecture]]
- [[pretraining-and-finetuning]]
- [[pytorch]]
- [[verify-against-a-reference-implementation]]
- [[small-hackable-educational-code]]
