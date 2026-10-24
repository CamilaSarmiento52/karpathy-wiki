---
type: claim
stated_on: 2022-11-21
confidence: stated
sources: ["[[youtube-2022-11-21-makemore-5-wavenet]]", "[[youtube-2024-06-09-reproduce-gpt-2]]"]
topic: "[[pytorch]]"
---
# PyTorch's documentation is unmaintained and will mislead you
> "as far as I can tell no one is maintaining any documentation" — [[youtube-2022-11-21-makemore-5-wavenet]] @52:51

## Context
In his closing notes on what the deep-learning development process looks like, he says PyTorch's documentation is not very good: the team spends its time on hardcore engineering of distributed primitives while the docs are wrong, incomplete and unclear, and you do your best with them ([[youtube-2022-11-21-makemore-5-wavenet]] @52:15, @52:51). It comes right after he says he spends a lot of time in the documentation reading what shapes each layer accepts and what it does ([[youtube-2022-11-21-makemore-5-wavenet]] @52:15).

In the GPT-2 lecture, published 2024-06-09, he repeats the complaint in smaller ways: a comment on DDP's `device_ids` argument is, he says, roughly nonsensical; autocast's rules for what converts to bfloat16 are not documented well; and of several mixed-precision tutorials he recommends one ([[youtube-2024-06-09-reproduce-gpt-2]] @3:00:24, @1:47:23, @1:42:51).

## Related claims
- **Note:** [[pytorch]] collects his earlier, smaller complaints about the same docs; the general one is made here ([[youtube-2022-11-21-makemore-5-wavenet]] @52:51).
- **Note:** [[deep-learning-is-largely-shape-gymnastics]] is the next of the same closing notes ([[youtube-2022-11-21-makemore-5-wavenet]] @53:24).
