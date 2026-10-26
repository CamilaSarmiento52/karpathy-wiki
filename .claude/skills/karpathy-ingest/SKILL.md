---
name: karpathy-ingest
description: Add one new Andrej Karpathy source (a post, video, talk, repo or thread) to the karpathy-wiki and compile it into the wiki, verified and committed. Use when the user types /karpathy-ingest with a URL or a raw/ path, or when the scheduled run has new raw files.
argument-hint: <url | raw/<medium>/<id>.md>
---
Ingest this into the karpathy-wiki: $ARGUMENTS

**Where to work.** All work happens in the karpathy-wiki repo. If the current folder is not that repo, read `~/.claude/agents/karpathy.md`, find the wiki path in its Grounding section, and `cd` there. Use the repo's `.venv/bin/python` for every script. Read `CLAUDE.md` in full before starting. Its §7 Ingest procedure and invariants are the rules; this skill only adds the steps around them.

## 1. Get the raw file

- If the argument is a path under `raw/`, use it as it is.
- If it is a URL, work out the medium and id, then fetch it:
  `.venv/bin/python scripts/fetch_one.py <medium> <id>`. This is the only way anything enters `raw/`. Never write raw files by hand.
  - `x.com/karpathy/status/<id>` → `x <id>` (for a thread, the post ids in order, comma-separated)
  - `github.com/<owner>/<repo>` → `github <owner>/<repo>`; a Discussion → `github <owner>/<repo>/discussions/<n>`
  - `karpathy.bearblog.dev/...` or `karpathy.github.io/...` → `blog <url>`
  - YouTube on his own channel → `youtube <id>`; on anyone else's channel → `talk <id>`. Check the uploader with `.venv/bin/yt-dlp --print uploader <url>` if unsure.
- If the manifest already has the item, say so and stop. If the fetch fails or there is no route for this kind of URL, stop and report it. Do not improvise a raw file.

## 2. Compile it (CLAUDE.md §7 Ingest)

Follow `staging/merge-brief.md` for a single source:
- Read the whole raw file.
- Write the source page.
- Reuse existing pages before creating new ones: search the type files in `wiki/index/` and the aliases.
- Set relations by the weakest true link. `extends` and `contradicts` need timeline entries.
- Never attribute to him the words of a host, a paper or an AI (CLAUDE.md §3).
- Dates are published dates.

Then update the Fed pages, the index type files, `hot.md` (keep 20), and `log.md`. The log entry must use these fields, because the morning brief reads them:

```
## YYYY-MM-DD ingest [[source-slug]]
- created: [[...]], [[...]]
- updated: [[...]]
- relations: [[a]] extends [[b]] (timeline [[t]])        (or "none")
- principles: quote added to [[p]]; promoted [[q]]       (or "none")
- verifier: N findings, N fixed                           (filled in at step 4)
- notes: anything a reviewer should know
```

## 3. Principles

If the source has a verbatim quote, under 15 words, that supports a principle in `wiki/principles/` or `_bench/`:
- Add it to that page's `quotes`, with its location, and cite it in `## In practice`.
- If a bench rule now has quotes from 2+ independent sources and is not `inferred`, move it to `wiki/principles/` with `status: promoted`. Lint enforces the conditions (`scripts/independence.json`).
- If any principle changed, run `.venv/bin/python scripts/build_agent.py`. If `~/.claude/agents/karpathy.md` exists, also run `.venv/bin/python scripts/install.py`.

## 4. Check, verify, fix

1. These must all be clean before you go on:
   - `.venv/bin/python scripts/lint_check.py`
   - `.venv/bin/python scripts/quote_check.py`
   - `.venv/bin/python scripts/build_agent.py --check`
   - `.venv/bin/python -m pytest -q tests`
2. Start a **fresh verifier** with the Agent tool (general-purpose). Give it this brief: read `staging/verify-brief.md` and follow it for the single source `<source-slug>`, writing `staging/verify/ingest-<source-slug>.md`; check every claim, timeline entry and principle quote this ingest touched, and at least one in five other sentences.
3. Apply every finding. Log the fixes in a `correction` entry. Fill in the `verifier:` line of the ingest entry. Rerun the checks in step 1.

## 5. Commit and report

- Commit locally, in one commit, with the message `Ingest <source-slug>` and the attribution line your instructions give. Never push.
- If any check still fails, do not commit. Report what failed.
- Reply in a few lines:
  - what the source is;
  - the pages created and updated;
  - any relation, or any principle change;
  - the verifier's result;
  - the commit hash.
