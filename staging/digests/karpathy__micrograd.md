# Digest: micrograd README
- raw: raw/github/karpathy__micrograd.md · published: 2026-08-03 · medium: github · words: 476
- source slug: github-2026-08-03-micrograd-readme

## Source page
```
---
type: source
raw_path: raw/github/karpathy__micrograd.md
published: 2026-08-03
medium: github
summary: README of micrograd, his tiny scalar autograd engine and PyTorch-like neural-net library, with its demo, tests against PyTorch, and a pointer to microgpt as the advanced example.
url: https://github.com/karpathy/micrograd
title: micrograd README
---
# micrograd README
Raw: [[raw/github/karpathy__micrograd]] · Original: https://github.com/karpathy/micrograd

Dated by the README's commit (7bc720e), not by the repo's creation; the repo itself is older.

## Summary
The README describes micrograd as a tiny autograd engine that implements backpropagation, reverse-mode autodiff, over a dynamically built DAG, plus a small neural-net library on top with a PyTorch-like API, about 100 and 50 lines respectively (§intro). The graph works only on scalars, so each neuron is broken into its individual adds and multiplies, which he says is still enough to build deep nets for binary classification, and he calls it potentially useful for education (§intro). It installs with pip, and a demo notebook trains a 2-layer MLP binary classifier on the moon dataset with an SVM max-margin loss and SGD (§Installation, §Training a neural net). A new section points to microgpt as the advanced example: a full GPT-2-like transformer in pure, dependency-free Python, built on a more efficient and better version of this engine that stores local gradients at forward time, the complete algorithm in one file with everything else just efficiency (§Training a GPT). A notebook draws graphviz traces of data and gradients, and the unit tests use PyTorch as the reference for gradients (§Tracing / visualization, §Running tests).

## Key points
- What the repo is: scalar autograd engine plus PyTorch-like nn library, ~100 + ~50 lines, pip-installable, MIT → [[micrograd]]
- Reverse-mode autodiff over a dynamically built DAG of scalars → [[backpropagation]]
- microgpt as the advanced example, with a better engine → [[microgpt]]
- Complete algorithm in one file, everything else efficiency → [[microgpt-is-the-full-algorithm-everything-else-is-efficiency]]
- Tests check gradients against PyTorch → [[verify-gradients-against-pytorch]]
- Tiny, potentially educational → [[small-hackable-educational-code]]

## Fed pages
- [[micrograd]]
- [[backpropagation]]
- [[microgpt]]
- [[microgpt-is-the-full-algorithm-everything-else-is-efficiency]]
- [[verify-gradients-against-pytorch]]
- [[small-hackable-educational-code]]
```

## Candidates

### artifact: micrograd
- existing: yes (so far sourced only from the 2022 lecture and later mentions; this is the first README source)
- frontmatter: keep repo_url, language Python. `status`: the README carries no deprecation or archive notice, unlike nanoGPT's; the page currently says active rests only on his 2022 stated intent and "a later GitHub snapshot should decide". This snapshot gives no status statement either way; merge may keep `active` and replace that sentence with "the 2026-08-03 README carries no deprecation notice", without claiming more.
- statements (what it says the repo is):
  - A tiny autograd engine, "with a bite" (§intro)
  - It implements backpropagation (reverse-mode autodiff) over a dynamically built DAG, and a small neural-net library on top with a PyTorch-like API (§intro)
  - The engine is about 100 lines and the library about 50 (§intro); consistent with the lecture's ~150 total ([[youtube-2022-08-16-micrograd]] @07:35), against the ~200 in the 2024 post ([[x-2024-02-21-technical-accessibility]]); all are his approximations
  - The DAG operates only on scalar values, so each neuron is chopped into its individual adds and multiplies; this is still enough for entire deep nets doing binary classification, as the demo notebook shows (§intro)
  - He calls it potentially useful for educational purposes (§intro)
  - It installs with `pip install micrograd` (§Installation)
  - The README's example exercises many operations and prints forward values and gradients (§Example usage) — code not copied
  - `demo.ipynb` trains a 2-layer MLP binary classifier from `micrograd.nn`, with an SVM max-margin loss and SGD; two 16-node hidden layers give a decision boundary on the moon dataset (§Training a neural net)
  - `trace_graph.ipynb` draws graphviz visualisations showing each node's data and gradient, e.g. a 2-D neuron via `draw_dot` (§Tracing / visualization)
  - Unit tests require PyTorch as the reference for verifying gradients, run with pytest (§Running tests)
  - Licence MIT (§License)
- relation: the existing page's statements from the lecture (two files, Module/zero_grad, PyTorch test, demo.ipynb with max-margin loss) are consistent. The lecture's demo description adds batching, L2 and learning-rate decay ([[youtube-2022-08-16-micrograd]] @2:19:18–@2:20:23); this README mentions only max-margin loss and SGD. Not a conflict; cite each separately.

### artifact: microgpt
- existing: no (created from the microgpt digest, `blog-2026-02-12-microgpt`)
- statements:
  - The README points to microgpt as a more advanced example that trains and samples a full GPT-2-like transformer in pure, dependency-free Python (§Training a GPT)
  - It builds on a more efficient and better version of micrograd's engine, storing local gradients at forward time instead of per-op backward closures (§Training a GPT)
  - It links the explainer post for a walkthrough (§Training a GPT)
- note: the forward-time local gradients match the post's `Value` design (children and local gradients recorded at each operation, [[blog-2026-02-12-microgpt]] §Autograd); the "better version" judgement is the README's, not the post's.

### claim: microgpt-is-the-full-algorithm-everything-else-is-efficiency
- existing: no (proposed in the microgpt digest)
- second source: the README calls microgpt the complete algorithm in a single file, with everything else just efficiency (§Training a GPT). Add to `sources`. Same claim, no new relation.

### topic: backpropagation
- existing: yes
- aliases to add: reverse-mode autodiff, DAG
- statements:
  - The README defines what micrograd implements as backpropagation, i.e. reverse-mode autodiff, over a dynamically built DAG (§intro)

### method: verify-gradients-against-pytorch
- existing: yes
- statements:
  - micrograd's unit tests use PyTorch as the reference for verifying the calculated gradients (§Running tests)

### method: small-hackable-educational-code
- existing: yes
- statements:
  - Both parts are tiny, about 100 and 50 lines, and he calls it potentially useful for education (§intro)
- merge may drop this if the micrograd page carries it already; keep only if a sentence on the method page cites it.

## Quotes
- "A tiny Autograd engine (with a bite! :))." (§intro)
- "Implements backpropagation (reverse-mode autodiff) over a dynamically built DAG" (§intro)
- "The DAG only operates over scalar values" (§intro)
- "Potentially useful for educational purposes." (§intro)
- "is the complete algorithm in a single file" (§Training a GPT)
- "everything else is just efficiency" (§Training a GPT)

## Notes for merge
- **Date:** 2026-08-03 is the commit date of 7bc720e951fe422b8f8814aa5aa1b64121d26b4c, not the repo's creation; the existing page says the repo was released about two years before the 2022 lecture ([[youtube-2022-08-16-micrograd]]). Do not write when the "Training a GPT" section was added or any order relative to the microgpt post; give both dates.
- First snapshot, so the file is `karpathy__micrograd.md` (no @commit suffix).
- **Code is linked, not copied.** The README's example and tracing snippets are not to be quoted; the printed numbers in the example are code output, leave them out.
- Headings are H3 (`### Installation` etc.); text before the first is §intro. The puppy image alt text "awww" is decoration.
- "an 2-layer neural network" typo in §Training a neural net; paraphrased, not quoted.
- The README says "GPT-2-like transformer"; the post says "GPT-2-like neural network architecture". Same thing; do not upgrade either to "GPT-2".
- The README itself is short and descriptive; no new claim of its own beyond restating the microgpt efficiency line.
