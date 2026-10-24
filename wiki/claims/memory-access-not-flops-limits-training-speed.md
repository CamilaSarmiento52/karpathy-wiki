---
type: claim
stated_on: 2024-06-09
confidence: stated
sources: ["[[youtube-2024-06-09-reproduce-gpt-2]]"]
context: ["[[github-2024-05-03-llmc-state-of-the-union]]"]
topic: "[[compute-efficiency]]"
---
# Memory access patterns, not FLOP counts, limit much of training speed
> "the fact that flops don't matter uh the entire memory access pattern matters" — [[youtube-2024-06-09-reproduce-gpt-2]] @2:04:42

## Context
In the GPT-2 lecture he says many deep-learning training workloads are memory-bound: the tensor cores spend most of their time idle because data cannot be loaded from memory fast enough, so 60% utilisation counts as doing extremely well ([[youtube-2024-06-09-reproduce-gpt-2]] @1:27:04, @1:27:38). He uses this to explain his first speed-up: switching matmuls to TF32 gave about 3× rather than the datasheet's 8×, because the workload was still moving float32 numbers through memory ([[youtube-2024-06-09-reproduce-gpt-2]] @1:38:24, @1:38:59).

The quote is his gloss on flash attention, which he calls a great example of being aware of the memory hierarchy: it does more FLOPs than the attention it replaces, yet runs faster because it never writes the T×T attention matrix to GPU high-bandwidth memory ([[youtube-2024-06-09-reproduce-gpt-2]] @2:01:13, @2:01:48, @2:04:42). Padding the vocabulary from 50,257 to 50,304 is a second case: it adds FLOPs and still made the step faster ([[youtube-2024-06-09-reproduce-gpt-2]] @2:10:51, @2:13:42). "Don't matter" is his phrasing in the moment; the title keeps to "much of".

## Related claims
- **Note:** [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]] rests partly on the same kind of work in llm.c, such as a fused classifier that avoids materialising normalised logits ([[github-2024-05-03-llmc-state-of-the-union]] §intro (Single GPU training)); no relation is set, since that page is about measured speed, not why ([[youtube-2024-06-09-reproduce-gpt-2]] @2:04:42).
