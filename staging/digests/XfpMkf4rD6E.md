# Digest: Stanford CS25: V2 I Introduction to Transformers w/ Andrej Karpathy
- raw: raw/talks/XfpMkf4rD6E.md · published: 2023-05-19 · medium: talk · words: 12926
- source slug: talk-2023-05-19-stanford-cs25-transformers

## Source page

```
---
type: source
raw_path: raw/talks/XfpMkf4rD6E.md
published: 2023-05-19
medium: talk
summary: Guest lecture opening Stanford's CS25 in which he traces how AI converged on the Transformer, explains attention as data-dependent message passing on a directed graph, walks through nanoGPT, and argues the Transformer is a general-purpose, efficient, optimizable computer capable of in-context learning.
url: https://www.youtube.com/watch?v=XfpMkf4rD6E
title: "Stanford CS25: V2 I Introduction to Transformers w/ Andrej Karpathy"
---
# Stanford CS25: V2 I Introduction to Transformers w/ Andrej Karpathy
Raw: [[raw/talks/XfpMkf4rD6E]] · Original: https://www.youtube.com/watch?v=XfpMkf4rD6E

## Summary
The course instructors introduce CS25 and an attention timeline for the first ten minutes; his
part starts at @10:05. He describes AI around 2011 as separate fields with their own feature
pipelines and vocabularies, then neural nets spreading after 2012 and, since 2017, every field
copy-pasting one architecture, the Transformer (@11:12, @12:50, @13:56). He traces the
architecture's history from the 2003 neural language model through sequence-to-sequence,
the encoder bottleneck and the 2014 soft-search attention paper, including an email from its
first author on where attention came from, to "Attention Is All You Need" (@15:00, @16:39,
@18:17, @19:57). He explains attention as the communication phase of the Transformer, a
data-dependent message passing scheme on directed graphs, then steps through nanoGPT's
decoder-only implementation (@22:45, @24:58, @31:02, @38:49). He covers how Transformers are
applied to images, speech, RL and multi-sensor inputs by chopping inputs into pieces
(@52:43, @54:23), names in-context learning as what makes them special (@55:30, @56:34), and
argues the architecture is expressive, optimizable and efficient, a general-purpose
computer (@58:12, @59:18, @59:51). Audience Q&A covers autoregression versus diffusion,
inductive biases and a scratchpad for extending memory (@50:15, @1:06:28, @1:08:47).

## Key points
- AI fields that once had separate methods and vocabularies converged on neural nets after 2012 and on one architecture after 2017 → [[ai-has-converged-on-one-architecture]]
- The path to the Transformer: neural LM 2003, seq2seq 2014, the encoder bottleneck, soft-search attention 2014, then 2017 → [[transformer-architecture]]
- The 2017 architecture has barely changed; pre-norm LayerNorm is the main change that stuck → [[the-transformer-has-proven-remarkably-resilient]]
- Attention is the communication phase: data-dependent message passing on a directed graph; the MLP is the compute phase → [[attention-is-a-communication-mechanism]], [[self-attention]]
- Heads are copies in parallel, layers copies in series; self- and cross-attention differ only in where keys and values come from → [[self-attention]]
- Encoder, decoder and encoder-decoder models differ in connectivity: delete the mask line for an encoder, add a cross-attention line for encoder-decoder → [[transformer-architecture]]
- nanoGPT walk-through: integer-encoded text, B×T batches, token plus position embeddings, blocks, LM head, cross-entropy → [[nanogpt]], [[tokenization]], [[embeddings]], [[character-level-language-modeling]]
- Images, speech, RL trajectories and extra sensor inputs are chopped up and fed in as a set → [[transformers-are-flexible-about-their-inputs]]
- In-context learning is what makes Transformers special; there may be something like gradient descent in the activations → [[in-context-learning]], [[transformers-are-capable-of-in-context-learning]]
- Expressive, optimizable and efficient at once: a general-purpose efficient optimizable computer → [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]]
- GPT runs natural-language programs given as prompts → [[gpt-is-a-general-purpose-computer-running-natural-language-programs]]
- With enough data, encode less inductive bias; biases live in connectivity and positional encodings → [[with-enough-data-encode-less-inductive-bias]]
- He does not love autoregressive sampling and finds diffusion more appealing → [[he-does-not-love-autoregressive-sampling]]

## Fed pages
- [[transformer-architecture]]
- [[self-attention]]
- [[attention-is-a-communication-mechanism]]
- [[nanogpt]]
- [[tokenization]]
- [[embeddings]]
- [[character-level-language-modeling]]
- [[small-hackable-educational-code]]
- [[in-context-learning]]
- [[ai-has-converged-on-one-architecture]]
- [[the-transformer-has-proven-remarkably-resilient]]
- [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]]
- [[gpt-is-a-general-purpose-computer-running-natural-language-programs]]
- [[transformers-are-capable-of-in-context-learning]]
- [[transformers-are-flexible-about-their-inputs]]
- [[with-enough-data-encode-less-inductive-bias]]
- [[he-does-not-love-autoregressive-sampling]]
```

## Candidates

### topic: transformer-architecture
- existing: yes
- aliases: add "Attention Is All You Need", encoder-decoder, cross-attention, encoder-only, BERT, T5, sequence to sequence, history of the Transformer
- statements:
  - **History (new section).** He likes the 2003 paper as the first popular application of neural nets to language modelling: an MLP taking three words and predicting a distribution over the fourth (@15:00, @15:32).
  - The 2014 sequence-to-sequence paper tackled variable-length input and output for translation with an encoder LSTM whose context vector conditions a decoder LSTM (@15:32, @16:05).
  - People quickly identified the encoder bottleneck: the whole source sentence packed into one vector seemed like too much information (@16:39).
  - The 2014 paper "neural machine translation by jointly learning to align and translate" let the decoder soft-search back over encoder words; the context vector is a softmax-weighted sum of encoder hidden states, which he calls the current modern equations of attention and, as far as he knows, the first use of the word for this mechanism (@16:39, @17:11, @17:44, @18:17).
  - He emailed the first author (caption "Dimitri"), who replied that the idea came from wanting the decoder to learn where to put a cursor on the source, inspired by middle-school translation exercises, and that it worked on the first try; per that email the name "attention" came from Yoshua Bengio (caption "Yeshua NGO") on a final pass, replacing "RNN search" (@18:17, @18:50, @19:23, @19:57). This is the author's account as relayed by him.
  - He reads the 2017 paper as deleting everything except attention, and as combining several things at once (positional encoding because attention operates over sets, the ResNet residual structure, attention interspersed with MLPs, layer norms from another paper, multiple heads, a 4x MLP expansion) into a very good local minimum in architecture space; he calls it a landmark paper (@19:57, @20:30, @21:04, @21:39).
  - The paper read as a random machine-translation paper that did not know what was coming, and he says he talked to authors who were unaware of the impact at the time (@49:02, @49:34).
  - Asked about precursors, he likens the Transformer to a ResNet with a self-attention block added alongside the pre-existing MLP block (@48:28).
  - **Variants.** Encoder tokens are fully connected; decoder tokens connect to all encoder states and only to earlier decoder tokens, giving a triangular structure; cross-attention consumes features from the top of the encoder (@26:06, @26:40).
  - To make an encoder, delete the mask line; for encoder-decoder, add a cross-attention line whose queries come from x and keys and values from the top of the encoder (@43:13, @43:47, @44:20).
  - GPT is decoder-only, BERT encoder-only, T5 encoder-decoder; BERT is trained with masking and other denoising objectives rather than next-token prediction (@44:20, @44:52).
  - **Block.** In nanoGPT's block, the residual pathway feeds a layer norm then self-attention (communicate), then the MLP (compute), a two-layer net with a GELU nonlinearity (caption "gallery") applied per node (@37:08, @37:41, @38:17).
  - The context length is finite, typically 1,024 or 2,048 tokens in such models; extending it is hard because attention is quadratic (@42:39).
  - **Why it works (see claim pages).** Expressive forward pass, optimizable through residuals and layer norms, and a shallow wide graph that suits GPU parallelism (@58:12, @58:44).
  - RNNs can in principle implement arbitrary programs but are long thin serial compute graphs, poorly optimizable and inefficient; Transformers have few hops from supervision to inputs and process every word in parallel (@1:02:29, @1:03:01, @1:03:35).

### topic: self-attention
- existing: yes
- aliases: add message passing, cross-attention, self-attention vs cross-attention
- statements:
  - He presents his view of attention as different from how he has seen it presented: the Transformer interleaves a communication phase (multi-headed attention) and a computation phase (the MLP) (@22:11, @22:45).
  - He wrote simple Python for one round of communication: each node holds a private data vector and emits a query (what I'm looking for), a key (what I have) and a value (what I will communicate) by linear transformations (@23:18, @23:52).
  - At each node, the query dot-products with the keys of nodes pointing to it to give unnormalised interestingness; softmax normalises the scores and a weighted sum of values updates the node (@24:26, @24:58).
  - The real implementation is the same scheme vectorised and batched, interspersed with layer norms to help training; it runs in every head in parallel and every layer in series, with different weights (@25:30, @26:06).
  - Multiple heads are independent applications of the same attention with different query, key and value weights, seeking different kinds of information in parallel (@27:14, @27:47).
  - Self- and cross-attention differ only in where keys and values come from (the node itself or an external source such as the encoder); algorithmically they are the same (@28:19, @28:53, @29:26).
  - The causal attention code is complicated only because of batching and masking the connectivity; tensors carry batch, head and time dimensions, and he invites students to step through it (@38:49, @39:55).
  - The mask sets disallowed affinities to negative infinity so softmax gives them zero weight; attention times V gathers information as a weighted sum of values (@40:29, @41:01).
  - In his experience the connectivity is fixed rather than changing with the data (@46:12, @46:44).
  - Asked about the square-root scaling, he says it controls the variance growing with dimension so softmax does not collapse to one-hot; almost an initialization thing (@52:09).
  - Patch-local attention can be imposed by masking the attention matrix, and people intersperse local and global layers because full attention is inefficient (@1:07:00).

### claim: attention-is-a-communication-mechanism
- existing: yes
- statements:
  - Restated here: attention is the communication phase of the Transformer, a data-dependent message passing scheme on directed graphs; forget machine translation, each node stores a vector (@22:45).
  - In nanoGPT with block size eight there are eight nodes: the first pointed to only by itself, the second by the first and itself, and so on (@37:08).
  - Answering a question, he suggests everything today might be a graph network, since the Transformer's native representation is sets connected by directed edges (@51:35).
- relation: same claim, second source (2023-05-19, after 2023-01-17). Add as a source; no new claim needed.
- quote: "it's really just a data dependent message passing on directed graphs" (@22:45)

### artifact: nanogpt
- existing: yes
- statements:
  - He describes nanoGPT as a complete, very minimal Transformer implementation he worked on "over the last few days", reproducing GPT-2 on OpenWebText; very readable at about 300 lines (@31:02).
  - He walks through it: the GPT class, token embeddings from nn.Embedding plus positional embeddings, blocks, a final layer norm, the LM head, and cross-entropy on targets offset by one (@34:55, @35:29, @36:01, @36:34).
  - Asked what he works on next, he says nanoGPT: moving from computer vision toward language, from minGPT rewritten into nanoGPT, trying to reproduce GPTs; he finds a ChatGPT-like product incrementally improved extremely interesting (@1:10:52).

### topic: tokenization
- existing: yes
- statements:
  - Transformers need text encoded as integers; in the simplest case each character gets an integer and the whole text becomes one long 1-D sequence (@31:35, @32:07).
  - With multiple documents people splice in special end-of-text tokens; these have no modelling impact beyond the Transformer learning that the token means wipe the memory (@32:07, @32:40).
  - Real models' tokens are usually BPE, SentencePiece or WordPiece tokens (@42:39). Mention only.

### topic: embeddings
- existing: yes
- statements:
  - Because the Transformer processes sets, token-identity embeddings and positional embeddings are added together to give what and where (@35:29, @36:01).
  - Extra inputs such as radar or vehicle information get a learnable special embedding token so the Transformer knows their source (@1:04:42).
  - Positional encodings can be hard-wired with sines and cosines, but he prefers a trainable vector that always sits at a location; they have very little inductive bias (@1:05:18, @1:05:57).
  - Rotary and relative positional encodings are now more common than the original (@22:11).

### topic: character-level-language-modeling
- existing: yes
- statements:
  - Tiny Shakespeare, one of his favourite toy datasets, is all of Shakespeare concatenated into a ~1 MB file (@31:35).
  - Batches are B×T chunks of the 1-D sequence; block size is the maximum context, and each 4×8 batch holds many examples because every prefix predicts its next element (@32:40, @33:15, @33:48, @34:19).
  - Generation starts from a start token such as a newline, feeds each sampled character back, and crops the context once it exceeds the block size (@41:34, @42:06, @42:39).

### method: small-hackable-educational-code
- existing: yes
- statements:
  - He presents nanoGPT as a serious implementation that is also very readable at about 300 lines, so everyone can take a look (@31:02).
- weak fit; merge may drop this and keep the sentence on [[nanogpt]] only.

### topic: in-context-learning
- existing: no
- aliases: In-context learning, meta-learning, few-shot learning, prompting with examples, scratchpad
- statements:
  - He points to the GPT-3 paper "Language Models are Few-Shot Learners", which he would have renamed something like "Transformers are capable of in-context learning or meta learning" (@55:30).
  - In the paper's setting the prompt holds a passage plus example question–answer pairs; accuracy improves with more examples in context (@56:02, @56:34).
  - He reads this as the Transformer learning in its activations without gradient descent, unlike finetuning, which updates on example–answer pairs by gradient descent (@56:34).
  - The paper distinguishes an outer loop (training by gradient descent) from an inner loop (in-context learning as the model reads the sequence) (@56:34, @57:07).
  - Recent papers, he says, hint that something like gradient-based learning may happen inside the activations; one proposes an operator (caption "Raw operator") that Transformers implement and on which ridge regression can be built (@57:07, @57:38). These are papers' positions, not his.
  - His own hand-wavy reason it is not impossible: forward, backward and update add to the weights, which looks like a ResNet, and a Transformer is a ResNet (@57:38).
  - On extending memory, he likes keeping the context fixed and teaching the model via prompt examples to write to a scratchpad between special tokens, which external logic saves and lets it attend over; because it is so meta-learned it can be taught to use such gadgets, like a person using a notepad (@1:08:47, @1:09:20).

### claim: ai-has-converged-on-one-architecture
- existing: no
- title: Since 2017, AI fields have converged on one architecture, the Transformer
- confidence: stated
- quote: "literally the architecture is converged to like one architecture" (@13:56)
- statements:
  - Around 2011 computer-vision papers spent pages on a zoo of feature descriptors with an SVM on top, collecting code from everywhere, and it did not work well (@11:12, @11:43, @12:16).
  - Each area of AI had its own vocabulary, so you could not read papers across areas (@12:16, @12:50).
  - From 2012 Krizhevsky (caption "askewsky") and colleagues showed a large neural net on a large dataset performs strongly; the focus moved from algorithms to compute and data, and the recipe copy-pasted across vision, NLP, speech, translation and RL, lowering the barrier to entry (@12:50, @13:23).
  - Since 2017 the Transformer is copy-pasted everywhere and what changes is the data and how it is chunked and fed; he calls this a caricature but a correct first-order statement (@13:56, @14:28).
  - He offers, hedged with "maybe", that this hints we are converging to something like what the brain does, since cortex is homogeneous across areas (@14:28, @15:00).
  - Examples: ViT patches, speech spectrogram slices including Whisper, Decision Transformer, and a Transformer at the computational heart of AlphaFold (@52:43, @53:17, @53:50).
- relation: none to an existing claim. **Note:** loosely adjacent to [[the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers]] (2022-09-07, machinery staying fixed across his own models), but that is about one lecture series' pipeline, not fields converging; do not link as supports.

### claim: the-transformer-has-proven-remarkably-resilient
- existing: no
- title: The 2017 Transformer architecture has barely changed since
- confidence: stated
- quote: "the gpts and everything else that you're seeing today is basically the 2017 architecture" (@21:39)
- statements:
  - Papers have tried to change its details and nothing sticks because it is quite good; the change he knows of that stuck is moving layer norms to the pre-norm position (@21:39).
  - He adds that positional encodings have changed (rotary, relative), but for the most part it is remarkably resilient (@22:11).
  - Five years on it has not changed even though everyone is trying to change it (@49:02).
- relation: none to an existing claim page. Consistent with the GPT lecture's sentence on [[transformer-architecture]] that GPT-3 is nearly identical to the lecture model (youtube-2023-01-17-gpt-from-scratch @1:50:56); merge may add a Note.

### claim: the-transformer-is-a-general-purpose-efficient-optimizable-computer
- existing: no
- title: He would have called the Transformer a general-purpose, efficient, optimizable computer
- confidence: stated
- quote: "I probably would have called the Transformer a general purpose efficient optimizable computer" (@59:18)
- statements:
  - Reading his tweets, which he says were written for general consumption and are a bit hyped, he argues the Transformer optimizes three properties at once: expressive forward pass (possibly even meta-learning), optimizable thanks to residuals and layer norms, and efficient (@58:12, @58:44).
  - It is a shallow wide computational graph suited to GPU parallelism; he thinks it was designed deliberately for GPUs, and he likes the earlier Neural GPU work that designs nets backwards from hardware constraints (@58:44).
  - He would have used this name instead of "Attention Is All You Need" in hindsight (@59:18).
  - Efficiency is less talked about but extremely important because scale matters in deep learning; efficient on current hardware means it can be made bigger (@1:03:35, @1:04:09).
  - RNNs' ability to implement arbitrary programs is to him a somewhat useless statement since they are not optimizable or efficient (@1:02:29).
- relation: none to an existing claim. Contrast with [[gpt-is-not-a-complicated-model]] (2023-01-08): compatible, no link needed.

### claim: gpt-is-a-general-purpose-computer-running-natural-language-programs
- existing: no
- title: GPT is a general-purpose computer, reconfigurable at runtime to run natural-language programs
- confidence: stated
- quote: "GPT is a general purpose computer reconfigurable at runtime to run natural language programs" (@59:51)
- statements:
  - From one of his tweets: earlier neural nets were special-purpose computers for specific tasks; programs are given as prompts and GPT runs them by completing the document (@59:51).
  - Another tweet: scale up the training set with a powerful enough net like a Transformer and it becomes a kind of general-purpose computer over text; instead of a single fixed sequence you design the sequence in the prompt (@1:00:30, @1:01:03).
- relation: **supports** [[english-is-the-new-programming-language]] (2025-06-19) and the [[software-3-0]] topic: the 2023 talk already frames prompts as programs that GPT runs (this source @59:51); the 2025 keynote names prompts "programs that program the LLM" and says we program computers in English (youtube-2025-06-19-software-is-changing @03:19, @04:23). Not extends: the later claim is about programming in English and everyone becoming a programmer, which this does not state. Also loosely related to [[llms-as-operating-systems]] (LLM as a new kind of computer, @10:01 there); a Note, not a claim link.

### claim: transformers-are-capable-of-in-context-learning
- existing: no
- title: In-context learning is what makes Transformers special
- confidence: stated
- quote: "Transformers are capable of in context learning or like meta learning" (@55:30)
- statements:
  - Answering what makes Transformers effective, he says in-context or meta-learning is kind of what makes them really special (@55:30).
  - See [[in-context-learning]] statements for the GPT-3 setting and the activations-as-learning reading (@56:34, @57:07).
- relation: none. Merge may fold this into the in-context-learning topic per the coarse-granularity rule.

### claim: transformers-are-flexible-about-their-inputs
- existing: no
- title: The Transformer makes it easy to feed in any extra input
- confidence: stated
- quote: "it's a very flexible framework" (@55:30)
- statements:
  - He calls the way Transformers were applied to vision "kind of ridiculous" from a computer-vision perspective: chop an image into squares and feed them in; the model must rediscover structure, but the simplest baseline works fairly well (@52:43, @53:17).
  - At Tesla, adding radar, map, vehicle-type or audio inputs to a convnet raised hard questions of where and how to feed them; with a Transformer you chop everything up, add it to the set and let self-attention figure out the communication (@54:23, @54:57).
  - This frees neural nets from laying out computation in Euclidean space; in attention everything is just sets, which he finds beautiful (@54:57, @55:30).
- relation: none. Could fold into [[ai-has-converged-on-one-architecture]] as context.

### claim: with-enough-data-encode-less-inductive-bias
- existing: no
- title: With enough data, hand-coded inductive biases tend to hurt
- confidence: stated
- quote: "if you have Infinity data then you actually want to encode less and less" (@1:06:28)
- statements:
  - With enough data, trying to put knowledge in is usually not productive; with little data you want biases, and convolutions may then be a good idea (@1:06:28).
  - In the Transformer the inductive biases are factored out of the core into node connectivity and positional encodings, where people add structure, and there are perhaps 200 or more papers on it (@1:07:00, @1:07:35).
- relation: none.

### claim: he-does-not-love-autoregressive-sampling
- existing: no
- title: He does not love autoregressive sampling and finds diffusion more appealing (2023)
- confidence: stated
- quote: "I certainly don't love the auto aggressive modeling approach" (@50:15)
- statements:
  - Sampling a token and committing to it seems weird to him; he suggests hybrids with diffusion or ways to edit sequences later within the autoregressive framework (@50:15).
  - He personally finds diffusion much more appealing, because when he writes he does a first draft and a better second draft rather than committing chunk by chunk (@50:15, @50:48).
- relation: none in the wiki today; a candidate for a timeline if later sources discuss diffusion LLMs.

## Quotes
- "attention is kind of like the communication phase of the Transformer" (@22:45)
- "it's really just a data dependent message passing on directed graphs" (@22:45)
- "heads is really just like copy paste in parallel" (@27:47)
- "layers are copy paste but in series" (@27:47)
- "literally the architecture is converged to like one architecture" (@13:56)
- "maybe we're converging to some kind of a uniform powerful learning algorithm here" (@15:00)
- "to me this is a really a landmark paper" (@20:30)
- "the gpts and everything else that you're seeing today is basically the 2017 architecture" (@21:39)
- "I certainly don't love the auto aggressive modeling approach" (@50:15)
- "the Transformer is a graphical Network processor" (@51:35)
- "Transformers are capable of in context learning or like meta learning" (@55:30)
- "the Transformer if you look at the computational graph is a shallow wide Network" (@58:44)
- "I probably would have called the Transformer a general purpose efficient optimizable computer" (@59:18)
- "GPT is a general purpose computer reconfigurable at runtime to run natural language programs" (@59:51)
- "the network becomes a kind of general purpose computer over text" (@1:00:30)
- "in deep learning scale matters" (@1:03:35)
- "if you have Infinity data then you actually want to encode less and less" (@1:06:28)
- "it's just like human learning to use a notepad right" (@1:09:20)

All grep-checked: each string occurs exactly once in the raw file.

## Notes for merge
- **Speakers.** @00:05 to mid-@10:05 is the course instructors (intro, attention timeline 2017–2022, future directions such as external memory and quadratic attention). None of it is his. He starts at "uh yes I'm excited to be here" inside the @10:05 block. Student questions are mostly inaudible or garbled (e.g. @29:58, @47:56, @1:01:56, @1:10:20); only his answers are attributed. At @42:39 he refers back to an instructor ("did mentioned") wanting longer context.
- **Date.** Published 2023-05-19; the lecture was given earlier (winter 2023 quarter per the intro; he says he worked on nanoGPT "over the last few days" @31:02, so likely around January 2023). Use published date for `stated_on`, but a reviewer may want a note.
- **Tweets.** @58:12–@1:01:03 he reads his own earlier tweets off slides, which he says were written for general consumption and are "a bit more high level and hype". The general-purpose-computer claims are from those tweets; their original dates are not in this raw.
- **Garbled captions.** "Cell potential"/"soft ocean"/"self-detension" = self-attention; "gallery nonlinearity" = GELU; "askewsky" = Krizhevsky; "Dimitri" = the first author of the 2014 attention paper (caption spelling only, surname not given); "Yeshua NGO" = Yoshua Bengio; "bits" @52:43 = ViTs; "alcohol"/"Alpha gold" = AlphaFold; "Tesla modeling paper" @19:57 likely garbled (he means the 2017 paper); "The Raw operator" @57:07 is a paper's operator name, garbled, do not guess; "auto aggressive" = autoregressive; "Bert" = BERT; "epe tokens" = BPE.
- **nanoGPT training time garbled.** @31:02 says reproducing GPT-2 took "one node of atpus for 38 hours or something like that remember correctly"; the hardware word is garbled and the figure is hedged. The nanoGPT README (github-2025-11-12) says about four days on 8×A100. Do not put the 38-hour number on the artifact page, or flag it as his hedged recollection.
- **Mentions without explanation:** Neural GPU (@58:44), Decision Transformer, Whisper, T5, BERT objectives, rotary/relative encodings, the "200 papers" on efficient attention, minGPT (@1:10:52), Tesla multi-sensor inputs (an anecdote, not a topic).
- **pretraining-and-finetuning** is not fed: finetuning appears only as the contrast to in-context learning (@56:34); put that sentence on in-context-learning.
- The ResNet analogy for in-context gradient descent (@57:38) he labels "much more handwavy"; keep the hedge.
- Granularity: five of the seven new claims are short; merge may fold transformers-are-capable-of-in-context-learning into in-context-learning and transformers-are-flexible-about-their-inputs into ai-has-converged-on-one-architecture. History is proposed as a section of transformer-architecture rather than a new page.
