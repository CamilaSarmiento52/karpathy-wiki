---
type: claim
stated_on: 2022-09-07
confidence: stated
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]"]
topic: "[[bigram-language-model]]"
---
# The counting bigram model and the one-layer neural net are the same model
> "So logits literally becomes the uh the the appropriate row of W." — [[youtube-2022-09-07-makemore-1-bigram]] @1:48:58

## Context
Casting the bigram model as a neural net, he says, ends up in a very similar position by a very different route ([[youtube-2022-09-07-makemore-1-bigram]] @1:03:22, @1:03:55). Gradient training on all bigrams reaches roughly 2.45 to 2.47, the same vicinity as counting, because no extra information is used ([[youtube-2022-09-07-makemore-1-bigram]] @1:44:36, @1:45:08). The explicit counting approach happens to optimise the loss very well without gradients because the bigram setup is so simple ([[youtube-2022-09-07-makemore-1-bigram]] @1:45:39). `W.exp()` is the counts array: counting filled it in directly while gradient descent arrived at it piece by piece following the loss ([[youtube-2022-09-07-makemore-1-bigram]] @1:49:31, @1:50:05). Sampling from the net gives the exact same names as sampling from P ([[youtube-2022-09-07-makemore-1-bigram]] @1:55:39, @1:56:11).
