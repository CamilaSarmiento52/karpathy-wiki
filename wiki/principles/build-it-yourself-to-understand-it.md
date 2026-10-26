---
type: principle
status: promoted
inferred: false
quotes:
  - {text: "Build the stuff yourself, but don't allow yourself copy-paste.", source: "[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]", location: "@29:27"}
  - {text: "write our own gpt2 class so that we have full understanding", source: "[[youtube-2024-06-09-reproduce-gpt-2]]", location: "@12:18"}
  - {text: "you will need to understand how it works under the hood", source: "[[youtube-2022-10-11-makemore-4-backprop-ninja]]", location: "@01:05"}
sources: ["[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]", "[[youtube-2024-06-09-reproduce-gpt-2]]", "[[youtube-2022-10-11-makemore-4-backprop-ninja]]", "[[talk-2026-04-29-sequoia-ascent-2026]]"]
---
# To learn something, build it yourself, without copy-paste

> "Build the stuff yourself, but don't allow yourself copy-paste." — [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @29:27
>
> "write our own gpt2 class so that we have full understanding" — [[youtube-2024-06-09-reproduce-gpt-2]] @12:18

## In practice

The rule is about learning. Asked how someone should learn from his nanochat repo, he says to build it yourself without copy-paste, because building from scratch forces you to face what you do not understand and did not know you did not understand ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @29:27). He adds that you should build the code, arrange it and get it to work, rather than write blog posts or slides ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @30:04).

When teaching, he writes the piece himself even when a library already has it. In the GPT-2 reproduction he writes his own GPT-2 class rather than work with the library's modeling file, which he calls too complicated ([[youtube-2024-06-09-reproduce-gpt-2]] @12:18). In makemore part 4 he has the learner backpropagate by hand, because backpropagation is a leaky abstraction you need to understand under the hood to debug a network ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @01:05).

When reviewing, flag code that misuses something the author evidently has not understood (what a call does to memory, gradients or shapes), not API trivia. In 2026 he says he no longer remembers details such as keepdims versus keepdim and does not need to, but you still need the fundamentals, such as whether a view shares storage, so that you do not copy memory around needlessly ([[talk-2026-04-29-sequoia-ascent-2026]] @21:16).

## Rests on

- [[learn-by-building-and-explaining]], [[spelled-out-build-from-scratch]]
- [[if-you-cannot-build-it-you-do-not-understand-it]], [[understand-backprop-even-with-autograd]]
- [[understanding-cannot-be-outsourced]] (context only: the Feynman line he endorses is not his own wording)
- [[backpropagation]], [[ai-for-education]]

## Sources

- [[talk-2025-10-17-dwarkesh-ghosts-not-animals]]
- [[youtube-2024-06-09-reproduce-gpt-2]]
- [[youtube-2022-10-11-makemore-4-backprop-ninja]]
- [[talk-2026-04-29-sequoia-ascent-2026]]
