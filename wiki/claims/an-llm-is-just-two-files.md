---
type: claim
stated_on: 2023-11-23
confidence: stated
sources: ["[[youtube-2023-11-23-intro-to-llms]]"]
topic: "[[pretraining-and-finetuning]]"
---
# A large language model is just two files: the parameters and the code that runs them
> "a large language model is just two files" — [[youtube-2023-11-23-intro-to-llms]] @00:00

## Context
His example is Llama 2 70B: a parameters file of 140 GB, 70 billion parameters stored at 2 bytes each in float16, and a run file, which in C would be about 500 lines with no dependencies ([[youtube-2023-11-23-intro-to-llms]] @01:40, @02:13). The two files are a self-contained package: compile the C code, point the binary at the parameters and talk to the model on a MacBook without internet ([[youtube-2023-11-23-intro-to-llms]] @02:45). He admits his demo video ran the 7B model, since 70B would be about 10 times slower ([[youtube-2023-11-23-intro-to-llms]] @03:18). The architecture and forward pass are understood and open; the magic, and the computational cost, is in obtaining the parameters, while running a trained network is fairly cheap ([[youtube-2023-11-23-intro-to-llms]] @03:52, @06:37).

## Related claims
- **Note:** [[gpt-is-not-a-complicated-model]] makes a similar point about code size (about 300 lines for minGPT's model); the pages are adjacent, not linked as support ([[youtube-2023-11-23-intro-to-llms]] @02:13).
- **Note:** [[pretraining-is-lossy-compression-of-the-internet]] says what the parameters file holds ([[youtube-2023-11-23-intro-to-llms]] @05:30).
