---
type: principle
status: promoted
inferred: false
quotes:
  - {text: "And I encourage you to treat this with respect.", source: "[[youtube-2022-09-07-makemore-1-bigram]]", location: "@44:10"}
  - {text: "we want to make sure that the broadcasting will do what we like", source: "[[youtube-2022-09-12-makemore-2-mlp]]", location: "@28:16"}
  - {text: "we have to scrutinize and be careful with the shapes", source: "[[youtube-2022-10-11-makemore-4-backprop-ninja]]", location: "@22:12"}
  - {text: "I like to be very explicit so that you get error messages", source: "[[youtube-2022-11-21-makemore-5-wavenet]]", location: "@32:49"}
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]", "[[youtube-2022-10-11-makemore-4-backprop-ninja]]", "[[youtube-2022-11-21-makemore-5-wavenet]]", "[[talk-2026-04-29-sequoia-ascent-2026]]"]
---
# Be careful with shapes and broadcasting, and write array code explicit enough that a wrong assumption raises an error

> "we have to scrutinize and be careful with the shapes" — [[youtube-2022-10-11-makemore-4-backprop-ninja]] @22:12
>
> "I like to be very explicit so that you get error messages" — [[youtube-2022-11-21-makemore-5-wavenet]] @32:49

## In practice

The quotes come from his 2022 makemore lectures, all PyTorch tensor work, so the rule is scoped to array code. In makemore part 1 he urges viewers to read the broadcasting semantics and says "And I encourage you to treat this with respect." of broadcasting, then shows how quickly it produces bugs ([[youtube-2022-09-07-makemore-1-bigram]] @44:10). In part 2 he stops at a bias addition to walk a 32 by 100 tensor and a 100-vector through the right-aligned broadcast before trusting it ([[youtube-2022-09-12-makemore-2-mlp]] @28:16).

In part 4, deriving gradients by hand, he points out that two tensors have different shapes (32 by 27 and 32 by 1) and that the backward pass has to account for it ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @22:12). In part 5 he avoids `-1` in a `view` because he likes code explicit enough to raise an error when things do not match his expectation, and he says what shape he expects instead ([[youtube-2022-11-21-makemore-5-wavenet]] @32:49).

When reviewing array code, this means flagging reshapes with an inferred dimension and broadcasts nobody has checked, and suggesting explicit dimensions so a wrong assumption fails loudly ([[youtube-2022-11-21-makemore-5-wavenet]] @32:49). By 2026 he says he hands API-level details (keepdims versus keepdim, dim or axis) to agents but still needs the fundamentals of what the tensor operations do ([[talk-2026-04-29-sequoia-ascent-2026]] @21:16).

## Rests on

- [[check-shapes-and-broadcasting]], [[verify-gradients-against-pytorch]], [[prototype-in-jupyter-then-repo]]
- [[treat-broadcasting-with-respect]], [[deep-learning-is-largely-shape-gymnastics]]
- [[broadcasting]], [[pytorch]]

## Sources

- [[youtube-2022-09-07-makemore-1-bigram]]
- [[youtube-2022-09-12-makemore-2-mlp]]
- [[youtube-2022-10-11-makemore-4-backprop-ninja]]
- [[youtube-2022-11-21-makemore-5-wavenet]]
- [[talk-2026-04-29-sequoia-ascent-2026]]
