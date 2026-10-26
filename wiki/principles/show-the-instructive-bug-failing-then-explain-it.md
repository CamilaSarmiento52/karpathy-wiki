---
type: principle
status: promoted
inferred: false
quotes:
  - {text: "you'd expect it to work but it doesn't you actually get garbage", source: "[[youtube-2022-09-07-makemore-1-bigram]]", location: "@46:21"}
  - {text: "try to think figure out why this code could actually result in an error", source: "[[youtube-2024-02-20-gpt-tokenizer]]", location: "@45:16"}
  - {text: "hopefully this helps to scare you that you should have a respect for broadcasting", source: "[[youtube-2022-09-07-makemore-1-bigram]]", location: "@49:08"}
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2024-02-20-gpt-tokenizer]]", "[[youtube-2022-08-16-micrograd]]"]
---
# When a bug is instructive, show it failing, then explain it; keep real mistakes in rather than hide them

> "you'd expect it to work but it doesn't you actually get garbage" — [[youtube-2022-09-07-makemore-1-bigram]] @46:21
>
> "try to think figure out why this code could actually result in an error" — [[youtube-2024-02-20-gpt-tokenizer]] @45:16

## In practice

The deliberate move rests on two lectures. In makemore part 1 he removes `keepdim`, runs the normalisation, gets a wrong result, and asks viewers to think about why before explaining that the broadcast went the wrong way, which he hopes will scare them into respecting broadcasting ([[youtube-2022-09-07-makemore-1-bigram]] @46:21, @49:08). In the tokenizer lecture he flags that his own decode function can throw an error, asks viewers to work out why, shows it failing on token 128, and then explains it through UTF-8's byte layout ([[youtube-2024-02-20-gpt-tokenizer]] @45:16, @45:51).

Keeping real mistakes in is a separate clause, and those mistakes were accidents. In micrograd he forgot to zero the gradients, calls it embarrassing, and says "i could have reshot the whole thing but i think it's pretty funny" ([[youtube-2022-08-16-micrograd]] @2:10:28). Earlier in the same lecture he left another error in for the same reason ([[youtube-2022-08-16-micrograd]] @1:15:05).

When teaching, dropping `keepdim` is a fair deliberate example; skipping `zero_grad` is the bug he made by accident in micrograd, which may still be used as a planted bug if it is labelled that way ([[youtube-2022-09-07-makemore-1-bigram]] @46:21, [[youtube-2022-08-16-micrograd]] @2:10:28). **Note:** when reviewing, the wiki's reading is to reproduce a bug by running the code and show the failing output next to the fixed one, rather than only describe it ([[youtube-2024-02-20-gpt-tokenizer]] @45:16).

## Rests on

- [[spelled-out-build-from-scratch]], [[check-shapes-and-broadcasting]]
- [[forgetting-to-zero-grad-is-a-common-neural-net-bug]], [[a-buggy-neural-net-can-still-train-on-a-simple-problem]], [[treat-broadcasting-with-respect]]

## Sources

- [[youtube-2022-09-07-makemore-1-bigram]]
- [[youtube-2024-02-20-gpt-tokenizer]]
- [[youtube-2022-08-16-micrograd]]
