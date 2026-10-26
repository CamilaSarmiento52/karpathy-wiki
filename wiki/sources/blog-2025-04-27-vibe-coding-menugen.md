---
type: source
raw_path: raw/blog/vibe-coding-menugen.md
published: 2025-04-27
medium: blog
summary: "His account of vibe coding MenuGen, a menu-to-pictures web app, end to end: the local demo was quick, while keys, deployment, auth and payments across many services were the slog."
url: https://karpathy.bearblog.dev/vibe-coding-menugen/
title: Vibe coding MenuGen
---
# Vibe coding MenuGen
Raw: [[raw/blog/vibe-coding-menugen]] · Original: https://karpathy.bearblog.dev/vibe-coding-menugen/

The post has no headings. Citations use `§intro ¶<lead>` for paragraphs that open with a bold-style lead phrase (¶Local version, ¶OpenAI API, ¶Replicate API, ¶Vercel deploy, ¶Clerk, ¶Stripe, ¶Database, ¶TLDR, ¶Going forward), `¶For now` for the closing paragraph, and `¶1`–`¶3` for the three opening paragraphs.

## Summary
MenuGen takes a photo of a restaurant menu and generates a picture for each item; he got a first version working on localhost at a vibe coding hackathon and then kept vibe coding to add deployment, authentication and payments (§intro ¶1, ¶2). He calls it his first end-to-end vibe coded app, built as someone with little web development experience, with all of the code written by Cursor and Claude (§intro ¶3). The local prototype came quickly, but API keys, rate limits, a Vercel deploy, Clerk authentication with a custom domain and Google OAuth, and Stripe payments took most of the effort, often because the LLM's knowledge of these services was out of date (§intro ¶Local version–¶Stripe). His summary is that it was fun as a local demo but a painful slog as a real app, and that most of his time went to configuring services in the browser, work an LLM cannot reach (§intro ¶TLDR). He suggests batteries-included platforms, services that address the user's LLM through CLIs, curl and Markdown docs, simpler stacks, and asks whether an app like MenuGen could be just a prompt (§intro ¶Going forward). He concludes vibe coding full web apps is messy today and not for anything important, but shows clear hints of greatness (§intro ¶For now).

**Note:** the post ends by linking its companion X post, [[x-2025-05-01-vibe-coding-hackathon]], which pastes this post's TLDR (§intro, last line).

## Key points
- MenuGen built end to end without writing code; what the process looked like → [[vibe-coding]]
- The code was quick; deployment and service configuration were the slog → [[deploying-a-vibe-coded-app-is-harder-than-writing-it]]
- Messy today, not for anything important, hints of greatness → [[vibe-coding-full-web-apps-is-not-yet-for-anything-important]]
- Services should talk to the user's LLM: CLI, curl, Markdown docs → [[building-for-agents]]
- Could the LLM answer with a webpage instead of text, along the lines of Artifacts → [[llm-gui]]
- Place in the sequence of his vibe coding statements → [[vibe-coding-over-time]]

## Fed pages
- [[vibe-coding]]
- [[deploying-a-vibe-coded-app-is-harder-than-writing-it]]
- [[vibe-coding-full-web-apps-is-not-yet-for-anything-important]]
- [[vibe-coding-is-for-throwaway-weekend-projects]]
- [[building-for-agents]]
- [[llm-gui]]
- [[vibe-coding-over-time]]
