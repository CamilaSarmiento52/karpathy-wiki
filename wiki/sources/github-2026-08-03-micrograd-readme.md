---
type: source
raw_path: raw/github/karpathy__micrograd.md
published: 2026-08-03
medium: github
summary: README of micrograd, his tiny scalar autograd engine and PyTorch-like neural-net library, with its demo, tests against PyTorch, and a pointer to microgpt as the advanced example built on a better version of the engine.
url: https://github.com/karpathy/micrograd
title: micrograd README
---
# micrograd README
Raw: [[raw/github/karpathy__micrograd]] · Original: https://github.com/karpathy/micrograd

The first README snapshot of micrograd in this wiki, dated by the commit it was read at (`7bc720e`), not by the repo's creation; the repo itself is older. Nothing here says when the "Training a GPT" section was added. Code snippets and their printed numbers are not reproduced.

## Summary
The README describes micrograd as a tiny autograd engine that implements backpropagation, reverse-mode autodiff, over a dynamically built DAG, with a small neural-net library on top with a PyTorch-like API, about 100 and 50 lines respectively (§intro). The graph works only on scalars, so each neuron is chopped into its individual adds and multiplies, which is still enough for entire deep nets doing binary classification; he calls it potentially useful for educational purposes (§intro). It installs with pip, and a demo notebook trains a 2-layer MLP binary classifier on the moon dataset with an SVM max-margin loss and SGD (§Installation, §Training a neural net). A section points to microgpt as a more advanced example: a full GPT-2-like transformer in pure, dependency-free Python, built on a more efficient and better version of this engine that stores local gradients at forward time, and the complete algorithm in a single file, everything else being just efficiency (§Training a GPT). A notebook draws graphviz traces of each node's data and gradient, and the unit tests use PyTorch as the reference for gradients (§Tracing / visualization, §Running tests).

## Key points
- What the repo is: scalar autograd engine plus PyTorch-like nn library, ~100 + ~50 lines, pip-installable, MIT → [[micrograd]]
- Reverse-mode autodiff over a dynamically built DAG of scalars → [[backpropagation]]
- microgpt as the advanced example, on a better engine → [[microgpt]]
- The complete algorithm in one file, everything else efficiency → [[microgpt-is-the-full-algorithm-everything-else-is-efficiency]]
- Tests check gradients against PyTorch → [[verify-gradients-against-pytorch]]

## Fed pages
- [[micrograd]]
- [[backpropagation]]
- [[microgpt]]
- [[microgpt-is-the-full-algorithm-everything-else-is-efficiency]]
- [[verify-gradients-against-pytorch]]
