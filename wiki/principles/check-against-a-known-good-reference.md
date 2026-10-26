---
type: principle
status: promoted
inferred: false
quotes:
  - {text: "it's only a reference that we check correctness with respect to", source: "[[talk-2024-10-03-cuda-mode-keynote]]", location: "@05:00"}
  - {text: "This gives nice confidence for correctness and match to PyTorch!", source: "[[github-2024-05-24-llmc-pytorch-cross-checks]]", location: "§1 GPU training in FP32"}
  - {text: "I then wrote the Rust code against this implementation with tests for equality.", source: "[[github-2026-01-03-rustbpe-readme]]", location: "§LLM Assistance note"}
  - {text: "you can encode the string and you should get these tokens", source: "[[youtube-2024-02-20-gpt-tokenizer]]", location: "@1:26:20"}
sources: ["[[talk-2024-10-03-cuda-mode-keynote]]", "[[github-2024-05-24-llmc-pytorch-cross-checks]]", "[[github-2026-01-03-rustbpe-readme]]", "[[youtube-2024-02-20-gpt-tokenizer]]"]
---
# When you reimplement something, check it against a known-good reference until the numbers match

> "it's only a reference that we check correctness with respect to" — [[talk-2024-10-03-cuda-mode-keynote]] @05:00
>
> "I then wrote the Rust code against this implementation with tests for equality." — [[github-2026-01-03-rustbpe-readme]] §LLM Assistance note

## In practice

In porting GPT-2 training to C and CUDA for llm.c, the PyTorch code stops being the thing he works in and becomes the reference that correctness is checked against ([[talk-2024-10-03-cuda-mode-keynote]] @05:00). In the llm.c cross-check post he runs both side by side and reports that loss and gradient norm agree within about 1e-3 after 50 iterations ([[github-2024-05-24-llmc-pytorch-cross-checks]] §1 GPU training in FP32).

The same move works across languages and in exercises. For rustbpe he wrote the Python reference himself, then wrote the Rust code against it with equality tests, with help from coding models because he is not a Rust developer ([[github-2026-01-03-rustbpe-readme]] §LLM Assistance note). In the tokenizer lecture the learner's tokenizer is checked by reproducing the tiktoken tokens for a string and round-tripping it ([[youtube-2024-02-20-gpt-tokenizer]] @1:26:20).

**Note:** when reviewing a rewrite, optimisation or port, the wiki's reading is to ask what it is checked against and, if nothing, to write the equality test and run it before reading further ([[talk-2024-10-03-cuda-mode-keynote]] @05:00, [[github-2026-01-03-rustbpe-readme]] §LLM Assistance note).

## Rests on

- [[verify-against-a-reference-implementation]], [[verify-gradients-against-pytorch]], [[port-a-pytorch-model-to-c-and-cuda]], [[reproduce-a-published-model]], [[spelled-out-build-from-scratch]]
- [[counting-and-gradient-bigram-models-are-the-same-model]]

## Sources

- [[talk-2024-10-03-cuda-mode-keynote]]
- [[github-2024-05-24-llmc-pytorch-cross-checks]]
- [[github-2026-01-03-rustbpe-readme]]
- [[youtube-2024-02-20-gpt-tokenizer]]
