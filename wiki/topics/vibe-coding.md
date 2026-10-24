---
type: topic
aliases: [Vibe coding, vibe coded]
first_seen: 2025-02-02
last_updated: 2026-04-02
sources: ["[[x-2025-02-02-vibe-coding]]", "[[youtube-2025-06-19-software-is-changing]]", "[[blog-2025-12-19-year-in-review-2025]]", "[[x-2026-04-02-llm-knowledge-bases]]", "[[youtube-2025-02-27-how-i-use-llms]]", "[[blog-2025-04-07-power-to-the-people]]", "[[blog-2025-04-27-vibe-coding-menugen]]", "[[x-2025-05-01-vibe-coding-hackathon]]", "[[github-2025-08-21-rendergit-readme]]", "[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
related: ["[[software-3-0]]", "[[english-is-the-new-programming-language]]", "[[vibe-coding-over-time]]"]
---
# Vibe coding
A term he coined for building software by talking to an LLM and accepting its output without reading the code, so that you "forget that the code even exists" ([[x-2025-02-02-vibe-coding]]).

## What he says
In the original post he describes dictating requests to Cursor Composer, always accepting all diffs, pasting errors back without comment, and asking for random changes when a bug will not go away ([[x-2025-02-02-vibe-coding]]). He called it fine for throwaway weekend projects and said it was not really coding ([[x-2025-02-02-vibe-coding]]).

In the talk published 2025-06-19 he said he expected the post to fizzle and was surprised it gave a name to something people felt but could not say ([[youtube-2025-06-19-software-is-changing]] @29:22, @29:56). He calls a video of kids vibe coding a gateway drug to software development ([[youtube-2025-06-19-software-is-changing]] @30:30). He vibe-coded an iOS app without knowing Swift and the MenuGen web app ([[youtube-2025-06-19-software-is-changing]] @31:04, @31:38). In the talk he calls MenuGen a negative-revenue app for him, on which he has lost a huge amount of money, since everyone gets $5 in free credits on sign-up ([[youtube-2025-06-19-software-is-changing]] @31:38, @32:13).

His lesson from MenuGen is that the code was the easy part: authentication, payments, domains and deployment took a week of clicking through browser instructions ([[youtube-2025-06-19-software-is-changing]] @32:13, @32:47). That frustration leads directly to his argument for [[building-for-agents]] ([[youtube-2025-06-19-software-is-changing]] @33:19).

**MenuGen, the written account (2025-04-27).** MenuGen takes a photo of a restaurant menu and generates an image for each item; he notes the pictures are not what that restaurant will serve, only the basic idea ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶2). He got the first version working on localhost at a vibe coding hackathon, then kept vibe coding to deploy it and add authentication and payments ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶1, ¶2). He calls it his first end-to-end vibe coded app, built as someone who tinkers but has little to no web development experience, into a product people can sign up and pay for, on which, he writes, he pockets a 10% markup ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶3). He wrote no code directly: "100% of the code was written by Cursor+Claude", and he says he does not really know how MenuGen works in the conventional sense ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶3). The LLMs, he sums up, have slightly outdated knowledge of everything, make subtle but critical design mistakes when watched closely, and sometimes hallucinate or gaslight ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶TLDR). His example is Claude matching Stripe payments to users by email, which could leave a buyer without credits; it rewrote the code with user ids when he pointed this out, and its promise to do better next time he calls gaslighting ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶Stripe). He left a database and work queue as future work, meaning more services, logins, keys and docs ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶Database). The two MenuGen claims below come from this post ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶TLDR, ¶For now). In the companion X post, dated 2025-05-01, he says he tinkers but is not a web developer by background, that Cursor with Claude and o3 wrote the code, and that he does not really know how the app works in the conventional sense he is used to as an engineer ([[x-2025-05-01-vibe-coding-hackathon]] #1). **Note:** the 10% markup is the post's figure and the negative revenue the talk's; each is given with its own source and they are not reconciled ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶3; [[youtube-2025-06-19-software-is-changing]] @32:13).

The rendergit README, dated 2025-08-21, says he vibe coded the utility a few months before, keeps using it very often and is sharing it without intending to maintain or support it; see [[rendergit]] ([[github-2025-08-21-rendergit-readme]] §Contributing).

By December 2025 he says vibe coding empowers trained professionals as well as regular people, and that he vibe-coded nanochat's Rust BPE tokenizer instead of learning Rust to that level ([[blog-2025-12-19-year-in-review-2025]] §5). He describes code as suddenly "free, ephemeral, malleable, discardable after single use" ([[blog-2025-12-19-year-in-review-2025]] §5).

In April 2026 he mentions vibe-coding a small search engine over his knowledge-base wiki ([[x-2026-04-02-llm-knowledge-bases]] §Extra tools).

In How I use LLMs, published 2025-02-27, he says the name for giving Cursor's Composer control, telling it what to do and hoping it works, is vibe coding, a name he thinks he probably minted ([[youtube-2025-02-27-how-i-use-llms]] @1:18:01). Worst case, he says, you fall back to ordinary programming, because all the files are there to inspect ([[youtube-2025-02-27-how-i-use-llms]] @1:18:01, @1:21:55). He builds a tic-tac-toe app from about five sentences, and adding confetti and a sound he admits he is not keeping full track of the code ([[youtube-2025-02-27-how-i-use-llms]] @1:16:19, @1:19:40, @1:21:55).

In Power to the people, dated 2025-04-07, he lists "People can now vibe code apps." among the things an individual can do at an adequate level without another expert ([[blog-2025-04-07-power-to-the-people]] §intro ¶3). Organisations, with their complexity and lower margin for error, are different: "You can't just vibe code something." ([[blog-2025-04-07-power-to-the-people]] §intro ¶4).

**Building nanochat (Dwarkesh, published 2025-10-17).** He built nanochat over a bit more than a month and sees three classes of coders: those who reject LLMs, the intermediate, where he is, writing from scratch with autocomplete as the architect, and vibe coders, who ask agents to implement things ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @30:43, @31:21). He partially vibe-coded nanochat's report, which was boilerplate and not mission-critical, and vibe-coded some of the Rust tokenizer, being fairly new to Rust, with a Python implementation he fully understands and tests, so he felt safer ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @34:26). Models, he says, increase accessibility to unfamiliar languages ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @34:26). For the core code they were not net useful; see [[coding-models-are-weak-at-code-never-written-before]] and [[autocomplete-is-his-coding-sweet-spot]] ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @33:14, @37:33). A lot of vibe coding lacks the high cost of failure that production code has, where any mistake can become a security vulnerability ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:45:02).

**Note:** the scope he gives the practice widens across these sources; see [[vibe-coding-over-time]] ([[x-2025-02-02-vibe-coding]], [[blog-2025-12-19-year-in-review-2025]]).

## Claims
- [[vibe-coding-is-for-throwaway-weekend-projects]]
- [[deploying-a-vibe-coded-app-is-harder-than-writing-it]] — MenuGen: the code was easy, the deployed app a slog
- [[vibe-coding-full-web-apps-is-not-yet-for-anything-important]] — April 2025: messy, but hints of greatness
- [[vibe-coding-will-terraform-software]]
- [[english-is-the-new-programming-language]]
- [[coding-models-are-weak-at-code-never-written-before]] — October 2025: not net useful for nanochat's novel code
- [[autocomplete-is-his-coding-sweet-spot]] — October 2025: his own mode, with agents for some code

## Related
- [[vibe-coding-over-time]]
- [[nanochat]] — its tokenizer was vibe-coded
- [[rendergit]] — a vibe-coded utility he keeps using
- [[software-3-0]]
- [[technology-diffusion]] — why individuals, not organisations, gain most from it so far
- [[ai-assisted-coding-loop]] — what he does when he is not vibe coding
