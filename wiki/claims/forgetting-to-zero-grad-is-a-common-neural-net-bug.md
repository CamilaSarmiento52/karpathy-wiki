---
type: claim
stated_on: 2022-08-16
confidence: stated
sources: ["[[youtube-2022-08-16-micrograd]]"]
topic: "[[gradient-descent]]"
supports: ["[[a-buggy-neural-net-can-still-train-on-a-simple-problem]]"]
---
# Forgetting to zero the gradients before backward is a common, subtle neural-net bug
> "you forgot to zero grad before that backward" — [[youtube-2022-08-16-micrograd]] @2:11:01

## Context
He made the bug on camera while training the micrograd MLP, says it is very common, and that it is number three on a list of most common neural-net mistakes he tweeted long ago ([[youtube-2022-08-16-micrograd]] @2:10:28, @2:11:01). Because every `_backward` does `+=`, grads accumulate across iterations unless reset; the fix is to set every parameter's grad to zero before `backward`, as PyTorch's `zero_grad` does ([[youtube-2022-08-16-micrograd]] @2:11:35, @2:12:09).

## Related claims
- Supports [[a-buggy-neural-net-can-still-train-on-a-simple-problem]]: this very bug still let his four-example net train ([[youtube-2022-08-16-micrograd]] @2:12:42).
