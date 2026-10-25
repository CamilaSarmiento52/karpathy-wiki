# Verification: batch 4, group E4 (llm-wiki gist, Sequoia Ascent talk, Sequoia blog summary, micrograd README)
Verified 2026-10-25 by a fresh reader. Sources: [[github-2026-04-04-llm-wiki-gist]], [[talk-2026-04-29-sequoia-ascent-2026]], [[blog-2026-04-30-sequoia-ascent-2026-summary]], [[github-2026-08-03-micrograd-readme]]

## Coverage
- pages checked: 34. Sources (4): the four above. Claims (16): a-wiki-compounds-where-rag-rediscovers, an-index-file-avoids-rag-at-moderate-scale, llms-make-wiki-maintenance-nearly-free, agentic-engineering-keeps-the-quality-bar-while-going-faster, in-software-3-0-some-apps-should-not-exist, neural-nets-may-become-the-host-process, hiring-should-test-building-a-big-project-with-agents, understanding-cannot-be-outsourced, no-rag-needed-for-a-small-wiki, vibe-coding-is-for-throwaway-weekend-projects, llms-are-the-kernel-of-an-emerging-operating-system, use-llms-as-tools-and-check-their-work, he-now-delegates-most-coding-to-agents, english-is-the-new-programming-language, software-2-0-automates-what-you-can-verify, microgpt-is-the-full-algorithm-everything-else-is-efficiency. Timelines (2): vibe-coding-over-time, llm-os-over-time. Topics (8): agentic-engineering, vibe-coding, software-3-0, llms-as-operating-systems, jagged-intelligence, llm-knowledge-bases, building-for-agents, backpropagation. Methods (2): llm-wiki-workflow, verify-gradients-against-pytorch. Artifacts (2): microgpt, micrograd.
- claim pages fully checked: 16. The eight E4 claims were checked in full. For the eight older claims I checked every sentence that cites an E4 source and every relation that involves one.
- timeline entries checked: 2 E4 entries (vibe-coding-over-time 2026-04-29, llm-os-over-time 2026-04-29) plus the 3 closing Notes that touch them. I also read the other entries on both pages for ordering.
- other sentences checked: about 75 of about 80 that cite E4 sources (nearly all of them).
- Fed pages: each source page's `## Fed pages` matches exactly the pages that cite it.
- Relations: each `extends` and `supports` link is set on both pages (agentic ↔ vibe-coding-is-for-throwaway; neural-nets ↔ kernel; index-file ↔ no-rag).

## Findings
### F1 — overstated — [[in-software-3-0-some-apps-should-not-exist]]
- sentence: "He finds those new possibilities more exciting than the speed-ups ([[talk-2026-04-29-sequoia-ascent-2026]] @07:04, @07:35)."
- cited: [[talk-2026-04-29-sequoia-ascent-2026]] @07:04–@07:35
- raw says: he hedges it: "And I almost think that that's / more exciting."
- fix: "He almost thinks those new possibilities are more exciting than the speed-ups ([[talk-2026-04-29-sequoia-ascent-2026]] @07:04, @07:35)."

### F2 — overstated — [[jagged-intelligence]]
- sentence: "His conclusion is to treat the models as tools and stay in the loop; see [[use-llms-as-tools-and-check-their-work]] ([[talk-2026-04-29-sequoia-ascent-2026]] @12:00)."
- cited: @12:00
- raw says: he gives two possible readings of continued jaggedness: first, "maybe something slightly off"; second, you need to be in the loop and treat the models as tools. It is not a single conclusion. The claim page use-llms-as-tools-and-check-their-work states this correctly.
- fix: "To whatever extent models remain jagged, he says, either something is slightly off or you need to treat them as tools and stay in the loop; see [[use-llms-as-tools-and-check-their-work]] ([[talk-2026-04-29-sequoia-ascent-2026]] @11:24, @12:00)."

### F3 — mis-cited — [[understanding-cannot-be-outsourced]]
- sentence: "**Note:** [[agentic-engineering-keeps-the-quality-bar-while-going-faster]] puts the human in charge of taste, spec and oversight; here the limit is understanding ([[talk-2026-04-29-sequoia-ascent-2026]] @21:51, @28:27)."
- cited: the claim page agentic-engineering-keeps-the-quality-bar…; talk @21:51
- raw says: the talk does say this, at @19:38 and @21:51. But the linked claim page says nothing about taste or spec; that material is on the topic page [[agentic-engineering]] under "What the human still owns".
- fix: "**Note:** on [[agentic-engineering]] he puts the human in charge of taste, spec and oversight ([[talk-2026-04-29-sequoia-ascent-2026]] @19:38, @21:51); here the limit is understanding ([[talk-2026-04-29-sequoia-ascent-2026]] @28:27). No relation is set."

### F4 — minor — [[microgpt]]
- sentence: "…he kept prompting an LLM to simplify more and "The models hate this. They can't do it.", which felt like being outside the RL circuits…"
- cited: [[talk-2026-04-29-sequoia-ascent-2026]] @22:58
- raw says: the quote is verbatim, but it is two sentences. CLAUDE.md invariant 7 allows at most one sentence per quote.
- fix: "…he kept prompting an LLM to simplify more; "The models hate this.", and they could not do it, which felt like being outside the RL circuits…"

### F5 — minor — [[building-for-agents]]
- sentence: "He used Codex 5.5, read the output and says it reads ok without glaring mistakes; …"
- cited: [[blog-2026-04-30-sequoia-ascent-2026-summary]] §intro
- raw says: "it reads ok without glaring mistakes". These are his exact words, written here without quotation marks (invariant 7). The source page does quote them.
- fix: "He used Codex 5.5, read the output and says "it reads ok without glaring mistakes"; …"

### F6 — minor — [[agentic-engineering-keeps-the-quality-bar-while-going-faster]], [[vibe-coding-over-time]]
- sentences: (claim, Related claims) "on 2026-04-29 he keeps vibe coding as floor-raising and adds a named professional counterpart…"; (timeline, last Note) "the 2026-04-29 entry keeps vibe coding's floor-raising role and adds a named professional discipline beside it…"
- cited: [[talk-2026-04-29-sequoia-ascent-2026]] @15:49; [[x-2025-02-02-vibe-coding]]
- raw says: "raising the floor" first appears in the 2026-04-29 talk. The 2025-02-02 post says throwaway weekend projects. "Keeps" suggests he used the floor-raising framing earlier, which the cited sources do not show.
- fix: claim: "on 2026-04-29 he describes vibe coding as raising the floor for everyone and adds a named professional counterpart…"; timeline: "the 2026-04-29 entry describes vibe coding as raising the floor and adds a named professional discipline beside it…"

## Special checks (all passed)
- **Sequoia blog, AI-written parts:** grepped the wiki for `blog-2026-04-30-sequoia-ascent-2026-summary`. Outside its own source page it is cited only on [[building-for-agents]] (three §intro sentences, all from the ~130-word intro), plus index, hot and log entries. I grepped the wiki for phrases that occur only in the AI-written text ("orchestrator of agents", "raises the ceiling", "model's rails", "startup wedge", "empirical familiarity", "less precise", "fine for prototypes", "serious teams", "a line I keep returning to", "do not fully excel", "may tell you to walk", "stop existing as apps", "Konstantine", "December 2025" next to talk citations). None is cited as his. I spot-checked 16 items in the source page's "What the AI-written parts add or soften" list against the blog; all are accurate, including §4's RAG contrast, §12's single-file microGPT, the absence of neural computers and the car wash from the summary, "Opus 4.7" replaced by "a state-of-the-art model", and Claude Code in place of "Alpha code".
- **Host attribution:** the host first says "agentic engineering" in her @15:17–@15:49 turn. The topic, the claim, the vibe-coding topic, the talk source page and the index all say he adopted and defined the term. No page says he coined it. "Everything is automatable. Amazing." is not quoted as his.
- **extends pairs:** agentic-engineering ↔ vibe-coding-is-for-throwaway was checked against @15:49/@16:22 and the 2025-02-02 post; it holds (adds, denies nothing). neural-nets ↔ kernel was checked against @08:07–@09:13 and intro-to-llms @42:06/@42:38; it holds and is marked hedged on both pages, the timeline and the topic. The YC "like the CPU" Note (@10:01) is correct. The terraform Note (year in review §5) is correct.
- **llm-wiki gist:** the source page correctly separates the gist's content from this repo's conventions. CLAUDE.md is identified as the gist's example schema name and the 2026-04-02 log line as illustrative. I found no repo design (claim or timeline pages, hot, manifest, quote rules) attributed to him. Every item in the "What it adds to the 2026-04-02 post" list checks against both texts.

## Checked and correct
- [[github-2026-04-04-llm-wiki-gist]]: header, Summary, What it adds, Key points: all supported
- [[talk-2026-04-29-sequoia-ascent-2026]]: host-turn list, caption-error list, Summary (5 sentences), Key points: all supported
- [[blog-2026-04-30-sequoia-ascent-2026-summary]]: header, §intro Summary (4 sentences, quote verbatim), AI-parts list (16 items spot-checked): all supported
- [[github-2026-08-03-micrograd-readme]]: header, Summary, Key points: all supported
- [[a-wiki-compounds-where-rag-rediscovers]], [[an-index-file-avoids-rag-at-moderate-scale]], [[llms-make-wiki-maintenance-nearly-free]]: titles, quotes (verbatim, §-correct), Context, Related claims, confidence: all supported
- [[agentic-engineering-keeps-the-quality-bar-while-going-faster]]: all supported apart from F6
- [[neural-nets-may-become-the-host-process]], [[hiring-should-test-building-a-big-project-with-agents]]: all supported
- [[in-software-3-0-some-apps-should-not-exist]]: all supported apart from F1
- [[understanding-cannot-be-outsourced]]: all supported apart from F3; quote verbatim @28:59, tweet attribution correct
- [[no-rag-needed-for-a-small-wiki]], [[vibe-coding-is-for-throwaway-weekend-projects]], [[llms-are-the-kernel-of-an-emerging-operating-system]], [[use-llms-as-tools-and-check-their-work]], [[he-now-delegates-most-coding-to-agents]], [[english-is-the-new-programming-language]], [[software-2-0-automates-what-you-can-verify]], [[microgpt-is-the-full-algorithm-everything-else-is-efficiency]]: E4 sentences and relations all supported
- [[vibe-coding-over-time]], [[llm-os-over-time]]: 2026-04-29 entries and closing Notes supported (F6 is the one wording issue)
- [[agentic-engineering]]: 22 sentences, all supported; definition and YC Note correct
- [[vibe-coding]], [[software-3-0]], [[llms-as-operating-systems]], [[llm-knowledge-bases]], [[backpropagation]]: E4 sentences all supported
- [[jagged-intelligence]]: 9 sentences; all supported apart from F2
- [[building-for-agents]]: 12 sentences; all supported apart from F5
- [[llm-wiki-workflow]], [[verify-gradients-against-pytorch]], [[micrograd]]: E4 sentences all supported
- [[microgpt]]: E4 sentences supported apart from F4
