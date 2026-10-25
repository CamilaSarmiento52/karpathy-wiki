---
type: method
steps:
  - Work on one small, concrete thing at a time
  - Write a concrete prompt so verification is likely to pass
  - Keep diffs small and incremental
  - Verify each diff before asking for more
  - Spin the generate-verify loop fast
  - Learn what each tool is good and bad at
  - Point at the spot and let autocomplete fill it
  - Hand boilerplate and unfamiliar languages to agents, with tests and a reference you understand
  - Ask the strongest model about the whole repo
sources: ["[[youtube-2025-06-19-software-is-changing]]", "[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
aliases: [Keep the AI on the leash]
---
# AI-assisted coding loop
How he says he works with coding agents when he is trying to get real work done rather than vibe coding ([[youtube-2025-06-19-software-is-changing]] @23:16, @23:48). Steps 6–9 are from the Dwarkesh interview, published 2025-10-17, about building nanochat ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @30:43).

## Steps
1. **One concrete thing.** He works on small chunks of a single concrete thing ([[youtube-2025-06-19-software-is-changing]] @23:48).
2. **Concrete prompt.** A vague prompt makes verification fail and starts a spin, so he spends more time being concrete ([[youtube-2025-06-19-software-is-changing]] @24:22).
3. **Small diffs.** He is always scared of diffs that are too big, and a 10,000-line diff is useless because he is still the bottleneck ([[youtube-2025-06-19-software-is-changing]] @22:43, @23:48).
4. **Verify.** He checks that each change introduces no bugs or security issues ([[youtube-2025-06-19-software-is-changing]] @23:16).
5. **Fast loop.** The goal is to spin generation and verification very fast ([[youtube-2025-06-19-software-is-changing]] @23:48).
6. **Know the tools.** Autocomplete and agents are tools; you have to learn what they are good and bad at and when to use them ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @31:21).
7. **Point, then autocomplete.** Instead of typing what he wants in English, he goes to where the code must appear and types the first few letters, a high-bandwidth specification; see [[autocomplete-is-his-coding-sweet-spot]] ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @33:50, @37:33).
8. **Agents where they fit.** He uses agents for boilerplate that is not mission-critical, such as nanochat's report, and in an unfamiliar language, Rust, where having a Python implementation he fully understands, plus tests, made him feel safer ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @31:21, @34:26).
9. **Ask the oracle.** For some questions he pastes the whole repo into the strongest model, GPT-5 Pro at the time ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @36:57).

## Seen in
- [[youtube-2025-06-19-software-is-changing]]
- [[partial-autonomy-apps]] — the product version of the same idea
- [[vibe-coding]] — the opposite mode
