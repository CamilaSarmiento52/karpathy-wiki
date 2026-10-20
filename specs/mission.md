# Mission

## Vision

A personal "Karpathy brain": a wiki compiled by an LLM from everything Andrej Karpathy has
published, plus an agent that teaches and reviews code the way he does. The wiki holds what
he knows and how he works. The agent uses it so that explanations are grounded in his words
and code is proven, not claimed.

The pattern is his own April 2026 "LLM Wiki": raw sources stay immutable, the LLM owns the
wiki, a schema file governs how pages are written, and ingest, query and lint keep it alive.

## Audience

One user: a freelancer and researcher who wants to understand AI deeply, ship client code
with confidence, and turn what she learns into research notes and content. She is not an ML
researcher and does not want to become one to use this.

## What it does

1. **Explains**: ask about any AI topic he has covered and get a walked-through answer,
   cited to his sources, in his teaching style (smallest version first, predict then run,
   show the broken version).
2. **Reviews**: hand it code and get his kind of review: what would break, proven by running
   it; what to delete; would he ship it.
3. **Learns**: a new post, video or repo improves the wiki without anyone editing pages by hand.

## Scope

- **In**: Karpathy's public output from 2023 onward (YouTube, X, GitHub, blog and
  newsletters, talks and interviews). Older material can be added later on request.
- **In**: one wiki, one sub-agent, three skills (teach, review, ingest), one run-gate hook.
- **Out**: voice cloning or impersonation. The agent follows his methods and cites his
  words; it does not pretend to be him.
- **Out**: other experts. The schema is designed to be reusable, but this project is
  Karpathy only.
- **Out**: a vector database or RAG layer. The wiki is the retrieval mechanism.

## Success criteria

- Any claim on any wiki page can be followed to a `raw/` file in two clicks.
- Every promoted rule has at least two independent sources with exact quotes; anything
  inferred is labelled as such and the agent says so when it uses it.
- `/karpathy-teach build a BPE tokenizer` produces: a definition of done, the smallest
  working version, a prediction before running, real output, a broken version, a fix, and a
  per-move rule checklist.
- `/karpathy-review` on a script that "works" finds a real failure condition and reproduces
  it by running the code.
- Asking about something he has never addressed returns "the wiki has nothing on this",
  never an invented position.
- `/karpathy-ingest <url>` on a new post updates every touched page, index, hot and log,
  and promotes a bench rule when the post supports it.
- The scheduled weekday run produces a short morning brief of what he published and what
  changed in the wiki.
