---
type: topic
aliases: [Software 3.0, Software 2.0, Software 1.0]
first_seen: 2025-06-19
last_updated: 2026-04-29
sources: ["[[youtube-2025-06-19-software-is-changing]]", "[[blog-2025-12-19-year-in-review-2025]]", "[[blog-2025-11-17-verifiability]]", "[[talk-2026-04-29-sequoia-ascent-2026]]"]
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

**Software 1.0 and 2.0 by what they automate (Verifiability, 2025-11-17).** He calls hand-written programs, which automate rote, easy-to-specify work such as typing, bookkeeping and human calculation, Software 1.0 ([[blog-2025-11-17-verifiability]] §intro). Software 2.0, pointing to his Software 2.0 blog post "from a while ago", writes programs by specifying objectives such as classification accuracy or reward functions and searching program space with gradient descent ([[blog-2025-11-17-verifiability]] §intro). His closing pair: Software 1.0 easily automates what you can specify, Software 2.0 what you can verify; see [[software-2-0-automates-what-you-can-verify]] ([[blog-2025-11-17-verifiability]] §intro). The post does not mention Software 3.0 or prompts ([[blog-2025-11-17-verifiability]] §intro).

**Sequoia Ascent (2026-04-29).** He restates the three: Software 1.0 is writing code, Software 2.0 is programming by arranging datasets, objectives and architectures and training networks, and because training on the internet forces a model to multitask, LLMs become a programmable computer in a certain sense ([[talk-2026-04-29-sequoia-ascent-2026]] @02:46, @03:18). In Software 3.0 programming turns to prompting, and what is in the context window is the lever over the LLM interpreter; his examples are an installer written as text for your agent and a one-prompt Gemini version of MenuGen; see [[english-is-the-new-programming-language]] and [[in-software-3-0-some-apps-should-not-exist]] ([[talk-2026-04-29-sequoia-ascent-2026]] @03:18, @04:22, @05:59). It is not only programming getting faster, he says: general information processing over unstructured data is now automatable, such as compiling a knowledge base, which no code could do before ([[talk-2026-04-29-sequoia-ascent-2026]] @06:32, @07:04). He restates the specify/verify pair for traditional computers and LLMs; see [[software-2-0-automates-what-you-can-verify]] ([[talk-2026-04-29-sequoia-ascent-2026]] @09:47). The "explicit rules / learned weights" phrasing at @02:11 is the host's ([[talk-2026-04-29-sequoia-ascent-2026]] @02:11).

**Note:** in the No Priors interview (published 2024-09-05) he tells the Tesla version without the Software 3.0 framing: the plan was always for the neural net to eat through the stack, discarding C++ code until it outputs steering commands ([[talk-2024-09-05-no-priors-ep-80]] @04:21, @04:54); see [[self-driving]].

**Note:** in the CUDA MODE keynote (published 2024-10-03) he uses the Software 2.0 term without defining it: if PyTorch, especially torch.compile, is a bit like GCC for Software 2.0, then llm.c is a bit like writing assembly, doing everything manually ([[talk-2024-10-03-cuda-mode-keynote]] @20:59, @21:32). That analogy leads into [[llms-may-write-custom-low-level-code-for-any-application]] ([[talk-2024-10-03-cuda-mode-keynote]] @22:05).

## Claims
- [[english-is-the-new-programming-language]]
- [[llms-may-write-custom-low-level-code-for-any-application]]
- [[software-2-0-automates-what-you-can-verify]] — 1.0 automates what you can specify, 2.0 what you can verify
- [[in-software-3-0-some-apps-should-not-exist]] — 2026-04-29: his MenuGen as one Gemini prompt

## Related
- [[llms-as-operating-systems]] — the computer that Software 3.0 programs
- [[vibe-coding]] — what programming in English looks like in practice
- [[partial-autonomy-apps]]
- [[gpt-is-a-general-purpose-computer-running-natural-language-programs]] — his 2023 tweet framing prompts as programs
- [[prompting-llms]] — how he says to write those programs
