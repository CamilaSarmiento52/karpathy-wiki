---
type: method
steps:
  - Derive the gradient by hand
  - Bump one input by h and recompute
  - Divide the change by h and compare
  - Rebuild the expression in PyTorch
  - Run forward and backward
  - Compare values and grads
sources: ["[[youtube-2022-08-16-micrograd]]"]
aliases: [inline gradient check, numerical gradient check, verify against PyTorch, PyTorch parity check, derive gradients by shape matching]
---
# Verify gradients against PyTorch
After deriving a gradient by hand he verifies it two ways: numerically, by bumping the input by a small h and reading the change in the output, and against PyTorch, by rebuilding the expression and comparing forward values and gradients ([[youtube-2022-08-16-micrograd]] @37:50, @1:39:28, @1:42:48).

## Steps
1. **Hand-derive, then bump.** After deriving a gradient by hand, bump the input by a small h in a scoped function and print (l2 - l1)/h ([[youtube-2022-08-16-micrograd]] @32:18, @32:51, @33:25).
2. **Inline gradient check.** He names this an inline gradient check: deriving backprop for the intermediates and estimating the derivative numerically with a small step ([[youtube-2022-08-16-micrograd]] @37:50).
3. **Every node.** He applies it to every node in the manual example (d, f, c, e, a, b), accepting small floating-point differences ([[youtube-2022-08-16-micrograd]] @36:47, @37:18, @46:45, @50:03).
4. **Rebuild in PyTorch.** Reproduce the expression with double-precision, single-element tensors with `requires_grad=True` ([[youtube-2022-08-16-micrograd]] @1:40:01, @1:41:08, @1:41:43).
5. **Compare.** Check that the forward output (0.707) and all gradients (0.5, 0, -1.5, 1) agree ([[youtube-2022-08-16-micrograd]] @1:39:28, @1:42:48).
6. **Match the API.** Design the toy library to match PyTorch's API on both the autograd and nn.Module sides; micrograd's test file does the comparison systematically for simple and more complicated expressions ([[youtube-2022-08-16-micrograd]] @1:44:26, @2:18:12, @2:18:45).

## Seen in
- [[youtube-2022-08-16-micrograd]]
- [[micrograd]]
