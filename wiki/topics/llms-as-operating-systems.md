---
type: topic
aliases: [LLM OS, LLMs are operating systems, LLM as kernel process, context window as RAM]
first_seen: 2023-11-23
last_updated: 2025-12-19
sources: ["[[youtube-2023-11-23-intro-to-llms]]", "[[youtube-2025-06-19-software-is-changing]]", "[[blog-2025-12-19-year-in-review-2025]]"]
related: ["[[software-3-0]]", "[[llm-gui]]", "[[jagged-intelligence]]"]
---
# LLMs as operating systems
His analogy that the LLM is a new kind of computer, first drawn in his November 2023 talk, where he calls the LLM the kernel process of an emerging operating system that coordinates memory and computational tools for problem solving ([[youtube-2023-11-23-intro-to-llms]] @42:06, @42:38). In 2025 he puts it as the model being like the CPU and the context window like memory, with the LLM orchestrating both ([[youtube-2025-06-19-software-is-changing]] @10:01).

## What he says
**The 2023 version.** He says it is not accurate to think of an LLM as a chatbot or word generator; it is more correct to see it as the kernel process of an emerging operating system ([[youtube-2023-11-23-intro-to-llms]] @42:06). His picture of an LLM in a few years: it reads and generates text, knows more than any single human, browses and uses retrieval, uses a calculator and Python, sees and generates images and video, hears and speaks, thinks for a long time with a System 2, maybe self-improves in narrow domains, and is customized into many experts ([[youtube-2023-11-23-intro-to-llms]] @42:38, @43:11). The memory hierarchy maps over, with the internet as disk via browsing and the context window as RAM, a finite, precious working memory that the kernel pages information in and out of ([[youtube-2023-11-23-intro-to-llms]] @43:45). He sees further equivalents in multithreading, multiprocessing, speculative execution, and user and kernel space ([[youtube-2023-11-23-intro-to-llms]] @44:18). The ecosystem matches too: proprietary systems like Windows and macOS against an open Linux-based ecosystem, and proprietary GPT, Claude and Bard against an open ecosystem mostly based on Llama ([[youtube-2023-11-23-intro-to-llms]] @44:52). On Chatbot Arena the closed models work a lot better, while open models work worse but may be good enough, and open source is chasing the proprietary ecosystems ([[youtube-2023-11-23-intro-to-llms]] @24:22, @24:55). The new computing stack, he says, is built around LLMs orchestrating tools through a natural-language interface ([[youtube-2023-11-23-intro-to-llms]] @45:25).

**The 2025 version.** He tries three analogies in turn. LLMs are like utilities, with capex to build the grid, opex to serve it, metered access per token, and an "intelligence brownout" when models go down ([[youtube-2025-06-19-software-is-changing]] @06:41, @07:14). They are like fabs, with large capex and research secrets centralising in labs ([[youtube-2025-06-19-software-is-changing]] @07:47, @08:22). But the analogy he finds strongest is the operating system: closed providers like Windows and macOS, and open models as a possible Linux ([[youtube-2025-06-19-software-is-changing]] @08:54, @09:28).

He places this at roughly the 1960s of computing: compute is expensive, so models are centralised in the cloud and time-shared, and personal computing has not happened yet ([[youtube-2025-06-19-software-is-changing]] @10:34, @11:05). Talking to a chatbot feels to him like using an operating system through a terminal ([[youtube-2025-06-19-software-is-changing]] @12:12).

One way LLMs differ is that they flip technology diffusion: consumers adopted them before governments and corporations ([[youtube-2025-06-19-software-is-changing]] @12:45, @13:18).

In December 2025 he restates the paradigm as similar to computers of the 1970s and 80s, expecting equivalents of personal computing, microcontrollers and an internet of agents ([[blog-2025-12-19-year-in-review-2025]] §6).

**Note:** the component he names differs: in 2023 the LLM is the kernel process, in 2025 it is like the CPU, with the context window as memory in both. This is a difference of wording, not a change of view ([[youtube-2023-11-23-intro-to-llms]] @42:06, @43:45; [[youtube-2025-06-19-software-is-changing]] @10:01).

**Note:** the decade he names moves from the 1960s in the talk to the 1970s–80s in the essay; both are framed as early-stage analogies, not a stated change of view ([[youtube-2025-06-19-software-is-changing]], [[blog-2025-12-19-year-in-review-2025]]).

## Claims
- [[llms-are-the-kernel-of-an-emerging-operating-system]] — the 2023 statement of the analogy

## Related
- [[software-3-0]]
- [[llm-gui]] — the GUI this computer does not have yet
- [[jagged-intelligence]] — the psychology of the thing running on it
- [[llm-tool-use]] — the tools the kernel coordinates
- [[llm-security]] — the security challenges of the new stack
