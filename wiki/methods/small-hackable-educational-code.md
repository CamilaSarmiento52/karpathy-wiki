---
type: method
steps:
  - Keep the whole thing in one or a few readable files
  - Keep PyTorch as the only dependency
  - Put configuration in the code and argparse, not switches
  - Hold the model to a few hundred lines
  - Give education-only code teeth when it needs them
  - Publish lecture code with its git history
  - Keep published lecture code as it was in the video
  - Keep the code clean enough to reference
  - Build the ramp as well as the code
  - Report lines of code and latency as numbers
  - Put simplicity ahead of efficiency and leave the rest to forks
sources: ["[[github-2022-11-20-makemore-readme]]", "[[github-2023-01-08-mingpt-readme]]", "[[github-2023-01-31-ng-video-lecture-readme]]", "[[youtube-2024-02-20-gpt-tokenizer]]", "[[x-2024-02-21-technical-accessibility]]", "[[github-2024-04-22-minbpe-readme]]", "[[github-2024-04-22-llmc-state-of-the-union]]", "[[github-2024-05-03-llmc-state-of-the-union]]", "[[github-2024-05-28-llmc-gpt-2-124m]]", "[[github-2024-05-29-llama2c-readme]]"]
aliases: [One hackable file, minimal educational re-implementation, hackable code, educational code]
---
# Small, hackable, educational code
How he writes the repos that accompany his lectures: makemore, he says, is not meant to be a heavyweight library with many switches and knobs but one hackable file, mostly intended for education ([[github-2022-11-20-makemore-readme]] §intro).

## Steps
1. **One file.** makemore is one hackable file, and he says it is mostly intended for educational purposes ([[github-2022-11-20-makemore-readme]] §intro).
2. **One dependency.** PyTorch is the only requirement ([[github-2022-11-20-makemore-readme]] §intro).
3. **Configuration in the code.** Rather than a library with "a billion switches and knobs", he points users to the argparse and the code itself for further training configurations ([[github-2022-11-20-makemore-readme]] §intro, §Usage).
4. **A few hundred lines.** minGPT tries to be small, clean, interpretable and educational, in contrast to implementations he found sprawling; the whole model is about 300 lines and the library three files ([[github-2023-01-08-mingpt-readme]] §intro). He criticises the Hugging Face language-modeling example as full-featured but hard to trace, with large functions mostly unused in the default setting ([[github-2023-01-08-mingpt-readme]] §References).
5. **Know the limit.** Once minGPT was widely referenced, large changes became harder, and education-only code lacked the teeth to reproduce benchmarks; he points to his rewrite nanoGPT for the direction he wanted instead ([[github-2023-01-08-mingpt-readme]] §intro).
6. **Publish with the history.** He publishes lecture code as a GitHub repo so people can easily hack it and walk through its `git log` history ([[github-2023-01-31-ng-video-lecture-readme]] §intro).
7. **Leave it as taught.** He keeps the published lecture code almost exactly as it was in the video, deferring the initialisation fix until a follow-up lecture explains it ([[github-2023-01-31-ng-video-lecture-readme]] §intro).

8. **Clean enough to reference.** He says he tried to keep minbpe's code fairly clean and understandable so learners can reference it when stuck on the exercise; it is in Python and not yet efficient, which he hopes to change ([[youtube-2024-02-20-gpt-tokenizer]] @1:26:20, @2:11:45, @2:12:18). The README says he tried hard to keep the code clean, readable and hackable and that readers should not be scared to read it; every file is very short, thoroughly commented and ends with a usage example, and the tests double as usage examples ([[github-2024-04-22-minbpe-readme]] §intro, §training).

9. **Small code is not enough on its own.** He was happy with how minimal micrograd's code was and assumed that, at about 200 commented lines with a README, it was self-explanatory; engagement showed otherwise until he made the video, so he adds building the ramp after building the thing ([[x-2024-02-21-technical-accessibility]]).

10. **Count the lines and the seconds.** In llm.c's first progress report he lists the main file's size, 2097 lines of clean code, beside nvcc compile latency (2.4 s) and launch-to-first-step latency (2.2 s), as headline numbers next to speed and memory ([[github-2024-04-22-llmc-state-of-the-union]] §intro (lines of code), §intro (latency)). In the next report he marks the growth to about 3,000 lines and the 4.3 s compile, which he says is now about as bad as `import torch`, as downsides, and keeps the simple version alive in a separate fp32 file meant to become pure CUDA kernels with no dependencies, the endpoint of a course that starts from the CPU-only `gpt2.c` ([[github-2024-05-03-llmc-state-of-the-union]] §intro (Lines of code), §intro (Latency), §intro (fp32 CUDA version plans)). By the GPT-2 (124M) post `train_gpt2.cu`, which he says started as a nice clean 1,000 lines of C, is closer to 3,500 ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (Code)).

11. **Simplicity first, by policy.** For llama2.c he wanted something super simple, minimal and educational, so he hard-coded the Llama 2 architecture in one pure-C inference file with no dependencies, and kept the fp32 forward pass as the easy-to-understand reference with quantization in a separate file ([[github-2024-05-29-llama2c-readme]] §intro, §int8 quantization). Its contributing policy says the repo should be the simplest, smallest, most hackable one for training and inference, not a framework of a thousand knobs across hundreds of files; it cares about efficiency but not at the cost of simplicity, readability or portability, and should not be full-featured, take 100 options or be the most efficient, with llama.cpp for those who care most about deployment efficiency ([[github-2024-05-29-llama2c-readme]] §contributing). Small, localised, broadly useful changes such as a loop reorder or a one-line OpenMP pragma are instant merges, while many `#ifdef`s, platform-specific code or hundreds of scenario-specific lines belong in forks ([[github-2024-05-29-llama2c-readme]] §contributing).

## Seen in
- [[github-2023-01-31-ng-video-lecture-readme]]
- [[ng-video-lecture]]
- [[github-2023-01-08-mingpt-readme]]
- [[mingpt]], [[nanogpt]]
- [[github-2022-11-20-makemore-readme]]
- [[makemore]]
- [[minbpe]]
- [[build-the-ramp-not-just-the-thing]]
- [[llm-c]]
- [[llama2c]]
