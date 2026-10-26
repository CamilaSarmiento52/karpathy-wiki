# Digest: Power to the people: How LLMs flip the script on technology diffusion
- raw: raw/blog/power-to-the-people.md · published: 2025-04-07 · medium: blog · words: 918 (frontmatter); 949 by wc
- source slug: blog-2025-04-07-power-to-the-people

Location scheme: the post has no headings, so every location is `§intro`; `¶N` is the
paragraph number (¶1 top-down diffusion … ¶6 sci-fi and Gibson; the trailing X-comments
line is not counted). Merge may drop the `¶N` and keep `§intro`.

## Source page
```
---
type: source
raw_path: raw/blog/power-to-the-people.md
published: 2025-04-07
medium: blog
summary: "His essay arguing that LLMs reverse the usual top-down diffusion of technology: so far they have helped individuals far more than corporations and governments."
url: https://karpathy.bearblog.dev/power-to-the-people/
title: "Power to the people: How LLMs flip the script on technology diffusion"
---
# Power to the people: How LLMs flip the script on technology diffusion
Raw: [[raw/blog/power-to-the-people]] · Original: https://karpathy.bearblog.dev/power-to-the-people/

## Summary
He says transformative technologies such as electricity, computers, the internet and GPS usually start with governments or the military, pass through corporations and only then reach individuals, and that LLMs reverse this (§intro ¶1, ¶2). ChatGPT gives regular people a large multiplier across many capabilities at a very low barrier, cheap or free and in their own language (§intro ¶2). He gives three reasons the gain is smaller in organisations: LLMs offer quasi-expert but shallow and fallible skill across many domains, which mostly makes an organisation's existing experts a bit better while letting an individual do things they could not do before; organisations face far more complexity, constraints and risk; and large organisations carry inertia (§intro ¶3, ¶4). Whether this lasts depends on how much better performance money can buy: today it cannot buy better ChatGPT, but train-time scaling, test-time scaling and ensembles push the other way while distillation pulls back (§intro ¶5). He closes that, at least for now, the future is "shockingly distributed", and that he loves it (§intro ¶6).

## Key points
- LLMs reverse the usual government → corporation → individual diffusion path → [[technology-diffusion]], [[llms-reverse-the-usual-diffusion-of-technology]]
- Why organisations benefit less: shallow quasi-expertise, complexity, inertia → [[technology-diffusion]]
- Versatile but shallow and fallible capability profile → [[jagged-intelligence]]
- Individuals can now vibe code apps; organisations cannot "just vibe code" → [[vibe-coding]], [[vibe-coding-over-time]]
- Money cannot (yet) buy better ChatGPT; forces that widen or narrow the gap → [[money-cannot-buy-better-chatgpt]]
- The YC talk's one-paragraph version of the flip → [[llms-as-operating-systems]]

## Fed pages
- [[technology-diffusion]]
- [[llms-reverse-the-usual-diffusion-of-technology]]
- [[money-cannot-buy-better-chatgpt]]
- [[jagged-intelligence]]
- [[vibe-coding]]
- [[vibe-coding-over-time]]
- [[llms-as-operating-systems]]
```

## Candidates

### topic: technology-diffusion
- existing: no page. The idea exists as one sentence on [[llms-as-operating-systems]] ("they flip technology diffusion", cited to the YC talk @12:45, @13:18). That page is about the OS analogy, so the essay does not fit there; I propose a new topic and a link from llms-as-operating-systems to it. If merge prefers coarse folding, the fallback is a bold-lead section on llms-as-operating-systems, but the essay's three-reason argument and the "dynamic range" section would overload that page.
- aliases: [Technology diffusion, Power to the people, LLMs flip technology diffusion, benefit distribution]
- sources: [[blog-2025-04-07-power-to-the-people]], [[youtube-2025-06-19-software-is-changing]] (@12:45, @13:18, @13:50); first_seen 2025-04-07, last_updated 2025-06-19
- related: [[llms-as-operating-systems]], [[ai-ecosystem]], [[jagged-intelligence]], [[vibe-coding]]
- statements:
  - Transformative technologies usually diffuse top-down, from government or military use through corporations to individuals; his examples are electricity, cryptography, computers, flight, the internet and GPS (§intro ¶1).
  - He gives the usual reason as new technologies being scarce, capital-intensive and needing specialised expertise early on (§intro ¶1).
  - He finds it unique that LLMs reverse this, benefiting regular people disproportionately while their impact on corporations and governments is more muted and lagging (§intro ¶2).
  - He cites ChatGPT as the fastest-growing consumer application in history, with 400 million weekly active users, used for writing, coding, translation, tutoring, summarisation, deep research and brainstorming (§intro ¶2).
  - He calls it a major multiplier to an individual's power, with a very low barrier: cheap or free, fast, available on demand behind a URL or on a local machine, and in anyone's native language (§intro ¶2).
  - Reason one: LLMs give quasi-expert performance across many domains at once, versatile but shallow and fallible; an organisation already concentrates diverse experts, so it gets a bit better at what it could already do, while an individual, usually expert in at most one thing, can do things they could not before (§intro ¶3).
  - His individual examples: vibe coding apps, approaching legal documents, grokking research papers, data analytics, generating marketing content, all at an adequate level without another expert (§intro ¶3).
  - Reason two: organisations face greater complexity and coordination (integrations, legacy systems, security, privacy, compliance, legal risk), which is hard to fit into a context window, with a lower margin for error (§intro ¶4).
  - Reason three: the inertia of large organisations, including culture, precedent, turf wars, communication overhead, retraining and bureaucracy (§intro ¶4).
  - He says he does not want to downplay LLMs' impact on organisations, but that for now and in aggregate they have changed individuals' lives significantly more (§intro ¶4).
  - Future diffusion depends on the "benefit distribution", which he ties to the dynamic range of performance as a function of capital spent (§intro ¶5). → also the claim money-cannot-buy-better-chatgpt
  - If money starts buying dramatically better models, he expects large organisations to buy more intelligence and an elite among individuals to split from the rest (§intro ¶5).
  - He says few science-fiction works predicted this progression; the AI revolution was supposed to be a secret government project, not ChatGPT on a phone in everyone's pocket (§intro ¶6).
  - YC talk version (published 2025-06-19): LLMs flip the direction of technology diffusion; governments and corporations are lagging consumers; his own use is like asking how to boil an egg; what is new is that LLMs are in the hands of all of us (@12:45, @13:18, @13:50).
- relation: **Note:** connects to [[ai-ecosystem]], where in March 2024 he worries about a few megacorps and calls AGI a magnifier of power (talk-2024-03-26-sequoia-making-ai-accessible @21:41); the essay's "elite may split away" scenario touches the same concern. My reading, so a **Note:** only.

### claim: llms-reverse-the-usual-diffusion-of-technology
- existing: no (the YC sentence on llms-as-operating-systems is not a claim page)
- title: "LLMs reverse the usual top-down diffusion of technology, so far benefiting individuals more than organisations"
- stated_on: 2025-04-07 · confidence: stated
- sources: [[blog-2025-04-07-power-to-the-people]], [[youtube-2025-06-19-software-is-changing]] (@12:45, @13:18)
- topic: [[technology-diffusion]]
- quote: "LLMs display a dramatic reversal of this pattern" (§intro ¶2)
- statements: as the topic's ¶2–¶4 statements; the hedge matters: "at least for the moment and in aggregate across society" (§intro ¶4), and "at least at this moment in time" (§intro ¶6). The title must keep "so far".
- relation to existing claims:
  - [[english-is-the-new-programming-language]]: weak **supports**. The essay says people without expertise can now vibe code apps (§intro ¶3); the claim page cites him saying everyone is now a programmer (youtube-2025-06-19-software-is-changing @28:49, @29:22). Both say LLMs let non-programmers build software. If merge finds this too loose, "none".
  - The YC talk repeats the flip (@12:45, @13:18); same position, so it is a second source, not a separate claim.
  - No contradiction anywhere.

### claim: money-cannot-buy-better-chatgpt
- existing: no
- title: "In April 2025 he said money could not buy better frontier LLM performance"
- stated_on: 2025-04-07 · confidence: stated
- topic: [[technology-diffusion]]
- quote: "Money can't buy better ChatGPT." (§intro ¶5)
- statements:
  - Today frontier-grade performance is very accessible and cheap, and beyond that a marginal dollar does not buy better performance, reliability or autonomy (§intro ¶5).
  - He illustrates with Bill Gates talking to GPT 4o just as you do (§intro ¶5).
  - He asks whether this can last: train-time scaling, test-time scaling and ensembles increase the dynamic range; distillation decreases it (§intro ¶5).
  - The moment money can buy a dramatically better model, he says, things change (§intro ¶5).
- relation to existing claims: none forced. [[scaling-offers-a-guaranteed-path-to-better-models]] (2023-11-23) is about scale improving models, not about who can buy them; the essay names train-time scaling as one force widening the range, consistent with it but not evidence for it. Say "none". Merge may fold this into the topic instead of a page; I keep it as a claim because it is dated, hedged ("Today") and could be revisited later (invariant 6).

### topic: jagged-intelligence (existing)
- statement to add: in April 2025 he describes LLM capability as quasi-expert across a very wide range of domains, versatile but shallow and fallible (§intro ¶3).
- **Note:** this is close to, but not the same words as, "jagged"; he does not use "jagged" or "people spirits" here. Add as a sentence with that caveat, or as `context` if merge thinks the fit is loose.

### topic: vibe-coding (existing) and timeline: vibe-coding-over-time (existing)
- statements:
  - He lists "vibe code apps" among things individuals can now do without an extra expert (§intro ¶3).
  - In organisations, with their complexity and low margin for error, "you can't just vibe code something" (§intro ¶4).
- timeline entry: **2025-04-07** — Says individuals can now vibe code apps but organisations cannot just vibe code, given their complexity ([[blog-2025-04-07-power-to-the-people]] §intro ¶3, ¶4).
- relation: **supports** [[vibe-coding-is-for-throwaway-weekend-projects]] in spirit: low-stakes individual use is fine, high-stakes organisational use is not; neither extends nor contradicts it. Weakest link: supports, or none if merge wants only explicit claims linked.

### topic: llms-as-operating-systems (existing)
- add a link: its "flip technology diffusion" sentence → "see [[technology-diffusion]]". The essay can be `context` there; it is not about the OS analogy.

## Quotes
- "LLMs display a dramatic reversal of this pattern" (§intro ¶2)
- "the average person has never experienced a technological unlock this dramatic, this fast." (§intro ¶2)
- "they are simultaneously versatile but also shallow and fallible." (§intro ¶3)
- "People can now vibe code apps." (§intro ¶3)
- "You can't just vibe code something." (§intro ¶4)
- "You might be one disastrous hallucination away from losing your job." (§intro ¶4)
- "Mary, Jim and Joes are experiencing the majority of the benefit" (§intro ¶4)
- "Money can't buy better ChatGPT." (§intro ¶5)
- "Bill Gates talks to GPT 4o just like you do." (§intro ¶5)
- "the moment money can buy dramatically better ChatGPT, things change." (§intro ¶5)
- "Surprise - the future is already here, and it is shockingly distributed." (§intro ¶6)
- "Personally, I love it." (§intro ¶6)

## Notes for merge
- The William Gibson line ("The future is already here, it's just not evenly distributed") is Gibson's, quoted by him; never quote it as his.
- "400 million weekly active users" and "fastest growing consumer application in history" are his figures at the time; attribute them, do not restate as fact.
- "Mary, Jim and Joes" is as written (not "Joe").
- "GPT-8-pro-max-high" / "GPT-6 mini" are jokes about future tiers, not real models.
- Do not write an order between this essay and the YC talk ("first argued in"); give both dates. In the talk he says "I wrote about uh this one particular property" (@12:45, verbatim caption), his own reference to having written about it; it does not name this post, so do not assert the link beyond a **Note:**.
- The essay ends with a link to a community-comments X version (status 1909308143156240538); no raw file for it was checked here.
