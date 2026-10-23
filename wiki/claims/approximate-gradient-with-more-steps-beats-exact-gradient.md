---
type: claim
stated_on: 2022-09-12
confidence: stated
sources: ["[[youtube-2022-09-12-makemore-2-mlp]]"]
topic: "[[gradient-descent]]"
---
# An approximate minibatch gradient with more steps beats an exact gradient with fewer steps
> "It's not the actual gradient direction." — [[youtube-2022-09-12-makemore-2-mlp]] @43:50

## Context
With minibatches the gradient quality is lower and the direction less reliable, but good enough on 32 examples to be useful ([[youtube-2022-09-12-makemore-2-mlp]] @43:50). He says it is much better to have an approximate gradient and take more steps than to evaluate the exact gradient and take fewer ([[youtube-2022-09-12-makemore-2-mlp]] @44:24). Because the minibatch loss is noisy, he evaluates on the full training set to judge progress ([[youtube-2022-09-12-makemore-2-mlp]] @44:24, @44:56).
