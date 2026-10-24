---
type: claim
stated_on: 2024-10-02
confidence: stated
sources: ["[[x-2024-10-02-gpu-mode-talk]]", "[[talk-2024-10-03-cuda-mode-keynote]]"]
context: ["[[blog-2025-12-19-year-in-review-2025]]", "[[talk-2023-05-25-state-of-gpt]]"]
topic: "[[software-3-0]]"
---
# He expects LLMs may come to write custom low-level code like llm.c for any application
> "LLMs may export custom binaries like llm.c for any application directly" — [[x-2024-10-02-gpu-mode-talk]]

## Context
The last item in his outline of the llm.c talk is a thought rather than a result: software abstractions like Python and PyTorch, he says, really exist only because humans are finite in knowledge, IQ and attention, and with increasing AI capability LLMs may export custom binaries like llm.c for any application directly, tearing apart and refactoring abstractions as needed ([[x-2024-10-02-gpu-mode-talk]]). The claim is hedged with "may" and conditioned on increasing AI capability ([[x-2024-10-02-gpu-mode-talk]]).

In the CUDA MODE keynote (published 2024-10-03) he gives the same thought as a motivation for starting llm.c, which he says was not haphazard ([[talk-2024-10-03-cuda-mode-keynote]] @20:59). Several people writing llm.c over about three months produced something faster than PyTorch for GPT-2 training, which he says proves it is possible, but costs several people several months ([[talk-2024-10-03-cuda-mode-keynote]] @21:32). If LLMs are about to get much better at coding, he expects an LLM could do this for any custom application: act as a kind of compiler, do all the llm.c work and output a binary you compile and run ([[talk-2024-10-03-cuda-mode-keynote]] @21:32, @22:05). Saying he does not actually know, he wonders whether Python, PyTorch and everything else is just a crutch because humans have finite knowledge, intelligence and attention ([[talk-2024-10-03-cuda-mode-keynote]] @22:05). In these early stages, he says, an LLM prompted to write GPT-2 in C probably would not produce llm.c, but with llm.c in its context, few-shot learning makes that much more likely, so llm.c could be useful example code ([[talk-2024-10-03-cuda-mode-keynote]] @22:05, @22:37). He calls this "not unlikely", then "kind of likely", says software development in general will probably change a lot, and calls llm.c an exploration of whether this is even possible ([[talk-2024-10-03-cuda-mode-keynote]] @22:37).

## Related claims
- **Note:** not a contradiction of [[use-llms-as-copilots-with-human-oversight]]: that is advice about using 2023's LLMs, this a conditional forecast, and he says current LLMs would likely fail from scratch ([[talk-2024-10-03-cuda-mode-keynote]] @22:37; [[talk-2023-05-25-state-of-gpt]] @39:57).
- **Note:** no relation set with [[vibe-coding-will-terraform-software]] (2025-12-19), which is about people building programs in English, while this is about LLMs writing low-level, abstraction-free code; the two point the same way but are different ideas ([[blog-2025-12-19-year-in-review-2025]] §5; [[x-2024-10-02-gpu-mode-talk]]).
