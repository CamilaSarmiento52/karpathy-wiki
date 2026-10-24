# Verification: batch 3, group D3 (power to the people, MenuGen blog, hackathon X post, grocery post, minbpe Discussion 98, rendergit README)
Verified 2026-10-24 by a fresh reader. Sources: [[blog-2025-04-07-power-to-the-people]], [[blog-2025-04-27-vibe-coding-menugen]], [[x-2025-05-01-vibe-coding-hackathon]], [[x-2025-07-08-ideal-grocery-store]], [[github-2025-08-08-minbpe-gpt-4-tokenizer-discussion]], [[github-2025-08-21-rendergit-readme]]

## Coverage
- pages checked: 20. Six source pages; claims [[deploying-a-vibe-coded-app-is-harder-than-writing-it]], [[vibe-coding-full-web-apps-is-not-yet-for-anything-important]], [[vibe-coding-is-for-throwaway-weekend-projects]], [[llms-reverse-the-usual-diffusion-of-technology]]; timeline [[vibe-coding-over-time]]; topics [[technology-diffusion]], [[vibe-coding]], [[jagged-intelligence]], [[building-for-agents]], [[llm-gui]], [[tokenization]]; artifacts [[rendergit]], [[minbpe]], [[calorie]].
- claim pages fully checked: 4 (each quote grepped, every Context and Related sentence read against the raw, including the YC-talk sentences @12:45, @13:18, @28:49, @29:22, @31:38, @32:13, @32:47).
- timeline entries checked: 6 of 6 plus the closing Note. That includes the phase 1 entries 2025-02-02, 2025-06-19, 2025-12-19 and 2026-04-02, checked against raw x/1886192184808149383, LCEmiRjPEtQ @30:30/@32:13, year-in-review-2025 §5 and x/2039805659525644595 "Extra tools".
- other sentences checked: 52 of ~70 (every sentence citing these sources on technology-diffusion, the MenuGen and rendergit paragraphs of vibe-coding, building-for-agents, llm-gui, jagged-intelligence, tokenization, minbpe, calorie and rendergit, plus all source-page Summaries).

## Findings
### F1: overstated, [[deploying-a-vibe-coded-app-is-harder-than-writing-it]]
- sentence: "The obstacles he lists are outside the code: OpenAI and Replicate keys and heavy rate limits (...); a Vercel build that failed only remotely (...); ... and Stripe snippets in JavaScript for a TypeScript app (...)."
- cited: [[blog-2025-04-27-vibe-coding-menugen]] §intro ¶OpenAI API–¶Stripe
- raw says: several of the listed obstacles are in the code. The Vercel build failed on linting errors in the code. Claude "hallucinated about 1000 lines of code" of deprecated Clerk APIs. The Stripe snippets broke the TypeScript build. He also caught Claude's email-matching bug in the payment code. The TLDR says only that he did not spend "all that much work in the code editor"; it does not say there were no code problems.
- fix: "Most of the obstacles he lists are in services and their configuration rather than in the app's logic: ..." Keep the list as it is.

### F2: overstated, [[vibe-coding-full-web-apps-is-not-yet-for-anything-important]] and [[vibe-coding-is-for-throwaway-weekend-projects]] (the `supports` sentence on both pages)
- sentence (full-web-apps page): "Supports [[vibe-coding-is-for-throwaway-weekend-projects]]: both keep vibe coding to low-stakes work; February calls it not too bad for throwaway weekend projects (...)". The weekend page has the same wording: "...again keeping it to low-stakes work".
- cited: [[x-2025-02-02-vibe-coding]]; [[blog-2025-04-27-vibe-coding-menugen]] §intro ¶For now
- raw says: February says vibe coding is "not too bad for throwaway weekend projects". It sets no limit, and the weekend claim's own Context says the post "does not say weekend projects are the only valid use". April does set a limit: "not a good idea for anything of actual importance". The `supports` link itself holds, because April's limit is consistent with February's low-stakes framing. Only the word "both keep" puts a restriction into February.
- fix (full-web-apps page): "Supports [[vibe-coding-is-for-throwaway-weekend-projects]]: February names throwaway weekend projects as where it is not too bad ([[x-2025-02-02-vibe-coding]]), and April, consistent with that, says full web apps are not yet for anything of actual importance (...)". On the weekend page, replace "again keeping it to low-stakes work" with "consistent with the low-stakes setting named here".

### F3: mis-cited, [[vibe-coding-is-for-throwaway-weekend-projects]]
- sentence: "Extended by [[deploying-a-vibe-coded-app-is-harder-than-writing-it]]: in the MenuGen post (2025-04-27) he takes a vibe coded app past the local demo to a deployed, paid product and finds the hard part is outside the code, a painful slog of services and settings ([[blog-2025-04-27-vibe-coding-menugen]] §intro ¶TLDR)."
- cited: §intro ¶TLDR only
- raw says: "paid product" (people can sign up for and pay for it) is in ¶3, not the TLDR.
- fix: cite "§intro ¶3, ¶TLDR". The deploying page already does.

### F4: overstated, [[technology-diffusion]]
- sentence: "If money starts buying dramatically better models, he expects large organisations to buy more intelligence and an elite among individuals to split away from the rest"
- cited: [[blog-2025-04-07-power-to-the-people]] §intro ¶5
- raw says: large organisations "get to" buy more intelligence. The elite "may once again split away". That is a possibility, not an expectation.
- fix: "...he says large organisations would get to buy more intelligence, and an elite among individuals may split away from the rest (...)."

### F5: minor, [[rendergit]] (status and language)
- sentence: "`status: active` because he says he keeps using it and nothing marks it deprecated, despite the maintenance disclaimer; `language: Python` is inferred from the pip and uv install and Pygments, since the README does not name the language (...)."
- cited: [[github-2025-08-21-rendergit-readme]] §Basic usage, §Contributing
- raw says: the README states neither one. It says nothing about status, and it never names Python (only uv, `pip install -e .` and Pygments). It also says "I don't super intend to maintain or support it". The page is honest that both are judgements, which is right. The problem is that this editorial reasoning sits as an unlabelled evidence bullet under `## What it demonstrates`.
- fix: begin the bullet with "**Note:**". `active` is defensible, because he still uses it and nothing marks it archived. `archived` would also be arguable, because he does not intend to maintain it. No value change is required.

### F6: minor, [[x-2025-07-08-ideal-grocery-store]]
- sentence: "minimally processed food only (his term is NOVA Group 1)"
- raw says: he writes "Minimally processed (NOVA Group 1)". NOVA is an existing classification he uses, not a term he coined, and "his term" can read as coinage.
- fix: "minimally processed food only (he specifies NOVA Group 1)".

### F7: minor, [[minbpe]]
- sentence: "The repo's Discussions hold his post of 2025-08-08 on training a GPT-4-style tokenizer with the Hugging Face Tokenizers library instead, ..."
- raw says: the post never mentions minbpe. "instead" implies an alternative to minbpe, which the same sentence then says the post does not set up.
- fix: delete "instead".

## Checked and correct
- **The `extends` link, deploying ↔ weekend-projects:** this is a real broadening, set on both pages. February describes vibe coding a "project or webapp" and judges it fine for throwaway weekend projects. MenuGen takes a hackathon local demo on to a deployed product people pay for (¶2, ¶3), and adds the new finding that the slog is in the services and the browser (¶TLDR). Neither denies the other. `supports` would also have been defensible, as the digest notes, but `extends` is not invented. The only problems with the wording are F1 and F3.
- **The `supports` link, full-web-apps → weekend-projects:** the link is real and set on both pages. Only the wording is off (F2). The Note saying it does not contradict vibe-coding-will-terraform-software is accurate: April is explicitly "today", and December's §5 says it "will terraform software".
- [[vibe-coding-over-time]]: all 6 entries and the closing Note are supported. 2025-02-02 matches the raw tweet. 2025-04-27 cites ¶TLDR and ¶For now. 2025-05-01 matches #1. 2025-06-19 matches @30:30 ("gateway drug") and @32:13; "retells" is safe because the talk was given after April. 2025-12-19 matches §5 ("empowers trained professionals", "terraform software and alter job descriptions"). 2026-04-02 matches "Extra tools" (vibe-coded search engine). No interval wording. The Note is labelled editorial.
- [[vibe-coding]]: the MenuGen figures sit with their own sources. The 10% markup is cited to the blog §intro ¶3. Negative revenue, the "huge amount of money" lost and the $5 free credits are cited to the YC talk @31:38/@32:13. The week is cited to the talk @32:47, not the blog. The reconciling Note is correct. The power-to-the-people quotes and the rendergit sentence are also correct: 9 sentences checked.
- [[deploying-a-vibe-coded-app-is-harder-than-writing-it]]: the quote is verbatim (¶TLDR). The title is no stronger than the blog plus the talk. "Not vibe coding solo devs prototyping apps." is verbatim (¶Going forward). The X post is treated as a second location, not as independent evidence. The YC sentences match @32:13/@32:47, and the "few hours" matches @32:47. All other sentences are correct.
- [[vibe-coding-full-web-apps-is-not-yet-for-anything-important]]: the quote is verbatim. "Not yet" in the title is fair given "today" and "needs a bit of time". The Context sentences are correct.
- [[llms-reverse-the-usual-diffusion-of-technology]]: the quote is verbatim (¶2). The "so far" hedge is kept. The YC sentences match @12:45/@13:18. The [[english-is-the-new-programming-language]] connection is correctly a Note with no link set; the other page has no back-link.
- [[technology-diffusion]] (new topic): 15 sentences checked; all correct apart from F4. The 400M figures are attributed to the post. The Gibson line is attributed to Gibson, and only "shockingly distributed" is quoted as his. "the average person has never experienced..." is verbatim. The talk Note does not assert that the talk names the post.
- [[jagged-intelligence]]: 3 sentences checked; the quote is verbatim, and the caveat about "jagged" not appearing in the essay is correct.
- [[building-for-agents]]: 5 sentences checked, all correct. The quotes are verbatim. The rendergit caveat (LLMs, not agents) is right. gitingest and DeepWiki are at @36:40.
- [[llm-gui]]: 2 sentences checked, correctly phrased as questions.
- [[tokenization]]: 5 sentences checked; every figure (32,768, one special token, 1B-character subset, ~10B tokens / ~30B chars / ~3 chars per token) matches the post and its code comments.
- [[calorie]]: the grocery-post Note is correct and labelled. Grep of wiki/sources/x-* and raw/x confirms the grocery post is currently the only X post on food. The calorie README raw has nothing on food quality. The post sits in `context`, not `sources`.
- [[rendergit]]: the other 6 sentences are supported, including the tagline, the two views, CXML (not expanded), the features list, the §Contributing disclaimer quote (verbatim) and the BSD0 licence.
- Source pages: all six Summaries are supported. The hackathon X Summary's "built a web app with auth, payments and deployment at a vibe coding hackathon" follows the X post's own wording. The blog says deployment came after the hackathon, but each source page keeps its own source's wording, which is fine.
