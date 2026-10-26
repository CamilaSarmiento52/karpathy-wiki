---
type: principle
status: bench
inferred: true
quotes:
  - {text: "it made an implicit assumption", source: "[[youtube-2025-02-27-how-i-use-llms]]", location: "@1:08:01"}
  - {text: "when to ask clarifying questions", source: "[[talk-2026-03-20-skill-issue]]", location: "@25:39"}
sources: ["[[youtube-2025-02-27-how-i-use-llms]]", "[[talk-2026-03-20-skill-issue]]", "[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
---
# State the assumptions you are making, and ask when the request leaves them open

This rule is inferred: no source states it.

> "it made an implicit assumption" — [[youtube-2025-02-27-how-i-use-llms]] @1:08:01
>
> "when to ask clarifying questions" — [[talk-2026-03-20-skill-issue]] @25:39

## In practice

Why it is an inference: each quote describes a failure he sees in models, not a rule he gives. In How I use LLMs, ChatGPT's analysis code filled in a missing 2015 value without saying so, and he calls this an implicit assumption and says to scrutinize the code ([[youtube-2025-02-27-how-i-use-llms]] @1:05:46, @1:08:01). In the Skill Issue interview he lists the nuance of what he intended, and knowing when to ask clarifying questions, among the things models struggle with ([[talk-2026-03-20-skill-issue]] @25:39). The imperative is this wiki's reading of those complaints. DESIGN.md's phrase that this is his top complaint about coding agents has no support in any raw file and is not repeated here.

A limit on the rule: he defends deliberate assumptions. Agents working on his repo were over-defensive, added try-catch statements and tried to make it a production code base, and he says "I have a bunch of assumptions in my code, and it's okay." ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @33:14).

When building or teaching, list the assumptions the request leaves open (data, shapes, scale, what "done" means) before writing code, and ask if one of them changes the result ([[talk-2026-03-20-skill-issue]] @25:39). When reviewing, name the assumptions that silently change a result, such as a filled-in missing value or an assumed dimension or default ([[youtube-2025-02-27-how-i-use-llms]] @1:05:46). Do not ask the author to justify, or guard against, deliberate simplifying assumptions, and do not suggest defensive code for them ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @33:14). Say that you are leaning on an inferred rule when you use it.

## Rests on

- [[verify-citations]], [[ai-assisted-coding-loop]], [[check-shapes-and-broadcasting]]
- [[coding-models-are-weak-at-code-never-written-before]], [[agent-failures-mostly-feel-like-a-skill-issue]]

## Sources

- [[youtube-2025-02-27-how-i-use-llms]]
- [[talk-2026-03-20-skill-issue]]
- [[talk-2025-10-17-dwarkesh-ghosts-not-animals]]
