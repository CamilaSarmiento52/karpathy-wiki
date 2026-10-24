# Digest: llama2.c README
- raw: raw/github/karpathy__llama2.c.md · published: 2024-05-29 · medium: github · words: 5037
- source slug: github-2024-05-29-llama2c-readme

## Source page
```
---
type: source
raw_path: raw/github/karpathy__llama2.c.md
published: 2024-05-29
medium: github
summary: "README of llama2.c, his minimal train-in-PyTorch, inference-in-one-C-file repo for the Llama 2 architecture: tiny TinyStories models, Meta checkpoints, int8 quantization, custom tokenizers, a training guide and a contributing policy that puts simplicity first."
url: https://github.com/karpathy/llama2.c
title: llama2.c README
---
# llama2.c README
Raw: [[raw/github/karpathy__llama2.c]] · Original: https://github.com/karpathy/llama2.c

Dated by the README's last commit (350e04f); much of the text reads as written earlier ("started recently").

## Summary
llama2.c trains the Llama 2 architecture in PyTorch and runs inference with one simple, roughly 700-line C file, a "fullstack" solution focused on minimalism and simplicity; he argues very small LLMs can perform surprisingly well in a narrow enough domain, citing TinyStories (§intro). It began as a weekend project in which he adapted nanoGPT to Llama 2 and wrote the C inference engine, choosing, unlike llama.cpp, to hard-code the architecture in pure C with no dependencies (§intro). The README walks through running his TinyStories models, loading Meta's Llama 2 and Code Llama checkpoints, int8 quantization that cut checkpoint size 4X and ran 3X faster, training your own model with a short hyperparameter guide, and training a custom tokenizer (§feel the magic, §Meta's Llama 2 models, §int8 quantization, §training, §custom tokenizers). He expects strong interest in custom micro-LLMs deployed near the edge and wants the repo to stay the simplest, most hackable reference implementation that people fork, not a full-featured or maximally efficient framework (§contributing).

## Key points
- The repo, its models, platforms, tests and forks → [[llama2c]]
- Started from nanoGPT, retuned to Llama 2 → [[nanogpt]]
- Very small LLMs can be strong in a narrow domain → [[small-llms-can-be-strong-in-narrow-domains]]
- He expects a lot of interest in custom micro-LLMs at the edge → [[he-expects-demand-for-custom-micro-llms-at-the-edge]]
- How Llama differs from GPT-1/2: RoPE, SwiGLU, RMSNorm, no biases, optional multiquery → [[transformer-architecture]]
- int8 weight and activation quantization, and why RMSNorm parameters stay float32 → [[quantization]]
- Temperature versus top-p, and his recommended defaults → [[sampling]]
- Small custom vocabularies for small applications → [[tokenization]]
- His brief training guide: size, context, batch, accumulation, learning rate, iterations → [[choose-training-hyperparameters]]
- Dropout 0.1 usually helps a bit at medium size → [[regularization]]
- Simple, readable, portable reference code you fork; what PRs he will merge → [[small-hackable-educational-code]]
- C and Python forward passes checked against known-good output → [[verify-against-a-reference-implementation]]

## Fed pages
- [[llama2c]]
- [[nanogpt]]
- [[small-llms-can-be-strong-in-narrow-domains]]
- [[he-expects-demand-for-custom-micro-llms-at-the-edge]]
- [[transformer-architecture]]
- [[quantization]]
- [[sampling]]
- [[tokenization]]
- [[choose-training-hyperparameters]]
- [[regularization]]
- [[small-hackable-educational-code]]
- [[verify-against-a-reference-implementation]]
```

## Candidates
### artifact: llama2c
- existing: no
- aliases: [llama2.c, baby Llama 2, tinyllamas]
- frontmatter: repo_url https://github.com/karpathy/llama2.c · language C (training in Python/PyTorch) · status active
- statements:
  - Train the Llama 2 architecture in PyTorch, then run inference with one simple 700-line C file, `run.c`; a "fullstack" train plus inference solution focused on minimalism and simplicity (§intro)
  - Because the architecture is identical it can load Meta's Llama 2 models, but only in fp32, so models above 7B are not practical (§intro, §Meta's Llama 2 models)
  - Started as a fun weekend project: he took nanoGPT, tuned it to the Llama 2 architecture instead of GPT-2, and the core work was the C inference engine; inspired by llama.cpp, but he wanted something super simple, minimal and educational, so he hard-coded the architecture in one dependency-free C file (§intro)
  - His 15M TinyStories model runs at about 110 tokens/s on his M1 MacBook Air; a 42M model still samples at interactive rates with more coherent stories (§feel the magic)
  - He trained a small TinyStories model series (260K, 15M, 42M, 110M) on 4X A100 40GB in a few hours each, the 110M in about 24 hours, hosted as tinyllamas (§models)
  - Llama 2 7B exported to a 26GB float32 file ran at about 4 tokens/s with OpenMP on a 96-thread cloud CPU; he would not run anything above 7B because 13B+ hits an integer overflow in pointer arithmetic and float32 is too slow (§Meta's Llama 2 models)
  - Chat mode (`-m chat`) works with Llama Chat; Code Llama support is incomplete and slightly buggy because some hyperparameters such as the RoPE constant changed (§Meta's Llama 2 models)
  - Hugging Face models with the Llama 2 architecture can be exported with `--hf` (§huggingface models)
  - Performance: `-O3` by default, `make runfast` (-Ofast) was fastest on his M1, `-march=native`, clang, and OpenMP; more threads is not always better, usually U-shaped, and with SMT use physical cores (§performance)
  - Builds on Windows, CentOS 7, Amazon Linux and Mac (§platforms)
  - Many community ports in other languages are listed (Rust, Go, Zig, Java, JavaScript and more) (§notable forks)
  - Todos at snapshot time include a CUDA `run.cu`, more C tests, a KV-cached PyTorch Engine, easier datasets, and LoRA finetuning (§unsorted todos)
- relation: links to [[nanogpt]] (its starting point).

### artifact: nanogpt
- existing: yes
- statements:
  - llama2.c started from nanoGPT, tuned to implement Llama 2 instead of GPT-2 (§intro)

### claim: small-llms-can-be-strong-in-narrow-domains
- existing: no
- title: Very small LLMs can perform surprisingly well if the domain is narrow enough
- confidence: stated
- stated_on: 2024-05-29 (README commit date)
- quote: "very small LLMs can have surprisingly strong performance" (§intro)
- context: he says you might think you need many-billion-parameter LLMs to do anything useful, but very small ones can be strong if the domain is narrow enough, citing the TinyStories paper as reference (§intro). His own 15M–110M TinyStories models are the repo's illustration (§feel the magic, §models). Keep "narrow enough" in the title; he does not say small models are generally strong.
- relation to existing claims: none.

### claim: he-expects-demand-for-custom-micro-llms-at-the-edge
- existing: no
- title: He expects a lot of interest in training custom micro-LLMs and deploying them near the edge
- confidence: stated
- stated_on: 2024-05-29
- quote: "there will be a lot of interest in training or finetuning custom micro-LLMs" (§contributing)
- context: "micro-LLMs" means about 100M to 1B parameters, up to about 10B, across many applications, deployed in edge-adjacent environments such as MCUs, phones, web browsers and laptops; he wants llama2.c to be the simplest, most hackable repo for that workflow, and expects most applications to fork it (§contributing). It is a prediction introduced with "I think".
- relation to existing claims: none. **Note:** [[llms-as-operating-systems]] and [[software-3-0]] are about large hosted models; no link proposed.

### topic: transformer-architecture
- existing: yes
- aliases to add: Llama, Llama 2, RoPE, SwiGLU, RMSNorm, multiquery attention
- statements:
  - The 110M model is GPT-1 sized and matches GPT-2 small except for a 1024 rather than 2048 max context (as he states it) (§models)
  - The only notable changes from GPT-1/2 in Llama: RoPE relative positional embeddings instead of absolute learned ones, SwiGLU in the MLP, RMSNorm instead of LayerNorm, bias=False on all Linear layers, and optional multiquery attention (§models)

### topic: quantization
- existing: no
- aliases: [int8 quantization, Q8_0, model quantization]
- statements:
  - The default `run.c` keeps the whole forward pass in fp32, easy to understand as reference code but with large checkpoints (4 bytes per weight) and a relatively slow forward pass (§int8 quantization)
  - Quantizing parameters to lower precision is a very common inference optimization, trading a little correctness for smaller checkpoints and faster forward passes (§int8 quantization)
  - Empirically LLMs tolerate precisions as low as 4-bit or lower; he uses int8 as a "safe" setting (§int8 quantization)
  - Only weights in matmuls are quantized; other parameters, especially RMSNorm scale and bias, stay float32 because those layers are very sensitive (§int8 quantization)
  - Quantizing weights only, then dequantizing for float32 inference, is fine if you only want smaller checkpoints; llama2.c also quantizes activations at runtime so matmuls run in pure integer arithmetic, which is where the speedups come from; the scheme is Q8_0, symmetric in [-127, 127] (§int8 quantization)
  - On Llama 2 7B: 26GB fp32 versus 6.7GB int8, 4.6 versus 14 tokens/s, a 3X speedup and 4X smaller checkpoint, at silently very slightly lower quality (§int8 quantization)

### topic: sampling
- existing: partly (alias "sampling" sits on [[character-level-language-modeling]], whose sampling material is the bigram loop)
- aliases: [temperature, top-p, nucleus sampling]
- statements:
  - His recommendation for about best results is temperature 1.0 with top-p 0.9 (§feel the magic)
  - Top-p keeps tokens with tiny probabilities from being sampled, so you cannot get "unlucky" and are less likely to go off the rails afterwards (§feel the magic)
  - To control diversity, vary either temperature (top-p off) or top-p (temperature 1), but not both (§feel the magic)
- note: merge may fold this into [[character-level-language-modeling]] rather than create a page; the bigram page is character-level, this is LLM sampling, so a separate coarse `sampling` topic seems justified.

### topic: tokenization
- existing: yes
- statements:
  - The default is the Llama 2 tokenizer with 32,000 tokens; for many small "boutique" LLMs that vocabulary may be overkill and you may be better off training your own (§custom tokenizers)
  - A smaller vocabulary gives fewer parameters (smaller embedding table), faster inference (fewer tokens to predict) and possibly shorter sequences (better compression on your data) (§custom tokenizers)
  - `train_vocab` uses sentencepiece BPE, starting from raw UTF-8 bytes and iteratively merging the most common consecutive pairs; he tried to reproduce the settings he thinks Meta used (§custom tokenizers)
  - A 4096-token vocabulary trained on TinyStories gives about the same sequence length per example as the 32,000-token Llama 2 tokenizer (§custom tokenizers)
  - Running inference with the wrong tokenizer yields good integer sequences translated through a different vocabulary, which looks like gibberish (§custom tokenizers)

### method: choose-training-hyperparameters
- existing: no (closest: [[learning-rate-sweep]], [[gradient-descent]])
- aliases: [brief training guide, set Transformer hyperparameters]
- steps (all §training):
  1. Scale dim, n_layers and n_heads together, using the table at the end of the Chinchilla paper and inter/extrapolating
  2. Set max context length to the number of tokens that matter for predicting the next one (Llama 2 uses 2048)
  3. Aim for a total batch size per update of about 100K tokens for medium applications (lower for tiny, ~0.5M or more for large GPT/Llama training)
  4. Max out batch_size to what memory allows, then raise gradient_accumulation_steps to reach the total
  5. Tune the learning rate as high as training allows: small nets can take 1e-3 or more, large nets need lower; 3e-4 is safe for medium but may be too low for small nets
  6. Set max_iters for training length; play with settings
- statements:
  - He mostly only tunes these parameters and leaves the rest unchanged (§training)
  - His 110M run, which he does not think is anywhere near optimal: dim 768, 12 layers, 12 heads (64 channels each), seq len 1024, batch 16, grad accumulation 8 for 131,072 tokens per update, LR 4e-4 (probably a little low), max_iters 200K (probably a bit high), dropout 0.1, DDP on 4 GPUs for about a day (§training)
- note: could instead be a section of [[gradient-descent]] (learning rate) plus [[learning-rate-sweep]]; I propose a method because it is an ordered how-to.

### topic: regularization
- existing: yes
- statements:
  - In his 110M run he used dropout 0.1, saying it usually helps a bit at medium size (§training)

### method: small-hackable-educational-code
- existing: yes
- statements:
  - He wanted something super simple, minimal and educational, so he hard-coded the Llama 2 architecture and wrote one pure-C inference file with no dependencies (§intro)
  - The goal is the simplest, smallest, most hackable repo for training and inference, not a complex framework with a thousand knobs across hundreds of files; most applications should fork and hack it (§contributing)
  - It cares about efficiency but not at the cost of simplicity, readability or portability; it should not be full-featured, take 100 options, or be the most efficient; people who care most about deployment efficiency should use llama.cpp (§contributing)
  - Readable training code (2 .py files) and about 500 lines of C inference are why people come; he wants it to stay a simplest "reference implementation" (§contributing)
  - Merge policy: small, localized, broadly applicable, clean changes (a loop reorder for locality, a one-line OpenMP pragma) are instant merges; many `#ifdef`s, platform-specific code, or hundreds of scenario-specific lines in `run.c` are poor fits better suited to forks (§contributing)
  - The fp32 forward pass is kept as the easy-to-understand reference, with quantization in a separate file, `runq.c` (§int8 quantization)
- relation: the method's step 5 ("know the limit", minGPT needed teeth, [[github-2023-01-08-mingpt-readme]] §intro) is the opposite pressure; llama2.c explicitly chooses simplicity over efficiency and sends efficiency seekers elsewhere. Not a contradiction (different repos, different goals).

### method: verify-against-a-reference-implementation
- existing: no (proposed in the minbpe digest)
- statements:
  - `test_all.py` forwards the model in C and Python for 200 steps and checks against known-good expected output, using the tiny 260K model (§tests)
  - The PyTorch `sample.py` on the same checkpoint gives the same results as `run.c` (§training)

## Quotes
- "with focus on minimalism and simplicity" (§intro)
- "very small LLMs can have surprisingly strong performance" (§intro)
- "this repo started recently as a fun weekend project" (§intro)
- "I wanted something super simple, minimal, and educational" (§intro)
- "Intuitively, top-p ensures that tokens with tiny probabilities do not get sampled" (§feel the magic)
- "Empirically, LLMs can tolerate precisions as low as 4-bit (or even lower)" (§int8 quantization)
- "because these layers are very sensitive" (§int8 quantization)
- "So we achieved a 3X speedup while reducing the checkpoint size by 4X." (§int8 quantization)
- "I mostly only ever tune these parameters and leave most of the others unchanged." (§training)
- "Dropout 0.1, as that usually helps a bit at medium size." (§training)
- "you might be much better off training your own tokenizers" (§custom tokenizers)
- "But more is not always better, usually this is a bit U shaped." (§performance)
- "there will be a lot of interest in training or finetuning custom micro-LLMs" (§contributing)
- "still cares about efficiency, but not at the cost of simplicity" (§contributing)
- "It shouldn't be full-featured." (§contributing)

## Notes for merge
- Locations: the README's first heading is `## llama2.c` (the repo title); I cite its text as `§intro`, as for other READMEs. Other headings are lowercase in the raw (`§feel the magic`, `§int8 quantization`, `§training`, `§custom tokenizers`, `§performance`, `§contributing`, …); `§Meta's Llama 2 models` keeps its capitals.
- Snapshot date versus writing date: the commit is 2024-05-29, but the text says the repo "started recently" and "work on model quantization is currently ongoing" (§intro) while also documenting `runq.c` (§int8 quantization). The intro is older than parts of the body. Do not date the weekend project from this file.
- Line counts disagree within the README: `run.c` is "700-line" in §intro and the inference code "500 lines of C" in §contributing. Keep each with its section.
- §models: the 110M model is GPT-2 small "except the max context length is only 1024 instead of 2048". The sentence does not say which model has 2048 (Llama 2 uses 2048 per §training). Paraphrase only as written, or leave the context comparison out; do not resolve it from outside knowledge.
- "It has been reported that despite efforts." (§Meta's Llama 2 models) is a broken sentence in the raw; do not paraphrase it. "integer flow" there means integer overflow; paraphrase as overflow and flag if unsure.
- Raw typos: "inscrutible", "efficieny", "Lllama"; avoid quoting them.
- The base-model sample (a Llama 2 7B output about cobalt oxide documents) and his shrug "base models..." (§Meta's Llama 2 models) loosely echo [[pretraining-gives-a-document-completer]], but he does not state the claim here; at most a **Note:** connection, no `supports`.
- The TinyStories reference is a paper's result he leans on; the claim is his ("in fact"), but say he cites TinyStories.
- Long sample stories and the forks list are not his writing (forks are others' projects); summarise, do not quote.
- Lambda Labs provided the training box (§ack); the Zero to Hero Discord is reused (§discord). Mentions only.
