---
type: method
steps:
  - Keep the whole thing in one or a few readable files
  - Keep PyTorch as the only dependency
  - Put configuration in the code and argparse, not switches
  - Hold the model to a few hundred lines
  - Give education-only code teeth when it needs them
  - Publish lecture code with its git history
  - Keep published lecture code as it was in the video
sources: ["[[github-2022-11-20-makemore-readme]]", "[[github-2023-01-08-mingpt-readme]]", "[[github-2023-01-31-ng-video-lecture-readme]]"]
aliases: [One hackable file, minimal educational re-implementation, hackable code, educational code]
---
# Small, hackable, educational code
How he writes the repos that accompany his lectures: makemore, he says, is not meant to be a heavyweight library with many switches and knobs but one hackable file, mostly intended for education ([[github-2022-11-20-makemore-readme]] §intro).

## Steps
1. **One file.** makemore is one hackable file, and he says it is mostly intended for educational purposes ([[github-2022-11-20-makemore-readme]] §intro).
2. **One dependency.** PyTorch is the only requirement ([[github-2022-11-20-makemore-readme]] §intro).
3. **Configuration in the code.** Rather than a library with "a billion switches and knobs", he points users to the argparse and the code itself for further training configurations ([[github-2022-11-20-makemore-readme]] §intro, §Usage).
4. **A few hundred lines.** minGPT tries to be small, clean, interpretable and educational, in contrast to implementations he found sprawling; the whole model is about 300 lines and the library three files ([[github-2023-01-08-mingpt-readme]] §intro). He criticises the Hugging Face language-modeling example as full-featured but hard to trace, with large functions mostly unused in the default setting ([[github-2023-01-08-mingpt-readme]] §References).
5. **Know the limit.** Once minGPT was widely referenced, large changes became harder, and education-only code lacked the teeth to reproduce benchmarks, which is why he started nanoGPT ([[github-2023-01-08-mingpt-readme]] §intro).
6. **Publish with the history.** He publishes lecture code as a GitHub repo so people can easily hack it and walk through its `git log` history ([[github-2023-01-31-ng-video-lecture-readme]] §intro).
7. **Leave it as taught.** He keeps the published lecture code almost exactly as it was in the video, deferring the initialisation fix until a follow-up lecture explains it ([[github-2023-01-31-ng-video-lecture-readme]] §intro).

## Seen in
- [[github-2023-01-31-ng-video-lecture-readme]]
- [[ng-video-lecture]]
- [[github-2023-01-08-mingpt-readme]]
- [[mingpt]], [[nanogpt]]
- [[github-2022-11-20-makemore-readme]]
- [[makemore]]
