---
type: artifact
repo_url: https://github.com/karpathy/build-nanogpt
language: Python
status: active
sources: ["[[github-2024-06-17-build-nanogpt-readme]]", "[[youtube-2024-06-09-reproduce-gpt-2]]"]
aliases: [build nanoGPT, build-nanoGPT]
---
# build-nanogpt
The code of his "Let's reproduce GPT-2 (124M)" lecture: a from-scratch reproduction of nanoGPT whose git commits were kept step by step and clean, so the history shows it being built, with the video introducing each commit ([[github-2024-06-17-build-nanogpt-readme]] §intro). `status: active` follows the README snapshot of 2024-06-17, which collects errata and gives no deprecation notice ([[github-2024-06-17-build-nanogpt-readme]] §Errata).

## What it demonstrates
- **Empty file to GPT-2.** It starts from an empty file and works up to reproducing GPT-2 (124M); with more patience or money the code can also reproduce the GPT-3 models ([[github-2024-06-17-build-nanogpt-readme]] §intro).
- **About an hour and $10.** He says GPT-2 (124M) probably trained for quite some time in 2019, while reproducing it today is a matter of about an hour and about $10, on a rented cloud GPU box if needed (he recommends Lambda) ([[github-2024-06-17-build-nanogpt-readme]] §intro). The lecture opens with the same estimate: roughly an hour, or probably less, and about $10 of cloud compute for what was a fairly complicated optimisation five years earlier ([[youtube-2024-06-09-reproduce-gpt-2]] @02:11, @02:45). **Note:** at launch he projected his on-camera run of 19,073 steps over 10B tokens on eight A100s at about 1.7 hours; he later says the epoch took roughly two hours ([[youtube-2024-06-09-reproduce-gpt-2]] @3:22:06, @3:48:43).
- **Built commit by commit.** In the lecture he says he made a git commit every time he added something, and releases the repo from scratch to the end ([[youtube-2024-06-09-reproduce-gpt-2]] @3:27:41).
- **Pretraining only.** GPT-2 and GPT-3 are simple language models trained on internet documents that only "dream" such documents, so the repo does not cover chat finetuning; that comes later ([[github-2024-06-17-build-nanogpt-readme]] §intro). It shows sample completions of "Hello, I'm a language model," after 10B and after 40B tokens of training ([[github-2024-06-17-build-nanogpt-readme]] §intro).
- **Errata and open issues.** The README is meant to collect FAQ and errata, "of which I am sure there will be a number"; its errata are a leftover attention-bias buffer after the switch to flash attention, older PyTorch struggling to convert uint16 to long, `torch.autocast` wanting a device type rather than a device, and `require_backward_grad_sync` affecting the forward pass too ([[github-2024-06-17-build-nanogpt-readme]] §intro, §Errata). In the lecture he plans to document the loss periodicity, torch.compile breaking generation and HellaSwag, and data permutation there ([[youtube-2024-06-09-reproduce-gpt-2]] @3:47:04, @4:00:28).
- **Where to ask.** Questions go to the repo's Discussions or the Zero to Hero Discord's #nanoGPT channel ([[github-2024-06-17-build-nanogpt-readme]] §intro; [[youtube-2024-06-09-reproduce-gpt-2]] @4:00:28, @4:01:02).
- **Not for production.** For production-grade runs very similar to nanoGPT he recommends litGPT and TinyLlama ([[github-2024-06-17-build-nanogpt-readme]] §Prod).

## Related
- [[nanogpt]] — what it reproduces from scratch
- [[spelled-out-build-from-scratch]] — the build method, one commit per step
- [[small-hackable-educational-code]] — clean history, production left to other repos
- [[reproduce-a-published-model]] — the lecture's reproduction steps
- [[llm-c]] — the C/CUDA parallel implementation the lecture ends on
