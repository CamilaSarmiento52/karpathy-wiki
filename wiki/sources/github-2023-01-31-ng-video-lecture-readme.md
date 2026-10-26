---
type: source
raw_path: raw/github/karpathy__ng-video-lecture.md
published: 2023-01-31
medium: github
summary: "README of ng-video-lecture, the code from the first nanoGPT lecture in his Zero To Hero series, published as a repo so people can hack it and read its git history, with a note that the lecture skipped weight initialisation."
url: https://github.com/karpathy/ng-video-lecture
title: ng-video-lecture README
---
# ng-video-lecture README
Raw: [[raw/github/karpathy__ng-video-lecture]] · Original: https://github.com/karpathy/ng-video-lecture

Dated by the README's last commit (5301c27). The repo's H1 reads "nanogpt-lecture".

## Summary
The repo holds the code written during the first nanoGPT lecture of his Neural Networks: Zero To Hero video series, published on GitHub so people can hack on it and walk through its `git log` (§intro). He adds a caveat: the lecture did not go into model initialisation, which he says is quite important for good performance; the code trains fine but converges more slowly because it starts from a poor spot in weight space (§intro). He points to the `_init_weights` function in nanoGPT's `model.py` as the fix, notes the lecture code names and stores modules differently so it cannot be copy-pasted across, and says he plans a supplementary lecture after which he will push the exact changes (§intro). Until then he keeps the repo almost exactly as covered in the video (§intro).

## Key points
- What the repo is and his initialisation caveat → [[ng-video-lecture]]
- Weight initialisation matters for convergence, and the lecture skipped it → [[weight-initialization]]
- The fix lives in nanoGPT's `_init_weights` → [[nanogpt]]
- Publishing lecture code as a hackable repo with readable history → [[small-hackable-educational-code]]

## Fed pages
- [[ng-video-lecture]]
- [[weight-initialization]]
- [[nanogpt]]
- [[small-hackable-educational-code]]
- [[how-he-explains]]
