---
type: topic
aliases: [Building for agents, llms.txt, LLM-legible docs]
first_seen: 2025-04-27
last_updated: 2026-07-03
sources: ["[[youtube-2025-06-19-software-is-changing]]", "[[github-2026-07-03-nanochat-readme]]", "[[x-2026-04-02-llm-knowledge-bases]]", "[[blog-2025-04-27-vibe-coding-menugen]]", "[[github-2025-08-21-rendergit-readme]]"]
related: ["[[vibe-coding]]", "[[llm-knowledge-bases]]"]
---
# Building for agents
His argument that agents are a new consumer of digital information, alongside humans using GUIs and programs using APIs, so infrastructure should be made readable and actionable for them ([[youtube-2025-06-19-software-is-changing]] @33:19, @33:53).

## What he says
He suggests an `llms.txt` file, like `robots.txt`, that tells LLMs what a domain is about in plain markdown ([[youtube-2025-06-19-software-is-changing]] @33:53, @34:25). He praises services that publish docs in markdown and replace every "click" instruction with a curl command an agent can run ([[youtube-2025-06-19-software-is-changing]] @34:59, @36:06). He names the Model Context Protocol as another way to speak to agents ([[youtube-2025-06-19-software-is-changing]] @36:06).

He likes tools where changing a URL makes something LLM-readable, such as gitingest and DeepWiki for GitHub repos ([[youtube-2025-06-19-software-is-changing]] @36:40, @37:12). Even though agents can click, he thinks it is still worth meeting them halfway ([[youtube-2025-06-19-software-is-changing]] @37:12, @37:48).

**The MenuGen post (2025-04-27).** Everything a service tells the user, he writes, will be copy-pasted straight into an LLM, so it might as well talk to the LLM directly ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶Going forward). His suggestions are a CLI tool, a backend configurable with curl commands and docs in Markdown: "Don't talk to a developer." but "Instruct and empower their LLM." ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶Going forward). He also wants an opinionated, batteries-included platform with domain, hosting, authentication, payments, database and server functions preconfigured, the opposite of Vercel Marketplace, and for his next app is considering plain HTML, CSS and JavaScript with a Python backend ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶Going forward).

**rendergit (README, 2025-08-21).** His [[rendergit]] renders a GitHub repo two ways: a browsable Human View, and an LLM View that gives the whole codebase as CXML text to paste into Claude or ChatGPT ([[github-2025-08-21-rendergit-readme]] §Basic usage, §Features). The README speaks of LLMs, Claude and ChatGPT, not of agents, and makes no argument; it is an example of a repo made LLM-readable, next to the gitingest and DeepWiki tools he praises in the YC talk ([[github-2025-08-21-rendergit-readme]] §Features; [[youtube-2025-06-19-software-is-changing]] @36:40).

The nanochat README sends readers with questions to DeepWiki first ([[github-2026-07-03-nanochat-readme]] §intro). In his knowledge-base workflow he builds small tools and hands them to the LLM via CLI ([[x-2026-04-02-llm-knowledge-bases]] §Extra tools).

## Related
- [[vibe-coding]] — MenuGen's DevOps pain is where this argument starts
- [[deploying-a-vibe-coded-app-is-harder-than-writing-it]] — the browser work an LLM cannot reach
- [[llm-knowledge-bases]]
- [[nanochat]]
- [[rendergit]] — a repo's Human View and LLM View
