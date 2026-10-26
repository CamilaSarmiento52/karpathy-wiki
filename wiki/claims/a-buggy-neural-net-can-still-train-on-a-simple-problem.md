---
type: claim
stated_on: 2022-08-16
confidence: stated
sources: ["[[youtube-2022-08-16-micrograd]]"]
topic: "[[gradient-descent]]"
supports: ["[[forgetting-to-zero-grad-is-a-common-neural-net-bug]]"]
---
# A buggy neural net can still appear to train when the problem is simple enough
> "your network might actually work" — [[youtube-2022-08-16-micrograd]] @2:13:16

## Context
The un-zeroed grads effectively gave a massive step size that happened to converge fast on his four-example problem; on a harder problem the bug would have prevented good optimisation ([[youtube-2022-08-16-micrograd]] @2:12:42, @2:13:49).

## Related claims
- Supported by [[forgetting-to-zero-grad-is-a-common-neural-net-bug]]: the bug in question ([[youtube-2022-08-16-micrograd]] @2:10:28, @2:11:01).
