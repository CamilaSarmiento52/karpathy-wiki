# Digest: nn-zero-to-hero README
- raw: raw/github/karpathy__nn-zero-to-hero.md · published: 2024-02-20 · medium: github · words: 917
- source slug: github-2024-02-20-nn-zero-to-hero-readme

## Source page
```
---
type: source
raw_path: raw/github/karpathy__nn-zero-to-hero.md
published: 2024-02-20
medium: github
summary: "README of Neural Networks: Zero to Hero, his YouTube course on coding and training neural networks from the basics, listing eight lectures from micrograd to the GPT tokenizer with a short description of each."
url: https://github.com/karpathy/nn-zero-to-hero
title: nn-zero-to-hero README
---
# nn-zero-to-hero README
Raw: [[raw/github/karpathy__nn-zero-to-hero]] · Original: https://github.com/karpathy/nn-zero-to-hero

Dated by the README's last commit (73c3fcc). The whole body sits under one heading, "Neural Networks: Zero to Hero"; locations below are `§intro` plus the lecture number.

## Summary
He describes Zero to Hero as a course on neural networks that starts at the basics, delivered as YouTube videos in which the viewer codes and trains networks along with him; the notebooks built in the videos live in the repo's `lectures/` directory and each lecture has exercises in its video description (§intro). The README lists eight lectures, from building micrograd to building the GPT tokenizer, each with a paragraph on what it covers and links to the video, notebooks and companion repo (§intro, Lectures 1–8). Some descriptions add his framing: the backprop lecture is meant to build intuition for debugging and innovating on modern networks and is not meant to be simply watched (§intro, Lecture 5); the WaveNet lecture shows a typical deep-learning development process of reading documentation and tracking tensor shapes (§intro, Lecture 6). The tokenizer lecture argues that many weird LLM behaviours trace back to tokenization and that ideally someone finds a way to delete that stage (§intro, Lecture 8). The list ends "Ongoing..." (§intro).

## Key points
- The course, its format and its lecture list → [[nn-zero-to-hero]]
- Lectures 1–6 map onto the micrograd and makemore repos → [[micrograd]], [[makemore]]
- The tokenizer as a separate pipeline stage with its own training set, BPE training, encode and decode → [[tokenization]]
- Many weird LLM problems trace back to tokenization, which he would ideally see deleted → [[a-lot-of-llm-oddness-traces-back-to-tokenization]]
- Lecture 8's code is minBPE → [[minbpe]]
- Work the exercise alongside the video rather than just watching → [[spelled-out-build-from-scratch]]
- Manual backprop builds the competence to debug and innovate → [[understand-backprop-even-with-autograd]]
- Development as reading docs and tracking multidimensional shapes → [[deep-learning-is-largely-shape-gymnastics]]
- BatchNorm as the first modern innovation that made deep nets easier to train → [[modern-innovations-make-precise-initialization-less-important]]

## Fed pages
- [[nn-zero-to-hero]]
- [[micrograd]]
- [[makemore]]
- [[tokenization]]
- [[a-lot-of-llm-oddness-traces-back-to-tokenization]]
- [[minbpe]]
- [[spelled-out-build-from-scratch]]
- [[understand-backprop-even-with-autograd]]
- [[deep-learning-is-largely-shape-gymnastics]]
- [[modern-innovations-make-precise-initialization-less-important]]
```

## Candidates
### artifact: nn-zero-to-hero
- existing: no
- aliases: [Neural Networks: Zero to Hero, Zero to Hero, Zero To Hero, nn-zero-to-hero]
- frontmatter: repo_url https://github.com/karpathy/nn-zero-to-hero · language Jupyter Notebook · status active (the list ends "Ongoing...")
- statements:
  - A course on neural networks starting at the basics, as a series of YouTube videos in which you code and train networks together with him (§intro)
  - The notebooks built in the videos are kept in the repo's `lectures/` directory; each lecture has exercises in its video description; he says it may grow into something more respectable (§intro)
  - Lecture 1 builds micrograd and covers backpropagation and training, assuming basic Python and a vague memory of high-school calculus (§intro, Lecture 1)
  - Lecture 2 builds a bigram character-level language model, to be made more complex in later videos up to a Transformer like GPT, focusing on torch.Tensor and the language-modelling framework of training, sampling and loss evaluation (§intro, Lecture 2)
  - Lecture 3 builds an MLP character-level model and introduces machine-learning basics: training, learning-rate tuning, hyperparameters, evaluation, train/dev/test splits, under- and overfitting (§intro, Lecture 3)
  - Lecture 4 looks at activation and gradient statistics, diagnostic tools for network health, why deep nets are fragile to train, and introduces Batch Normalization; residual connections and Adam are left as todos (§intro, Lecture 4)
  - Lecture 5 backpropagates by hand through the 2-layer MLP with BatchNorm, at tensor level rather than micrograd's scalars (§intro, Lecture 5)
  - Lecture 6 deepens the MLP into a tree-like, WaveNet-like (2016) convolutional architecture; causal dilated convolutions are not yet covered (§intro, Lecture 6)
  - Lecture 7 builds a GPT following "Attention is All You Need" and GPT-2/GPT-3, touches on ChatGPT, and has GitHub Copilot help write the GPT; he recommends the earlier makemore videos first (§intro, Lecture 7)
  - Lecture 8 builds the GPT-series tokenizer from scratch, with minBPE as its code (§intro, Lecture 8)
- relation to existing pages: links to the seven existing lecture source pages (see Notes), [[micrograd]], [[makemore]], [[minbpe]].

### topic: tokenization
- existing: yes
- aliases to add: GPT tokenizer, encode/decode
- statements:
  - He calls the tokenizer a necessary and pervasive component of LLMs that translates between strings and tokens, text chunks (§intro, Lecture 8)
  - Tokenizers are a completely separate stage of the LLM pipeline, with their own training sets and training algorithm (Byte Pair Encoding), and after training they implement encode (strings to tokens) and decode (tokens to strings) (§intro, Lecture 8)

### claim: a-lot-of-llm-oddness-traces-back-to-tokenization
- existing: no
- title: A lot of weird LLM behaviours and problems trace back to tokenization
- confidence: stated
- stated_on: 2024-02-20 (README commit date; the lecture is linked but not ingested)
- quote: "a lot of weird behaviors and problems of LLMs actually trace back to tokenization" (§intro, Lecture 8)
- topic: [[tokenization]]
- context: from the lecture description, which also says the lecture discusses why tokenization is at fault and why someone ideally finds a way to delete the stage entirely (§intro, Lecture 8). The README does not list which problems; do not name any.
- relation to existing claims: none in the wiki. Same slug as the parallel tokenizer-lecture digest (`zduSFxRajkE.md`, source `youtube-2024-02-20-gpt-tokenizer`), which proposes this claim and a separate `tokenization-free-modeling-would-be-amazing-but-is-unproven`; this README's "ideally finds a way to delete this stage entirely" belongs on that second claim as supporting evidence from the same day.

### method: spelled-out-build-from-scratch
- existing: yes
- statements:
  - Each lecture ships exercises in its video description (§intro)
  - For the backprop lecture he recommends working the exercise yourself alongside the video, unpausing to see him give the answer when stuck; the video is not meant to be simply watched (§intro, Lecture 5)
  - Lecture 7 asks viewers to watch the earlier makemore videos first, since it takes autoregressive language modelling and tensor basics for granted (§intro, Lecture 7)

### claim: understand-backprop-even-with-autograd
- existing: yes
- relation: supports. The README says manual backprop builds competence and intuition for how nets are optimised and sets you up to innovate on and debug modern networks more confidently (§intro, Lecture 5); the claim page has backprop as a leaky abstraction worth understanding despite autograd ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @00:31). Same lecture, later description; supporting evidence, not a new position.

### claim: deep-learning-is-largely-shape-gymnastics
- existing: yes
- relation: supports. The lecture 6 description lists "keeping track of multidimensional tensor shapes" among what a typical deep-learning development process looks like (§intro, Lecture 6); the claim page quotes the video's "gymnastics around these multi-dimensional arrays" ([[youtube-2022-11-21-makemore-5-wavenet]] @53:24).

### claim: modern-innovations-make-precise-initialization-less-important
- existing: yes
- relation: supports, weakly. The lecture 4 description calls Batch Normalization the first modern innovation that made training deep nets much easier, with residual connections and Adam as later todos (§intro, Lecture 4); the claim page says those innovations make exact initialisation less important ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @36:26). The README speaks of training being easier, not of initialisation; merge may prefer a context sentence over a `supports` link.

## Quotes
- "A course on neural networks that starts all the way at the basics." (§intro)
- "This video is not super intended to be simply watched." (§intro, Lecture 5)
- "the first modern innovation that made doing so much easier: Batch Normalization" (§intro, Lecture 4)
- "keeping track of multidimensional tensor shapes" (§intro, Lecture 6)
- "The Tokenizer is a necessary and pervasive component of Large Language Models (LLMs)" (§intro, Lecture 8)
- "a lot of weird behaviors and problems of LLMs actually trace back to tokenization" (§intro, Lecture 8)
- "why someone out there ideally finds a way to delete this stage entirely" (§intro, Lecture 8)

## Notes for merge
- Location convention: the README's only heading is `## Neural Networks: Zero to Hero` (the repo title) and every lecture is a bold line, not a heading. I used `§intro` for the title section, matching the ng-video-lecture and nanoGPT source pages, plus "Lecture N" for precision. If lint wants the literal heading, use `§Neural Networks: Zero to Hero`.
- The prompt said five lectures already have source pages; the index has seven: Lecture 1 [[youtube-2022-08-16-micrograd]], 2 [[youtube-2022-09-07-makemore-1-bigram]], 3 [[youtube-2022-09-12-makemore-2-mlp]], 4 [[youtube-2022-10-04-makemore-3-activations-batchnorm]], 5 [[youtube-2022-10-11-makemore-4-backprop-ninja]], 6 [[youtube-2022-11-21-makemore-5-wavenet]], 7 [[youtube-2023-01-17-gpt-from-scratch]] (video ids match). Lecture 8 (zduSFxRajkE, "Let's build the GPT Tokenizer") has no source page yet, but a parallel digest exists in this batch (`staging/digests/zduSFxRajkE.md`, slug `youtube-2024-02-20-gpt-tokenizer`); the README commit and the lecture share the date 2024-02-20. The nn-zero-to-hero artifact can link all seven in `## Related`; that is a Note-level connection, cite this README for the listing.
- The batch-1 merge map dropped the topic `neural-networks-zero-to-hero` as mention-only and deferred it to this README. I propose it as an artifact (it is a repo); merge may prefer a topic.
- Lecture 4's description praises BatchNorm as making training easier; [[avoid-batch-normalization-where-possible]] has him telling learners to avoid it. Both can hold (useful innovation, bug-prone in practice); not a contradiction, no link proposed.
- Lecture 7's link to nanoGPT is not in this README; do not add it from here.
- Lecture 6 says WaveNet's hierarchy is implemented with causal dilated convolutions "not yet covered"; the wavenet-hierarchical-model page already covers this from the video.
