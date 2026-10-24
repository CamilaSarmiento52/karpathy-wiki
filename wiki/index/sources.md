# Sources

One page per raw file: talks, lectures, posts, READMEs, threads. Alphabetical. Maintained by ingest; do not edit by hand.

- [[blog-2025-12-19-year-in-review-2025|2025 LLM Year in Review]] — six 2025 paradigm changes: RLVR, jagged intelligence, LLM apps, Claude Code, vibe coding, LLM GUI
- [[github-2022-11-20-makemore-readme|makemore README]] — one hackable PyTorch file; bigram to Transformer models for line-per-example generation, CNN in progress
- [[github-2023-01-08-mingpt-readme|minGPT README]] — his ~300-line GPT re-implementation, semi-archived in January 2023 in favour of nanoGPT; his notes on the GPT papers
- [[github-2023-01-31-ng-video-lecture-readme|ng-video-lecture README]] — the GPT lecture's code as a hackable repo with its git log; the lecture skipped weight initialisation
- [[github-2023-07-25-karpathy-profile-readme|karpathy profile README]] — his GitHub profile README: one sentence, he likes deep neural nets
- [[github-2024-02-20-nn-zero-to-hero-readme|nn-zero-to-hero README]] — the Zero to Hero course's lecture list, micrograd to the GPT tokenizer, with his framing of each lecture
- [[github-2024-04-22-minbpe-readme|minbpe README]] — basic and regex BPE tokenizers that train, encode and decode; a GPT-4 wrapper matching tiktoken; exercise and lecture
- [[github-2025-11-12-nanogpt-readme|nanoGPT README]] — his earlier training/finetuning repo, marked deprecated in favour of nanochat
- [[github-2026-07-03-nanochat-readme|nanochat README]] — minimal single-node harness that trains a GPT-2-grade chat model, set by one depth dial
- [[talk-2023-05-19-stanford-cs25-transformers|Stanford CS25: Introduction to Transformers]] — guest lecture: AI converging on the Transformer, attention as message passing, nanoGPT walk-through, in-context learning
- [[talk-2023-05-25-state-of-gpt|State of GPT]] — Microsoft Build 2023: the four-stage assistant recipe, then prompting, tools, finetuning and human-overseen use
- [[talk-2024-03-26-sequoia-making-ai-accessible|Making AI accessible with Andrej Karpathy and Stephanie Zhan]] — Sequoia interview: LLM OS, open weights vs open source, scale, energy efficiency, Elon's style, AlphaGo step two, the ecosystem
- [[x-2024-02-21-technical-accessibility|on technical accessibility]] — micrograd stagnated until the video; build the thing, then build the ramp
- [[x-2025-02-02-vibe-coding|There's a new kind of coding I call "vibe coding"]] — the post that coined vibe coding
- [[x-2026-04-02-llm-knowledge-bases|LLM Knowledge Bases]] — his workflow for an LLM-compiled Obsidian wiki, the pattern this project follows
- [[youtube-2022-08-16-micrograd|The spelled-out intro to neural networks and backpropagation: building micrograd]] — builds a scalar autograd engine from a blank notebook and trains a tiny MLP
- [[youtube-2022-09-07-makemore-1-bigram|The spelled-out intro to language modeling: building makemore]] — bigram character model built by counting and as a one-layer net; they are the same model
- [[youtube-2022-09-12-makemore-2-mlp|Building makemore Part 2: MLP]] — the Bengio 2003 MLP character model; minibatches, learning-rate sweep, train/dev/test splits
- [[youtube-2022-10-04-makemore-3-activations-batchnorm|Building makemore Part 3: Activations & Gradients, BatchNorm]] — initial loss and the hockey stick, saturated tanh, Kaiming init, batch normalization, and his activation/gradient/update-ratio plots
- [[youtube-2022-10-11-makemore-4-backprop-ninja|Building makemore Part 4: Becoming a Backprop Ninja]] — the MLP's backward pass written by hand at tensor level, checked against PyTorch; cross-entropy and batchnorm gradients in closed form
- [[youtube-2022-11-21-makemore-5-wavenet|Building makemore Part 5: Building a WaveNet]] — block size 3 to 8, a WaveNet-like tree of progressive fusion, torch.nn-style containers, a 3-D BatchNorm bug, and his Jupyter-to-repo workflow
- [[youtube-2023-01-17-gpt-from-scratch|Let's build GPT: from scratch, in code, spelled out.]] — a decoder-only Transformer on tiny Shakespeare from an empty file; self-attention derived step by step; pretraining versus finetuning
- [[youtube-2023-11-23-intro-to-llms|Intro to Large Language Models (1hr talk)]] — general-audience talk: two files, lossy compression, finetuning, scaling, tools, System 2, the LLM OS kernel, security
- [[youtube-2024-02-20-gpt-tokenizer|Let's build the GPT Tokenizer]] — byte-level BPE from scratch, GPT-2/GPT-4 regex, tiktoken, special tokens, SentencePiece, and the LLM failures he traces to tokenization
- [[youtube-2025-06-19-software-is-changing|Andrej Karpathy: Software Is Changing (Again)]] — YC keynote on Software 3.0, the LLM OS, partial autonomy and building for agents
