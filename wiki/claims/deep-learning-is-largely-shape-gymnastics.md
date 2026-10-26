---
type: claim
stated_on: 2022-11-21
confidence: stated
sources: ["[[youtube-2022-11-21-makemore-5-wavenet]]", "[[github-2024-02-20-nn-zero-to-hero-readme]]"]
topic: "[[pytorch]]"
---
# Much of deep-learning development is making tensor shapes work
> "there's a lot of gymnastics around these multi-dimensional arrays" — [[youtube-2022-11-21-makemore-5-wavenet]] @53:24

## Context
He says a ton of the work is making shapes work: whether arrays are 2-D, 3-D or 4-D, which layers take which shapes, NCL versus NLC, viewing and permuting ([[youtube-2022-11-21-makemore-5-wavenet]] @52:51, @53:24). He spends a lot of time babysitting shapes in Jupyter notebooks before moving code to the repository ([[youtube-2022-11-21-makemore-5-wavenet]] @53:24). The lecture itself is the example: the hierarchy is a `view` into (B, T//n, C*n) plus the same Linear layer, and its shape bug was a BatchNorm reducing over the wrong dimensions of a 3-D input ([[youtube-2022-11-21-makemore-5-wavenet]] @32:15, @40:32).
 The Zero to Hero README's description of the lecture lists keeping track of multidimensional tensor shapes, alongside reading a lot of documentation and moving between notebooks and repository code, as part of what a typical deep-learning development process looks like ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 6).

## Related claims
- **Note:** [[treat-broadcasting-with-respect]] is the earlier, narrower warning about one of these shape mechanics; the method he uses for both is [[check-shapes-and-broadcasting]] ([[youtube-2022-11-21-makemore-5-wavenet]] @53:24).
- **Note:** [[pytorch-documentation-is-unreliable]] precedes this in the same closing notes ([[youtube-2022-11-21-makemore-5-wavenet]] @52:51).
