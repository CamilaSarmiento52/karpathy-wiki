---
type: method
steps:
  - Pick a known-good reference implementation
  - Run the same input through the reference and yours
  - Compare your code with the reference code
  - Show the matching outputs side by side
  - Repeat the comparison on edge cases such as special tokens
  - Round-trip to check nothing is lost
  - Benchmark speed and memory against the reference, with the setting spelled out
  - Match whole training runs with schedules switched off
  - Check that more GPUs at the same total batch give the same run
  - Test both implementations against known-good output
  - Publish the comparable reference run with its known differences
sources: ["[[youtube-2024-02-20-gpt-tokenizer]]", "[[github-2024-04-22-minbpe-readme]]", "[[github-2024-04-22-llmc-state-of-the-union]]", "[[github-2024-05-03-llmc-state-of-the-union]]", "[[github-2024-05-24-llmc-pytorch-cross-checks]]", "[[github-2024-05-28-llmc-gpt-2-124m]]", "[[github-2024-05-29-llama2c-readme]]", "[[youtube-2024-06-09-reproduce-gpt-2]]", "[[github-2024-07-11-llmc-gpt-2-1-6b]]"]
aliases: [parity check, reproduce the reference output, match tiktoken, benchmark against PyTorch, cross-check against a reference]
---
# Verify against a reference implementation
When he reimplements something that already exists, he treats matching the existing implementation's output as the test that his version is right: for the tokenizer lecture the reference is tiktoken's GPT-4 encoding ([[youtube-2024-02-20-gpt-tokenizer]] @1:26:20).

## Steps
1. **Pick the reference.** For the GPT-4 tokenizer he takes OpenAI's tiktoken, the official inference library, as the known-good implementation ([[youtube-2024-02-20-gpt-tokenizer]] @1:11:42, @1:26:20).
2. **Same input, both implementations.** Once you have written your tokenizer, encoding a string should give the same tokens tiktoken gives ([[youtube-2024-02-20-gpt-tokenizer]] @1:26:20).
3. **Compare the code too.** He reads OpenAI's GPT-2 `encoder.py` against his own and finds that, apart from a byte-encoder layer, it is algorithmically identical to what he built ([[youtube-2024-02-20-gpt-tokenizer]] @1:15:36, @1:16:44, @1:17:50).
4. **Show the parity in the docs.** The minbpe README verifies feature parity by encoding the same text, mixing ASCII, punctuation, Korean and an emoji, with tiktoken's `cl100k_base` and with `GPT4Tokenizer`, and printing identical token lists ([[github-2024-04-22-minbpe-readme]] §inference: GPT-4 comparison).
5. **Edge cases too.** It repeats the check with `<|endoftext|>` and special tokens allowed, getting the same ids ([[github-2024-04-22-minbpe-readme]] §inference: GPT-4 comparison).
6. **Round-trip.** Encoding and decoding the same string should recover it ([[youtube-2024-02-20-gpt-tokenizer]] @55:56, @1:26:20).
7. **Benchmark against it, and say how.** For llm.c he also uses the PyTorch implementation as the yardstick for speed and memory: he names the hardware (a profile on an A10, timings on his A100), names what the PyTorch run used (fp32, no flash attention, slightly stale PyTorch) and calls the setting constrained, then compares peak memory from `nvidia-smi` and gives the PyTorch command to reproduce it ([[github-2024-04-22-llmc-state-of-the-union]] §intro, §intro (peak memory)). In the next report he compares against the strongest PyTorch setup he knows (nightly, mixed precision, compile, flash attention) and separately against the stable release, gives both invocations, the hardware and driver versions and tokens per second, shows how one trick, padding the vocabulary, moves the gap from about 11% to about 7%, flags a PyTorch memory number he does not trust, and reports his own regressions in lines of code and compile time ([[github-2024-05-03-llmc-state-of-the-union]] §intro (Single GPU training), §intro (Peak memory), §intro (Fine print), §intro (Latency)).

8. **Match whole training runs.** Once llm.c could do serious pretraining runs, he opened a thread comparing llm.c and PyTorch training with the focus on correctness, the two runs matching, and set speed aside ([[github-2024-05-24-llmc-pytorch-cross-checks]] §intro). Both sides train GPT-2 (124M) from scratch on FineWeb with micro-batch 16, sequence length 1024 and a total batch of 131072, learning rate 1e-4, warmup, learning-rate decay and weight decay switched off, for 50 iterations; he gives both commands, pins the repo commit and the GPU (an A100 40GB), and suggests TinyStories for anyone who does not want to preprocess FineWeb, where the numbers differ but the two should still match ([[github-2024-05-24-llmc-pytorch-cross-checks]] §1 GPU training in FP32). His result: after 50 iterations the two are within about 1e-3 or less in loss and gradient-norm difference, shown side by side, which he says gives confidence in correctness and the match to PyTorch ([[github-2024-05-24-llmc-pytorch-cross-checks]] §1 GPU training in FP32). The reference keeps its role after the reproduction: he calls `train_gpt2.py` a parallel implementation used for error checking and unit tests, without full feature parity ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (Tokenizer)).
9. **Scale out without changing the run.** With the total batch unchanged, llm.c on 4 GPUs should give exactly the same results, only faster, because only the number of gradient-accumulation steps falls; the 4-GPU PyTorch run did not yet match, and he posted the log while tracking it down ([[github-2024-05-24-llmc-pytorch-cross-checks]] §multiGPU).
10. **Freeze a known-good output.** llama2.c's `test_all.py` forwards the tiny 260K model in both C and Python for 200 steps and checks the output against a known-good expected output, and running PyTorch's `sample.py` on the same checkpoint as `run.c` gives the same results ([[github-2024-05-29-llama2c-readme]] §tests, §training).

**Note:** the commands he posts under the FP32 heading compile llm.c in FP32 but pass bfloat16 and flash attention on the PyTorch side, so the wiki does not say both sides ran in fp32 ([[github-2024-05-24-llmc-pytorch-cross-checks]] §1 GPU training in FP32).

**Two checks in the GPT-2 lecture (2024-06-09).** When his samples did not match the Hugging Face pipeline's, he replicated his own sampling loop on the Hugging Face model, got his results, and concluded his model was right and the pipeline does something extra ([[youtube-2024-06-09-reproduce-gpt-2]] @40:26, @40:59). At the end he lines up the llm.c and PyTorch runs step by step and shows the printed losses and norms are identical, the C version only faster ([[youtube-2024-06-09-reproduce-gpt-2]] @3:58:46, @3:59:19).

11. **Publish the comparable run and its differences.** In the 1.6B post he gives the full `torchrun` command for a relatively comparable PyTorch run, says the PyTorch script is a testing reference rather than an implementation so its loop differs in places (the dataloader does not permute shards, for example), and notes the vocabulary hack he applied to it ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (PyTorch comparison)). He then reports memory and step time, names a known cause of the gap, and says the PyTorch side may not be maximally tuned, inviting others to check ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (PyTorch comparison)).

## Seen in
- [[minbpe]]
- [[github-2024-04-22-minbpe-readme]]
- [[youtube-2024-02-20-gpt-tokenizer]]
- [[verify-gradients-against-pytorch]] — the gradient-specific version of the same habit
- [[llm-c]] — speed and memory against the PyTorch reference
- [[reproduce-a-published-model]] — what the parity checks prepared for
- [[llama2c]] — C against Python
- [[youtube-2024-06-09-reproduce-gpt-2]]
