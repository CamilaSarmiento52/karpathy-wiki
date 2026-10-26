---
type: principle
status: promoted
inferred: false
quotes:
  - {text: "I may reject the PR because the complexity is not worth it.", source: "[[github-2024-09-24-llmc-readme]]", location: "§repo"}
  - {text: "but not at the cost of simplicity, readability or portability", source: "[[github-2024-05-29-llama2c-readme]]", location: "§contributing"}
  - {text: "it's too much complexity for not enough gain at this point", source: "[[talk-2024-10-03-cuda-mode-keynote]]", location: "@15:58"}
  - {text: "minGPT tries to be small, clean, interpretable and educational", source: "[[github-2023-01-08-mingpt-readme]]", location: "§intro"}
sources: ["[[github-2024-09-24-llmc-readme]]", "[[github-2024-05-29-llama2c-readme]]", "[[talk-2024-10-03-cuda-mode-keynote]]", "[[github-2023-01-08-mingpt-readme]]", "[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
---
# Keep the main code small and readable; reject complexity that does not pay for itself

> "I may reject the PR because the complexity is not worth it." — [[github-2024-09-24-llmc-readme]] §repo
>
> "it's too much complexity for not enough gain at this point" — [[talk-2024-10-03-cuda-mode-keynote]] @15:58

## In practice

He weighs the trade rather than always choosing the shortest code. The llm.c README keeps the mainline simple and readable and says a PR that buys 2% speed for 500 lines of complex C and an exotic dependency may be rejected, while making cuBLAS the default is a no-brainer: much faster, one interpretable line, a common dependency ([[github-2024-09-24-llmc-readme]] §repo). In the CUDA MODE keynote he describes deleting the CUDA streams and making llm.c single-threaded after race conditions, because the overlap was too much complexity for the gain ([[talk-2024-10-03-cuda-mode-keynote]] @15:58).

Every quote is about his own reference or educational repos. llama2.c still cares about efficiency, but not at the cost of simplicity, readability or portability; he expects applications to fork it and points deployment-focused users to llama.cpp ([[github-2024-05-29-llama2c-readme]] §contributing). minGPT aims to be small, clean, interpretable and educational, at about 300 lines for the model ([[github-2023-01-08-mingpt-readme]] §intro).

When reviewing any code, ask what each addition buys (speed, correctness, reach) against its lines, dependencies and knobs, and propose removing what does not pay ([[github-2024-09-24-llmc-readme]] §repo). Only in educational or reference code, prefer one hackable file over flags and frameworks; he sets his own code apart from a production code base, so do not push that style onto production code ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @33:14, [[github-2024-05-29-llama2c-readme]] §contributing).

## Rests on

- [[small-hackable-educational-code]], [[port-a-pytorch-model-to-c-and-cuda]]
- [[neural-net-training-should-not-be-complicated]], [[gpt-is-not-a-complicated-model]], [[coding-models-are-weak-at-code-never-written-before]]
- [[compute-efficiency]]

## Sources

- [[github-2024-09-24-llmc-readme]]
- [[github-2024-05-29-llama2c-readme]]
- [[talk-2024-10-03-cuda-mode-keynote]]
- [[github-2023-01-08-mingpt-readme]]
- [[talk-2025-10-17-dwarkesh-ghosts-not-animals]]
