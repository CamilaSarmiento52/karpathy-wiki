---
type: artifact
repo_url: https://github.com/karpathy/nn-zero-to-hero
language: Python (Jupyter notebooks)
status: active
sources: ["[[github-2024-02-20-nn-zero-to-hero-readme]]"]
context: ["[[github-2023-07-25-karpathy-profile-readme]]"]
aliases: ["Neural Networks: Zero to Hero", Zero to Hero, nn-zero-to-hero]
---
# nn-zero-to-hero
The repository of Neural Networks: Zero to Hero, which he describes as a course on neural networks starting all the way at the basics: a series of YouTube videos in which you code and train neural networks together with him, with the Jupyter notebooks built in the videos kept in the repo's `lectures/` directory ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro).

## What it demonstrates
- Every lecture has a set of exercises in its video description, and he says the course may grow into something more respectable ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro).
- Lecture 1 builds micrograd and covers backpropagation and training, assuming basic Python and a vague memory of high-school calculus ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 1).
- Lecture 2 builds a bigram character-level language model, to be made more complex in later videos up to a modern Transformer like GPT, focusing on `torch.Tensor` and the language-modelling framework of training, sampling and loss evaluation ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 2).
- Lecture 3 builds an MLP character-level model and introduces machine-learning basics such as learning-rate tuning, hyperparameters, evaluation, train/dev/test splits and under- and overfitting ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 3).
- Lecture 4 examines activation and gradient statistics and diagnostic tools for a network's health, explains why deep nets can be fragile to train, and introduces BatchNorm as the first modern innovation that made that much easier; residual connections and Adam are left as todos ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 4).
- Lecture 5 backpropagates by hand through the two-layer MLP with BatchNorm, at the level of tensors rather than micrograd's scalars ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 5).
- Lecture 6 deepens the MLP into a tree-like convolutional architecture similar to DeepMind's 2016 WaveNet, leaving causal dilated convolutions not yet covered ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 6).
- Lecture 7 builds a GPT following "Attention is All You Need" and OpenAI's GPT-2 and GPT-3, with GitHub Copilot helping write it; he recommends the earlier makemore videos first ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 7).
- Lecture 8 builds the GPT-series tokenizer from scratch ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 8).
- `status: active` rests on the list ending "Ongoing..." at this snapshot ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro).

## Related
- [[micrograd]], [[makemore]] — the companion repos of lectures 1–6
- [[spelled-out-build-from-scratch]] — the teaching method the lectures use
- **Note:** his one-line GitHub profile says he likes deep neural nets; this course is where he teaches them from the basics ([[github-2023-07-25-karpathy-profile-readme]] §intro, [[github-2024-02-20-nn-zero-to-hero-readme]] §intro).
