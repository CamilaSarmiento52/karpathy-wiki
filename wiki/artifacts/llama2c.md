---
type: artifact
repo_url: https://github.com/karpathy/llama2.c
language: C
status: active
sources: ["[[github-2024-05-29-llama2c-readme]]"]
aliases: [llama2.c, baby Llama 2, tinyllamas, run.c]
---
# llama2.c
His repo for training the Llama 2 architecture in PyTorch and then running inference with one simple 700-line C file, `run.c`; he calls it a "fullstack" train plus inference solution for Llama 2, focused on minimalism and simplicity ([[github-2024-05-29-llama2c-readme]] §intro).

## What it demonstrates
- **Where it came from.** He says it started as a fun weekend project: he took nanoGPT, tuned it to the Llama 2 architecture instead of GPT-2, and the core work was the C inference engine; inspired by llama.cpp but wanting something super simple, minimal and educational, he hard-coded the architecture in one dependency-free C file ([[github-2024-05-29-llama2c-readme]] §intro).
- **Tiny models.** His 15M-parameter TinyStories model runs at about 110 tokens/s on his M1 MacBook Air, and a 42M model still samples at interactive rates with more coherent stories ([[github-2024-05-29-llama2c-readme]] §feel the magic). He trained a series of 260K, 15M, 42M and 110M models on 4X A100 40GB, each in a few hours and the 110M in about 24 hours, and hosts them as tinyllamas ([[github-2024-05-29-llama2c-readme]] §models).
- **Meta's checkpoints.** Because the architecture is identical it can run Meta's Llama 2 models: the 7B exported to a 26GB float32 file ran at about 4 tokens/s with OpenMP on 96 threads of his cloud CPU box; he would not run anything above 7B, because 13B+ hits an integer overflow in pointer arithmetic and float32 inference would be unusably slow ([[github-2024-05-29-llama2c-readme]] §Meta's Llama 2 models). Chat mode works with Llama Chat, and Code Llama support is incomplete and a bit buggy because some hyperparameters, such as the RoPE constant, changed ([[github-2024-05-29-llama2c-readme]] §Meta's Llama 2 models). Hugging Face models with the Llama 2 architecture can be exported with `--hf` ([[github-2024-05-29-llama2c-readme]] §huggingface models).
- **Quantized inference.** `runq.c` adds int8 quantization, 4X smaller and 3X faster on Llama 2 7B in his timing, while `run.c` stays the fp32 reference ([[github-2024-05-29-llama2c-readme]] §int8 quantization).
- **Speed on CPUs.** `make runfast` (-Ofast) was fastest on his M1; `-march=native`, clang and OpenMP help, and more threads is not always better, usually a bit U-shaped ([[github-2024-05-29-llama2c-readme]] §performance). It builds on Windows, CentOS 7, Amazon Linux and Mac ([[github-2024-05-29-llama2c-readme]] §platforms).
- **Tests and forks.** `test_all.py` forwards the model in C and Python against known-good output, and the README lists many community ports to other languages by other people ([[github-2024-05-29-llama2c-readme]] §tests, §notable forks).
- **Todos at the snapshot.** A CUDA `run.cu`, more C tests, an Engine class with a KV cache for PyTorch inference, easier datasets, and LoRA finetuning ([[github-2024-05-29-llama2c-readme]] §unsorted todos).
- `status: active` rests on the README calling the project young and moving quickly and on its open todo list; it has no deprecation notice ([[github-2024-05-29-llama2c-readme]] §intro, §unsorted todos). `language: C` is the inference engine; training is in Python with PyTorch ([[github-2024-05-29-llama2c-readme]] §intro).

## Related
- [[nanogpt]] — its starting point
- [[small-llms-can-be-strong-in-narrow-domains]] — the claim the tiny models illustrate
- [[small-hackable-educational-code]] — the contributing policy
- [[compute-efficiency]] — int8 quantization
- [[sampling-from-language-models]] — temperature and top-p
- [[transformer-architecture]] — Llama's changes from GPT-2
- [[llm-c]] — his C/CUDA training codebase
