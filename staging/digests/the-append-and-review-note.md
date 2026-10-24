# Digest: The append-and-review note
- raw: raw/blog/the-append-and-review-note.md · published: 2025-03-19 · medium: blog · words: 746
- source slug: blog-2025-03-19-append-and-review-note

## Source page
```
---
type: source
raw_path: raw/blog/the-append-and-review-note.md
published: 2025-03-19
medium: blog
summary: "His note-taking approach of many years: one plain text note in Apple Notes, new items appended at the top, and occasional reviews that rescue what still matters while the rest sinks."
url: https://karpathy.bearblog.dev/the-append-and-review-note/
title: The append-and-review note
---
# The append-and-review note
Raw: [[raw/blog/the-append-and-review-note]] · Original: https://karpathy.bearblog.dev/the-append-and-review-note/

The post has no headings; three paragraphs open with a label. Citations use `§intro (Data structure)`, `§intro (Append)`, `§intro (Review)`, `§intro (Example usage)`, and plain `§intro` for the opening and closing paragraphs.

## Summary
He describes a note-taking approach that has worked well for him for many years and that he calls the "append-and-review note"; he finds it super simple yet covering most day-to-day note-taking (§intro). The data structure is one text note called "notes" in Apple Notes, because more than one note, sorted into folders, costs too much cognitive bloat, while a single note keeps CTRL+F trivial (§intro (Data structure)). He appends any idea or todo to the top as plain text, without dates, links or tags, except "watch:", "listen:" and "read:" prefixes he can search for (§intro (Append)). Older items sink as if under gravity; every now and then he scrolls down, rescues what deserves attention by copying it back to the top, sometimes merges related notes, and rarely deletes anything (§intro (Review)). He lists everyday uses, from a movie someone recommends to a TODO list for the day and the commands of a hyperparameter sweep, and says writing something down lets him clear his working memory and focus on something else (§intro (Example usage), §intro).

## Key points
- One note, append at the top, review by scrolling and rescuing → [[append-and-review-note]]
- A single note instead of many notes in folders → [[one-text-note-beats-many-organized-notes]]

## Fed pages
- [[append-and-review-note]]
- [[one-text-note-beats-many-organized-notes]]
```

## Candidates
### method: append-and-review-note
- existing: no
- aliases: [append-and-review note, one text note, note-taking]
- steps:
  1. Keep one plain text note
  2. Append every idea or todo at the top
  3. Skip metadata except watch:, listen:, read: tags
  4. Scroll down now and then and skim
  5. Copy what still matters back to the top
  6. Merge related notes; rarely delete
- statements:
  - He has used the approach for many years and finds it simple while covering most day-to-day note-taking (§intro)
  - One text note called "notes" in Apple Notes; Apple handles offline editing, syncing between devices and backup (§intro (Data structure))
  - Any idea, todo or anything else is appended to the top as text, from his computer at work or his iPhone on the go (§intro (Append))
  - He does not find structured metadata (dates, links, concepts, tags) useful and does not add it by default; the exception is "watch:", "listen:" or "read:" prefixes he can CTRL+F when looking for something to watch, listen to or read (§intro (Append))
  - New items push old ones down "almost as if under gravity"; every now and then he scrolls and skims, and copy-pastes anything that deserves attention back to the top (§intro (Review))
  - Sometimes he merges, processes, groups or modifies related notes; he deletes a note only rarely; notes that repeatedly do not deserve attention keep sinking but are never lost (§intro (Review))
  - Example uses include a random idea while on the go, a movie or book recommendation, a morning TODO list, a draft tweet that needs more thought, a quote, numbers from a paper, a shell command he keeps forgetting, the commands and outcome of a hyperparameter sweep, and dumping worries into a list when stressed (§intro (Example usage))
  - Re-ordering notes, he sometimes finds he has thought about the same thing from different perspectives, merges them and feels additional insight (§intro (Example usage))
  - Writing something down lets him move on, wipe his working memory and focus fully elsewhere, confident he will revisit it at review (§intro)
  - The note has grown giant over the years; some ideas fail repeated review and sink, and sometimes an old idea becomes relevant in a new light (§intro)
- relation to existing pages: [[llm-knowledge-bases]] / [[llm-wiki-workflow]] are his other personal knowledge practice in the wiki (published 2026-04-02). Not the same idea: append-and-review is one unstructured note with no links or tags, the LLM wiki is an LLM-compiled linked wiki. Not a recurrence strong enough for a shared topic. Proposed: a labelled **Note:** on [[llm-knowledge-bases]] (this source in its `context`), e.g. "**Note:** in a post published 2025-03-19 he described a manual practice for personal notes, a single unstructured text note he appends to and reviews ([[blog-2025-03-19-append-and-review-note]]); it is a different approach, not an earlier form of the wiki." No order or change of mind may be implied.

### claim: one-text-note-beats-many-organized-notes
- existing: no
- title: "For him, one text note works better than many notes sorted into folders"
- confidence: stated
- quote: "A single note means CTRL+F is simple and trivial." (§intro (Data structure))
- statements:
  - Maintaining more than one note and sorting them into folders and recursive substructures "costs way too much cognitive bloat" (§intro (Data structure))
  - He does not find tagging notes with structured metadata useful (§intro (Append))
  - He closes with "One text note ftw." (§intro)
- relation to existing claims: none. (Thematically near his code-simplicity claims such as [[neural-net-training-should-not-be-complicated]], but those are about neural-net code; any link is my reading. Do not set `supports`.)

## Quotes
- "I call it the "append-and-review note"." (§intro)
- "I maintain one single text note in the Apple Notes app just called "notes"." (§intro (Data structure))
- "A single note means CTRL+F is simple and trivial." (§intro (Data structure))
- "costs way too much cognitive bloat" (§intro (Data structure))
- "everything else starts to sink towards the bottom, almost as if under gravity" (§intro (Review))
- "I delete a note only rarely." (§intro (Review))
- "They are never lost, they just don't deserve the top of mind." (§intro (Review))
- "wipe my working memory, and focus fully on something else at that time" (§intro)
- "One text note ftw." (§intro)

## Notes for merge
- Locations: no markdown headings. "Data structure.", "Append.", "Review." and "Example usage:" are inline paragraph labels; cited as `§intro (<label>)`. The two paragraphs after the example list and the final line are plain `§intro`.
- The hyperparameter-sweep example (recording the commands he ran and the outcome) is a mention, not an explanation; do not add it to [[learning-rate-sweep]] or [[quick-experiment-loop]] as a step.
- "I stumbled on" — he does not claim to have invented the approach; he says he calls it the append-and-review note.
- Apple Notes is his tool; the post does not argue Apple Notes over other apps beyond saying Apple does a good job of offline editing, sync and backup.
