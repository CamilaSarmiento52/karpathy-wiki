---
type: topic
aliases: [PyTorch, tensors, view, nn.Module, torch.cat]
first_seen: 2022-08-16
last_updated: 2022-09-12
sources: ["[[youtube-2022-08-16-micrograd]]", "[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]"]
related: ["[[micrograd]]", "[[verify-gradients-against-pytorch]]", "[[backpropagation]]"]
---
# PyTorch
micrograd is roughly modelled on PyTorch, which he says is what you would use in production ([[youtube-2022-08-16-micrograd]] @1:39:28).

## What he says
In PyTorch everything is a tensor, an n-dimensional array of scalars; he makes single-element tensors, casts to double to match Python's float64, and sets `requires_grad=True` because leaf tensors default to no gradient for efficiency ([[youtube-2022-08-16-micrograd]] @1:40:01, @1:41:08, @1:41:43). Tensors have `.data`, `.grad` and `.backward()` like micrograd's `Value`; `.item()` strips the single element out ([[youtube-2022-08-16-micrograd]] @1:42:15, @1:43:20). micrograd's `Neuron`, `Layer`, `MLP`, `parameters()`, `Module` and `zero_grad` deliberately match the nn.Module API ([[youtube-2022-08-16-micrograd]] @1:44:26, @1:58:14, @2:18:12).

He spent about 15 minutes and could not find tanh's backward in PyTorch's source, where a search gave 2,800 results in 406 files; it lives in a CPU kernel and a CUDA kernel inside binary-ops code ([[youtube-2022-08-16-micrograd]] @2:21:33, @2:22:07, @2:22:40, @2:23:11). He says such libraries are meant to be used rather than inspected ([[youtube-2022-08-16-micrograd]] @2:22:07). New ops can be registered as a `torch.autograd.Function` subclass with a forward and a backward, becoming a Lego block in the larger library ([[youtube-2022-08-16-micrograd]] @2:23:43, @2:24:15).

Tensor basics from the first makemore lecture: `torch.zeros((3,5))` defaults to float32, counts use `dtype=torch.int32`, and indexing is zero-based, as in `a[1,3]` ([[youtube-2022-09-07-makemore-1-bigram]] @13:48, @14:20). Indexing a tensor returns a tensor; `.item()` pops out the Python number ([[youtube-2022-09-07-makemore-1-bigram]] @20:23, @30:18). `N[0, :]` and `N[0]` both grab a row ([[youtube-2022-09-07-makemore-1-bigram]] @24:48, @25:21). `torch.tensor` infers its dtype while `torch.Tensor` returns a float tensor; he recommends the lowercase one and says the docs are unclear ([[youtube-2022-09-07-makemore-1-bigram]] @1:07:47, @1:08:55, @1:09:28). He wants viewers to get used to reading documentation and Q&A threads because some of this is not well documented ([[youtube-2022-09-07-makemore-1-bigram]] @1:09:28). `torch.randn` draws from a normal distribution, with most values near zero and few above 3 in magnitude ([[youtube-2022-09-07-makemore-1-bigram]] @1:13:53, @1:14:27).

In the second makemore lecture he says Torch is a very large library and there are usually many ways to implement something, some faster or shorter ([[youtube-2022-09-12-makemore-2-mlp]] @19:58). `torch.cat` concatenates a sequence of tensors along a dimension; indexing each position by hand does not generalise to other block sizes, while `torch.unbind` returns the slices along a dimension and makes the concatenation generalise ([[youtube-2022-09-12-makemore-2-mlp]] @20:31, @22:10, @22:43). A tensor's storage is always a one-dimensional vector; `.view` changes storage offset, strides and shape, so no memory is copied, moved or created, and passing -1 lets PyTorch infer a dimension ([[youtube-2022-09-12-makemore-2-mlp]] @24:24, @24:57, @27:10). He points to a blog post on PyTorch internals and says he may make a video on tensor internals ([[youtube-2022-09-12-makemore-2-mlp]] @24:57, @25:29). Concatenation, by contrast, creates a whole new tensor with new storage, so it is less efficient than a view ([[youtube-2022-09-12-makemore-2-mlp]] @27:10, @27:43). PyTorch indexing is flexible: a tensor can be indexed with a list, a tensor or a multi-dimensional tensor of integers, so `C[X]` embeds a 32-by-3 array of indices at once ([[youtube-2022-09-12-makemore-2-mlp]] @16:34, @17:07, @18:16).

## Claims
- [[micrograd-is-all-you-need-everything-else-is-efficiency]]
- [[treat-broadcasting-with-respect]]

## Related
- [[micrograd]] — the toy library modelled on it
- [[verify-gradients-against-pytorch]]
- [[backpropagation]]
- [[broadcasting]]
- [[check-shapes-and-broadcasting]]
- [[embeddings]] — indexing the lookup table
