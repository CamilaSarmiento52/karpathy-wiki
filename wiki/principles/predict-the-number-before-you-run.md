---
type: principle
status: promoted
inferred: false
quotes:
  - {text: "you will have a rough idea for what loss to expect at initialization", source: "[[youtube-2022-10-04-makemore-3-activations-batchnorm]]", location: "@04:28"}
  - {text: "we can actually guess at what the loss should be", source: "[[youtube-2023-01-17-gpt-from-scratch]]", location: "@28:03"}
  - {text: "what do we expect to see before this actually happens", source: "[[youtube-2024-06-09-reproduce-gpt-2]]", location: "@1:04:39"}
  - {text: "your network might actually work", source: "[[youtube-2022-08-16-micrograd]]", location: "@2:13:16"}
sources: ["[[youtube-2022-10-04-makemore-3-activations-batchnorm]]", "[[youtube-2023-01-17-gpt-from-scratch]]", "[[youtube-2024-06-09-reproduce-gpt-2]]", "[[youtube-2022-08-16-micrograd]]"]
---
# Before you run it, say what number you expect; then compare

> "you will have a rough idea for what loss to expect at initialization" — [[youtube-2022-10-04-makemore-3-activations-batchnorm]] @04:28
>
> "what do we expect to see before this actually happens" — [[youtube-2024-06-09-reproduce-gpt-2]] @1:04:39

## In practice

In makemore part 3 the first recorded loss is 27; he says you almost always have a rough idea of the loss to expect at initialization from the loss function and the problem setup, so 27 tells him the initialization is wrong, and he works out the expected value for 27 characters with the viewer ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @04:28). In the GPT lecture he does the same with 65 vocabulary elements: he expects about 4.17, gets 4.87, and reads the gap as initial predictions that are not diffuse enough ([[youtube-2023-01-17-gpt-from-scratch]] @28:03).

He also predicts the shape of a run, not only its first number. Before the first training run in the GPT-2 reproduction he asks what to expect and answers that the loss should come down, but not too much, because many of the 50,257 tokens never occur in the data ([[youtube-2024-06-09-reproduce-gpt-2]] @1:04:39).

The reason is that buggy code can still train. In micrograd a real bug went unnoticed because the problem was simple; he says you may have lots of bugs and the network might still work ([[youtube-2022-08-16-micrograd]] @2:13:16). So when reviewing training or numeric code, state the expected first loss, shape or output, run it, and treat a mismatch as something to explain even if the run "works"; "it trains" is not evidence of correctness on its own ([[youtube-2022-08-16-micrograd]] @2:13:16).

## Rests on

- [[training-diagnostics]], [[diagnose-under-or-overfitting]]
- [[the-hockey-stick-loss-means-training-is-wasting-steps]], [[a-buggy-neural-net-can-still-train-on-a-simple-problem]], [[forgetting-to-zero-grad-is-a-common-neural-net-bug]]
- [[loss-functions]], [[weight-initialization]]

## Sources

- [[youtube-2022-10-04-makemore-3-activations-batchnorm]]
- [[youtube-2023-01-17-gpt-from-scratch]]
- [[youtube-2024-06-09-reproduce-gpt-2]]
- [[youtube-2022-08-16-micrograd]]
