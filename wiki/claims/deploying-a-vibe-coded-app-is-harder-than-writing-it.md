---
type: claim
stated_on: 2025-04-27
confidence: stated
sources: ["[[blog-2025-04-27-vibe-coding-menugen]]", "[[x-2025-05-01-vibe-coding-hackathon]]", "[[youtube-2025-06-19-software-is-changing]]"]
topic: "[[vibe-coding]]"
context: ["[[x-2025-02-02-vibe-coding]]"]
extends: ["[[vibe-coding-is-for-throwaway-weekend-projects]]"]
---
# Vibe coding MenuGen's code was the easy part; making it a real, deployed app was the slog
> "a bit of a painful slog as a deployed, real app" — [[blog-2025-04-27-vibe-coding-menugen]] §intro ¶TLDR

## Context
**Vibe coding MenuGen, 2025-04-27.** He sums up MenuGen as an exhilarating, fun escapade as a local demo and a painful slog as a deployed, real app ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶TLDR). The local prototype appeared very quickly from Cursor and Claude 3.7; he felt 80% done but says it was closer to 20% ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶Local version). He compares building a modern app to assembling IKEA furniture (he writes "IKEA future"): services, docs, API keys, configurations, dev and prod deployments, rate limits and pricing tiers ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶TLDR).

The obstacles he lists are outside the code: OpenAI and Replicate keys and heavy rate limits ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶OpenAI API, ¶Replicate API); a Vercel build that failed only remotely and API keys that had to be added by hand in Vercel's settings, which took him an hour to realise ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶Vercel deploy); Clerk's production mode requiring a custom domain, DNS changes and a Google OAuth setup across Vercel, Clerk and Google, where he thought of quitting ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶Clerk); and Stripe snippets in JavaScript for a TypeScript app, with products, prices and keys created twice ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶Stripe). Along the way Claude kept hallucinating deprecated APIs for these services, and he worked around it by pasting docs back and forth ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶OpenAI API, ¶Clerk).

What interested him most was that he spent little time in the code editor and most of it in the browser, moving between tabs and settings; that work and state is not accessible to an LLM, which he sets against the idea of automating society by 2027 ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶TLDR). He says the infrastructure was built for teams of professional web developers in a pre-LLM world, "Not vibe coding solo devs prototyping apps." ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶Going forward).

**X post, 2025-05-01.** Announcing MenuGen on X, he says the more interesting part for him was how easy or hard it is to build and deploy a full web app today if you are not a web developer, and pastes the blog's TLDR ([[x-2025-05-01-vibe-coding-hackathon]] #1). The TLDR is the same text as the blog's, a second location rather than a second statement ([[x-2025-05-01-vibe-coding-hackathon]] #1; [[blog-2025-04-27-vibe-coding-menugen]] §intro ¶TLDR).

**YC talk, published 2025-06-19.** He says the code was the easy part of vibe coding MenuGen; authentication, payments, the domain name and deployment were not code but DevOps in the browser, which was slow and took another week ([[youtube-2025-06-19-software-is-changing]] @32:13, @32:47). The demo worked on his laptop in a few hours ([[youtube-2025-06-19-software-is-changing]] @32:47). The week is the talk's figure; the blog gives no total time ([[youtube-2025-06-19-software-is-changing]] @32:47; [[blog-2025-04-27-vibe-coding-menugen]] §intro ¶TLDR).

## Related claims
- Extends [[vibe-coding-is-for-throwaway-weekend-projects]]: the February post judged the practice fine for throwaway weekend projects ([[x-2025-02-02-vibe-coding]]); the MenuGen post takes it past the local demo to a deployed, paid product and finds the new difficulty outside the code ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶3, ¶TLDR). Both hold; the dated pair is on [[vibe-coding-over-time]].
- **Note:** a companion to [[vibe-coding-full-web-apps-is-not-yet-for-anything-important]], from the same post: this claim is about where the difficulty lies, that one about what the practice is fit for today ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶TLDR, ¶For now).
