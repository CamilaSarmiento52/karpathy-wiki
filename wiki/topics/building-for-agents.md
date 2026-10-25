---
type: topic
aliases: [Building for agents, llms.txt, LLM-legible docs, writing for LLMs]
first_seen: 2025-04-27
last_updated: 2026-07-03
sources: ["[[youtube-2025-06-19-software-is-changing]]", "[[github-2026-07-03-nanochat-readme]]", "[[x-2026-04-02-llm-knowledge-bases]]", "[[blog-2025-04-27-vibe-coding-menugen]]", "[[github-2025-08-21-rendergit-readme]]", "[[x-2025-11-18-reading-with-llms]]", "[[talk-2026-03-20-skill-issue]]", "[[github-2026-03-21-autoresearch-readme]]"]
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

**Writing for an LLM (X, 2025-11-18).** On the flip side of reading with LLMs, he says writers explaining something may increasingly shift from writing for another human to writing for an LLM, because once an LLM "gets it" it can target, personalise and serve the idea to its user; see [[writers-may-increasingly-write-for-llms]] ([[x-2025-11-18-reading-with-llms]] #1). The post speaks of LLMs and writers, not agents, docs or llms.txt ([[x-2025-11-18-reading-with-llms]] #1).

**The customer is agents (Skill Issue, 2026-03-20).** After his home claw replaced six smart-home apps, he says those apps in a sense should not exist: everything should be exposed API endpoints, with agents as the glue that calls the tools ([[talk-2026-03-20-skill-issue]] @13:08, @13:41). He wants his treadmill's data through an API, not a web UI and a login flow ([[talk-2026-03-20-skill-issue]] @13:41). The industry has to reconfigure in many ways, he says, because "the customer is not the human anymore" but agents acting on behalf of humans ([[talk-2026-03-20-skill-issue]] @14:13).

**Explaining to agents.** He says that a year or more earlier he would have made a video stepping through microGPT; he tried, but found it adds little, because anyone can ask their agent to explain 200 lines in various ways: "I'm not explaining to people anymore." ([[talk-2026-03-20-skill-issue]] @1:02:46). If you explain things to agents, they can route them to each person in their language with infinite patience; a skill instructs the agent how to teach, and he could script a microGPT curriculum as one ([[talk-2026-03-20-skill-issue]] @1:02:46, @1:03:20, @1:03:53). He still thinks he explains a little better than agents, but calls it a losing battle as models improve ([[talk-2026-03-20-skill-issue]] @1:03:53). Library documentation, he says, should be markdown for agents rather than HTML for humans ([[talk-2026-03-20-skill-issue]] @1:04:26). His job is now the few bits agents cannot produce, such as microGPT itself ([[talk-2026-03-20-skill-issue]] @1:04:59, @1:05:33). **Note:** this goes further than [[writers-may-increasingly-write-for-llms]] (2025-11-18), which said writers "may increasingly" write for LLMs; here he says he already explains to agents ([[x-2025-11-18-reading-with-llms]] #1; [[talk-2026-03-20-skill-issue]] @1:02:46).

**program.md as a skill (autoresearch README, 2026-03-21).** In [[autoresearch]] the human writes `program.md`, the Markdown instructions that give the agents context, and he calls it essentially a super lightweight "skill" ([[github-2026-03-21-autoresearch-readme]] §intro, §Running the agent). The README also speaks to agents as readers: people can "have their agents reference" the parent nanochat repo, and for small machines he suggests pasting the guide and the full source into a coding agent ([[github-2026-03-21-autoresearch-readme]] §Platform support).

## Claims
- [[writers-may-increasingly-write-for-llms]] — writing for the LLM that serves the reader

## Related
- [[vibe-coding]] — MenuGen's DevOps pain is where this argument starts
- [[deploying-a-vibe-coded-app-is-harder-than-writing-it]] — the browser work an LLM cannot reach
- [[llm-knowledge-bases]]
- [[nanochat]]
- [[rendergit]] — a repo's Human View and LLM View
- [[claws]] — a persistent agent that glues home APIs together
