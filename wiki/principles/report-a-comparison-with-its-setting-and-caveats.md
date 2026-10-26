---
type: principle
status: promoted
inferred: false
quotes:
  - {text: "in this constrained setting", source: "[[github-2024-04-22-llmc-state-of-the-union]]", location: "§intro"}
  - {text: "so it's not a super fair comparison", source: "[[github-2024-05-28-llmc-gpt-2-124m]]", location: "§intro"}
  - {text: "I wouldn't say I have full confidence that the PyTorch script is maximally tuned", source: "[[github-2024-07-11-llmc-gpt-2-1-6b]]", location: "§intro"}
  - {text: "this is not an exactly fair comparison but it's a good cross check", source: "[[youtube-2024-06-09-reproduce-gpt-2]]", location: "@3:44:15"}
sources: ["[[github-2024-04-22-llmc-state-of-the-union]]", "[[github-2024-05-28-llmc-gpt-2-124m]]", "[[github-2024-07-11-llmc-gpt-2-1-6b]]", "[[youtube-2024-06-09-reproduce-gpt-2]]"]
---
# When you compare a result with a baseline, state the setting and what might make the comparison unfair

> "this is not an exactly fair comparison but it's a good cross check" — [[youtube-2024-06-09-reproduce-gpt-2]] @3:44:15
>
> "I wouldn't say I have full confidence that the PyTorch script is maximally tuned" — [[github-2024-07-11-llmc-gpt-2-1-6b]] §intro

## In practice

All four quotes are from 2024 and caveat a comparison against PyTorch or OpenAI's GPT-2, in llm.c posts and the GPT-2 lecture; the rule is about comparisons, not every result. In the April llm.c update he reports llm.c about 6.4% faster than PyTorch, names the PyTorch setup (fp32, no flash attention, slightly stale PyTorch), says the speed-up holds in that constrained setting, and gives the command to reproduce it ([[github-2024-04-22-llmc-state-of-the-union]] §intro). Before comparing his 1.6B run with PyTorch, he says he is not fully confident the PyTorch script is maximally tuned ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro).

The llm.c GPT-2 124M post and the GPT-2 lecture caveat the same comparison: his model beats OpenAI's checkpoint on FineWeb validation loss, but GPT-2 was trained on a different data distribution, so he calls it not a fair comparison and leans on HellaSwag instead ([[github-2024-05-28-llmc-gpt-2-124m]] §intro, [[youtube-2024-06-09-reproduce-gpt-2]] @3:44:15). These are two texts with one caveat, not two separate examples.

When building, this means every number compared with a baseline comes with the command, the hardware, the baseline's setup and what the baseline may be missing ([[github-2024-04-22-llmc-state-of-the-union]] §intro). When reviewing, a speed-up or better-loss claim without its baseline and setting is incomplete; ask whether the comparison is fair ([[github-2024-05-28-llmc-gpt-2-124m]] §intro).

## Rests on

- [[reproduce-a-published-model]], [[verify-against-a-reference-implementation]]
- [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]], [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]], [[inherited-gpt-3-hyperparameters-look-conservative]], [[only-actual-metrics-are-real-and-comparable]]
- [[llm-evaluation]]

## Sources

- [[github-2024-04-22-llmc-state-of-the-union]]
- [[github-2024-05-28-llmc-gpt-2-124m]]
- [[github-2024-07-11-llmc-gpt-2-1-6b]]
- [[youtube-2024-06-09-reproduce-gpt-2]]
