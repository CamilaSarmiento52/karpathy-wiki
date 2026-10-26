---
type: source
raw_path: raw/blog/microgpt.md
published: 2026-02-12
medium: blog
summary: "His guide to microgpt, a 200-line, dependency-free Python file that trains and samples a small GPT on a names dataset, walked through section by section, with what changes at production scale."
url: https://karpathy.github.io/2026/02/12/microgpt/
title: microgpt
---
# microgpt
Raw: [[raw/blog/microgpt]] · Original: https://karpathy.github.io/2026/02/12/microgpt/

Text before `## Dataset` is cited `§intro`; FAQ questions are plain lines, cited `§FAQ`. Code is linked, not copied: the script is a GitHub gist (https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95) and the step-by-step versions a second gist, build_microgpt.py (https://gist.github.com/karpathy/561ac2de12a47cc06a23691e1be9543a). The post never mentions nanochat. Two timing figures are kept apart: about a minute for the whole script on his MacBook (§Run it) and seconds for a single training step (§FAQ).

## Summary
He calls microgpt an art project: one file of 200 lines of pure Python with no dependencies that trains and runs a GPT, containing dataset, tokenizer, autograd engine, a GPT-2-like network, the Adam optimizer, and the training and inference loops; he says everything else is just efficiency, that he cannot simplify it further, and that it is the culmination of micrograd, makemore, nanoGPT and a decade-long effort to reduce LLMs to their essentials (§intro). The post steps through the code: a 32,000-name dataset where each name is a document, a character tokenizer with a BOS delimiter token, a scalar `Value` autograd class built from local gradients and the chain rule, 4,192 parameters, and a one-layer GPT-2-style model with RMSNorm, no biases, ReLU and an explicit KV cache that is backpropagated through during training (§Dataset, §Tokenizer, §Autograd, §Parameters, §Architecture). Training runs 1,000 single-document steps of cross-entropy loss and Adam with linear learning-rate decay, taking the loss from about 3.3 to about 2.37, then samples new names with a temperature (§Training loop, §Inference, §Run it). He suggests a progression of six files that add one component at a time, kept as revisions of a gist (§Progression). A closing section lists what changes on the way to a production LLM, data, subword tokenizers, tensors on GPUs, wider and deeper models with newer blocks, large-batch training, tuned optimisation, post-training and serving, none of which, he says, alters the core algorithm (§Real stuff), and an FAQ relates microgpt to ChatGPT and to hallucinations (§FAQ).

## Key points
- What microgpt is, what it contains, how it is published and run → [[microgpt]]
- 200 lines holding the full algorithm; everything else is efficiency → [[microgpt-is-the-full-algorithm-everything-else-is-efficiency]], [[micrograd-is-all-you-need-everything-else-is-efficiency]]
- Built on a scalar autograd engine like micrograd's; he points to the micrograd video → [[micrograd]], [[backpropagation]]
- Local gradients as lego blocks, chain rule, gradient accumulation on branches, same algorithm as PyTorch on scalars → [[backpropagation]]
- GPT-2-like block with RMSNorm, no biases, ReLU; attention as communication, MLP as computation, residuals; what production models change → [[transformer-architecture]]
- Q/K/V intuition, KV cache present even in training → [[self-attention]]
- Attention as a token communication mechanism, restated → [[attention-is-a-communication-mechanism]]
- Character tokenizer with BOS; production BPE with ~100K tokens → [[tokenization]]
- Cross-entropy as surprise; Adam with bias correction and linear decay → [[loss-functions]], [[gradient-descent]]
- Temperature sampling until BOS → [[sampling-from-language-models]]
- Base model as a document completer; SFT and RL → [[pretraining-gives-a-document-completer]], [[pretraining-and-finetuning]]
- Hallucinated names and false facts as plausible completions → [[llm-hallucinations]]
- Names dataset from makemore, generating new name-like documents → [[character-level-language-modeling]], [[makemore]]
- Named among the projects it culminates → [[nanogpt]]
- One dependency-free file that breaks across three columns → [[small-hackable-educational-code]]
- Six-step progression, one component at a time, in gist revisions → [[spelled-out-build-from-scratch]]
- Evidence for the simplicity claims → [[gpt-is-not-a-complicated-model]], [[neural-net-training-should-not-be-complicated]]

## Fed pages
- [[microgpt]]
- [[microgpt-is-the-full-algorithm-everything-else-is-efficiency]]
- [[micrograd]]
- [[makemore]]
- [[nanogpt]]
- [[backpropagation]]
- [[transformer-architecture]]
- [[self-attention]]
- [[attention-is-a-communication-mechanism]]
- [[tokenization]]
- [[loss-functions]]
- [[gradient-descent]]
- [[sampling-from-language-models]]
- [[pretraining-and-finetuning]]
- [[pretraining-gives-a-document-completer]]
- [[llm-hallucinations]]
- [[character-level-language-modeling]]
- [[small-hackable-educational-code]]
- [[spelled-out-build-from-scratch]]
- [[gpt-is-not-a-complicated-model]]
- [[neural-net-training-should-not-be-complicated]]
- [[micrograd-is-all-you-need-everything-else-is-efficiency]]
- [[how-he-explains]]
- [[start-from-the-simplest-thing-that-shows-it]]
