# Digest: CUDA Mode Keynote | Andrej Karpathy | Eureka Labs
- raw: raw/talks/aR6CzM0x-g0.md · published: 2024-10-03 · medium: talk · words: ~5,200 (23:21)
- source slug: talk-2024-10-03-cuda-mode-keynote

## Source page
```
---
type: source
raw_path: raw/talks/aR6CzM0x-g0.md
published: 2024-10-03
medium: talk
summary: "His CUDA MODE keynote on llm.c: how frustration with torch.compile led him to drop PyTorch, how he ported GPT-2 layer by layer to one C file and then to CUDA with a team of contributors, what it took to beat PyTorch on GPT-2 training, and why he thinks LLMs may one day write code like llm.c for any custom application."
url: https://www.youtube.com/watch?v=aR6CzM0x-g0
title: "CUDA Mode Keynote | Andrej Karpathy | Eureka Labs"
---
# CUDA Mode Keynote | Andrej Karpathy | Eureka Labs
Raw: [[raw/talks/aR6CzM0x-g0]] · Original: https://www.youtube.com/watch?v=aR6CzM0x-g0

## Summary
After a host's introduction, he tells the story of llm.c: while preparing a YouTube video on GPT training he hit torch.compile errors in eval and inference he could not solve, and decided to write the whole computation himself (@01:45, @02:19, @03:22). He lists what PyTorch gives you that he had to replace, ports each layer from PyTorch to explicit PyTorch, a hand-derived backward and plain C on float arrays checked against the PyTorch reference, then strings the layers into one dependency-free C file with all memory allocated once (@03:55, @05:00, @05:32, @06:37, @07:09, @08:48). Moving to CUDA, he develops kernels that match the C version exactly, finds CUDA harder to learn than he expected, and credits contributors who arrived from the internet with much of the optimisation, from cuBLAS and cuDNN flash attention to mixed precision, Packed128, determinism and a sharded optimizer, while he rejected complexity that did not pay for itself (@10:27, @11:33, @13:11, @14:17, @15:58, @17:05). The result reproduces GPT-2 (1.6B) on one H100 node in about 24 hours and, at the time of the post, used about 30% less memory and trained about 20% faster than PyTorch, specifically for GPT-2 (@17:38, @18:10, @19:17). He closes with a further motivation: if llm.c is like writing assembly by hand, LLMs that become better at coding may act as a compiler that writes such code for any custom application, with llm.c as example code in their context (@20:59, @21:32, @22:05, @22:37).

## Key points
- Origin: torch.compile errors, stages of grief, writing it himself; Maldives jetlag; Avengers; 60 contributors; Lambda; Llama 3 and fp8 coming; forks → [[llm-c]]
- What PyTorch provides (array, autograd, device, dtype, compile, distributed) and what dropping it costs → [[pytorch]]
- Layer by layer: explicit PyTorch, hand-derived backward, C on float arrays, string together, CUDA kernels v1…v6 → [[port-a-pytorch-model-to-c-and-cuda]]
- PyTorch becomes only the reference to check correctness; kernels match the specification exactly → [[verify-against-a-reference-implementation]]
- No tensor abstraction, just float arrays; why should it be more complicated → [[neural-net-training-should-not-be-complicated]]
- Too much complexity for not enough gain: CUDA streams nuked, PRs rejected, ZeRO-2 not merged → [[small-hackable-educational-code]]
- cuBLAS, cuDNN flash attention, bf16, fusions, recompute, Packed128 and SASS, determinism without atomics, NCCL, ZeRO-1, multi-node, ~50% MFU → [[compute-efficiency]]
- CUDA was harder to learn than he expected; books out of date → [[learning-cuda-was-harder-than-he-expected]]
- ~30% less memory, ~20% faster than PyTorch for GPT-2 training at the time; anything else is a lot of trouble → [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- GPT-2 (1.6B), one H100 node, ~24 hours, roughly $600; beats GPT-2 on HellaSwag → [[reproduce-a-published-model]], [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- People came from the internet to help; one of his favourite things about an open-source MIT repo → [[build-and-publish-projects]]
- torch.compile as GCC for Software 2.0, llm.c as assembly → [[software-3-0]]
- LLMs as a compiler for custom applications; Python and PyTorch as a crutch for finite humans; llm.c as few-shot example code → [[llms-may-write-custom-low-level-code-for-any-application]], [[prompting-llms]]

## Fed pages
- [[llm-c]]
- [[pytorch]]
- [[port-a-pytorch-model-to-c-and-cuda]]
- [[verify-against-a-reference-implementation]]
- [[neural-net-training-should-not-be-complicated]]
- [[small-hackable-educational-code]]
- [[compute-efficiency]]
- [[learning-cuda-was-harder-than-he-expected]]
- [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- [[reproduce-a-published-model]]
- [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- [[build-and-publish-projects]]
- [[software-3-0]]
- [[llms-may-write-custom-low-level-code-for-any-application]]
- [[prompting-llms]]
```

## Candidates
### artifact: llm-c
- existing: yes
- statements:
  - He sums the project up as training Transformers in C "and a pinch of C++" (@01:11).
  - **Origin (his account).** Roughly a year before the talk, by his words, he was making a video for his YouTube series on GPT training and hacking on nanoGPT; wrapping the model for device, compile and DDP made it hard to see what the abstractions did (@01:45, @02:19). Training worked, but eval and inference failed with torch.compile errors he could not resolve; after about two hours he decided to write the whole thing himself, since the algorithm was clear in his mind (@02:19, @02:50, @03:22, @03:55).
  - **The C file.** One C file, about 2,000 lines "if I remember correctly", with no dependencies; it compiles and runs instantly, allocates all memory in one blob so it cannot run out of memory later, is fully deterministic, can in principle train GPT-2, and runs "on a potato"; he jokes it would suit a von Neumann probe (@08:48, @09:21).
  - Most of this work happened on vacation in the Maldives while jetlagged, waking at 1am with nothing to do; he jokes it is a recommended way to develop software (@09:55, @10:27).
  - **Contributors.** His own CUDA kernels were "okay" but not great; a team of contributors assembled from the internet, a few of whom he calls core devs, started optimising and writing the kernels; over time about 60 contributors; Lambda sponsors compute (@12:39, @13:11, @13:44).
  - **Result.** GPT-2 (1.6B), which he calls state of the art around 2019, trains on a single H100 node in about 24 hours for roughly $600; no Python or PyTorch needed, only cuDNN as the heaviest dependency and that optional; almost 50% MFU on one node; it beats GPT-2 on HellaSwag, which he reads as the optimisation going well with no crazy numerical issues or loss spikes at this size (@17:38, @18:10, @18:44).
  - Looking back, it was not all that simple: it took a few months for a few people (@19:50); later he says multiple people over about three months (@21:32).
  - **Ongoing.** Llama 3.1 training support "very very soon", fp8 support in a big PR, many forks of which he names the AMD fork as very active and the C++ CUDA fork as nice (@20:25).
  - He says llm.c is fairly readable, clean and well documented, maybe about 3,000 lines of mostly C, and encourages forking (@20:59).
- relation: the existing page's 2024-07-11 numbers ($672, 29%, 19%) differ from his rounded talk figures; cite each with its source.

### method: port-a-pytorch-model-to-c-and-cuda
- existing: no
- aliases: Port a PyTorch layer to C, llm.c porting process, layer-by-layer port
- steps (proposed):
  1. Keep the PyTorch model as the reference only
  2. Write each layer's forward pass explicitly
  3. Derive and write each layer's backward pass
  4. Port forward and backward to C on float arrays
  5. Pre-plan and allocate all memory once
  6. String the layers together and check against PyTorch
  7. Port each layer to CUDA, trivial kernel first
  8. Swap in library kernels, then optimise
- statements:
  - The PyTorch code stops being the main thing and becomes only the reference against which correctness is checked (@05:00).
  - For layernorm he wrote the forward pass in explicit PyTorch, because PyTorch's own layernorm is a block that calls into CUDA kernels, and checked it matched (@05:32).
  - He wrote the backward pass with pen and paper, still in PyTorch but explicit, and checked forward and backward against PyTorch's layernorm (@06:05).
  - Porting to C is simpler than you might think: float arrays for inputs, outputs, means, standard deviations, weights and biases, no tensor abstraction or any other abstraction, fully self-contained (@06:37, @07:09).
  - In `main` all memory is allocated once at the start: parameters, their gradients, AdamW's m and v buffers, and activations with their gradients; then forwards, backwards and the update are called in order (@07:09, @07:42, @08:15).
  - With a starter pack (GPT-2 weights in one binary, tinyshakespeare, the tokenizer) you compile and run, and verify that the PyTorch and C code are identical (@08:15, @08:48).
  - On GPU, in `dev/cuda`, he writes a series of kernels (versions 1, 2, 3 … 6) for each layer that match the specification exactly and give the same numbers; the first is usually trivial, parallelising over batch and time with one thread per output element and copy-pasted C code, while later ones get elaborate (warp reductions, shared memory, cache streaming hints) (@10:27, @11:00, @11:33).
  - Then he swaps matmuls to cuBLAS and attention to cuDNN flash attention rather than writing his own (@13:44, @14:17).
- relation: new method page; [[verify-against-a-reference-implementation]] and [[verify-gradients-against-pytorch]] in Related; the X post and the README (§tutorial layernorm guide, §test) are further sources.

### topic: pytorch
- existing: yes
- statements:
  - What PyTorch gives you, by his list: an n-dimensional array (without it, pointer arithmetic to ravel and unravel indices), autograd (else write every forward and backward), device (else manage host and device memory yourself), dtype conversions, torch.compile (else do kernel fusions and space/time optimisation by hand) and distributed (else spin up processes and communicate with NCCL yourself) (@03:55, @04:27, @05:00).
  - He calls PyTorch really nice and says that without it you are "kind of naked in the world" (@05:00).
  - Stacking device, compile and DDP abstractions confused him about their order and what they did to the model; he says he does not fully understand how they work (@01:45, @02:19).
  - torch.compile takes about a minute, which he personally does not like to work with (@19:50).
- note: the PyTorch-forum and "ptrblck" passage is a joke about seeking help; do not cite as a claim about PyTorch support.

### method: verify-against-a-reference-implementation
- existing: yes
- statements:
  - PyTorch becomes only a correctness reference (@05:00); each layer's explicit forward and backward are checked against PyTorch (@05:32, @06:05); the strung-together C program is verified identical to the PyTorch code (@08:48); every CUDA kernel version matches the specification exactly and gives the same numbers (@10:27).
  - Because a PyTorch implementation is kept in parallel, the equivalent training loop can be run side by side for comparison (@18:44, @19:17).

### claim: neural-net-training-should-not-be-complicated
- existing: yes
- statements:
  - In the C port he wanted to keep things simple, with no tensor or other abstraction, just float arrays and operations on them, asking why it should be a lot more complicated than that (@06:37, @07:09).
- relation: **supports** (same claim, new source; the keynote states the float-array view at @06:37).
- caution: at @19:50 he says that, looping back, "it wasn't all that simple": a lot was involved and it took a few people a few months. This is about building the fast, multi-GPU project, not about the arithmetic of training; it does not contradict the claim. Merge should cite both so the page does not read as if he said the whole project was simple.

### method: small-hackable-educational-code
- existing: yes
- statements:
  - CUDA streams to overlap computation produced weird race conditions, so he deleted all of them and made everything single-threaded; llm.c is not as overlapped as it could be, but it was too much complexity for not enough gain at that point (@15:25, @15:58).
  - A ZeRO-2 pull request was not yet merged, as far as he believes, because it gets messy; a lot of llm.c is balancing improvement and speed against the complexity introduced (@17:05).
  - He has rejected many pull requests because the code starts to get crazy, which he thinks reduces how many people can be on board with the project (@17:05, @17:38).
  - He says he tried to keep it clean and well documented and encourages forking (@20:59).
- relation: same policy as README §repo; cite both.

### topic: compute-efficiency
- existing: yes
- statements:
  - cuBLAS for matmuls instead of fp32 hand-rolled ones; cuDNN's flash attention rather than writing his own (@13:44, @14:17).
  - Mixed precision: decide for every parameter and activation tensor which is float32 and which bfloat16, and convert between them (@14:17).
  - Kernel fusions; recompute settings that redo part of the forward pass in the backward; contributor work minimising backward-pass memory (@14:50).
  - Packed128, a data structure that in their experience forces the compiler to use the 128-bit load and store instructions it otherwise often does not; found by reading the SASS assembly for a loop (@14:50, @15:25).
  - Full determinism is hard because some kernels cannot use atomics; the encoder backward is trivial with atomics and non-trivial without (@15:58, @16:31). Stochastic rounding is in, for accuracy (@15:58, @16:31).
  - Multi-GPU: NCCL all-reduce and a sharded optimizer state (ZeRO-1) that spreads AdamW's large float buffers across GPUs to lower memory per GPU (@16:31, @17:05). Multi-node synchronises across machines (@17:38).
  - Almost 50% MFU on one node, which he calls quite good (@18:44).

### claim: learning-cuda-was-harder-than-he-expected (optional)
- existing: no
- title: "He found CUDA harder to learn than he expected"
- confidence: stated
- stated_on: 2024-10-03
- quote: "it's not exactly trivial to learn Cuda unfortunately" (@11:33)
- statements:
  - He knew some CUDA going in, but says getting better at it is not trivial and was harder than he expected (@11:33, @12:06).
  - Books are partly out of date; PMPP is quite good but mostly beginner level and lacks many kernels llm.c ended up using; the CUDA C++ programming guide is not very readable for newcomers; he calls one blog post by someone at Anthropic way better than anything we deserve, and wishes there were more like it (@12:06, @12:39).
  - He hopes events like CUDA MODE speed up the availability of CUDA know-how (@12:39).
- relation to existing claims: none.
- recommendation: a personal experience rather than a position; merge may fold it into [[llm-c]] or [[compute-efficiency]] as cited sentences instead of a page. Note that it bears on the forecast claim below: the difficulty of hand-writing this code is part of why he thinks LLMs writing it would matter (@21:32), but he does not connect the two himself.

### claim: llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements
- existing: yes
- statements:
  - At the time of the 1.6B post, llm.c used about 30% less memory and was about 20% faster in training throughput; he does not know whether that still holds because the PyTorch team keeps optimising, and is not sure he fully optimised the PyTorch implementation, saying he did his personal best (@19:17).
  - The advantage is specific to GPT-2 training: to train anything else you are in a lot of trouble and have to change the code a lot (@19:17, @19:50). It also compiles and runs much faster (@19:50).
- relation: supports (same claim; rounded versions of the 2024-07-11 29% / 19%). Keep "in his measurements" and his GPT-2-only scope.

### method: reproduce-a-published-model
- existing: yes
- statements:
  - After all the work, llm.c reproduces the 1.6B GPT-2 on a single H100 node in about 24 hours for roughly $600, with no Python, PyTorch, conda or pip, only an optional cuDNN (@17:38, @18:10).

### claim: his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag
- existing: yes
- statements:
  - He says the 1.6B run beats GPT-2 on HellaSwag, which indicates the optimisation went well (@18:44). [caption: "H swag"]
- relation: supports (same claim, no new number). Optional; merge may skip.

### method: build-and-publish-projects
- existing: yes
- statements:
  - People came from the internet to help, which he calls one of his favourite things that can happen with an open-source MIT-licensed repo (@13:11, @13:44); "we learned a lot and we made friends along the way" (@19:50).
- relation: fits step 6 (take the reward when people fork and build on it).

### topic: software-3-0
- existing: yes (alias Software 2.0)
- statements:
  - If PyTorch, especially torch.compile, is a bit like GCC for Software 2.0, a compiler, then llm.c is a bit like writing assembly, doing everything manually (@20:59, @21:32).
- note: the only use of "Software 2.0" in this talk; the page's sources are 2025. Add as a dated sentence; `first_seen` would move to 2024-10-03 only if merge counts this as discussing the topic (it uses the term without defining it; `context` may be safer).

### claim: llms-may-write-custom-low-level-code-for-any-application
- existing: no
- title: "He expects LLMs may come to write custom low-level code like llm.c for any application" — alternatives: "LLMs may act as a compiler for custom applications". Do not drop the hedge.
- confidence: stated (hedged: "I don't actually know", "maybe", "not unlikely", "kind of likely")
- stated_on: 2024-10-02 (the X post) if both sources are used; the keynote is published 2024-10-03.
- quote: "the llms could could act as a kind of compiler for any custom application" (@22:05)
- statements:
  - He says starting llm.c was not haphazard; he had another motivation (@20:59).
  - Writing llm.c, several people over about three months, produced something faster than PyTorch for GPT-2 training, which he says proves it is possible, but it costs several people several months (@21:32).
  - If LLMs are about to get much better at coding, he expects an LLM could do this for any custom application: act as a compiler, do all the llm.c work and output a binary you compile and run (@21:32, @22:05).
  - He wonders, saying he does not actually know, whether Python, PyTorch and everything else is just a crutch because humans have finite knowledge, intelligence and attention, and whether you would rather write all code as custom CUDA kernels (@22:05).
  - In these early stages LLMs might not write such code from scratch: prompted to write GPT-2 in C you probably would not get llm.c, but with llm.c in context, few-shot learning makes it much more likely; so llm.c could be useful example code for LLMs about to write custom applications (@22:05, @22:37).
  - He thinks this is not unlikely, then "kind of likely", to happen; software development in general will probably change a lot; to him llm.c is an exploration of whether this is even possible (@22:37).
- **change of view / relation to existing claims:**
  - No existing claim page is about LLMs writing CUDA or other low-level code (searched claims, topics, methods and timelines for llm.c, CUDA, compiler, binary, custom). So this does not change a recorded view; it is new.
  - **Not `contradicts` [[use-llms-as-copilots-with-human-oversight]]** (2023-05-25): that advice is about using today's LLMs in low-stakes copilot roles; this is a conditional forecast ("if LLMs are about to become much better at coding") and he says current LLMs would likely fail from scratch (@22:37). Both can hold.
  - **Not `extends`** of any earlier claim. The closest earlier page is [[gpt-is-a-general-purpose-computer-running-natural-language-programs]] (CS25, published 2023-05-19), which is about prompts as programs, not LLMs emitting code; no relation.
  - **Later pages it may be weighed against** (2025, so this would be the earlier side): [[vibe-coding-will-terraform-software]] (2025-12-19) and [[english-is-the-new-programming-language]] (2025-06-19). His "software development in general will probably change a lot" (@22:37) is compatible with the 2025 terraform claim, and the 2025-12-19 essay's code as "free, ephemeral, malleable, discardable after single use" (on [[vibe-coding]]) is a cousin of custom per-application code. I recommend a **Note:** linking them, not `supports`/`extends`: the 2024 claim is about LLMs writing low-level, abstraction-free code for performance; the 2025 claims are about people building programs in English. If merge prefers a link, `supports` toward [[vibe-coding-will-terraform-software]] is the weakest defensible one; `extends` would need a timeline and overstates the connection.
  - Internal consistency: the claim leans on [[neural-net-training-should-not-be-complicated]] (no abstractions, float arrays, @06:37) and on [[software-3-0]] (the Software 2.0 compiler analogy, @20:59). **Note:** links only.

### topic: prompting-llms
- existing: yes (aliases include in-context learning, few-shot prompting)
- statements:
  - He expects few-shot learning to help: an LLM given llm.c as example code in its context is far more likely to produce llm.c-like code than one prompted from scratch (@22:37).
- note: one applied sentence; `context` may be the right field.

## Quotes
- "we're training Transformers uh in C and a pinch of C++" (@01:11)
- "I don't fully understand how any of this works" (@02:19)
- "without pytorch we're kind of naked in the world right" (@05:00)
- "I don't want to create any abstraction really" (@06:37)
- "it's just float arrays and operations on float arrays" (@06:37)
- "it's not exactly trivial to learn Cuda unfortunately" (@11:33)
- "people just come from the internet and help contribute it's amazing" (@13:44)
- "it's too much complexity for not enough gain at this point" (@15:58)
- "I've actually rejected a lot of PRS because of that" (@17:05)
- "we have almost a 50% mfu here on one uh node" (@18:44)
- "if you want to train anything else you're in a lot of trouble" (@19:17)
- "turns out it wasn't all that simple there was a lot of stuff involved" (@19:50)
- "then LMC is a bit like writing assembly" (@21:32) [LMC = llm.c, caption]
- "the llms could could act as a kind of compiler for any custom application" (@22:05)
- "is just a crutch because we humans are finite" (@22:05)
- "software development in general will probably change a lot" (@22:37)

## Notes for merge
- **Host vs him.** [00:00] and [00:39] are an unnamed host's introduction (founding member of OpenAI, ex-Google Brain, DeepMind, Tesla, joined the CUDA MODE Discord to hack on llm.c). None of it is his. The [01:11] block starts with the host ("Only Andre [Applause]") and switches to him at "kathi wow okay". Everything from there to [23:11] is his; no other speaker, no Q&A.
- **Caption garbles.** llm.c appears as "lm. C", "LMC", "L.C", "L C", "Eli", "Eleni", "El and", "L Andi", "llmc"; "N GPT" (@01:45) is probably nanoGPT (README calls `train_gpt2.py` a tweaked nanoGPT), flag as caption; "CH discuss"/"PTR blck" (@02:50) are the PyTorch forum and a forum user; "torch compal" = torch.compile; "Ayman probe"/"van probe" = von Neumann probe (the X post spells it); "kuas" = cuBLAS; "CN"/"CNN"/"C" (@14:17, @18:10) = cuDNN; "nickel" = NCCL; "admw" = AdamW; "Z1"/"01"/"02" = ZeRO-1/ZeRO-2; "SAS" = SASS; "mvcc" = nvcc; "War produce" = warp reduce; "pmpp" = the PMPP book; "H swag" = HellaSwag; "L spikes" = loss spikes; "gbt2"/"up2" = GPT-2; "Pyro implementation" = PyTorch; "kudam mode"/"cud mode" = CUDA MODE. Do not quote garbled passages.
- **Names.** He names core devs as "Eric Arun alexar" (@13:11) and others "Ross wheeler and chinel"; the 2024-07-11 Discussion lists handles @ngc92, @ademeure, @gordicaleksa, @rosslwheeler. Do not map caption names to handles. "Simon who at anthropic" (@12:39) is a blog author; no name beyond that in the caption.
- **Numbers differ from the Discussions; cite each with its source.** Keynote: ~24 h, "roughly $600", ~30% less memory, ~20% faster, almost 50% MFU, ~60 contributors, single C file ~2,000 lines "if I remember correctly", whole project "maybe like I think 3,000 lines", "a few months", "three months". The 2024-07-11 Discussion: $672, 29%, ~19%, ~5,000 lines. The README: CPU file ~1,000 lines, ~7% faster. The X post: $672, 29%, 19%.
- **His dates.** "roughly a year ago" (@01:45) is his own phrase for the origin; the Discussions date day 24 to 2024-05-03. Quote his words if used; do not compute a start date.
- **Recording vs published.** The X post (2024-10-02) says he gave the talk "last week"; the video is published 2024-10-03. Recording date likely differs from the published date; do not state one.
- Slide asides (@03:55 "I don't know why those bullet points are one1", @11:00 "I don't know what this is I'm going to skip that") are about slide rendering; ignore.
- The "stages of grief" and Maldives passages are jokes; paraphrase as his account, not as advice.
- "state-of-the-art llm as of 2019 or so" (@17:38) about GPT-2 relates to [[gpt-2-is-the-first-recognizably-modern-llm-stack]] only loosely; not proposed as a source there.
- The forecast claim is also in the X post's last bullet; give both sources on one claim page.
