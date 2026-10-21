---
type: topic
aliases: [Building for agents, llms.txt, LLM-legible docs]
first_seen: 2025-06-19
last_updated: 2026-07-03
sources: ["[[youtube-2025-06-19-software-is-changing]]", "[[github-2026-07-03-nanochat-readme]]", "[[x-2026-04-02-llm-knowledge-bases]]"]
related: ["[[vibe-coding]]", "[[llm-knowledge-bases]]"]
---
# Building for agents
His argument that agents are a new consumer of digital information, alongside humans using GUIs and programs using APIs, so infrastructure should be made readable and actionable for them ([[youtube-2025-06-19-software-is-changing]] @33:19, @33:53).

## What he says
He suggests an `llms.txt` file, like `robots.txt`, that tells LLMs what a domain is about in plain markdown ([[youtube-2025-06-19-software-is-changing]] @33:53, @34:25). He praises services that publish docs in markdown and replace every "click" instruction with a curl command an agent can run ([[youtube-2025-06-19-software-is-changing]] @34:59, @36:06). He names the Model Context Protocol as another way to speak to agents ([[youtube-2025-06-19-software-is-changing]] @36:06).

He likes tools where changing a URL makes something LLM-readable, such as gitingest and DeepWiki for GitHub repos ([[youtube-2025-06-19-software-is-changing]] @36:40, @37:12). Even though agents can click, he thinks it is still worth meeting them halfway ([[youtube-2025-06-19-software-is-changing]] @37:12, @37:48).

The nanochat README sends readers with questions to DeepWiki first ([[github-2026-07-03-nanochat-readme]] §intro). In his knowledge-base workflow he builds small tools and hands them to the LLM via CLI ([[x-2026-04-02-llm-knowledge-bases]] §Extra tools).

## Related
- [[vibe-coding]] — MenuGen's DevOps pain is where this argument starts
- [[llm-knowledge-bases]]
- [[nanochat]]
