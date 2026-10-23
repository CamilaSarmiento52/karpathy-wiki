---
type: claim
stated_on: 2022-09-07
confidence: stated
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]"]
topic: "[[regularization]]"
---
# Pushing weights toward zero is equivalent to count smoothing
> "trying to incentivize W to be near zero is basically equivalent to label smoothing." — [[youtube-2022-09-07-makemore-1-bigram]] @1:51:45

## Context
Zero weights give uniform probabilities, just as adding huge counts to the table does ([[youtube-2022-09-07-makemore-1-bigram]] @1:50:40, @1:51:13). The regularization strength controls the amount of counts you add; strong enough and the predictions become uniform ([[youtube-2022-09-07-makemore-1-bigram]] @1:53:26, @1:54:00). What he calls label smoothing here is the technique he called model smoothing earlier in the lecture ([[youtube-2022-09-07-makemore-1-bigram]] @1:01:43, @1:51:45).
