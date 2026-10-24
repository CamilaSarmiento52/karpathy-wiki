---
type: topic
aliases: [Software 3.0, Software 2.0, Software 1.0]
first_seen: 2025-06-19
last_updated: 2025-12-19
sources: ["[[youtube-2025-06-19-software-is-changing]]", "[[blog-2025-12-19-year-in-review-2025]]"]
context: ["[[talk-2024-09-05-no-priors-ep-80]]", "[[talk-2024-10-03-cuda-mode-keynote]]"]
related: ["[[english-is-the-new-programming-language]]", "[[llms-as-operating-systems]]", "[[vibe-coding]]"]
---
# Software 3.0
His name for programming an LLM with prompts: Software 1.0 is code, Software 2.0 is neural network weights shaped by data and an optimizer, and Software 3.0 is prompts, which he describes as "programs that program the LLM" ([[youtube-2025-06-19-software-is-changing]] @01:39, @03:19).

## What he says
He says software barely changed for about 70 years and then changed twice in the last few years ([[youtube-2025-06-19-software-is-changing]] @00:34). What made 3.0 new to him is that neural networks became programmable once large language models arrived, rather than being fixed-function classifiers ([[youtube-2025-06-19-software-is-changing]] @02:45).

He illustrates the three paradigms with sentiment classification: write Python, train a classifier, or write a few-shot prompt ([[youtube-2025-06-19-software-is-changing]] @03:19). He sees Hugging Face as the GitHub of Software 2.0 ([[youtube-2025-06-19-software-is-changing]] @02:12).

At Tesla he watched the Autopilot neural network grow while C++ code was deleted, and he says Software 3.0 is now eating through the stack the same way ([[youtube-2025-06-19-software-is-changing]] @04:56, @05:32). His advice to people entering the industry is to be fluent in all three paradigms and move between them as the task needs ([[youtube-2025-06-19-software-is-changing]] @05:32).

By the end of 2025 he describes LLMs as the next major computing paradigm and says AI crossed the threshold to build impressive programs simply via English ([[blog-2025-12-19-year-in-review-2025]] §5, §6).

**Note:** in the No Priors interview (published 2024-09-05) he tells the Tesla version without the Software 3.0 framing: the plan was always for the neural net to eat through the stack, discarding C++ code until it outputs steering commands ([[talk-2024-09-05-no-priors-ep-80]] @04:21, @04:54); see [[self-driving]].

**Note:** in the CUDA MODE keynote (published 2024-10-03) he uses the Software 2.0 term without defining it: if PyTorch, especially torch.compile, is a bit like GCC for Software 2.0, then llm.c is a bit like writing assembly, doing everything manually ([[talk-2024-10-03-cuda-mode-keynote]] @20:59, @21:32). That analogy leads into [[llms-may-write-custom-low-level-code-for-any-application]] ([[talk-2024-10-03-cuda-mode-keynote]] @22:05).

## Claims
- [[english-is-the-new-programming-language]]
- [[llms-may-write-custom-low-level-code-for-any-application]]

## Related
- [[llms-as-operating-systems]] — the computer that Software 3.0 programs
- [[vibe-coding]] — what programming in English looks like in practice
- [[partial-autonomy-apps]]
- [[gpt-is-a-general-purpose-computer-running-natural-language-programs]] — his 2023 tweet framing prompts as programs
- [[prompting-llms]] — how he says to write those programs
