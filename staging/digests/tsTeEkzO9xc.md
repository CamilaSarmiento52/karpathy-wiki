# Digest: Andrej Karpathy's Keynote & Winner Pitches at UC Berkeley AI Hackathon 2024 Awards Ceremony
- raw: raw/talks/tsTeEkzO9xc.md · published: 2024-07-03 · medium: talk · words: 15423 total; about 4,100 in his keynote (blocks [03:27]–[21:39])
- source slug: talk-2024-07-03-berkeley-hackathon-keynote

## Source page
```
---
type: source
raw_path: raw/talks/tsTeEkzO9xc.md
published: 2024-07-03
medium: talk
summary: "His keynote at the UC Berkeley AI Hackathon 2024 closing ceremony: the LLM OS as a new computing paradigm, and his advice to builders: small projects snowball, put in 10,000 hours, publish projects."
url: https://www.youtube.com/watch?v=tsTeEkzO9xc
title: "Andrej Karpathy's Keynote & Winner Pitches at UC Berkeley AI Hackathon 2024 Awards Ceremony"
---
# Andrej Karpathy's Keynote & Winner Pitches at UC Berkeley AI Hackathon 2024 Awards Ceremony
Raw: [[raw/talks/tsTeEkzO9xc]] · Original: https://www.youtube.com/watch?v=tsTeEkzO9xc

The recording is a full awards ceremony. Only his keynote, from about @03:27 to @21:39, is his; the hosts, judges, sponsors and team pitches that fill the rest are not cited here.

## Summary
He opens by saying the scale of today's AI scene is not normal compared with the small academic field he entered about 15 years earlier (@04:14, @04:54). He sees the cause as a new computing paradigm, comparing it to the 1980s of computing: the LLM is like a CPU working on tokens, the context window like RAM, and he calls the whole an LLM OS (@06:10, @06:49). He imagines many digital entities working together in the digital space, with physical automation lagging because bits are easier than atoms, and tells the audience they have agency over what that future looks like (@08:04, @08:42, @10:30). The rest is advice from his own career: small projects can snowball into big ones, as his game-programming tutorials led to CS231n, Zero to Hero and LLM101n and a Reddit chatbot at OpenAI led to GPT-4o (@12:23, @13:01, @14:50, @15:27); success comes from repeated practice, about 10,000 hours (@16:04, @19:11); and building and publishing projects keeps the brain rewarded on the way there (@19:48, @20:24, @21:02). He closes with "keep hacking" (@21:39).

## Key points
- The LLM as the CPU of a new computer, with the context window as RAM; he calls it the LLM OS and compares the moment to the 1980s of computing → [[llms-as-operating-systems]]
- Many digital entities doing work in the digital space; physical automation will probably lag digital → [[physical-automation-will-lag-digital-automation]]
- Small, fragile projects can snowball into big ones: his teaching path and OpenAI's Reddit chatbot → [[small-projects-can-snowball]]
- Success comes largely from repeated practice; count hours toward 10,000, failures included → [[success-comes-from-repeated-practice]]
- Work on projects end to end and publish them → [[build-and-publish-projects]]
- LLM101n, the course he had just put on GitHub → [[llm101n]]
- His teaching projects in sequence, as he tells it → [[his-teaching-over-time]]

## Fed pages
- [[llms-as-operating-systems]]
- [[physical-automation-will-lag-digital-automation]]
- [[small-projects-can-snowball]]
- [[success-comes-from-repeated-practice]]
- [[build-and-publish-projects]]
- [[llm101n]]
- [[his-teaching-over-time]]
```

## Candidates

### topic: llms-as-operating-systems
- existing: yes (aliases: LLM OS, LLMs are operating systems)
- aliases to add: "LLM OS" already present; "lmos" is the caption's spelling (do not add as alias)
- statements:
  - He says the reason for the current AI boom is that the nature of computation is changing and a new computing paradigm is starting, which he calls very rare (@06:10).
  - He says it feels almost like the 1980s of computing again (@06:10).
  - In his analogy the LLM is like the CPU, working on tokens (little string pieces) instead of instructions over bytes; the context window of tokens stands in for RAM of bytes, and there are equivalents of disk and the rest (@06:10, @06:49).
  - He calls the LLM the orchestrator and names the whole an LLM OS, saying he has tweeted about it in more detail before (@06:49).
  - He sees it as a new computer people are learning to program: what it is good and bad at, how to put it into products, how to get the most out of it (@06:49).
  - He points to the GPT-4o demo as something you can talk to in audio that sees, hears and paints, and notes that in the film "Her" the AI is called an operating system (@06:49, @07:27).
- relation to existing pages: **supports / earlier instance.** This is the earliest dated source for the analogy; the topic's `first_seen` would move from 2025-06-19 to 2024-07-03. Same CPU / context-window-as-memory mapping as [[youtube-2025-06-19-software-is-changing]] @10:01. **The decade differs:** 1980s here (@06:10), 1960s in the YC talk (@10:34), 1970s–80s in the year-in-review essay (§6). The page's existing Note frames the decade shift as an analogy, not a change of view; this source should be added to that Note, not turned into a contradiction. Neither talk's claim is "it is literally the Nth decade", so `contradicts` does not apply.

### claim: physical-automation-will-lag-digital-automation
- existing: no
- aliases: bits before atoms
- title as a sentence: Automation of physical infrastructure will probably lag digital automation, because bits are easier than atoms
- confidence: stated (hedged: "probably")
- quote: "slightly lagging behind a lot of the digital Innovations" (@08:42)
- statements:
  - He says models in practice will probably do a lot of problem solving in the digital space, not only emotional-intelligence conversation as in "Her" (@08:04).
  - He pictures many digital entities given tasks, talking to and collaborating with each other, automating a lot of digital infrastructure (@08:04).
  - He says physical infrastructure may follow but is at an earlier stage and will probably lag digital innovations because bits are easier to work with than atoms (@08:42).
  - Using "I, Robot" (set in 2035) he says that in 10 years you can squint and imagine robots performing tasks, and asks how we would program them and make sure they do what we want (@08:42, @09:19).
- relation to existing pages: none. **Note:** [[this-is-the-decade-of-agents]] (2025-06-19) is about the pace of agents generally; this 2024 talk does not give a timescale for digital agents, only a "maybe in 10 years" squint for robots (@09:19). Do not force a link.

### claim: small-projects-can-snowball
- existing: no
- aliases: snowball, small snowballs
- title as a sentence: Small, fragile projects can snowball into very big ones
- confidence: stated
- quote: "it's very easy to dismiss these small snowballs because they're so fragile" (@14:50)
- statements:
  - He finds it incredible how sometimes very small projects can snowball into really big ones (@11:09).
  - Several of his early hackathon-style projects (a Rubik's Cube color extractor, a janky neuroevolution simulator) did not snowball; he does not call them wasted work, saying they still helped him along the way (@11:47, @12:23).
  - His game-programming tutorials on YouTube, about 13 years earlier, led to popular Rubik's Cube videos, an interest in teaching, CS231n at Stanford, the Zero to Hero series and then LLM101n (@11:47, @12:23, @13:01, @13:39).
  - At OpenAI, early on, someone worked on a Reddit chatbot that looked easy to dismiss next to the goal of competing with Google (@14:14, @14:50).
  - He says the Reddit chatbot was really a language model that could be trained on any data; after the Transformer and a wider web domain, it led to GPT-1 through GPT-4 and GPT-4o (@14:50, @15:27).
  - He tells the hackers that some of their projects probably will not go anywhere and some probably will, and they should keep the momentum (@16:04).
- relation to existing pages: none.

### claim: success-comes-from-repeated-practice
- existing: no
- aliases: 10,000 hours, ten thousand hours
- title as a sentence: To a very large extent, success comes from repeated practice, on the order of 10,000 hours
- confidence: stated
- quote: "success comes from just repeated practice" (@16:04)
- statements:
  - He says he is quite a big believer in Malcolm Gladwell's 10,000 hours: to a very large extent success comes from a huge amount of repeated practice (@16:04). (The idea is Gladwell's; the belief is his.)
  - His advice is to count hours rather than worry about whether you are succeeding or failing; failed projects still add to the counter (@16:04, @16:41).
  - Example: awesomemovies.life, a weekend movie-recommendation site, looked impressive to a reply on X, but it was about his 20th site like it: Linode, a Flask server, scraping, TF-IDF vectors, an SVM, remixing code snippets from earlier projects (@16:41, @17:16, @17:53).
  - Example: when he joined Tesla Autopilot to lead computer vision, about seven or eight years earlier, he rewrote the vision network training codebase from scratch in PyTorch in his first months; it became the kernel of what exists now, and it did not feel impressive to him after five PhD years of doing the same (@17:53, @18:33, @19:11).
  - He says things that look impressive look much less so once you have done them 20 times (@19:11).
  - He works out 10,000 hours at six hours a day as about five years, roughly the length of a PhD (@19:11, @19:48).
- relation to existing pages: none. **Note:** [[spelled-out-build-from-scratch]] step 8 mentions a bug he made "for the 20th time"; same phrase, unrelated idea.

### method: build-and-publish-projects
- existing: no
- aliases: work on projects, publish your projects, keep the dopamine flowing
- steps (proposed):
  - Pick a project and work on it end to end
  - Learn what you need on demand
  - Remix code from earlier projects
  - Publish it
  - Let the audience raise your bar
  - Take the reward when people use it
  - Count the hours, not the outcomes
- statements:
  - He says your brain is a reward machine, and his way of giving it rewards is doing projects and publishing them, good and bad (@19:48, @20:24).
  - Projects make you work end to end and in depth, learning on demand what you need, unlike the breadth-wise, just-in-case learning of classes; he says the two complement each other (@20:24).
  - Putting projects up is a "Jedi mind trick": thinking of friends, family and future employers looking at it raises the bar and makes you work harder (@20:24, @21:02).
  - When people like, fork and build on your project, that reward feels good, and this keeps you going toward 10,000 hours and lets a project snowball (@21:02, @21:39).
  - The remix step comes from the website example: he already had code snippets lying around and remixed them (@17:53).
- relation to existing pages: none. Joins [[small-projects-can-snowball]] and [[success-comes-from-repeated-practice]]; he presents the three as one loop in his summary (@21:02, @21:39).

### artifact: llm101n
- existing: no (no page; `raw/github/karpathy__LLM101n.md` exists and may be digested separately)
- aliases: LLM101n, LLM 101n, "Let's build a Storyteller"
- statements:
  - He describes LLM101n as his next class, about building a storyteller, a ChatGPT-like system to generate stories with (@13:01).
  - The idea is to build everything from scratch, from basic prerequisites to a ChatGPT clone in the storytelling domain (@13:01).
  - He says he had put it on GitHub two or three days earlier and that it was raw and at an early stage (@13:01).
- frontmatter: repo_url not stated in this source; language and status not stated. Take them from the README source.
- relation to existing pages: **Note:** "build everything from scratch" matches [[spelled-out-build-from-scratch]] in spirit; this source does not describe how, so cite it there only as context, if at all.

### timeline: his-teaching-over-time
- existing: no
- optional; merge may prefer sentences on [[small-projects-can-snowball]] instead
- entries he gives, in his order (dates relative to 2024 as he says them):
  - about 13 years earlier: game-programming tutorials on YouTube (@11:47)
  - then: Rubik's Cube videos that became popular, sparking his interest in teaching (@12:23)
  - as a Stanford PhD student: developed and taught CS231n, which he calls the first big deep-learning class at Stanford (@12:23)
  - then: the Zero to Hero YouTube series on deep learning (@12:23, @13:01)
  - 2024: LLM101n (@13:01)
- **Note:** the topic field would be teaching; no topic page exists. Only [[spelled-out-build-from-scratch]] and Zero to Hero sources (micrograd, makemore, GPT lectures) could anchor it.

## Quotes
- "this is not normal for AI" (@04:14)
- "the nature of computation basically is changing" (@06:10)
- "1980s of computing all over again" (@06:10)
- "I call this like the large language model lmos" (@06:49)
- "I actually find this picture kind of Bleak" (@09:55)
- "you should feel a lot of agency over what you want the future" (@10:30)
- "it's very easy to dismiss these small snowballs because they're so fragile" (@14:50)
- "success comes from just repeated practice" (@16:04)
- "this is my 20th time like making a website like this" (@17:16)
- "your brain is a reward machine and it wants rewards" (@19:48)
- "you're learning it on demand" (@20:24)
- "a really good Jedi mind trick" (@20:24)
- "And the message is just keep hacking." (@21:39)

## Notes for merge
- **Speaker boundaries.** His keynote starts mid-block [03:27], right after the host (Caroline Winnett, SkyDeck) says "Andrej come on out, Karpathy, yes big applause! Thank you." His first words: "Hi everyone! Yeah uh, so thank you for inviting me." It ends in block [21:39] with "And that's it! Thank you." Block [22:14] opens with the host: "Andrej Kaparthy, everybody!" Everything before [03:27] (SkyDeck intro, sponsors, fund) and from [22:14] to the end [1:32:27] (judges, eight team pitches, judge feedback, sponsor prizes) is other speakers. He is not one of the judges named at [23:28]–[24:05], and no later block quotes him. Nothing outside [03:27]–[21:39] is digested.
- **Whitespace.** The raw uses non-breaking spaces (U+00A0, often two) at caption line wraps. Quotes 2, 4, 6, 7, 9 and 10, and the physical-automation claim quote, cross such a wrap and are written here with single ordinary spaces; a string match must normalise whitespace. Quotes 1, 3, 5, 8, 11, 12, 13 match byte-for-byte.
- **Caption errors:** "lmos" = LLM OS (@06:49); "contact window" = context window, "dis" = disk (@06:49); "GPT 40" = GPT-4o (@06:49, @15:27); "restricted boltim machine" = restricted Boltzmann machine (@04:54); "resonet" = ResNet (@19:11); "agree with the whole thing from scratch" at @18:33 is garbled, probably "rewrote"; "Kaparthy" is the host's caption (@22:14); "hackaton" (@10:30, @19:48).
- **Garbled number:** OpenAI "worth uh maybe somewhere just below 1 billion" (@15:27) is almost certainly a caption or speech error; do not repeat the figure.
- **Relative dates:** "15 years in AI", "13 years ago" (tutorials), "7 years ago" (OpenAI founding, eight people in Greg's apartment), "seven or eight years ago" (Tesla), "two three weeks ago" (GPT-4o demo), "two or three days ago" (LLM101n on GitHub), "a few weeks ago" (awesomemovies.life). All relative to the talk; do not convert them to absolute years without another source. The video was published 2024-07-03; the talk itself may be a little earlier.
- **Mentioned, not explained:** "feel the AGI" (@09:19), Nvidia as the most valuable US company (@05:31), RBMs and contrastive divergence on MNIST as early-2010s practice (@04:54), OpenAI founded as a counterbalance to Google (@13:39, @14:14), the movies "Her" and "I, Robot". None is a topic candidate.
- **Not in this source:** micrograd, nanoGPT, minGPT, llm.c, Software 3.0 by name, small-hackable-educational-code. Do not add this source to those pages. Zero to Hero is only named.
- **Relations:** only [[llms-as-operating-systems]] (supports, earlier date, decade differs as an analogy). No `contradicts` anywhere. Do not link the awesomemovies.life weekend project to the vibe-coding claims; he built it from his own snippets, and the talk says nothing about AI-assisted coding.
- The two images he shows (a bleak generated picture, and a harmonious high-tech one) are described only through his words (@09:55, @10:30).
