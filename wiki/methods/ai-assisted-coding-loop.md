---
type: method
steps:
  - Work on one small, concrete thing at a time
  - Write a concrete prompt so verification is likely to pass
  - Keep diffs small and incremental
  - Verify each diff before asking for more
  - Spin the generate-verify loop fast
sources: ["[[youtube-2025-06-19-software-is-changing]]"]
aliases: [Keep the AI on the leash]
---
# AI-assisted coding loop
How he says he works with coding agents when he is trying to get real work done rather than vibe coding ([[youtube-2025-06-19-software-is-changing]] @23:16, @23:48).

## Steps
1. **One concrete thing.** He works on small chunks of a single concrete thing ([[youtube-2025-06-19-software-is-changing]] @23:48).
2. **Concrete prompt.** A vague prompt makes verification fail and starts a spin, so he spends more time being concrete ([[youtube-2025-06-19-software-is-changing]] @24:22).
3. **Small diffs.** He is always scared of diffs that are too big, and a 10,000-line diff is useless because he is still the bottleneck ([[youtube-2025-06-19-software-is-changing]] @22:43, @23:48).
4. **Verify.** He checks that each change introduces no bugs or security issues ([[youtube-2025-06-19-software-is-changing]] @23:16).
5. **Fast loop.** The goal is to spin generation and verification very fast ([[youtube-2025-06-19-software-is-changing]] @23:48).

## Seen in
- [[youtube-2025-06-19-software-is-changing]]
- [[partial-autonomy-apps]] — the product version of the same idea
- [[vibe-coding]] — the opposite mode
