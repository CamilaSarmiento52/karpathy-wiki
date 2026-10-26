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
- Many weird LLM problems trace back to tokenization, which he would ideally see deleted → [[a-lot-of-llm-oddness-traces-back-to-tokenization]], [[tokenization-free-modeling-would-be-amazing-but-is-unproven]]
- Lecture 8's code is minBPE → [[minbpe]]
- Every lecture ships exercises; work the backprop exercise alongside the video rather than just watching → [[spelled-out-build-from-scratch]]
- Manual backprop builds the competence to debug and innovate → [[understand-backprop-even-with-autograd]]
- Development as reading docs and tracking multidimensional shapes → [[deep-learning-is-largely-shape-gymnastics]]

## Fed pages
- [[nn-zero-to-hero]]
- [[micrograd]]
- [[makemore]]
- [[tokenization]]
- [[spelled-out-build-from-scratch]]
- [[understand-backprop-even-with-autograd]]
- [[deep-learning-is-largely-shape-gymnastics]]
- [[a-lot-of-llm-oddness-traces-back-to-tokenization]]
- [[tokenization-free-modeling-would-be-amazing-but-is-unproven]]
- [[minbpe]]
- [[how-he-explains]]
- [[invite-the-learner-to-try-first]]
