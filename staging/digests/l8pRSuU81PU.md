# Digest: Let's reproduce GPT-2 (124M)
- raw: raw/youtube/l8pRSuU81PU.md · published: 2024-06-09 · medium: youtube · words: 43817
- source slug: youtube-2024-06-09-reproduce-gpt-2

## Source page

```
---
type: source
raw_path: raw/youtube/l8pRSuU81PU.md
published: 2024-06-09
medium: youtube
summary: Four-hour lecture that writes GPT-2 (124M) from scratch in PyTorch, loads OpenAI's released weights to check it, speeds training about elevenfold on one A100, adopts GPT-3 optimisation settings, scales to eight GPUs with DDP, and trains on FineWeb-Edu until it beats the GPT-2 124M checkpoint on HellaSwag.
url: https://www.youtube.com/watch?v=l8pRSuU81PU
title: "Let's reproduce GPT-2 (124M)"
---
# Let's reproduce GPT-2 (124M)
Raw: [[raw/youtube/l8pRSuU81PU]] · Original: https://www.youtube.com/watch?v=l8pRSuU81PU

Many numbers in this lecture come from the GPT-2 and GPT-3 papers, OpenAI's released code,
or hardware datasheets; the pages that cite it say which numbers are the paper's and which
are his own run's.

## Summary
A 4-hour Zero to Hero lecture that reproduces the 124M-parameter GPT-2, which he says now
takes about an hour and about $10 of rented compute (@02:11, @02:45). He starts at the target:
he loads OpenAI's released weights through Hugging Face, writes his own GPT-2 class of under
100 lines that matches its parameter names, and checks that it generates coherent text
(@03:50, @12:50, @27:27, @40:59). He then trains from random weights, adding weight tying and
the GPT-2 initialisation (@1:06:20, @1:13:36), and speeds one training step from about 1,000 ms
to about 93 ms with TF32, bfloat16 autocast, torch.compile, flash attention and a vocabulary
padded to 50,304 (@1:36:41, @1:43:58, @1:48:29, @2:00:09, @2:09:10, @2:14:49). Because the
GPT-2 paper is vague, he takes AdamW betas, gradient clipping, a warmup-plus-cosine learning-rate
schedule, weight decay and a 0.5M-token batch from the GPT-3 paper, simulating the batch with
gradient accumulation and spreading it over eight GPUs with distributed data parallel
(@2:15:20, @2:16:28, @2:21:02, @2:28:53, @2:36:15, @2:46:53). He trains on a 10B-token sample of
FineWeb-Edu, checks validation loss and HellaSwag, and reports beating the GPT-2 124M
checkpoint after 10B tokens and nearly matching GPT-3 124M after an overnight 40B-token run
(@3:12:45, @3:28:13, @3:44:15, @3:49:15). He ends with open issues and points to llm.c and the
build-nanogpt repo (@3:56:27, @4:00:28).

## Key points
- GPT-2 is a decoder-only Transformer with pre-norm LayerNorm, a final LayerNorm, GELU and a clean residual stream; attention is the reduce, the MLP the map → [[transformer-architecture]], [[activation-functions]]
- Learned position embeddings recover sinusoid-like structure; token embedding and output head share one matrix (weight tying) → [[embeddings]]
- GPT-2's initialisation from OpenAI's code (std 0.02) and the GPT-2 paper's 1/√N residual scaling → [[weight-initialization]]
- The GPT-2 vocabulary is 50,000 merges, 256 byte tokens and an end-of-text token → [[tokenization]]
- The speed-up sequence: TF32, bfloat16 autocast, torch.compile, flash attention, nice numbers, fused AdamW, DDP → [[training-efficiency]]
- AdamW settings, gradient clipping, warmup and cosine decay, weight decay and gradient accumulation from the GPT-3 paper → [[gradient-descent]], [[regularization]]
- Expected loss at initialisation, overfitting one batch, watching the gradient norm and validation loss → [[training-diagnostics]], [[diagnose-under-or-overfitting]]
- WebText, Common Crawl, data mixtures and FineWeb-Edu → [[pretraining-data]]
- HellaSwag as a smooth, early-signal eval for small models → [[llm-evaluation]]
- Pretraining alone gives a model that dreams documents; supervised finetuning swaps the dataset → [[pretraining-and-finetuning]]
- His working method for reproducing a released model → [[reproduce-a-published-model]]
- The lecture's repo with one commit per step, and its relation to nanoGPT and llm.c → [[build-nanogpt]], [[nanogpt]], [[llm-c]]

## Fed pages
- [[transformer-architecture]]
- [[activation-functions]]
- [[embeddings]]
- [[weight-initialization]]
- [[tokenization]]
- [[pytorch]]
- [[loss-functions]]
- [[gradient-descent]]
- [[regularization]]
- [[overfitting-and-generalization]]
- [[character-level-language-modeling]]
- [[pretraining-and-finetuning]]
- [[training-efficiency]]
- [[pretraining-data]]
- [[llm-evaluation]]
- [[training-diagnostics]]
- [[diagnose-under-or-overfitting]]
- [[small-hackable-educational-code]]
- [[spelled-out-build-from-scratch]]
- [[prototype-in-jupyter-then-repo]]
- [[reproduce-a-published-model]]
- [[build-nanogpt]]
- [[nanogpt]]
- [[llm-c]]
- [[reproducing-gpt-2-takes-about-an-hour-and-ten-dollars]]
- [[adamw-is-a-bug-fix-of-adam]]
- [[use-torch-compile-by-default]]
- [[memory-access-not-flops-limits-training-speed]]
- [[use-nice-numbers-in-neural-network-code]]
- [[gradient-clipping-is-a-patch-on-deeper-issues]]
- [[batch-size-ramp-is-a-systems-gain-not-an-algorithmic-one]]
- [[inherited-gpt-3-hyperparameters-look-conservative]]
- [[his-gpt-2-reproduction-beat-the-checkpoint-on-fewer-tokens]]
- [[pretraining-gives-a-document-completer]]
- [[gpt-is-not-a-complicated-model]]
- [[pytorch-documentation-is-unreliable]]
- [[attention-is-a-communication-mechanism]]
- [[forgetting-to-zero-grad-is-a-common-neural-net-bug]]
```

## Candidates

### topic: transformer-architecture
- existing: yes
- aliases to add: GPT-2 architecture, pre-norm, clean residual stream, map-reduce view
- statements:
  - The GPT-2 miniseries runs from 124M to 1,558M parameters; he says the parameter table in the GPT-2 paper is wrong and points to OpenAI's repo noting the error (@01:05).
  - The 124M model has 12 layers and 768 channels (@01:38); these are properties of the released model, not his choice.
  - GPT-2 is a decoder-only Transformer: the original Transformer's encoder and the cross-attention that used it are removed (@13:55).
  - Per the GPT-2 paper, the layer norms move before the attention and MLP, and an extra layer norm is added before the final classifier (@14:29, @16:48).
  - The final language-model head projects 768 channels to the 50,257-token vocabulary and GPT-2 uses no bias there (@16:48).
  - He wants a single clean residual stream from supervision down to the tokens, because addition passes gradients to both branches unchanged; normalisations inside the residual path are undesirable (@18:28, @19:04).
  - Attention is where the 1,024 tokens communicate and exchange information, a pooling or weighted-sum reduce; the MLP acts on each token individually, a map; the Transformer is a repeated map-reduce in which each block refines the residual stream (@19:38, @20:12).
  - He implements all heads in one attention module, treating the head count as a batch dimension; it is mathematically equivalent to the earlier concatenated-heads version, only more efficient in PyTorch (@24:38, @25:46, @26:20, @26:53).
  - His complete GPT-2 implementation is under 100 lines, against roughly 2,000 lines in Hugging Face's `modeling_gpt2.py` (@27:27).
  - GPT-2 and GPT-3 architectures are very similar; the main change is context length from 1,024 to 2,048, and GPT-3 was trained longer on more data, reaching 175B parameters against GPT-2's 1.6B (his summary of the papers) (@2:15:55, @2:16:28).
  - To be faithful to GPT-3 one would set sequence length 2,048 and micro-batch 32 so that a step stays at about half a million tokens (@3:52:03).
- relation: this source repeats the attention/MLP split described in the GPT lecture ([[youtube-2023-01-17-gpt-from-scratch]] @1:25:52) and adds the map-reduce framing; see the claim relation below.

### topic: activation-functions
- existing: yes
- aliases to add: GELU, tanh-approximate GELU, SwiGLU
- statements:
  - The GPT-2 MLP is two linear layers around a GELU, using the tanh approximation (@20:46).
  - GELU is like a smoother ReLU without an exactly flat tail at zero; it comes from the "Gaussian error linear units" paper (@21:18).
  - As far as he can tell, the approximate version exists because the erf needed for exact GELU was very slow in TensorFlow at the time, and BERT and GPT-2 picked it up; today he expects no big difference and would prefer the exact version, but keeps the approximation to reproduce GPT-2 exactly (@21:51, @22:25).
  - GELU always contributes a local gradient, so it avoids the dead-ReLU problem where activations in the flat region get exactly zero gradient (@22:57).
  - More modern networks such as Llama 3 change this nonlinearity again, to SwiGLU and variants (@23:31).

### topic: embeddings
- existing: yes
- aliases to add: weight tying, tied embeddings, shared input-output embedding, learned position embeddings
- statements:
  - In the released GPT-2 weights the token embedding is 50,257 × 768 and the position embedding covers 1,024 positions, each a learned 768-dimensional vector (@06:06, @07:13).
  - Plotted, the learned position embeddings show sinusoid-like structure; their jaggedness suggests to him the model was somewhat undertrained, and since they start as random noise the smooth structure falling out of optimisation is impressive (@08:19, @09:30, @10:03).
  - In the original Transformer paper the positional encodings were, if he remembers correctly, fixed sinusoids; in GPT-2 they are trained parameters, which seems to work about as well (@10:03, @10:37).
  - In GPT-2 the token embedding at the bottom and the language-model head at the top are the same tensor: identical shape, identical values and the same data pointer (@1:06:53, @1:07:27, @1:07:58).
  - This weight tying comes from the "Attention is all you need" paper and a 2017 paper it cites; the intuition is that semantically similar tokens should be close in embedding space and should also get similar output probabilities (@1:07:58, @1:08:34, @1:09:07).
  - The cited paper observed output embeddings behave like word embeddings and found much better performance when tying them (his summary of that paper) (@1:09:41).
  - He could not find the tying in Hugging Face's implementation but found it in OpenAI's original TensorFlow GPT-2 code, where the token embedding is reused to compute the logits and gets gradient from both ends (@1:10:14, @1:10:46, @1:11:19).
  - Tying saves about 40M of the 124M parameters, roughly 30%, which may be one reason it helps when training is short (@1:13:03).

### topic: weight-initialization
- existing: yes
- aliases to add: GPT-2 initialization, residual scaling, 1/sqrt(N) init, NANOGPT_SCALE_INIT
- statements:
  - The GPT-2 and GPT-3 papers are not explicit about initialisation, so he reads it from OpenAI's released code: normal weights with std 0.02, zero biases, token embeddings at 0.02 and position embeddings at 0.01 (@1:13:36, @1:14:09).
  - He uses 0.02 for both embeddings; zero bias is not PyTorch's default, which is uniform; LayerNorm's default scale 1 and offset 0 is what he wants (@1:15:16, @1:15:49).
  - 0.02 is roughly consistent with Xavier-style 1/√(fan-in) for GPT-2's widths (about 0.03 for 768, 0.02 for 1,600), though ideally the scale would grow with model size (@1:16:23, @1:16:59).
  - The GPT-2 paper scales residual-layer weights at initialisation by 1/√N, N the number of residual layers (paper's statement) (@1:16:59).
  - His demonstration: adding 100 unit-Gaussian contributions to a residual stream grows its standard deviation to about 10, and scaling each by 1/√n brings it back to about 1 (@1:18:05, @1:18:37, @1:19:14).
  - He flags the projection layers with a `NANOGPT_SCALE_INIT` attribute and uses 2 × n_layer because each block adds to the residual path twice, once from attention and once from the MLP (@1:19:48, @1:20:59).
  - Because of weight tying the shared tensor is initialised twice with the same 0.02, which he leaves alone (@1:20:59, @1:21:33).
- relation: the minGPT README recorded that he could not find the 1/√N residual initialisation in OpenAI's GPT-2 code ([[github-2023-01-08-mingpt-readme]] §References (GPT-2)); here he implements it from the GPT-2 paper. Not a contradiction; a reviewer may want a Note.

### topic: tokenization
- existing: yes
- aliases to add: GPT-2 tokenizer, tiktoken, end-of-text token
- statements:
  - The GPT-2 vocabulary of 50,257 is 50,000 BPE merges, 256 byte tokens and one special end-of-text token that delimits documents and can start generation (@27:59, @28:35).
  - He tokenizes with OpenAI's tiktoken GPT-2 encoding (@35:29).
  - The GPT-2 tokenizer compresses English roughly 3:1, so 1,000 characters is about 300 tokens; tiny Shakespeare's roughly 1M characters became 338,000 tokens (@46:06, @1:05:47).
  - In the FineWeb-Edu preprocessing each document starts with the end-of-text token (id 50256), even though it is called end of text (@3:15:31).
  - Tokens are stored as uint16 because GPT-2's maximum token id is well below 65,535 (@3:16:03, @3:16:39).
  - He points to his separate tokenization video for detail (@06:39).

### topic: pytorch
- existing: yes
- aliases to add: torch.compile, autocast, scaled_dot_product_attention, torchrun, state_dict, device
- statements:
  - He uses Hugging Face Transformers to get GPT-2 in PyTorch because the original code is TensorFlow, which he says is not used as much anymore; he likes PyTorch a lot more (@03:50, @04:23).
  - Some TensorFlow-derived weights are transposed relative to what PyTorch wants, so he hardcodes which to transpose when loading (@29:45).
  - He is not sure `model.eval()` does anything for this model, since it has no dropout or batchnorm, but calls it as good practice (@33:46, @34:20).
  - `torch.no_grad()` tells PyTorch no backward will follow, so it need not cache intermediates (@37:07, @37:39).
  - He auto-detects the best available device: CPU, then CUDA, then MPS on Apple silicon (@43:15, @43:49).
  - `module.to(device)` moves a module in place, but `tensor.to(device)` returns a new tensor, a bug he hit on camera (@1:00:07, @1:00:42).
  - `loss.item()` ships the single-element tensor back to the CPU as a float (@59:00).
  - Without `torch.cuda.synchronize()` the CPU only queues GPU kernels, so timings are wrong (@1:33:17, @1:33:50).
  - He writes the learning-rate schedule himself rather than using PyTorch's scheduler, because it is five lines he fully understands and he dislikes abstractions he cannot see into, calling it personal style (@2:22:45).
  - He keeps a separate `torch.Generator` for sampling so it does not disturb the training RNG, seeded differently per rank (@3:26:35, @3:27:09).
  - torch.compile broke his sampling and HellaSwag code with an error he could not resolve, so he disabled it for those runs (@3:27:09, @3:38:55).
  - To resume training you must save the optimizer state, AdamW's m and v buffers, and think through RNG state, not only the model's state dict (@3:53:43, @3:54:15).

### topic: loss-functions
- existing: yes
- statements:
  - `F.cross_entropy` does not take B×T×vocab inputs, so logits are flattened to (B·T, vocab) and targets to B·T (@53:55, @54:28).
  - Cross-entropy, like MSE, reduces by mean by default; this is why gradient accumulation must divide the loss by the number of steps (@2:40:49, @2:43:37, @2:44:10).

### topic: gradient-descent
- existing: yes
- aliases to add: AdamW, Adam, learning-rate schedule, cosine decay, warmup, gradient clipping, gradient accumulation, batch size
- statements:
  - He switches from SGD to AdamW, which keeps first- and second-moment buffers (something like momentum and something like RMSProp), normalises each gradient element and optimises language models faster; he treats it as a black box here (@56:46, @57:19, @57:51).
  - `backward()` always adds to `.grad`, so gradients must be zeroed first (@58:28).
  - 3e-4 is a pretty good default learning rate for early debugging (@1:01:14).
  - The GPT-2 paper is vague on optimisation and OpenAI released only inference code, so he follows the GPT-3 paper; GPT-2 has weights but no details, GPT-3 details but no weights (@2:15:20, @2:15:55).
  - GPT-3 paper settings he adopts: Adam β1 0.9, β2 0.95, ε 1e-8; clip the global gradient norm at 1.0 (@2:16:28, @2:17:02).
  - Clipping computes the square root of the sum of all squared gradients and caps it, guarding against a bad batch shocking the model (@2:17:37, @2:18:12).
  - GPT-3 paper schedule: linear warmup over the first 375M tokens, cosine decay to 10% over 260B tokens, then training continues at 10% (paper's numbers) (@2:21:02, @2:21:35).
  - The GPT-3 table gives a maximum learning rate of 6e-4 for the 12-layer, 768-wide "small" model, which he adopts (@2:23:19).
  - His schedule warms up from a small nonzero rate and decays to 10% at the last step, unlike GPT-3's 300B-token horizon where decay ends at 260B; he does not think it matters much (@2:24:26, @2:24:59, @2:25:33).
  - Which schedule to use is up to you; cosine was popularised by GPT-2 and GPT-3, and schedules are an active research area (@2:26:05).
  - He skips the GPT-3 paper's gradual batch-size ramp (see claim) (@2:26:05, @2:26:38).
  - GPT-3 samples data without replacement until an epoch boundary, which his loader already does (@2:28:21).
  - In the GPT-3 table bigger networks use lower learning rates and bigger batches; the 124M model uses about 0.5M tokens per batch (paper) (@2:35:04, @2:35:40).
  - He wants that batch size because batch size is coupled to the other optimisation hyperparameters (@2:36:15).
  - Gradient accumulation simulates any batch serially: he sets 2^19 = 524,288 tokens, runs 32 forward-backward passes of 16 × 1,024 tokens, and steps once, about 3 seconds per step on one GPU (@2:36:48, @2:37:23, @2:37:58, @2:38:32).
  - The naive version is wrong: summing gradients over micro-steps drops the mean's normaliser, so the loss must be divided by the accumulation steps; he shows this on a toy MSE example (@2:39:41, @2:41:57, @2:42:30, @2:43:04, @2:44:45).
  - With accumulation, the micro-batch size B becomes purely a performance setting; any B should give the same optimisation up to floating point (@2:46:21).
  - He says the relationships between weight decay, learning rate, batch size and Adam's parameters are complicated, and he is mostly copying OpenAI's settings (@2:33:54, @2:34:29).

### topic: regularization
- existing: yes
- statements:
  - The GPT-3 paper uses weight decay 0.1; AdamW's PyTorch default is 0.01 (@2:28:53, @2:29:27).
  - He decays only 2-D tensors, the matmul weights and embeddings, and not biases or LayerNorm parameters (@2:30:02, @2:30:34).
  - Weight decay pulls weights down so the network spreads work over more channels rather than letting any one weight grow large (@2:30:34, @2:31:07).
  - In his run, 50 tensors were decayed and 98 were not, the non-decayed ones holding only about 100,000 parameters (@2:32:47).

### topic: overfitting-and-generalization
- existing: yes
- statements:
  - With roughly infinite data he expects train and validation loss to be about the same; a validation split matters more in multi-epoch training, where a big model may memorise (@3:24:20, @3:24:55, @3:25:28).
  - He also evaluates OpenAI's GPT-2 124M on the FineWeb-Edu validation split as a reference, while noting it is not a fair comparison because GPT-2 trained on a different distribution (@3:24:20, @3:24:55).

### topic: character-level-language-modeling
- existing: yes (alias "sampling")
- statements:
  - His sampling loop takes only the last position's logits, applies softmax and top-k with k = 50, the Hugging Face pipeline default, which keeps the model from sampling rare tokens and going off the rails (@37:39, @38:13, @38:45).
  - His samples did not match the Hugging Face pipeline's; replicating the loop with the Hugging Face model directly gave the same results as his, so he concludes his model is correct and the pipeline does something extra (@40:26, @40:59).
- note: the page is framed around characters; merge may prefer a sentence on [[pytorch]] or a broader sampling home.

### topic: pretraining-and-finetuning
- existing: yes
- aliases to add: supervised fine-tuning, SFT
- statements:
  - Everything built is only pretraining: the model dreams documents and you cannot talk to it like ChatGPT (@3:55:21).
  - Supervised finetuning is not much more complicated: swap in a conversational dataset with a user-assistant structure and continue training, filling in user tokens and sampling assistant tokens (@3:55:54).

### topic: training-efficiency
- existing: no (coarse home for the whole speed-up sequence; DDP included as a section)
- aliases: mixed precision, TF32, bfloat16, bf16, autocast, torch.compile, kernel fusion, flash attention, nice numbers, vocab 50304, memory bound, GPU memory hierarchy, tensor cores, fused AdamW, distributed data parallel, DDP, tokens per second
- statements:
  - Start from what the hardware offers and whether you are using it; his box has eight A100 SXM 80GB GPUs, rented from Lambda Labs, which he discloses sponsors his work (@1:22:39, @1:23:11).
  - PyTorch defaults to float32 for parameters and activations, which he says is far more precision than deep learning needs (@1:23:43, @1:24:17).
  - A100 datasheet figures he reads: about 19.5 TFLOPS in FP32, about 8× that with TF32, about 16× (312 TFLOPS) with FP16/BF16; the sparsity figures do not apply; INT8 is for inference because training needs floats to match normal distributions (@1:24:50, @1:25:25, @1:25:58, @1:26:31).
  - Many training workloads are memory-bound: tensor cores wait for data, and 60% utilisation counts as doing extremely well (@1:27:04, @1:27:38).
  - A tensor core is an instruction for a small 4×4 matrix multiply; nearly all the Transformer's work is matrix multiplies, and at 124M the 768-to-50,257 classifier dominates (@1:28:12, @1:28:45, @1:29:21).
  - TF32 keeps FP32's sign and 8 exponent bits but truncates the mantissa inside the instruction (19 of 32 bits), invisibly to the code; empirically he cannot tell the difference (@1:31:01, @1:31:36, @1:32:09).
  - His baseline with batch 16 and sequence 1,024 was about 1,000 ms per step; he reports tokens per second as the objective throughput measure (@1:34:24, @1:36:09, @1:36:41).
  - One line, `set_float32_matmul_precision('high')`, gave about 3× (1,000 to about 300 ms), not 8×, because the workload is still memory-bound on FP32 data (@1:36:41, @1:38:24, @1:38:59).
  - BF16 keeps FP32's exponent range and drops more mantissa; FP16 reduces range and needs gradient scalers, which BF16 (from Ampere) avoids (@1:40:07, @1:40:40, @1:41:12, @1:41:45, @1:42:18).
  - Following PyTorch guidance, he wraps only the forward pass and loss in `torch.autocast` to bfloat16, leaving backward and optimizer step alone (@1:42:51, @1:43:25, @1:43:58).
  - Under autocast the logits become bfloat16 while parameters stay float32; matrix multiplies are converted but operations like softmax, layer norm and the loss may stay in float32 (@1:44:32, @1:45:06, @1:45:41, @1:46:15).
  - BF16 took his step from about 333 to 300 ms and throughput from about 50,000 to 55,000 tokens per second; he accepts slightly less precision because you can train longer to make up for it (@1:46:51, @1:47:57).
  - torch.compile, a compiler for neural networks like GCC for C/C++, took the step from 300 to 129 ms, about 2.3× from one line (@1:48:29, @1:49:35).
  - It removes the Python interpreter from the forward pass and fuses kernels: his GELU example shows elementwise operations making repeated trips between GPU memory (HBM) and the chip, which fusion replaces with one round trip (@1:50:43, @1:51:15, @1:53:28, @1:54:36, @1:55:09).
  - On-chip memory (L1, L2, registers, SRAM) is very fast but only tens of megabytes; HBM is tens of gigabytes but expensive to reach (@1:57:23, @1:58:28, @1:59:03).
  - Flash attention (Stanford, 2022) is a kernel fusion torch.compile cannot find because it needs an algorithmic rewrite; it does more FLOPs but the paper cites up to 7.6× speed, since it never materialises the T×T attention matrix in HBM (@2:00:09, @2:01:13, @2:01:48, @2:02:23).
  - It rests on the online softmax trick from a 2018 NVIDIA paper (@2:02:57, @2:03:32, @2:04:08).
  - Swapping the four attention lines for `F.scaled_dot_product_attention` took the step from about 130 to 96 ms with the same loss (@2:05:15, @2:05:49, @2:06:21).
  - Padding the vocabulary from 50,257 to 50,304 adds FLOPs but took the step from 96.5 to 93 ms, because CUDA kernels work in power-of-two block tiles and handle leftovers with slow boundary kernels; the extra tokens are never used and are driven to zero probability (@2:09:10, @2:10:51, @2:11:25, @2:12:33, @2:13:08, @2:13:42).
  - On PyTorch nightly the gain was 4%; on PyTorch 2.3.1 or earlier he says it would be about 30% (@2:14:16).
  - Overall he went from about 1,000 to about 93 ms per step, about 11× (@2:14:49).
  - Fused AdamW updates all parameters in one kernel; he does not know why it is not the default; it took the step from 93 to 90 ms (@2:31:41, @2:32:13, @2:33:20).
  - Distributed data parallel launches one process per GPU via `torchrun`; each knows its rank, local rank and world size, works on different data, and gradients are averaged (@2:47:27, @2:48:00, @2:48:34, @2:49:07).
  - DDP's backward calls all-reduce to average gradients across ranks and can overlap communication with the backward pass (@3:00:59, @3:01:34).
  - With gradient accumulation he syncs only on the last micro-step by toggling `require_backward_grad_sync` directly rather than using the `no_sync` context manager, which he calls a naughty thing to do (@3:02:40, @3:03:14, @3:03:48, @3:04:23).
  - The logged loss must also be all-reduced, and the data loader strides by rank (@2:57:35, @2:58:10, @3:05:31, @3:06:38).
  - On eight GPUs he reached about 1.5M tokens per second (@3:07:44, @3:21:29).
  - Single- and multi-GPU numbers differ slightly because the loader wraps differently; with a small total batch they match (@3:08:51, @3:09:24, @3:09:57).
  - On FineWeb-Edu with micro-batch 64 per GPU no accumulation was needed; a step took about 330 ms and the 19,073-step run about 1.7 hours (@3:20:45, @3:21:29, @3:22:06).
  - In llm.c, his CUDA implementation ran at about 223,000 tokens per second against about 185,000 for the PyTorch version on one GPU, with identical losses and norms; he is not sure he squeezed the PyTorch side fully (@3:58:46, @3:59:19).
- relation: Note-level link only to [[micrograd-is-all-you-need-everything-else-is-efficiency]] (2022 claim that everything beyond micrograd is efficiency); this lecture's second hour is that efficiency. Do not set supports without a reviewer's agreement.

### topic: pretraining-data
- existing: no (if merge prefers fewer pages, a section on [[pretraining-and-finetuning]]; other batch sources likely discuss FineWeb too)
- aliases: FineWeb, FineWeb-Edu, WebText, OpenWebText, Common Crawl, data mixtures, RedPajama, SlimPajama
- statements:
  - Per the GPT-2 paper, WebText was built from Reddit outbound links with at least 3 karma, 45M links and 40 GB of text; it was never released, and OpenWebText attempts to reproduce it (@3:09:57, @3:10:32).
  - Common Crawl is extremely noisy, "much worse than you think", mostly ad spam, tables and stock tickers, so people filter it heavily and train on curated mixtures (@3:11:05, @3:11:38).
  - GPT-3's mixture, never released, added WebText, books and Wikipedia to Common Crawl (@3:11:38).
  - He names RedPajama and its cleaned, deduplicated SlimPajama subset as representative of such mixtures (@3:11:38, @3:12:12).
  - FineWeb filters Common Crawl to 15T tokens; FineWeb-Edu is a 1.3T educational and 5.4T high-educational subset (Hugging Face's figures as he reads them) (@3:12:12, @3:12:45).
  - He uses its 10B-token sample because in his previous experiments that suffices to get close to GPT-2 performance (@3:13:17, @3:13:50).
  - The FineWeb-Edu filters were applied, he believes, with Llama 3 70B judging which content is educational (@3:14:58).
  - He shards it into 100 numpy files of 100M tokens, the first being validation (@3:16:39, @3:17:14, @3:17:48).
  - He suspects the 10B sample was not properly shuffled, giving his loss curve a periodicity he does not fully understand (@3:46:29, @3:47:04).
  - For multi-epoch runs one should permute documents within shards each epoch, and possibly the shards, because document order is a spurious correlation (@3:49:49, @3:50:22).
  - Possible reasons his model beat GPT-2 on fewer tokens include FineWeb-Edu being English-only with little math and code, and today's data getting more care over deduplication and quality filtering than early WebText (@3:45:24, @3:48:11).

### topic: llm-evaluation
- existing: no
- aliases: HellaSwag, evals, Eleuther evaluation harness, early signal, validation loss as eval
- statements:
  - HellaSwag (2019) is a sentence-completion multiple-choice set with one natural continuation and wrong options drawn from ActivityNet and WikiHow contexts (@3:28:13, @3:28:47, @3:29:22, @3:29:55).
  - The wrong options were generated adversarially by language models to be hard for models but easy for humans; per the paper, humans scored 95% and the best models of the time 48% (@3:30:32).
  - Today models score about 96%, so he considers it crushed, with the last points likely dataset errors (@3:31:05).
  - People like it because it is smooth and gives early signal: small models start at the 25% chance level and improve slowly; it appears in the GPT-3 paper, not GPT-2 (@3:31:05, @3:31:39, @3:32:15).
  - Small models cannot do multiple choice with labels, so he scores each option as a token completion and picks the lowest average loss, which he believes is how GPT-3 did it; seeing all options at once is an easier format (@3:32:47, @3:33:55, @3:34:29, @3:35:02).
  - His script scores GPT-2 124M at 29.55% and GPT-2 XL at about 49%; the Eleuther harness gets slightly different numbers, possibly from using multiple choice (@3:37:16, @3:37:48).
  - HellaSwag might have leaked into FineWeb's training data; he hopes Hugging Face deduplicated against it but cannot be sure, so it is not a perfect eval (@3:45:57, @3:46:29).
  - Saving checkpoints lets you evaluate more carefully later, for example with the Eleuther harness on math, code or other languages (@3:54:47, @3:55:21).

### topic (existing method): training-diagnostics
- existing: yes
- statements:
  - With 50,257 tokens he expects an initial loss of -ln(1/50257) ≈ 10.82 and saw about 11, so the initial distribution is roughly diffuse (@55:37, @56:11).
  - Early loss drops come cheaply from pushing down tokens that never occur in the data (@1:04:39, @1:05:12).
  - He always visualises the gradient norm from clipping: well-behaved is good, climbing or spiking signals instability (@2:18:49).
  - In his run the norm started around 30 and settled below 1; a sequence of 28, 6, 2, then 10 struck him as a little funky but not insane (@2:20:30).
  - He evaluates validation loss every 100 (later 250) steps over about 20 batches, samples text periodically, and logs train loss, validation loss and HellaSwag to a text file he plots (@3:23:11, @3:23:47, @3:39:28, @3:43:03).
  - He reads sample quality over training: still garbled at step 1,000, more coherent by step 10,000 (@3:26:00, @3:41:45).

### method (existing): diagnose-under-or-overfitting
- existing: yes (alias "overfit a single batch")
- statements:
  - Before real training he overfits a single 4 × 32 batch until the loss is very low, showing the Transformer can memorise it (@1:00:42, @1:01:14).

### method (existing): small-hackable-educational-code
- existing: yes
- statements:
  - He made git commits every time he added something and releases the repo from scratch to the end, documented in its commit history (@3:27:41).
  - He prefers a few lines he fully understands over library abstractions (@2:22:45).

### method (existing): spelled-out-build-from-scratch
- existing: yes
- statements:
  - He writes the GPT-2 class from scratch rather than using `modeling_gpt2.py`, which he finds too complicated, to have full understanding (@12:18, @12:50).
  - He debugs the gradient-accumulation bug on a toy MSE network in a notebook before fixing the real code (@2:39:41, @2:40:15).

### method (existing): prototype-in-jupyter-then-repo
- existing: yes
- statements:
  - He runs Jupyter inside VS Code to keep one interface, and runs `train_gpt2.py` from the terminal on a cloud box he connects VS Code to (@05:32, @1:23:11, @30:18).

### method: reproduce-a-published-model
- existing: no (fallback: steps on [[spelled-out-build-from-scratch]])
- aliases: start at the target, load the released weights first
- steps (each cited):
  - Load the released checkpoint and sample from it to see the target (@03:18, @11:44).
  - Write your own model class matching the reference's parameter names so the weights port over (@15:04, @27:27).
  - Load the weights into your class and check that it generates coherent text, confirming it is the same model family (@12:50, @13:22, @40:59).
  - Re-initialise from random and train, aiming to beat the checkpoint (@41:32, @13:22).
  - Take architecture from the reference model and optimisation settings from the paper that documents them (here GPT-3) (@03:18, @2:15:55).
  - Compare against the checkpoint on the same validation set and a standard eval (@3:24:20, @3:44:15).
  - Check that a faster or parallel implementation gives the same numbers as the reference (@3:09:57, @3:59:19).

### artifact: build-nanogpt
- existing: no
- aliases: build-nanogpt, "build n GPT" (caption)
- repo_url: not given in this raw; a README `raw/github/karpathy__build-nanogpt.md` exists for merge to take it from
- statements:
  - He releases the lecture's code as a repo built up with a git commit per addition, starting from scratch (@3:27:41).
  - He plans to document remaining issues there: the loss periodicity, torch.compile breaking generation and HellaSwag, and data permutation (@3:47:04, @4:00:28).
  - Questions go to its discussions, issues and pull requests, or the Zero to Hero Discord (@4:00:28, @4:01:02).

### artifact (existing): nanogpt
- existing: yes
- statements:
  - What the lecture builds was building toward nanoGPT (@3:56:27).
  - In llm.c, `train_gpt2.py` is essentially nanoGPT, the PyTorch reference that the CUDA code matches (@3:56:27, @3:57:01).

### artifact: llm-c
- existing: no (llm.c has its own README and discussions in raw/github; merge may create it from those)
- aliases: llm.c
- statements:
  - llm.c is a pure CUDA implementation of GPT-2/GPT-3 training, with a nanoGPT-like PyTorch file as reference code (@3:56:27, @3:57:01).
  - It produces the same losses and norms as the PyTorch version but runs faster, starts faster and takes less space; he notes it is specific to GPT-2/3 while PyTorch is general (@3:57:37, @3:58:11, @3:58:46, @3:59:19).

### claim: reproducing-gpt-2-takes-about-an-hour-and-ten-dollars
- title: Reproducing GPT-2 124M now takes about an hour and about $10 of cloud compute
- confidence: stated
- quote: "today you can reproduce this model in roughly an hour or probably less even" (@02:11)
- statements: what was a fairly complicated optimisation five years ago now takes roughly an hour and about $10 on a rented cloud machine (@02:11, @02:45). His own 10B-token run on 8 A100s took about 1.7 hours (@3:22:06).
- relation: none set. Note for merge: the nanochat README's "$48 in about two hours on 8×H100 for a GPT-2-grade model" ([[github-2026-07-03-nanochat-readme]] §Leaderboard) measures a different target (beating GPT-2's CORE score), so do not call it extends or contradicts without checking.

### claim: adamw-is-a-bug-fix-of-adam
- title: In his view AdamW is a bug fix of Adam
- confidence: stated ("in my opinion", "is what I would say")
- quote: "adom w is a bug fix of atom is what I would say" (@57:19) — captions garble AdamW/Adam
- statements: he specifically likes the AdamW variant because in his opinion it fixes a bug; he does not explain the bug here (@56:46, @57:19).
- relation: none.

### claim: use-torch-compile-by-default
- title: He says you should use torch.compile almost by default unless debugging
- confidence: stated
- quote: "there's no real good reason for you to not use torch compile" (@1:49:01)
- statements: he feels you should almost always use it unless debugging; it gave 2.3× from one line (@1:49:01, @1:49:35). Caveat from the same video: it broke his sampling and HellaSwag code, so he turned it off for those runs (@3:27:09, @3:38:55).
- relation: none.

### claim: memory-access-not-flops-limits-training-speed
- title: Memory access patterns, not FLOP counts, limit much of training speed
- confidence: stated
- quote: "the fact that flops don't matter uh the entire memory access pattern matters" (@2:04:42)
- statements: many training workloads are memory-bound (@1:27:04, @1:27:38); TF32 gave 3× rather than 8× because of it (@1:38:59); flash attention does more FLOPs yet runs faster by avoiding HBM reads and writes (@2:01:13, @2:01:48). The quote is his gloss on flash attention; "don't matter" is his phrasing, keep the title no stronger.
- relation: none.

### claim: use-nice-numbers-in-neural-network-code
- title: Use numbers with many powers of two in neural-network and CUDA code
- confidence: stated
- quote: "it is simultaneously the dumbest and the most brilliant optimization" (@2:06:54); also verified: "pretty much you always want to use nice numbers" (@2:07:28)
- statements: nice numbers have many factors of two; CUDA kernels work in power-of-two blocks and need special-case handling otherwise (@2:06:54, @2:07:28); scan code for ugly numbers like 50,257 or GPT-2 XL's 25 heads (@2:08:01, @2:08:36); padding to 50,304 was faster despite more FLOPs (@2:10:51, @2:13:42); also keep batch sizes nice (@1:35:32, @3:22:06).
- relation: none. Merge may fold into [[training-efficiency]] if it prefers fewer claims.

### claim: gradient-clipping-is-a-patch-on-deeper-issues
- title: He calls gradient-norm clipping a hacky patch, though people still use it
- confidence: stated
- quote: "it's about like a patch on top of like deeper issues" (@2:18:49)
- statements: clipping bounds the shock from an unlucky batch; he calls it a bit of a hacky solution that people still use fairly often (@2:18:12, @2:18:49). He follows GPT-3's clip at 1.0 anyway (@2:17:02).
- relation: none.

### claim: batch-size-ramp-is-a-systems-gain-not-an-algorithmic-one
- title: As he understands it, GPT-3's batch-size ramp is a speed gain, not an optimisation improvement
- confidence: stated (hedged: "my understanding is")
- quote: "it's more of a systems and speed Improvement" (@2:26:38)
- statements: he skips the ramp because it complicates the arithmetic, and his understanding is that it is not a major improvement (@2:26:38); early in training the model mostly learns which tokens appear, so per-example gradients are highly correlated and a small batch gives nearly the same gradient; later they decorrelate (@2:27:13, @2:27:46).
- relation: none. Note for merge: the minGPT README records the ramp as part of GPT-3's recipe ([[github-2023-01-08-mingpt-readme]] §References (GPT-3)); not a conflict, that page is his notes on the paper.

### claim: inherited-gpt-3-hyperparameters-look-conservative
- title: The GPT-3 learning rate he inherited may be very conservative
- confidence: stated (hedged: "it's possible", "for some reason")
- quote: "the gpt3 hyper parameters that we are inheriting are actually extremely conservative" (@3:51:29)
- statements: people in a related repo found the maximum learning rate could be about 3× higher; he says it is possible these hyperparameters are not set precisely and are quite tunable (@3:51:29). He also says the 715-step warmup is very mild and about 100 might do (@3:20:10).
- relation: none.

### claim: his-gpt-2-reproduction-beat-the-checkpoint-on-fewer-tokens
- title: His 10B-token run surpassed GPT-2 124M on HellaSwag, with caveats he lists
- confidence: stated (his result)
- quote: "we were able to do so with only training on 10 billion tokens" (@3:44:50)
- statements:
  - After one epoch of the 10B sample his validation loss fell below OpenAI's GPT-2 124M checkpoint on FineWeb-Edu, which he calls not an exactly fair comparison (@3:43:41, @3:44:15).
  - His HellaSwag rose from 25% past GPT-2 124M; he says GPT-2 trained on 100B tokens (his statement; not quoted from the paper here) (@3:44:15, @3:44:50).
  - An overnight four-epoch, about 40B-token run reached HellaSwag 33.24, almost GPT-3 124M, which he says trained on 300B tokens (@3:48:43, @3:49:15, @3:52:37).
  - He calls it about 10× better learning efficiency and does not know exactly what to attribute it to beyond the data distribution, possible eval contamination and data quality (@3:45:24, @3:45:57, @3:48:11, @3:50:56).
  - Caveat quote: "this is not a perfect eval and there's some caveats here" (@3:45:57).
- relation: none to existing claims.

### claim (existing): pretraining-gives-a-document-completer
- relation: supports. 2023: pretraining yields a document completer that babbles internet ([[youtube-2023-01-17-gpt-from-scratch]] @1:51:29). Here: the model dreams documents and you cannot talk to it like ChatGPT until finetuned on conversations (@3:55:21, @3:55:54). Same position, restated.

### claim (existing): gpt-is-not-a-complicated-model
- relation: supports. minGPT README: GPT is not a complicated model ([[github-2023-01-08-mingpt-readme]] §intro). Here: his full GPT-2 is under 100 lines against about 2,000 in Hugging Face's file (@27:27). He does not repeat the phrase; this is evidence, not a restatement.

### claim (existing): pytorch-documentation-is-unreliable
- relation: supports. 2022: docs wrong, incomplete, unclear ([[youtube-2022-11-21-makemore-5-wavenet]] @52:51). Here: the DDP `device_ids` comment is roughly nonsensical (@3:00:24); autocast's rules are not documented well (@1:47:23); among several mixed-precision tutorials he recommends one and not five other copies (@1:42:51).

### claim (existing): attention-is-a-communication-mechanism
- relation: supports. 2023: attention is a communication mechanism ([[youtube-2023-01-17-gpt-from-scratch]] @1:11:26). Here: attention is a communication operation where tokens exchange information, the reduce to the MLP's map (@19:38, @20:12).

### claim (existing): forgetting-to-zero-grad-is-a-common-neural-net-bug
- relation: supports (weak). 2022: forgetting to zero grad is a common bug ([[youtube-2022-08-16-micrograd]] @2:11:01). Here: always remember to start from a zero gradient because backward always does a plus-equals (@58:28). He checks Copilot did not forget it; he does not call it common here.

## Quotes
- "today you can reproduce this model in roughly an hour or probably less even" (@02:11)
- "clean residual pathway is desirable from an optimization perspective" (@19:04)
- "so the attention is the reduce and the MLP is the map" (@20:12)
- "adom w is a bug fix of atom is what I would say" (@57:19)
- "if you're getting 60% uh utilization you're actually doing extremely well" (@1:27:38)
- "there's no real good reason for you to not use torch compile" (@1:49:01)
- "the fact that flops don't matter uh the entire memory access pattern matters" (@2:04:42)
- "it is simultaneously the dumbest and the most brilliant optimization" (@2:06:54)
- "gpt3 we have lots of details but no weights" (@2:15:55)
- "it's about like a patch on top of like deeper issues" (@2:18:49)
- "I fully understand what's happening inside these lines" (@2:22:45)
- "this comment for what device IDs is is roughly nonsensical" (@3:00:24)
- "this is a naughty thing to do" (@3:04:23)
- "we were able to do so with only training on 10 billion tokens" (@3:44:50)
- "this is not a perfect eval and there's some caveats here" (@3:45:57)
- "the documents are currently glued together in the exact same identical manner" (@3:50:22)
- "the gpt3 hyper parameters that we are inheriting are actually extremely conservative" (@3:51:29)
- "you can't talk to it like you can talk to chat GPT" (@3:55:21)

All grepped: each appears exactly once in the raw file.

## Notes for merge
- **Paper vs his result.** Paper/code/datasheet numbers: 124M = 12 layers × 768; vocab 50,257; context 1,024 (released model); pre-norm and 1/√N residual init (GPT-2 paper); std 0.02 / 0.01 (OpenAI code); β 0.9/0.95, ε 1e-8, clip 1.0, warmup 375M tokens, cosine to 10% over 260B, horizon 300B, lr 6e-4, batch 0.5M, weight decay 0.1, batch ramp, sampling without replacement (GPT-3 paper); WebText 45M links / 40 GB / ≥3 karma (GPT-2 paper); HellaSwag humans 95% / then-SOTA 48% (HellaSwag paper); 7.6× (flash attention paper); 19.5 / 156 / 312 TFLOPS (A100 datasheet); FineWeb 15T, FineWeb-Edu 1.3T / 5.4T (Hugging Face). His results: initial loss ~11 vs 10.82 expected; ~1,000 → 93 ms (≈11×) then 90 ms with fused AdamW; 1.5M tokens/s on 8 GPUs; 19,073 steps ≈ 10B tokens ≈ 1.7 h; HellaSwag 29.55% for GPT-2 124M by his script; overnight 40B run HellaSwag 33.24; llm.c 223k vs PyTorch 185k tokens/s. "GPT-2 trained on 100B tokens" and "GPT-3 124M on 300B tokens" are his statements in the video.
- **Garbled numbers.** "163,000 tokens per second" at @1:36:41 for the FP32 baseline is inconsistent with 16 × 1,024 tokens per ~1 s (≈16,300); likely a caption error, avoid citing it. Losses "6.05 661" then "6.58" at @2:05:49/@2:06:21 are garbled; he says they are identical up to floating point. "1973 steps" at @3:19:35 is 19,073 (he says "19073" at @3:22:06; 10B / 2^19 ≈ 19,073). "only 10 million training" at @3:45:24 means 10 billion. "only 10x the token budget" at @3:47:37 is a slip for 10× fewer tokens; do not quote it. "1,24" throughout means 1,024; "124" for block size at @27:59 means 1,024.
- **Caption misspellings:** atom/adom = Adam/AdamW; G/Galo/10h = GELU/tanh; Javier = Xavier; microad = micrograd; cattin = c_attn; hos mag / H swag / hell swag = HellaSwag; Uther/Luther harness = EleutherAI evaluation harness; nickel = NCCL; SMS = SMs; lm. C / llm Doc = llm.c; build n GPT = build-nanogpt; tich/Tik token = tiktoken; fine web edu / webd = FineWeb-Edu; llama 370b = Llama 3 70B.
- **Disclosure:** he says Lambda Labs sponsors his development (@1:23:11). Keep if the hardware sentence is used.
- **Mentions without explanation:** mechanistic interpretability (@11:10); SwiGLU (@23:31); stochastic regularizers / adaptive dropout behind GELU (@21:51); the bug AdamW fixes; gradient scalers for FP16 ("a whole video by itself", @1:41:45); the GPT-2 1.5B "XL" naming quirk in Hugging Face (@04:56).
- **Hedges to keep:** he is not sure what `model.eval()` does here (@34:20), not sure what autocast converts (@1:47:23), not sure why torch.compile does not find flash attention (@2:05:15), not sure why fused AdamW is not default (@2:33:20), believes Llama 3 70B did the FineWeb-Edu filtering (@3:14:58), believes GPT-3 scored HellaSwag by completion "as far as I know" (@3:34:29).
- **Uses Copilot on camera** for small completions and checks its output (@53:21, @58:28, @1:11:54, @1:20:25); could support [[ai-assisted-coding-loop]] only as context, 2024 not 2025; not proposed.
- **Relation to minGPT README:** that README noted he could not find the 1/√N residual init in OpenAI's GPT-2 code; this video implements it from the paper text, not from code. Not a contradiction.
- **New-page judgement calls:** training-efficiency, pretraining-data, llm-evaluation, reproduce-a-published-model, build-nanogpt, llm-c, plus nine claims. If merge wants fewer, the most foldable are use-nice-numbers-in-neural-network-code (into training-efficiency) and reproduce-a-published-model (into spelled-out-build-from-scratch).
