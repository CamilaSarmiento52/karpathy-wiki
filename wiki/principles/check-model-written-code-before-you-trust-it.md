---
type: principle
status: promoted
inferred: false
quotes:
  - {text: "I always go in small incremental chunks.", source: "[[youtube-2025-06-19-software-is-changing]]", location: "@23:48"}
  - {text: "we have to keep the AI on the leash", source: "[[youtube-2025-06-19-software-is-changing]]", location: "@22:43"}
  - {text: "use it as a tool in a toolbox don't trust it fully", source: "[[youtube-2025-02-05-deep-dive-into-llms]]", location: "@3:30:23"}
  - {text: "I would always encourage you to scrutinize the code", source: "[[youtube-2025-02-27-how-i-use-llms]]", location: "@1:05:46"}
  - {text: "This keeps the scope manageable and diffs reviewable.", source: "[[github-2026-03-21-autoresearch-readme]]", location: "§Design choices"}
sources: ["[[youtube-2025-06-19-software-is-changing]]", "[[youtube-2025-02-05-deep-dive-into-llms]]", "[[youtube-2025-02-27-how-i-use-llms]]", "[[github-2026-03-21-autoresearch-readme]]", "[[talk-2026-03-20-skill-issue]]", "[[talk-2026-04-29-sequoia-ascent-2026]]", "[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]", "[[blog-2025-04-27-vibe-coding-menugen]]"]
---
# Keep model-written code reviewable and check it before you trust it, more carefully the more the code matters

> "I always go in small incremental chunks." — [[youtube-2025-06-19-software-is-changing]] @23:48
>
> "use it as a tool in a toolbox don't trust it fully" — [[youtube-2025-02-05-deep-dive-into-llms]] @3:30:23

## In practice

This rule is dated. 2025: small diffs, check everything. In the YC talk he says he is scared of diffs that are too big, works in small incremental chunks, and that a 10,000-line diff is not useful to him because he is still the bottleneck ([[youtube-2025-06-19-software-is-changing]] @22:43, @23:48). In the Deep Dive lecture he tells viewers to use models as a tool, check their work and own the product ([[youtube-2025-02-05-deep-dive-into-llms]] @3:30:23). In How I use LLMs, ChatGPT's analysis code silently filled a missing 2015 value, and he urges viewers to scrutinize the code ([[youtube-2025-02-27-how-i-use-llms]] @1:05:46).

Since December, as he says in interviews published in 2026, his practice differs in kind. He hands whole new functionalities to parallel agents and reviews their work as best he can, depending on how much he cares about that code ([[talk-2026-03-20-skill-issue]] @04:25). He says the chunks just came out fine, he cannot remember the last time he corrected the agent, and he trusted the system more and more ([[talk-2026-04-29-sequoia-ascent-2026]] @01:08). Oversight now sits at the spec and the quality bar: agentic engineering preserves the quality bar and you are still responsible for your software, and people own the spec and the oversight while agents do the details ([[talk-2026-04-29-sequoia-ascent-2026]] @15:49, @20:44). Do not claim he reads every line of agent code in 2026. The "small" part holds for 2025 and for autoresearch, whose single file to modify keeps diffs reviewable ([[github-2026-03-21-autoresearch-readme]] §Design choices).

When reviewing model-written code, read for what he has seen models get wrong: over-defensive try-catch code, bloat and deprecated APIs in his own repo ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @33:14), hallucinated deprecated APIs while building MenuGen ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶OpenAI API, ¶Clerk authentication), and silently filled values ([[youtube-2025-02-27-how-i-use-llms]] @1:05:46). Say which you found, and check more carefully the more the code matters ([[talk-2026-03-20-skill-issue]] @04:25).

## Rests on

- [[ai-assisted-coding-loop]], [[verify-citations]]
- [[use-llms-as-tools-and-check-their-work]], [[use-llms-as-copilots-with-human-oversight]], [[coding-models-are-weak-at-code-never-written-before]], [[agentic-engineering-keeps-the-quality-bar-while-going-faster]], [[he-now-delegates-most-coding-to-agents]]
- [[vibe-coding]], [[partial-autonomy-apps]]

## Sources

- [[youtube-2025-06-19-software-is-changing]]
- [[youtube-2025-02-05-deep-dive-into-llms]]
- [[youtube-2025-02-27-how-i-use-llms]]
- [[github-2026-03-21-autoresearch-readme]]
- [[talk-2026-03-20-skill-issue]]
- [[talk-2026-04-29-sequoia-ascent-2026]]
- [[talk-2025-10-17-dwarkesh-ghosts-not-animals]]
- [[blog-2025-04-27-vibe-coding-menugen]]
