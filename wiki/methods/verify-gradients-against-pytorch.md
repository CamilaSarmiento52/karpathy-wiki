---
type: method
steps:
  - Derive the gradient by hand
  - Bump one input by h and recompute
  - Divide the change by h and compare
  - Rebuild the expression in PyTorch
  - Run forward and backward
  - Compare values and grads
  - At tensor level, scrutinise the shapes first
  - Derive on a tiny concrete example, then arrange for the shapes to work out
  - Retain intermediate grads and compare exact, approximate and max difference
  - Expect failures on unfinished branches
sources: ["[[youtube-2022-08-16-micrograd]]", "[[youtube-2022-10-11-makemore-4-backprop-ninja]]"]
aliases: [inline gradient check, numerical gradient check, verify against PyTorch, PyTorch parity check, derive gradients by shape matching, check manual gradients against PyTorch, cmp, gradient checking]
---
# Verify gradients against PyTorch
After deriving a gradient by hand he verifies it two ways: numerically, by bumping the input by a small h and reading the change in the output, and against PyTorch, by rebuilding the expression and comparing forward values and gradients ([[youtube-2022-08-16-micrograd]] @37:50, @1:39:28, @1:42:48). At the tensor level, in the fourth makemore lecture, the same habit becomes a `cmp` utility that checks each manual gradient against PyTorch's `.grad`, and a derivation trick of making the shapes work out rather than remembering formulas ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @17:46, @50:01).

## Steps
1. **Hand-derive, then bump.** After deriving a gradient by hand, bump the input by a small h in a scoped function and print (l2 - l1)/h ([[youtube-2022-08-16-micrograd]] @32:18, @32:51, @33:25).
2. **Inline gradient check.** He names this an inline gradient check: deriving backprop for the intermediates and estimating the derivative numerically with a small step ([[youtube-2022-08-16-micrograd]] @37:50).
3. **Every node.** He applies it to every node in the manual example (d, f, c, e, a, b), accepting small floating-point differences ([[youtube-2022-08-16-micrograd]] @36:47, @37:18, @46:45, @50:03).
4. **Rebuild in PyTorch.** Reproduce the expression with double-precision, single-element tensors with `requires_grad=True` ([[youtube-2022-08-16-micrograd]] @1:40:01, @1:41:08, @1:41:43).
5. **Compare.** Check that the forward output (0.707) and all gradients (0.5, 0, -1.5, 1) agree ([[youtube-2022-08-16-micrograd]] @1:39:28, @1:42:48).
6. **Match the API.** Design the toy library to match PyTorch's API on both the autograd and nn.Module sides; micrograd's test file does the comparison systematically for simple and more complicated expressions ([[youtube-2022-08-16-micrograd]] @1:44:26, @2:18:12, @2:18:45).

At tensor level, from the backprop lecture, where the whole MLP backward pass is derived by hand and checked line by line ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @07:46, @1:26:06):

7. **Scrutinise the shapes first.** Before each backward line he writes out the shapes of every tensor involved; a 32×64 reduced to 1×64 in the forward pass tells him there will be a broadcast in the backward ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @22:12, @1:08:38, @1:09:12, @1:18:48).
8. **Tiny concrete example.** He picks a 2×2 or 3×3 case, writes the operation out element by element, differentiates the multiplies and adds as in micrograd, and generalises the pattern; he says he always likes to work with simpler examples ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @14:26, @42:50, @43:23, @45:02).
9. **Make the shapes work out.** He never remembers the matmul backward formulas: dX must have X's shape and must be a matmul of the incoming gradient and the other operand, with a transpose placed so the shapes work out, and there is only one way to do that; for a bias, the shape tells him which axis to sum over ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @49:29, @50:01, @50:37, @51:44, @52:17, @52:54).
10. **Glued expressions on paper.** For batchnorm he does the same with symbols: draw the compute graph, mark which nodes are vectors and which scalars, and backprop in topological order ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:38:50, @1:39:25).
11. **Unmask with non-zero init.** He initialises biases to small random numbers rather than zero, because zeros can mask an incorrect gradient implementation, and keeps a bias before batchnorm, though unnecessary, to have one more gradient to check ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @07:46, @08:20, @08:52).
12. **Retain and compare.** He breaks the forward pass into many intermediate tensors, calls `retain_grad` on them, and a `cmp` utility reports exact equality, `torch.allclose` approximate equality and the maximum absolute difference against `.grad` ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @07:46, @09:26, @09:58, @17:46, @18:19).
13. **Expect failures on half-done branches.** A node fed by two branches fails the check until the second contribution is added, which shows the checker can detect a wrong gradient and does not just say yes ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:03:34, @1:16:31).
14. **Approximate for analytic shortcuts.** The closed-form cross-entropy and batchnorm gradients match only approximately, at about 5e-9 or 1e-9, and he does not know exactly where the differences come from ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:32:09, @1:51:37).
15. **Check inside the loop, then cut autograd.** In the full training loop he runs 100 iterations and breaks to check the gradients against PyTorch before removing `loss.backward()`; historically the equivalent was a numerical gradient checker against the hand-written backward pass ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @06:41, @1:51:04, @1:51:37).

## Seen in
- [[youtube-2022-08-16-micrograd]]
- [[youtube-2022-10-11-makemore-4-backprop-ninja]]
- [[micrograd]]
- [[makemore]]
- [[backpropagation]], [[check-shapes-and-broadcasting]]
- [[verify-against-a-reference-implementation]] — the general parity habit; this page is about gradients
