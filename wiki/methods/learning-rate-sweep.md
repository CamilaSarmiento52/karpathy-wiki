---
type: method
steps:
  - Reset the parameters
  - Bracket too-slow and exploding rates by hand
  - Build 1,000 exponents from -3 to 0 and take 10 to the power
  - Run 1,000 steps using the i-th rate at step i
  - Plot loss against exponent
  - Pick a value in the valley before instability
sources: ["[[youtube-2022-09-12-makemore-2-mlp]]"]
aliases: [learning rate search, LR range test]
---
# Learning-rate sweep
How he finds a learning rate: sweep exponentially spaced candidates over a short run and read the loss-versus-exponent plot ([[youtube-2022-09-12-makemore-2-mlp]] @47:07, @50:25).

## Steps
1. **Find the range.** Reset the parameters and print the loss every step for a short run to find a reasonable search range ([[youtube-2022-09-12-makemore-2-mlp]] @45:28, @46:01).
2. **Bracket it.** A very low rate barely decreases the loss; around 1 it is unstable; 10 does not work, so the right value is between 0.001 and 1 ([[youtube-2022-09-12-makemore-2-mlp]] @46:01, @46:34, @47:07).
3. **Exponential grid.** Stepping linearly between rates does not make sense; use `torch.linspace` on exponents from -3 to 0 with 1,000 steps and raise 10 to them, so the candidates are exponentially spaced ([[youtube-2022-09-12-makemore-2-mlp]] @47:07, @47:42).
4. **One rate per step.** Index the learning rate by the step number, starting very low and ending at 1, tracking the rate and loss used ([[youtube-2022-09-12-makemore-2-mlp]] @48:14, @48:47).
5. **Plot against the exponent.** Plot losses against the exponent rather than the raw rate; the plot shows nothing happening at low rates, a valley, then instability, and the good setting is in the valley around exponent -1 ([[youtube-2022-09-12-makemore-2-mlp]] @49:52, @50:25).
6. **Pick.** This gave him confidence that 0.1 was a fairly good rate ([[youtube-2022-09-12-makemore-2-mlp]] @50:59).

## Seen in
- [[youtube-2022-09-12-makemore-2-mlp]]
- [[makemore]]
