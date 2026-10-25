# Merge brief (batches 2–4)

You are the MERGE step for an LLM-compiled wiki about Andrej Karpathy, in
`/Users/camilasarmiento/Documents/AI os/karpathy-wiki`. **You are the only writer of
`wiki/` right now.** You write only under `wiki/`. Never touch `raw/` or `staging/`.

## Read first, in this order

1. `CLAUDE.md`: follow §4 (page types, frontmatter, body), §5 (citations, evidence blocks,
   quotes), §6 (index files, hot, log) and §7 Ingest steps 3–11 exactly.
2. The batch merge map your prompt names. It fixes the canonical slugs. Create ONLY the
   pages it assigns to your group; every other candidate becomes cited sentences on the
   page the map points to.
3. `wiki/hot.md`, the tail of `wiki/log.md`, and the index type files in `wiki/index/`.
4. Before editing an existing page, read it in full. Style models:
   `wiki/topics/tokenization.md`, `wiki/claims/use-cross-entropy-not-a-hand-rolled-loss.md`,
   `wiki/methods/training-diagnostics.md`, `wiki/artifacts/nanogpt.md`, and a talk source
   page such as `wiki/sources/youtube-2025-06-19-software-is-changing.md`.
5. Your digests, in published order. Process one source at a time.

## For each source

1. Write the source page from the digest's "## Source page". Fix `## Key points` arrows
   and `## Fed pages` to the canonical slugs; Fed pages lists exactly the pages that end
   up citing this source.
2. Create or extend each page the map routes this source to. When you add a source to an
   existing page: add it to `sources` (or `context` if only background), update a topic's
   `first_seen` / `last_updated` (min / max `published` over `sources` only), add cited
   sentences, and list the page in the source's Fed pages.
3. Add each new page to its type file in `wiki/index/` (alphabetical,
   `- [[slug|Title]] — one-line summary`). Do not list pages in `wiki/index.md`.
4. Prepend one line per page change to `wiki/hot.md`; keep only the 20 newest lines.
5. Append `## <today> ingest [[source-slug]]` to `wiki/log.md` (created / updated / notes).
   Never edit past entries.
6. Run `.venv/bin/python scripts/lint_check.py` from the repo root and fix every finding
   before the next source.

At the end, lint must print `0 findings`, and `.venv/bin/python -m pytest -q tests` must
pass.

## Rules that matter most

- Every paragraph and list item in an evidence section cites a source page:
  `([[talk-2023-05-25-state-of-gpt]] @12:34)` for video and talks, `§heading` for text.
  Locations come from the digests.
- Paraphrase no stronger than the digest's statement. No facts from your own knowledge.
  Your own connections between pages start with **Note:** and still cite.
- **AI-written text is not his** (CLAUDE.md §3): never cite an AI-written part of a source as
  his view or quote; the digest marks those parts.
- **Talks include other speakers.** Never attribute a host's or interviewer's words, or a
  paper's finding, to him. The digests mark these; respect the marks.
- Garbled caption numbers flagged in a digest's notes are never repeated as fact.
- Quotes: only verbatim quotes from the digests, under 15 words, in quotation marks with a
  citation. A claim page's first body line is `> "quote" — [[source-slug]] @time`. Lint
  string-matches every claim quote against the raw file.
- Correct spelling outside quotes (PyTorch, BatchNorm, nanoGPT, llm.c, LoRA, GPT-4).
- Claim frontmatter: `type, stated_on, confidence, sources, topic`. `supports` is set on
  both pages, and each side's Related claims line cites the passage it relies on.
  `extends` / `contradicts` need a timeline entry for both claims; the map says where
  they are expected (usually nowhere).
- Timeline pages: `type: timeline`, `topic: "[[topic-slug]]"`, dated bullets oldest first,
  each citing a source page.
- **Dates are published dates** (CLAUDE.md §2). Never write "N months later", "a week
  after" or "first said in" between sources; write the dates. Talks can be published long
  after they were given (CS25: given ~January 2023, published May 2023).
- YAML values containing `: ` must be quoted (a source `summary` broke lint this way).
- Every new page needs an inbound link from a content page (Fed pages count; index files,
  hot and log do not).

## Report back

In under 200 words: pages created and updated (counts by type), the final lint line, and
every decision the map did not settle, so the next group and the verifier know.
