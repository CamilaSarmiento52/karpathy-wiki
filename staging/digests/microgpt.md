# Digest: microgpt
- raw: raw/blog/microgpt.md · published: 2026-02-12 · medium: blog · words: 5524
- source slug: blog-2026-02-12-microgpt

## Source page
```
---
type: source
raw_path: raw/blog/microgpt.md
published: 2026-02-12
medium: blog
summary: His guide to microgpt, a 200-line, dependency-free Python file that trains and samples a small GPT on a names dataset, walked through section by section, with what changes at production scale.
url: https://karpathy.github.io/2026/02/12/microgpt/
title: microgpt
---
# microgpt
Raw: [[raw/blog/microgpt]] · Original: https://karpathy.github.io/2026/02/12/microgpt/

Code is linked, not copied: the script is a GitHub gist (https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95); the step-by-step versions are a second gist, build_microgpt.py (https://gist.github.com/karpathy/561ac2de12a47cc06a23691e1be9543a).

## Summary
He calls microgpt an art project: one file of 200 lines of pure Python with no dependencies that trains and runs a GPT, containing dataset, tokenizer, autograd engine, a GPT-2-like network, the Adam optimizer, and the training and inference loops; he says everything else is just efficiency, that he cannot simplify it further, and that it is the culmination of micrograd, makemore, nanoGPT and a decade-long effort to reduce LLMs to their essentials (§intro). The post steps through the code: a 32,000-name dataset where each name is a document, a character tokenizer with a BOS delimiter token, a scalar `Value` autograd class built from local gradients and the chain rule, 4,192 parameters, and a one-layer GPT-2-style model with RMSNorm, no biases, ReLU and an explicit KV cache that is backpropagated through during training (§Dataset, §Tokenizer, §Autograd, §Parameters, §Architecture). Training runs 1,000 single-document steps of cross-entropy loss and Adam with linear learning-rate decay, taking the loss from about 3.3 to about 2.37, then samples new names with a temperature (§Training loop, §Inference, §Run it). He suggests a progression of six files that add one component at a time, kept as revisions of a gist (§Progression). A closing section lists what changes on the way to a production LLM, data, subword tokenizers, tensors on GPUs, wider and deeper models with newer blocks, large-batch training, tuned optimisation, post-training and serving, none of which, he says, alters the core algorithm (§Real stuff), and an FAQ relates microgpt to ChatGPT and to hallucinations (§FAQ).

## Key points
- What microgpt is, what it contains, how it is published and run → [[microgpt]]
- 200 lines holding the full algorithm; everything else is efficiency → [[microgpt-is-the-full-algorithm-everything-else-is-efficiency]]
- Built on a scalar autograd engine like micrograd's; he points to the micrograd video for it → [[micrograd]], [[backpropagation]]
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
- One dependency-free file that breaks across three columns → [[small-hackable-educational-code]]
- Six-step progression, one component at a time, in gist revisions → [[spelled-out-build-from-scratch]]
- Further support for simplicity claims → [[gpt-is-not-a-complicated-model]], [[neural-net-training-should-not-be-complicated]], [[micrograd-is-all-you-need-everything-else-is-efficiency]]

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
```

## Candidates

### artifact: microgpt
- existing: no (new slug, as instructed)
- aliases: [microgpt, microgpt.py, build_microgpt]
- frontmatter: repo_url https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95 (a gist, not a repo) · language Python · status active (the post gives no status; nothing says otherwise)
- statements:
  - He calls it his new art project: a single file of 200 lines of pure Python with no dependencies that trains and runs inference on a GPT (§intro)
  - The file holds dataset, tokenizer, autograd engine, a GPT-2-like architecture, the Adam optimizer, the training loop and the inference loop; he says everything else is just efficiency and he cannot simplify it further (§intro)
  - He calls it the culmination of multiple projects, naming micrograd, makemore and nanogpt, and of a decade-long obsession to simplify LLMs to their bare essentials; he thinks it is beautiful and notes it breaks across three columns (§intro)
  - It is published as a GitHub gist, as a web page at karpathy.ai/microgpt.html, as a Google Colab notebook, and as a triptych print on his art store (§intro)
  - The default dataset is about 32,000 names from the makemore repo, one per line, each name a document; the run reports 32,033 docs (§Dataset, §Run it)
  - The model is one layer, 16-dimensional embeddings, 4 heads, block size 16, with 4,192 parameters; he contrasts 1.6 billion for GPT-2 and hundreds of billions for modern LLMs (§Parameters)
  - It follows GPT-2 with three simplifications: RMSNorm instead of LayerNorm, no biases, ReLU instead of GeLU (§Architecture)
  - It processes one token at a time with no batch dimension, so it builds the KV cache explicitly (§Architecture)
  - Training is 1,000 steps, one document per step; loss falls from about 3.3, the random-guess value for 27 tokens, to about 2.37 (§Training loop)
  - It needs only Python, no pip install, and takes about a minute on his MacBook (§Run it)
  - Inference samples 20 new names at temperature 0.5, which he calls hallucinated names (§Inference, §Run it)
  - The build_microgpt.py gist keeps six versions as revisions, train0.py to train5.py, each adding one component, train5.py being train.py (§Progression)
  - He suggests trying another dataset, training longer or enlarging the model; the rest of the code does not need to change for a new dataset (§Run it, §FAQ)
- relation to existing pages:
  - [[micrograd]]: its autograd is a scalar `Value` class; he points readers to the micrograd video (VMj-3S1tku0, i.e. [[youtube-2022-08-16-micrograd]]) for this part (§Autograd), and names micrograd among the projects it culminates (§intro). The post does not itself say it differs from micrograd's engine; the micrograd README (2026-08-03 digest) says it builds on a more efficient and better version of that engine.
  - [[makemore]]: named among the culminated projects (§intro); the dataset is downloaded from makemore's names.txt (§Dataset).
  - [[nanogpt]]: named among the culminated projects only (§intro). No further comparison.
  - [[nanochat]]: **not mentioned in the post.** Any link must be a **Note:** (e.g. both are his from-scratch GPT code, nanochat a full harness, microgpt the algorithm alone); the source does not connect them.
  - [[character-level-language-modeling]]: same task as makemore's, new names one character at a time.

### claim: microgpt-is-the-full-algorithm-everything-else-is-efficiency
- existing: no
- title: "microgpt's 200 lines hold the full algorithmic content of a GPT; everything else is efficiency"
- confidence: stated
- quote: "Everything else is just efficiency." (§intro)
- statements:
  - He says the file contains the full algorithmic content of what is needed and that everything else is just efficiency (§intro)
  - He says he cannot simplify it any further (§intro)
  - Between microgpt and a production LLM a long list of things change, but he says none alter the core algorithm and overall layout; they are what makes it work at scale (§Real stuff)
  - Tensor autograd on GPUs is the same math over many scalars in parallel (§Real stuff); his scalar Value backward is the same algorithm as PyTorch's loss.backward(), smaller and simpler but much less efficient (§Autograd)
  - Production inference is still next-token prediction with much engineering spent on speed (§Real stuff)
  - He concludes that if you understand microgpt, you understand the algorithmic essence (§Real stuff)
  - The FAQ answer on speed: one scalar at a time in pure Python, while a GPU runs the same math on millions of scalars in parallel (§FAQ)
- relations:
  - **extends** [[micrograd-is-all-you-need-everything-else-is-efficiency]] (2022-08-16): there, a scalar autograd engine is all you need to train neural nets and tensors are purely for efficiency ([[youtube-2022-08-16-micrograd]] @05:56, @06:30); here the same reduction is broadened from training neural nets to the whole GPT pipeline, dataset to inference (§intro, §Real stuff). Both hold. `extends` requires a timeline: proposed below. If merge prefers no timeline, the weaker `supports` is also true (microgpt is evidence that a scalar engine suffices for a GPT).
  - **supports** [[gpt-is-not-a-complicated-model]] (2023-01-08): minGPT README says GPT is not complicated and most complexity is batching for efficiency ([[github-2023-01-08-mingpt-readme]] §intro); microgpt runs a GPT with no batch dimension and no parallel time steps (§Architecture) in 200 lines (§intro).
  - **supports** [[neural-net-training-should-not-be-complicated]] (2024-07-11): llm.c post calls training one loop of simple arithmetic ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Code)); microgpt's loop is five steps, pick a document, forward, loss, backward, update (§Training loop), in pure Python (§intro).
  - topic: [[transformer-architecture]] or [[small-hackable-educational-code]] (merge choice).

### claim (optional; merge may fold into the topic): hallucinated-names-and-false-facts-are-the-same-phenomenon
- existing: no
- title: "A hallucinated name from microgpt and a false fact from ChatGPT are the same phenomenon"
- confidence: stated
- quote: "It has no concept of truth" (§FAQ)
- statements:
  - The model samples from a probability distribution and only knows what sequences are statistically plausible given the training data (§FAQ)
  - He says microgpt hallucinating a name like "karia" is the same phenomenon as ChatGPT confidently stating a false fact: plausible-sounding completions that are not real (§FAQ)
- relation: **none** set. [[hallucinations-come-from-imitating-confident-answers]] (2025-02-05) explains why models answer confidently (imitating confident training answers); this one explains hallucination as plausible sampling. Both can hold; at most a **Note:** link. Not `contradicts`, not `extends` (different mechanism, not a broadening).
- Recommended: fold as a statement on [[llm-hallucinations]] rather than a new page (coarse-topic rule).

### topic: backpropagation
- existing: yes
- aliases to add: local gradient, reverse topological order
- statements:
  - Training needs, for each parameter, whether nudging it up raises or lowers the loss and by how much; the graph funnels many inputs to one scalar loss and backpropagation works backwards from it using the chain rule (§Autograd)
  - Each operation is like a lego block that knows its forward output and its local gradient with respect to each input; that is all autograd needs, the rest is the chain rule (§Autograd)
  - His operation set: add, multiply, power, log, exp, relu, each with its local derivative (§Autograd)
  - backward() walks the graph in reverse topological order from the loss, starting with the loss's gradient set to 1, and multiplies local gradients along every path; he explains the chain rule with a car, bicycle and walking-man speed analogy (§Autograd)
  - Gradients accumulate (+=) because when a value is used in several places, contributions from each path must be summed, per the multivariable chain rule (§Autograd)
  - A worked example matches PyTorch's .backward() exactly; he calls it the same algorithm on scalars instead of tensors (§Autograd)
  - A gradient gives the direction and steepness of each input's influence on the loss, which lets the parameters be nudged to lower it (§Autograd)
- relation: consistent with the 2022 lecture account already on the page; no new claim.

### topic: transformer-architecture
- existing: yes
- aliases to add: KV cache, GQA, Grouped Query Attention, Mixture of Experts, MoE, gated linear activations (RMSNorm, RoPE already present)
- statements:
  - He frames the model as a stateless function: token, position, parameters and cached keys/values in, next-token logits out (§Architecture)
  - microgpt follows GPT-2 with RMSNorm instead of LayerNorm, no biases and ReLU instead of GeLU; RMSNorm rescales to unit root-mean-square to stabilise training and is a simpler variant of GPT-2's LayerNorm (§Architecture)
  - Token and position embeddings are added; he notes modern LLMs usually skip position embeddings for relative schemes such as RoPE (§Architecture)
  - The MLP projects up to 4x the embedding dimension, applies ReLU and projects back; it is where most per-position "thinking" happens and is local in time; the Transformer intersperses communication (attention) with computation (MLP) (§Architecture)
  - Residual connections add each block's output to its input, letting gradients flow directly and making deeper models trainable (§Architecture)
  - Production models are similar-looking Transformers, much wider (10,000+ embedding dimensions) and deeper (100+ layers), with RoPE, GQA, gated activations and MoE; the core structure of attention and MLP on a residual stream is preserved (§Real stuff)
- relation: supports the page's existing communication/computation framing; **Note:** link to [[microgpt]].

### topic: self-attention
- existing: yes
- aliases to add: KV cache, query/key/value
- statements:
  - Query says what the token is looking for, key what it contains, value what it offers if selected; his example is the second "m" in "emma" attending to the earlier "e" as a recent vowel (§Architecture)
  - Each head scores its query against all cached keys scaled by the square root of the head dimension, softmaxes, and takes a weighted sum of cached values; heads are concatenated and projected (§Architecture)
  - Attention is the only place a token at position t looks at past tokens (§Architecture)
  - He says the KV cache is conceptually always there, even in training; production hides it inside vectorised attention, and in microgpt the cached keys and values are live graph nodes that are backpropagated through (§Architecture)

### claim: attention-is-a-communication-mechanism
- existing: yes
- new source, restatement: "Attention is a token communication mechanism." (§Architecture). Add the post to `sources`; relation: same claim, no new link.

### topic: tokenization
- existing: yes
- statements:
  - The simplest tokenizer gives each unique character an integer; the integers have no meaning, they might as well be emoji (§Tokenizer)
  - A special BOS token marks where a document starts and ends; each name is wrapped with BOS on both sides, giving a vocabulary of 27 (§Tokenizer)
  - Production tokenizers like tiktoken work on chunks of characters; production BPE merges frequent sequences, giving ~100K tokens and more content per position (§Tokenizer, §Real stuff)

### topic: loss-functions
- existing: yes
- statements:
  - The per-position loss is the negative log probability of the correct next token, which he calls cross-entropy; it measures how surprised the model is, 0 at probability 1 and infinite near 0, averaged over the document (§Training loop)
  - Initial loss of about 3.3 equals random guessing among 27 tokens (§Training loop)

### topic: gradient-descent
- existing: yes (Adam is an alias)
- statements:
  - Plain gradient descent would subtract learning rate times gradient; Adam keeps running means of gradients (momentum) and squared gradients (per-parameter rate), with bias corrections for their zero start, and he decays the rate linearly (§Training loop)
  - Gradients are reset to zero after each update (§Training loop)
  - At scale, optimisation becomes its own discipline: reduced precision, tuned learning rate, weight decay, betas, warmup and decay that depend on model size, batch and data; scaling laws like Chinchilla guide compute allocation; teams run small experiments first because mistakes can waste millions of dollars (§Real stuff)

### topic: sampling-from-language-models
- existing: yes
- statements:
  - Sampling starts from BOS, samples a token from the softmax, feeds it back and stops at BOS or the maximum length (§Inference)
  - Temperature divides logits before softmax: 1.0 is the learned distribution, lower sharpens toward the top choices, near 0 is greedy, higher flattens toward more diverse, less coherent output (§Inference)

### topic: pretraining-and-finetuning
- existing: yes
- statements:
  - The base model is a document completer, not a chatbot; turning it into ChatGPT takes SFT, swapping documents for curated conversations, where algorithmically nothing changes, then RL, where responses are scored by humans, a judge model or an algorithm (§Real stuff)
  - In RL, he says, the model is still training on documents, now made of tokens from the model itself (§Real stuff)
  - Production data is trillions of tokens of web text, books and code, deduplicated, quality-filtered and mixed (§Real stuff)
  - A chat with ChatGPT is, from the model's side, a document it completes; ChatGPT is the same predict-sample-repeat loop scaled up, plus post-training (§Dataset, §FAQ)

### claim: pretraining-gives-a-document-completer
- existing: yes
- new source, restatement: base model "is a document completer, not a chatbot" (§Real stuff). Add to `sources`; no new link.

### topic: llm-hallucinations
- existing: yes
- statements: see the optional claim above (§FAQ). Also: he calls microgpt's generated names "hallucinated" throughout (§Dataset, §Inference).

### topic: character-level-language-modeling
- existing: yes
- statements:
  - The goal is to learn the statistical patterns of the names and generate new, plausible-sounding ones (§Dataset)
  - What the model learns: names often start with consonants, "qu" appears together, three consonants in a row are rare; it learns a distribution that reflects such rules, not the rules (§FAQ)
  - Swap in city names, Pokemon names, words or short poems and it learns those instead (§FAQ)

### method: small-hackable-educational-code
- existing: yes
- statements:
  - microgpt is one file of 200 lines of pure Python with no dependencies at all, not even PyTorch (§intro, §Run it)
  - He says it even breaks across three columns (§intro)
  - It is available as a gist, a web page and a Colab notebook where readers can ask Gemini about it (§intro, §Run it)
- note: the page's step "Keep PyTorch as the only dependency" is exceeded here (zero dependencies); merge may reword the step or add a sentence, not contradict it.

### method: spelled-out-build-from-scratch
- existing: yes
- statements:
  - He advises building it up like layers of an onion: bigram count table with no gradients; MLP with manual numerical and analytic gradients and SGD; autograd replacing manual gradients; position embeddings, single-head attention, RMSNorm and residuals; multi-head attention and the layer loop; Adam (§Progression)
  - Each version is a revision of the build_microgpt.py gist, so the diffs show one component added at a time (§Progression)
  - He explains each piece with plain-language intuitions: lego blocks for operations, a car-bicycle-walker analogy for the chain rule, the "emma" example for attention (§Autograd, §Architecture)
- relation: this method already has "Build the explicit baseline, then the neural net"; train0.py (bigram counts, no net) fits it.

### claims (existing, relation only): gpt-is-not-a-complicated-model, neural-net-training-should-not-be-complicated, micrograd-is-all-you-need-everything-else-is-efficiency
- See relations under the new claim. The post does not repeat the phrases "not a complicated model" or "should not be that complicated"; it gives evidence (200 lines, no batching, five-step loop), so these are `supports`, not restatements. Its "everything else is just efficiency" echoes the 2022 wording in substance ("micrograd is what you need..."; tensors purely for efficiency), hence `extends`.

### timeline (proposed): everything-else-is-efficiency-over-time
- existing: no
- needed only if merge sets `extends` above
- entries: 2022-08-16 [[micrograd-is-all-you-need-everything-else-is-efficiency]]; 2023-01-08 [[gpt-is-not-a-complicated-model]]; 2024-07-11 [[neural-net-training-should-not-be-complicated]]; 2026-02-12 [[microgpt-is-the-full-algorithm-everything-else-is-efficiency]]; 2026-08-03 micrograd README restating it about microgpt ([[github-2026-08-03-micrograd-readme]] §Training a GPT)
- framing: accumulated, not changed; dated bullets only, no intervals.

## Quotes
- "Everything else is just efficiency." (§intro)
- "I cannot simplify this any further." (§intro)
- "a decade-long obsession to simplify LLMs to their bare essentials" (§intro)
- "your conversation with it is just a funny looking “document”" (§Dataset) — curly quotes in raw
- "Think of each operation as a little lego block" (§Autograd)
- "algorithmically identical, significantly smaller and simpler, but of course a lot less efficient" (§Autograd)
- "The parameters are the knowledge of the model." (§Parameters)
- "Attention is a token communication mechanism." (§Architecture)
- "The Transformer intersperses communication (Attention) with computation (MLP)." (§Architecture)
- "But the KV cache is conceptually always there, even during training." (§Architecture)
- "microgpt contains the complete algorithmic essence of training and running a GPT." (§Real stuff)
- "Algorithmically, nothing changes." (§Real stuff, on SFT)
- "if you understand microgpt, you understand the algorithmic essence." (§Real stuff)
- "It has no concept of truth" (§FAQ)
- "These are the same knobs that matter at scale." (§FAQ)

## Notes for merge
- **Code is linked, not copied.** The raw contains the full script inline; do not quote or reproduce any code, config line or code comment. Hyperparameter numbers (16-dim, 4 heads, 1 layer, block 16, 1,000 steps, lr 0.01, temperature 0.5) are paraphrased facts, fine as prose.
- Headings: text before `## Dataset` is §intro. FAQ questions are plain lines, not headings; cite §FAQ. The "Progression" and lego-block tables lost their markup in the raw.
- **Inconsistency to avoid combining:** §Run it says the script takes about 1 minute on his MacBook (1,000 steps); §FAQ says a single training step takes seconds. Do not derive a per-step time; cite each where used.
- "32,000 names" in §Dataset; the printed run shows 32,033 docs (§Run it). Use "about 32,000".
- GPT-2 is given 1.6 billion parameters here (§Parameters), i.e. the largest GPT-2; do not conflate with the 124M used elsewhere in the wiki.
- Typos in raw (avoid quoting these sentences): "initates", "vocavulary" (§Tokenizer); "inmput", "interately" (§Autograd); "the model things should come next" (§Architecture); "stastical" (§Run it).
- The triptych art-store mention and "art project" framing are his; a sentence is fine, no claim.
- The post never mentions nanochat. The nanochat relation can only be a **Note:**.
- The micrograd video link in §Autograd is VMj-3S1tku0 = [[youtube-2022-08-16-micrograd]]; he calls it a 2.5-hour video.
- Do not write order between this post (2026-02-12) and the micrograd README snapshot (2026-08-03) beyond their dates.
- FAQ "Does the model understand?": he says that is philosophical but mechanically no magic is happening; the mechanism is in the 200 lines. Could be a sentence on [[llms-are-mostly-inscrutable-empirical-artifacts]] as a **Note:** at most; not a relation (different question: mechanism vs learned parameters).
