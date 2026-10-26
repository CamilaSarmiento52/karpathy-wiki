# Digest: ng-video-lecture README
- raw: raw/github/karpathy__ng-video-lecture.md · published: 2023-01-31 · medium: github · words: 189
- source slug: github-2023-01-31-ng-video-lecture-readme

## Source page
```
---
type: source
raw_path: raw/github/karpathy__ng-video-lecture.md
published: 2023-01-31
medium: github
summary: README of ng-video-lecture, the code from the first nanoGPT lecture in his Zero To Hero series, published as a repo so people can hack it and read its git history, with a note that the lecture skipped weight initialisation.
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
- Weight initialisation matters for convergence, and the lecture skipped it → [[model-initialization-matters-for-good-performance]]
- The fix lives in nanoGPT's `_init_weights` → [[nanogpt]]
- Publishing lecture code as a hackable repo with readable history → [[small-hackable-educational-code]]

## Fed pages
- [[ng-video-lecture]]
- [[model-initialization-matters-for-good-performance]]
- [[nanogpt]]
- [[small-hackable-educational-code]]
```

## Candidates
### artifact: ng-video-lecture
- existing: no
- aliases: [nanogpt-lecture, nanoGPT lecture code, "Let's build GPT" code]  ← the last alias is my label for the lecture, not from this source; drop if merge wants only sourced aliases
- frontmatter: repo_url https://github.com/karpathy/ng-video-lecture · language Python · status active (no deprecation; he says he is keeping it as is)
- statements:
  - Code created in the Neural Networks: Zero To Hero video series, specifically the first lecture on nanoGPT (§intro)
  - Published as a GitHub repo so people can easily hack it and walk through its `git log` history (§intro)
  - He did not cover model initialisation in the lecture; the code trains and works but converges more slowly because it starts in a not-great spot in weight space (§intro)
  - He points to the `# init all weights` comment and the `_init_weights` call in nanoGPT's `model.py` for the proper initialisation (§intro)
  - The lecture code names and stores modules differently from nanoGPT, so the init code cannot be directly copy-pasted (§intro)
  - His plan at the time: publish a supplementary lecture covering initialisation, then push the exact code changes; meanwhile the repo stays almost exactly as covered in the video (§intro)
  - Licence MIT (§License)
- relation to existing pages: links to [[nanogpt]] (the lecture builds toward it; the fix is in its `model.py`). Future link to lecture source `youtube-2023-01-17-gpt-from-scratch` once ingested (not in index); the lecture video predates this README by two weeks.

### claim: model-initialization-matters-for-good-performance
- existing: no
- title as a sentence: Model initialisation is quite important for good performance
- confidence: stated
- quote: "it is quite important for good performance" (§intro)
- stated_on: 2023-01-31
- topic: none existing; could attach to [[gpt-architecture]] (from the minGPT digest) or stand alone
- context: said of the lecture's GPT code, which converges more slowly without the nanoGPT-style `_init_weights` (§intro). Do not generalise beyond "for this kind of model, in his experience".
- relation to existing pages: none. **Note:** the minGPT README's GPT-2 notes record the 1/√N residual-scaling init and the N(0, 0.02) init from GPT-1 ([[github-2023-01-08-mingpt-readme]] §References); a `supports` link is defensible only if merge treats those notes as his view rather than paper summaries.

### method: small-hackable-educational-code
- existing: no (shared with makemore and minGPT digests)
- statements from this source:
  - Publish lecture code as a repo so people can hack it and walk through the `git log` history (§intro)
  - Keep the published code almost exactly as it was in the video, deferring improvements until a follow-up lecture explains them (§intro)

### topic (mention only, not a candidate): neural-networks-zero-to-hero
- The series is named and linked but not explained here. Create the topic when a lecture source is ingested; then add this source as `context`.

## Quotes
- "it is quite important for good performance" (§intro) — 7 words
- "so it is almost exactly what we actually covered in the video" (§intro) — 12 words

## Notes for merge
- Read at commit 5301c27d52dace5699faedb3a67bc29ebfd89ea6 (2023-01-31). The repo H1 is "nanogpt-lecture" while the GitHub name is ng-video-lecture; keep the slug `ng-video-lecture` and put `nanogpt-lecture` in aliases.
- Only two headings: the body before `### License` is §intro; §License.
- The README says "the first lecture on nanoGPT"; it does not name the video or give a date. The lecture candidate slug `youtube-2023-01-17-gpt-from-scratch` is the parent's expectation, not from this source.
- The promised supplementary lecture and code push are stated as plans at snapshot time; do not write that they happened. A later snapshot would be a new source.
- Smallest of the three READMEs: it feeds one artifact, one modest claim and the shared method; it should not create a nanoGPT-lecture topic by itself.
