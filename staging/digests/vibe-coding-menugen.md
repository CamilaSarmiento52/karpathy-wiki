# Digest: Vibe coding MenuGen
- raw: raw/blog/vibe-coding-menugen.md · published: 2025-04-27 · medium: blog · words: 2491 (frontmatter); 2513 by wc
- source slug: blog-2025-04-27-vibe-coding-menugen

Location scheme: the post has no headings, so every location is `§intro`. Most paragraphs
open with a bold-style lead phrase; I cite those as `¶<lead>` (¶Local version, ¶OpenAI API,
¶Replicate API, ¶Vercel deploy, ¶Clerk, ¶Stripe, ¶Database, ¶TLDR, ¶Going forward, and
¶For now for the closing paragraph). The three opening paragraphs are ¶1–¶3. Merge may keep
only `§intro`.

## Source page
```
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

## Summary
MenuGen takes a photo of a restaurant menu and generates a picture for each item; he got a first version working on localhost at a vibe coding hackathon and then kept vibe coding to add deployment, authentication and payments (§intro ¶1, ¶2). He calls it his first end-to-end vibe coded app, built as someone with little web development experience, with all of the code written by Cursor and Claude (§intro ¶3). The local prototype came quickly, but API keys, rate limits, a Vercel deploy, Clerk authentication with a custom domain and Google OAuth, and Stripe payments took most of the effort, often because the LLM's knowledge of these services was out of date (§intro ¶Local version–¶Stripe). His summary is that it was fun as a local demo but a painful slog as a real app, and that most of his time went to configuring services in the browser, work an LLM cannot reach (§intro ¶TLDR). He suggests batteries-included platforms, services that address the user's LLM through CLIs, curl and Markdown docs, simpler stacks, and asks whether an app like MenuGen could be just a prompt (§intro ¶Going forward). He concludes vibe coding full web apps is messy today and not for anything important, but shows clear hints of greatness (§intro ¶For now).

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
- [[building-for-agents]]
- [[llm-gui]]
- [[vibe-coding-over-time]]
```

## Candidates

### topic: vibe-coding (existing)
- existing: yes. The page already describes MenuGen from the YC talk (@31:38, @32:13, @32:47). This post is the fuller, written account; add it to `sources` and give MenuGen a short paragraph cited to the blog, keeping the talk sentences as they are.
- statements:
  - He wanted an app that shows pictures of the dishes on a menu and built it at a recent vibe coding hackathon (§intro ¶1).
  - You photograph a menu and it generates images for all the items; he notes they are not what that restaurant will serve but give the basic idea (§intro ¶2).
  - The first version worked on localhost at the hackathon; afterwards he kept vibe coding to deploy it and add authentication and payments (§intro ¶2).
  - He calls it his first end-to-end vibe coded app, built as someone who tinkers but has little to no web development experience, into a product people can sign up for and pay for, with a 10% markup (§intro ¶3).
  - He wrote no code directly; Cursor and Claude wrote all of it, and he says he does not really know how MenuGen works in the conventional sense (§intro ¶3).
  - With Cursor and Claude 3.7 the React frontend appeared very quickly; he felt 80% done but says it was closer to 20% (§intro ¶Local version).
  - Claude repeatedly hallucinated deprecated APIs, model names and conventions for OpenAI, Replicate and Clerk, which he worked around by pasting documentation back and forth (§intro ¶OpenAI API, ¶Replicate API, ¶Clerk).
  - He caught Claude matching Stripe payments to users by email, which could leave a buyer without credits; Claude rewrote it with user ids, and its promise to do better next time he calls gaslighting (§intro ¶Stripe).
  - He summarises that LLMs have slightly outdated knowledge of everything, make subtle but critical design mistakes when watched closely, and sometimes hallucinate or gaslight (§intro ¶TLDR).
  - He leaves a database and work queue as future work: more services, logins, keys and docs (§intro ¶Database).
  - He hopes to see the barrier to building an app drop to about zero, so anyone can publish one as easily as a TikTok (§intro ¶For now).
- **Note:** the "watch them closely" lesson is consistent with [[ai-assisted-coding-loop]] (keep the AI on the leash, youtube-2025-06-19-software-is-changing @22:43), but here he is vibe coding, not running that loop; link only with a **Note:**.

### claim: deploying-a-vibe-coded-app-is-harder-than-writing-it
- existing: no claim page; the idea is present as topic sentences on [[vibe-coding]] and [[vibe-coding-over-time]] cited to the YC talk (@32:13, @32:47).
- title: "Vibe coding MenuGen's code was the easy part; making it a real, deployed app was the slog"
- stated_on: 2025-04-27 · confidence: stated
- sources: [[blog-2025-04-27-vibe-coding-menugen]], [[x-2025-05-01-vibe-coding-hackathon]], [[youtube-2025-06-19-software-is-changing]] (@32:13, @32:47)
- topic: [[vibe-coding]]
- quote: "a bit of a painful slog as a deployed, real app" (§intro ¶TLDR)
- statements:
  - It was a fun escapade as a local demo and a painful slog as a deployed app (§intro ¶TLDR).
  - Building a modern app is like assembling IKEA furniture (written "IKEA future"): services, docs, API keys, configurations, dev/prod deployments, rate limits, pricing tiers (§intro ¶TLDR).
  - What interested him most was that he spent little time in the code editor and most of it in the browser, moving between tabs and settings (§intro ¶TLDR).
  - That work and state is not accessible to an LLM, which he sets against automating society by 2027 (§intro ¶TLDR).
  - The concrete obstacles: OpenAI and Replicate keys and rate limits (§intro ¶OpenAI API, ¶Replicate API); a Vercel build that failed only remotely and env keys that had to be set by hand in Vercel settings, an hour lost (§intro ¶Vercel deploy); Clerk's production mode needing a custom domain, DNS and a Google OAuth setup across three dashboards, where he thought of quitting (§intro ¶Clerk); Stripe snippets in JavaScript for a TypeScript app and two rounds of products, prices and keys (§intro ¶Stripe).
  - He says the infrastructure was designed for teams of professional web developers in a pre-LLM world, not solo vibe coders (§intro ¶Going forward).
- relation to existing claims:
  - YC talk (published 2025-06-19) states the same lesson: the code was the easy part, making it real took another week (@32:13, @32:47). Same position, so the talk is a second source. Do not write "first said in the blog"; give both dates.
  - [[vibe-coding-is-for-throwaway-weekend-projects]]: **extends**. The February post judged vibe coding acceptable for throwaway weekend projects (x-2025-02-02-vibe-coding); this post takes it past the weekend demo to a deployed, paid product and finds the new difficulty is outside the code. Both can hold. (If merge wants the weakest link, "supports" is defensible too: the local demo fits the weekend-project use, the real app is where it gets hard.) I recommend `extends`, which needs a timeline entry (it has one).
  - [[vibe-coding-will-terraform-software]]: none. Different subject (job and software change versus deployment pain).

### claim: vibe-coding-full-web-apps-is-not-yet-for-anything-important
- existing: no
- title: "In April 2025 he judged vibe coding full web apps messy and not a good idea for anything important"
- stated_on: 2025-04-27 · confidence: stated
- sources: [[blog-2025-04-27-vibe-coding-menugen]]
- topic: [[vibe-coding]]
- quote: "not a good idea for anything of actual importance" (§intro ¶For now)
- statements:
  - Vibe coding full web apps today is kind of messy and not a good idea for anything of actual importance (§intro ¶For now).
  - In the same breath he sees clear hints of greatness and thinks the industry needs time to adapt to LLMs (§intro ¶For now).
  - He is left with an equal mix of amazement, since it is possible and much faster than before, and frustration (§intro ¶Going forward).
- relation to existing claims:
  - [[vibe-coding-is-for-throwaway-weekend-projects]]: **supports**. Both limit vibe coding to low-stakes work: February says fine for throwaway weekend projects (x-2025-02-02-vibe-coding), April says not for anything of actual importance (§intro ¶For now).
  - [[vibe-coding-will-terraform-software]] (2025-12-19): none, not contradicts. December adds professional uses and says it "will" reshape software (blog-2025-12-19-year-in-review-2025 §5); April is explicitly "today" and already expects the industry to adapt. Both can be true. A **Note:** on the timeline can place them side by side without asserting a change of mind.
  - Merge may fold this into the previous claim as one page; they are different statements (where the difficulty is versus what it is fit for), so I keep two.

### topic: building-for-agents (existing)
- existing: yes. Its YC sentences (llms.txt, markdown docs, curl instead of "click") are the same idea; this post states it as concrete suggestions.
- statements:
  - Everything a service tells the user will be pasted into an LLM, so services might as well talk to the LLM directly (§intro ¶Going forward).
  - His suggestions: a CLI tool, a backend configurable with curl commands, docs in Markdown; do not ask a developer to visit, look or click, but instruct and empower their LLM (§intro ¶Going forward).
  - He also wants an opinionated, batteries-included platform with domain, hosting, auth, payments, database and server functions preconfigured, "the opposite of Vercel Marketplace" (§intro ¶Going forward).
  - For his next app he is considering plain HTML/CSS/JS with a Python backend instead of serverless "modern web development" (§intro ¶Going forward).
- relation: topic, no claim link. The existing page's line "MenuGen's DevOps pain is where this argument starts" (Related) can now cite the blog as well as the talk.

### topic: llm-gui (existing)
- statement: he asks whether MenuGen could be just a prompt, with the LLM responding not with text but a simple webpage, along the lines of Artifacts, and whether many apps could look like that (§intro ¶Going forward).
- These are questions, not claims; paraphrase as "he asks whether". Could also sit on [[software-3-0]] (an app as a prompt, compared with a custom GPT). Pick one; I suggest llm-gui for the webpage-instead-of-text point and leave software-3-0 alone.

### timeline: vibe-coding-over-time (existing)
- entry: **2025-04-27** — Vibe codes MenuGen end to end; the local demo is quick, deployment is the slog, and full web apps are not yet for anything important → [[deploying-a-vibe-coded-app-is-harder-than-writing-it]], [[vibe-coding-full-web-apps-is-not-yet-for-anything-important]] ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶TLDR, ¶For now)
- The existing 2025-06-19 entry (talk: "builds MenuGen and finds DevOps, not code, is the hard part") should stay, but reword so it does not read as the first MenuGen account: e.g. "Retells MenuGen in the YC talk; the code was the easy part" with both sources available. No interval wording.

## Quotes
- "I felt like I was 80% done" (§intro ¶Local version)
- "Seeing a new website materialize so quickly is a strong hook." (§intro ¶Local version)
- "100% of the code was written by Cursor+Claude" (§intro ¶3)
- "I thought of quitting the project around here" (§intro ¶Clerk)
- "which I know is just gaslighting" (§intro ¶Stripe)
- "a bit of a painful slog as a deployed, real app" (§intro ¶TLDR)
- "Building a modern app is a bit like assembling IKEA future." (§intro ¶TLDR)
- "I didn't even spend all that much work in the code editor itself." (§intro ¶TLDR)
- "I spent most of it in the browser, moving between tabs and settings" (§intro ¶TLDR)
- "how are we supposed to be automating society by 2027 like this?" (§intro ¶TLDR)
- "Not vibe coding solo devs prototyping apps." (§intro ¶Going forward)
- "Don't talk to a developer." (§intro ¶Going forward)
- "Instruct and empower their LLM." (§intro ¶Going forward)
- "Could MenuGen be just a prompt?" (§intro ¶Going forward)
- "not a good idea for anything of actual importance" (§intro ¶For now)
- "there are clear hints of greatness" (§intro ¶For now)

## Notes for merge
- "IKEA future" is his typo for "IKEA furniture"; quote as written, paraphrase as furniture.
- **Money:** here he says he pockets a 10% markup and it "could earn some $" passively (§intro ¶3, ¶For now). In the YC talk (published 2025-06-19) he calls it a negative-revenue app on which he has lost a huge amount of money (@32:13). These are statements about the app's finances at two dates, not positions; do not build a claim or a "change" from them, and do not write an interval.
- **Duration:** the blog gives no total time; "took another week" is from the talk (@32:47). Do not attribute the week to the blog. The blog's specific times are "1 hour later" (Vercel env keys) and waking up "the next morning" (Clerk).
- The model is "Claude 3.7" in Cursor here (§intro ¶Local version); the companion X post says "Cursor+Claude/o3". Keep each source's wording.
- He was "told later" that rate limits are anti-fraud measures and "told" Replicate is moving to pre-purchased credits; these are reports, not his findings.
- "Vercel KV, which I know is actually deprecated" is his statement; keep it attributed.
- "the @levelsio dream" refers to another person's model of passive app income; mention not needed.
- The hackathon is not named. The post ends linking the companion X post (raw `x/1917961248031080455`, digested separately as `x-2025-05-01-vibe-coding-hackathon`); link the two source pages.
- No order assertions between this post, the X post and the YC talk beyond their dates.
