---
type: claim
stated_on: 2022-08-16
confidence: stated
sources: ["[[youtube-2022-08-16-micrograd]]"]
topic: "[[backpropagation]]"
supports: ["[[neural-networks-are-just-mathematical-expressions]]"]
---
# micrograd is all you need to train neural nets; everything else is efficiency
> "micrograd is what you need to train your networks" — [[youtube-2022-08-16-micrograd]] @06:30

## Context
Tensors package scalars into arrays to exploit parallelism; he says none of the math changes and that this is done purely for efficiency ([[youtube-2022-08-16-micrograd]] @05:56, @06:30). He also says it is not pedagogically useful to deal with tensors from scratch ([[youtube-2022-08-16-micrograd]] @06:30). About 150 lines of code is all you need to understand neural-net training; there is a lot to efficiency, but that is all that is fundamentally happening ([[youtube-2022-08-16-micrograd]] @07:35).

The granularity of operations is up to you: you can implement backward for a single plus or for a composite like tanh, as long as you have a forward pass and can write the local derivative, which he shows by building tanh atomically and then from exp with identical gradients ([[youtube-2022-08-16-micrograd]] @58:24, @1:37:47, @1:38:22, @1:38:54). PyTorch's `torch.autograd.Function` registration is the same idea ([[youtube-2022-08-16-micrograd]] @2:23:43, @2:24:15).

By contrast he searched PyTorch for tanh, got 2,800 results in 406 files, and spent 15 minutes before finding the backward kernel; he says these libraries are complex and meant to be used, not really inspected ([[youtube-2022-08-16-micrograd]] @2:21:33, @2:22:07). Finding the real code for what micrograd does in a few lines is difficult ([[youtube-2022-08-16-micrograd]] @2:23:11).

## Related claims
- Supports [[neural-networks-are-just-mathematical-expressions]]: if a net is an expression over scalars, a scalar autograd engine is enough to train it ([[youtube-2022-08-16-micrograd]] @04:19, @06:30).
