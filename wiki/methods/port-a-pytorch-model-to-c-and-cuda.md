---
type: method
steps:
  - Keep the PyTorch model only as the reference
  - Rewrite each layer's forward pass in explicit PyTorch
  - Derive the backward pass by hand and check it against PyTorch
  - Port forward and backward to C on plain float arrays
  - Pre-plan and allocate all memory once
  - String the layers together and check the program against PyTorch
  - Port each layer to CUDA, trivial kernel first, every version matching
  - Swap in library kernels for matmul and attention
  - Add mixed precision and further optimisations
  - Cut optimisations whose complexity does not pay
  - Scale out to multiple GPUs and nodes
sources: ["[[x-2024-10-02-gpu-mode-talk]]", "[[talk-2024-10-03-cuda-mode-keynote]]", "[[github-2024-09-24-llmc-readme]]"]
aliases: [Port a PyTorch layer to C, llm.c porting process, layer-by-layer port, port PyTorch to C/CUDA]
---
# Port a PyTorch model to C and CUDA
How he built [[llm-c]]: after torch.compile errors he could not solve, he decided to write the whole computation himself, which meant replacing what PyTorch provides, its array, autograd, device, dtype, compile and distributed pieces, and porting GPT-2 one layer at a time from PyTorch to C and then to CUDA ([[talk-2024-10-03-cuda-mode-keynote]] @03:22, @03:55, @05:00; [[x-2024-10-02-gpu-mode-talk]]).

## Steps
1. **PyTorch becomes the reference.** The PyTorch code stops being the thing you work on and becomes only the reference you check correctness against ([[talk-2024-10-03-cuda-mode-keynote]] @05:00).
2. **Explicit forward pass.** For each layer, write the forward pass in explicit PyTorch; for layernorm he had to, because PyTorch's own layernorm is a block that calls into CUDA kernels, and he checked the two were equivalent ([[talk-2024-10-03-cuda-mode-keynote]] @05:32; [[x-2024-10-02-gpu-mode-talk]]).
3. **Backward by hand.** Derive the backward pass with pen and paper, still in explicit PyTorch, and check forward and backward against PyTorch's layer ([[talk-2024-10-03-cuda-mode-keynote]] @06:05; [[x-2024-10-02-gpu-mode-talk]]).
4. **C on float arrays.** Port forward and backward to C, which he says is simpler than you might think: float arrays for inputs, outputs, means, standard deviations, weights and biases, with no tensor abstraction or any other abstraction, fully self-contained ([[talk-2024-10-03-cuda-mode-keynote]] @06:37, @07:09; [[x-2024-10-02-gpu-mode-talk]]). The llm.c README keeps a step-by-step tutorial of this for layernorm ([[github-2024-09-24-llmc-readme]] §tutorial).
5. **Memory once.** In `main`, allocate all memory a single time at the start: parameters and their gradients, AdamW's m and v buffers, and activations with their gradients; from then on it is just data flowing through ([[talk-2024-10-03-cuda-mode-keynote]] @07:09, @07:42; [[x-2024-10-02-gpu-mode-talk]]).
6. **String it together and check.** Call all the forwards, then all the backwards, then the update; with a starter pack of GPT-2 weights, tinyshakespeare and the tokenizer you compile and run one C file, about 2,000 lines as he remembers it, and verify that the PyTorch and C code are identical ([[talk-2024-10-03-cuda-mode-keynote]] @08:15, @08:48; [[x-2024-10-02-gpu-mode-talk]]). The README's unit test does this check on logits, loss and ten training steps ([[github-2024-09-24-llmc-readme]] §test).
7. **CUDA kernels, trivial first.** In `dev/cuda`, write a series of kernels for each layer, versions 1, 2, 3 and on, that match the specification exactly and give the same numbers; the first is usually trivial, parallelising over batch and time with one thread per output element and the C code pasted in, and later ones get elaborate, with warp reductions, shared memory and cache streaming hints ([[talk-2024-10-03-cuda-mode-keynote]] @10:27, @11:00, @11:33). This gets the whole model training on one GPU in fp32 ([[talk-2024-10-03-cuda-mode-keynote]] @13:44; [[x-2024-10-02-gpu-mode-talk]]).
8. **Library kernels.** Switch matmuls from hand-rolled fp32 to cuBLAS, and use cuDNN's flash attention rather than writing your own, which he says would be pretty complicated ([[talk-2024-10-03-cuda-mode-keynote]] @13:44, @14:17; [[x-2024-10-02-gpu-mode-talk]]).
9. **Precision and optimisations.** Decide for every parameter and activation tensor which is float32 and which bfloat16, and convert between them; then kernel fusions, recompute settings, backward-pass memory savings, Packed128, stochastic rounding and full determinism ([[talk-2024-10-03-cuda-mode-keynote]] @14:17, @14:50, @15:58; [[x-2024-10-02-gpu-mode-talk]]).
10. **Cut what does not pay.** CUDA streams to overlap computation caused race conditions, so he deleted them all and made everything single-threaded: too much complexity for not enough gain at that point ([[talk-2024-10-03-cuda-mode-keynote]] @15:25, @15:58).
11. **Scale out.** Add NCCL all-reduce across GPUs and a sharded optimizer state (ZeRO-1), then multi-node synchronisation ([[talk-2024-10-03-cuda-mode-keynote]] @16:31, @17:05, @17:38; [[x-2024-10-02-gpu-mode-talk]]).

## Seen in
- [[llm-c]]
- [[x-2024-10-02-gpu-mode-talk]], [[talk-2024-10-03-cuda-mode-keynote]]
- [[verify-against-a-reference-implementation]], [[verify-gradients-against-pytorch]] — the checks the port relies on
- [[small-hackable-educational-code]] — the complexity budget behind step 10
