---
type: claim
stated_on: 2022-09-07
confidence: stated
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]"]
topic: "[[softmax]]"
---
# Only the forward pass changes on the way to transformers
> "None of this will fundamentally change." — [[youtube-2022-09-07-makemore-1-bigram]] @1:46:46

## Context
Future nets in the series will take more previous characters and be more complex, but will still output logits that go through softmax, negative log likelihood and gradient descent ([[youtube-2022-09-07-makemore-1-bigram]] @1:46:12, @1:46:46). The only change is how the forward pass computes logits from the previous characters, all the way to the transformer ([[youtube-2022-09-07-makemore-1-bigram]] @1:46:46, @1:57:19).
