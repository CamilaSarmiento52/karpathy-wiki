---
type: claim
stated_on: 2024-04-22
confidence: stated
sources: ["[[github-2024-04-22-llmc-state-of-the-union]]", "[[github-2024-05-03-llmc-state-of-the-union]]", "[[youtube-2024-06-09-reproduce-gpt-2]]", "[[github-2024-07-11-llmc-gpt-2-1-6b]]"]
topic: "[[compute-efficiency]]"
---
# In his measurements, llm.c trained GPT-2 faster than PyTorch
> "PyTorch comparison (fp32, no flash attention, slightly stale PyTorch) is 78.2ms/iteration" — [[github-2024-04-22-llmc-state-of-the-union]] §intro

## Context
In his first State of the Union for [[llm-c]] he measures about 73 ms per training iteration on his A100 against 78.2 ms for the PyTorch comparison run, which used fp32, no flash attention and a slightly stale PyTorch; he calls the result about 6.4% faster "in this constrained setting" ([[github-2024-04-22-llmc-state-of-the-union]] §intro). In the same report peak memory reads a constant 8753 MiB in `nvidia-smi` against 12879 MiB for the PyTorch code, 32% lower, and he gives the PyTorch command to reproduce it ([[github-2024-04-22-llmc-state-of-the-union]] §intro (peak memory)). All of these are his measurements; he scopes the speed figure to "this constrained setting" ([[github-2024-04-22-llmc-state-of-the-union]] §intro).
In the 2024-05-03 report he says llm.c trains GPT-2 (124M) on one GPU "faster than PyTorch nightly by ~7%", with no asterisks, against what he calls the fastest PyTorch run he knows how to configure for one-GPU training on Ampere, with mixed precision, torch compile and flash attention ([[github-2024-05-03-llmc-state-of-the-union]] §intro (Single GPU training)). Against the stable PyTorch 2.3.0 it is about 46% faster, and he credits the PyTorch team with recent changes that greatly sped up the GPT-2 setting; against his own April 22 report it is about a 3X speedup ([[github-2024-05-03-llmc-state-of-the-union]] §intro (Single GPU training)).

His fine print: an A100 40GB PCIe on Lambda; llm.c at about 167K tokens/s on a pull request about to merge (about 160K on master) against PyTorch at about 150K, about 11%; padding PyTorch's vocabulary to 50304 lifts it to about 156K and leaves about 7% ([[github-2024-05-03-llmc-state-of-the-union]] §intro (Fine print)). Peak memory at batch 32 and sequence length 1024 is 16.6 GiB for llm.c against 37.2 GiB for PyTorch, a PyTorch number he says feels suspiciously high and he means to investigate ([[github-2024-05-03-llmc-state-of-the-union]] §intro (Peak memory)). **Note:** each percentage holds only against its own baseline ([[github-2024-05-03-llmc-state-of-the-union]] §intro).

In the GPT-2 lecture, published 2024-06-09, he runs both on one GPU on camera: about 223,000 tokens per second for llm.c against about 185,000 for the PyTorch version, with identical losses and norms, and says he does not have full confidence he squeezed all the juice out of the PyTorch implementation ([[youtube-2024-06-09-reproduce-gpt-2]] @3:58:46, @3:59:19).

**At 1.6B (2024-07-11).** For a relatively comparable 1.6B run in PyTorch nightly, with the vocabulary hacked to 50304, he measures about 80GB of memory against llm.c's 57GB, a 29% improvement, and about 3386 against 2750 ms per iteration, llm.c stepping about 19% faster ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (PyTorch comparison)). Some of the gain has a known origin, such as llm.c's fused classifier that kicks off the backward pass, which he says torch.compile does not do as far as he knows ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (PyTorch comparison)). He does not have full confidence that the PyTorch script is maximally tuned and shows the comparison so others can check and help tune; his conclusion is scoped to GPT-2/3 training ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (PyTorch comparison)).
