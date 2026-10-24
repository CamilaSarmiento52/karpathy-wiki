---
type: claim
stated_on: 2022-10-11
confidence: stated
sources: ["[[youtube-2022-10-11-makemore-4-backprop-ninja]]", "[[github-2024-02-20-nn-zero-to-hero-readme]]"]
topic: "[[backpropagation]]"
---
# Autograd being available is no reason to ignore how backpropagation works, because it is a leaky abstraction
> "I'd like to call back propagation a leaky abstraction" — [[youtube-2022-10-11-makemore-4-backprop-ninja]] @00:31

## Context
He says backprop does not make neural networks work magically: you cannot stack arbitrary differentiable Lego blocks and cross your fingers, and if you do not understand its internals it will not work, or not work optimally, and you will need those internals to debug it ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @01:05). He refers to a blog post of his on this from a while ago, and lists examples: saturating nonlinearities killing gradients and dead neurons, which he has already covered, and exploding or vanishing gradients in RNNs, which he is about to cover ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @00:31, @01:37). A code snippet he found in the wild tried to clip the loss when the author meant to clip gradients, which silently zeroed the gradients of outliers; he reads this as the author not understanding backprop ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @02:11). He does not think it is okay to ignore how backprop works because PyTorch or other frameworks offer autograd; micrograd covered it only at the level of scalars, which he does not think is enough ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @02:43). The exercise, he says, makes you better at debugging neural networks and makes everything fully explicit ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @03:16). He acknowledges that writing a backward pass by hand is not recommended today and nobody does it outside exercises, though ten years earlier it was standard ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @03:16, @03:49). Closing, he says that in practice you probably do not want to derive these yourself and should use PyTorch's autograd, but should have the intuition for how gradients flow ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:54:25).
 The Zero to Hero README (2024-02-20 snapshot) describes the same lecture as building competence and intuition for how neural nets are optimised, setting you up to innovate on and debug modern networks more confidently ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 5).

## Related claims
- **Note:** [[micrograd-is-all-you-need-everything-else-is-efficiency]] is the earlier, scalar-level version of the same stance; here he says the scalar engine alone is not enough and moves to tensors ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @02:43).
