---
type: claim
stated_on: 2025-10-17
confidence: stated
sources: ["[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]", "[[github-2026-01-31-nanochat-beating-gpt-2]]"]
context: ["[[youtube-2023-11-23-intro-to-llms]]"]
topic: "[[scaling-laws]]"
---
# Progress has come from data, hardware, software and algorithms all improving, with no one of them winning
> "Everything plus 20%." — [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:05:39

## Context
Asked whether the transformer will still be there in ten years, he reasons by what he calls translation invariance in time: in 2015 there were convolutional networks, residual networks were new and the transformer did not exist ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @24:27, @25:05). His bet is that in ten years we are still training giant neural networks with a forward and backward pass and gradient descent, much bigger and somewhat different ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @25:05, @26:54). Reproducing Yann LeCun's 1989 convolutional network, he halved the error with 33 years of algorithms, and further gains needed ten times the data, computational optimisations and longer training with dropout and other regularisation ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @25:42, @26:18). So he expects more data, better hardware, kernels and software, and better algorithms, with "no one of them is winning too much" ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @26:18). Asked about nanochat-versus-nanoGPT-style tweaks, he expects more of the same for the most part: datasets to get much better, hardware, kernels and algorithms too, "nothing dominates" ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:04:30, @1:05:03, @1:05:39).

In the nanochat post of 2026-01-31 he explains nanochat's roughly 600× cheaper GPT-2 the same way: "The gains come from everywhere", better hardware (H100 against TPU v3), software (Flash Attention 3, torch.compile), algorithms (Muon, architectural improvements) and data (FineWeb-edu) ([[github-2026-01-31-nanochat-beating-gpt-2]] §intro).

## Related claims
- **Note:** [[gpt-2-training-cost-falls-to-about-40-percent-a-year]] (2026-01-31) gives the cost figure that this four-way account explains ([[github-2026-01-31-nanochat-beating-gpt-2]] §intro; [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @26:18). No relation is set.
- **Note:** no relation to [[scaling-offers-a-guaranteed-path-to-better-models]]. In 2023 he said scaling parameters and data gives a guaranteed improvement, with algorithmic progress a nice bonus ([[youtube-2023-11-23-intro-to-llms]] @26:02, @27:10); here no single factor wins and algorithms, data and hardware improve about equally ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @26:18). Scaling can be sufficient for some improvement while, historically, other factors contributed as much; the emphasis differs and neither denies the other.
