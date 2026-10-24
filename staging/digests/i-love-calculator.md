# Digest: I love calculator
- raw: raw/blog/i-love-calculator.md · published: 2024-09-08 · medium: blog · words: 773
- source slug: blog-2024-09-08-i-love-calculator

## Source page
```
---
type: source
raw_path: raw/blog/i-love-calculator.md
published: 2024-09-08
medium: blog
summary: A short essay holding up the pocket calculator, self-contained and owned outright, as an ideal against technology drifting toward accounts, data harvesting and dependency bloat.
url: https://karpathy.bearblog.dev/i-love-calculator/
title: I love calculator
---
# I love calculator
Raw: [[raw/blog/i-love-calculator]] · Original: https://karpathy.bearblog.dev/i-love-calculator/

The post has no headings, so all citations are `§intro`.

## Summary
Browsing a book on the history of the pocket calculator, he realises he loves the calculator, not as a device to buy today but as a product of technology and a symbol of a philosophy (§intro). He describes it as a plugin for the brain that extends its arithmetic, with an almost zero "dependency footprint": it needs only light or commodity batteries, is bought in one exchange and is then yours, and would work if carried thousands of years back in time (§intro). He contrasts it with modern technology through a long list of what it does not do: no internet setup, no accounts or logins, no location or bluetooth requests, no subscriptions or upsells, no usage tracking, no data harvesting or breaches, no breaking when servers go down; its computation stays private on the device (§intro). His example of the opposite is a CO2 monitor that demanded an account, an app and precise location before it would report his room's CO2 (§intro). He asks whether this drift is companies hyperoptimizing shareholder value under regulation, and says consumers and developers should remember what technology could be: like the calculator, at least as a platonic ideal to approach along various dimensions (§intro). He closes with links to related work he found enjoyable and influential (§intro).

## Key points
- The calculator as a self-contained, owned, private tool, set against user-hostile, dependency-bloated technology → [[user-hostile-technology]]
- Technology could be like the calculator, as an ideal to approach → [[technology-could-be-like-the-calculator]]
- Bought once and then his, with no other master → [[he-prefers-to-pay-and-be-the-customer]]

## Fed pages
- [[user-hostile-technology]]
- [[technology-could-be-like-the-calculator]]
- [[he-prefers-to-pay-and-be-the-customer]]
```

## Candidates
### topic: user-hostile-technology
- existing: no (checked `wiki/index/topics.md` and grep for privacy, dependency, subscription, calculator; `calculator` appears only on [[llm-tool-use]] as a tool an LLM calls, unrelated)
- aliases: [digital hygiene, digital privacy, privacy and security, internet of shit, dependency footprint, the calculator ideal]
- recurrence: yes, in his own words across two sources in this batch — the calculator post and `blog-2025-03-17-digital-hygiene` both use the CO2 monitor that demanded an account/app/precise location as the example, both link @internetofshit, and both prefer owning or paying for a product to being monetised (see digital-hygiene digest). Shared topic, two `sources`.
- statements (this source):
  - Struck by a book on the pocket calculator, he says he loves the calculator not as a device to buy today but as a product of technology and a symbol of a philosophy (§intro)
  - He calls it a plugin for your brain that extends its arithmetic and makes you smarter (§intro)
  - It has an almost zero "dependency footprint": it needs only light from its solar panel and/or commodity batteries, is bought in a single exchange, and is then yours (§intro)
  - He lists what it does not do: no internet setup, bluetooth or location requests, accounts or logins, frequent updates, subscription upsells, attempts to become a platform, card on file, usage tracking, review prompts, data harvesting or leaks, newsletters, ToS notifications, or breaking when servers go down (§intro)
  - Its computation is private, secure and confined to the device, with no record logged anywhere (§intro)
  - His counter-example: a CO2 monitor with thousands of positive reviews demanded an account, an app download and precise location before it would report the CO2 in his room (§intro)
  - He asks (as questions, not assertions) whether the drift toward complex, dependency-bloated, user-hostile technology comes from companies hyperoptimizing shareholder value under regulation, preferring renting to selling and monetising customer data, and whether governments are lagging (§intro)
  - As consumers we can fight the drift by eating into the shareholder-value term; as developers we can add "the regularizing gradient of ideology" to the optimization (§intro)
  - He lists related content he found enjoyable and influential: Internet of shit, "Technology without industry", TechJudge, and "Too much efficiency makes everything worse" (§intro)

### claim: technology-could-be-like-the-calculator
- existing: no
- title: "Technology could be like the calculator, as an ideal to approach"
- confidence: stated
- quote: "It could be like the calculator." (§intro)
- statements:
  - It is up to consumers and developers to remember what technology could be: like the calculator (§intro)
  - He hedges it: maybe not concretely for all products and services, but as a platonic ideal one can approach along various dimensions (§intro)
- relation to existing claims: none. (Not to be linked to [[neural-net-training-should-not-be-complicated]] or [[small-hackable-educational-code]]: those are about code simplicity; any link would be my reading, at most a **Note:**.)

### claim: he-prefers-to-pay-and-be-the-customer
- existing: no
- shared with `blog-2025-03-17-digital-hygiene`, which is the primary source (it states the position directly); this post supports it.
- title: "He prefers to pay for products and be the customer, not the product"
- confidence: stated (in digital hygiene); this post's contribution is implied
- statements (this source):
  - Of the calculator: you buy it in one exchange, then it is yours; "You paid for it and now it is yours." and "It has no other master." (§intro)
  - He asks why companies would sell a product when they can rent it and monetise customer data (§intro, posed as a question)
- relation to existing claims: none in the wiki. Within this batch, this source `supports` the digital-hygiene statement; it is one claim page with two sources, not two pages.

No method candidate: the post describes no procedure.

## Quotes
- "I... love... calculator." (§intro)
- "It makes you smarter." (§intro)
- "The calculator is a fully self-contained arithmetic plugin for your brain." (§intro)
- "You paid for it and now it is yours." (§intro)
- "It has no other master." (§intro)
- "It just does the thing." (§intro)
- "It won't break when the servers go down." (§intro)
- "It could be like the calculator." (§intro)
- "the regularizing gradient of ideology" (§intro)

## Notes for merge
- Locations: no headings; everything is `§intro`.
- Two lines in the raw are image captions (the CO2 monitor sentence and "Toy mathematical model of a company…"); the images are not in the raw. The CO2 monitor sentence is still his text and can be cited.
- His shareholder-value explanation is posed entirely as questions ("Are these symptoms…?"); do not write it as his assertion.
- The four linked works are other people's; he only says he found them enjoyable and influential. Do not attribute their arguments to him.
- **Checked the suggested link to [[calorie]]:** the calorie README (`raw/github/karpathy__calorie.md`) says nothing about accounts, networking, privacy or dependencies; it is one `index.html` you open in a browser. A connection to "simple, local, non-networked technology" would be my reading, not his. At most a labelled **Note:** on [[user-hostile-technology]] or [[calorie]]; it is not a recurrence and does not justify the topic.
- The real recurrence is with digital hygiene (same CO2 monitor anecdote, same @internetofshit link, same pay-to-own preference). Do not write order between the two posts ("he returned to"); give dates.
- "dependency footprint" here is about a product's reliance on the technosphere, not code dependencies; do not merge it into [[small-hackable-educational-code]]'s "one dependency" step.
