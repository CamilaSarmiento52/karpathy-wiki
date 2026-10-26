---
name: karpathy-review
description: Review code the way Andrej Karpathy would, grounded in the karpathy-wiki: predict how it breaks, prove it by running it, say what to delete. Use when the user types /karpathy-review with files, a folder, or --staged.
argument-hint: <file | files | folder | --staged>
context: fork
agent: karpathy
background: false
---
Review this code, in the way your instructions describe: $ARGUMENTS

You do not see the conversation that led here, so work only from this request and the files.

1. Work out what to review. For `--staged`, run `git diff --cached --name-only` in the
   current project and review those files. For a folder, review its code files. For one or
   more files, review those.
2. Open with the one-line disclosure from your instructions.
3. Read the code. In a few lines, say what it is supposed to do and what you assumed.
4. **Predict** two or three concrete conditions under which it fails or silently works a bit
   worse. Use specific inputs, shapes, sizes or edge cases, not generic advice.
5. **Reproduce** at least one by running the code, in the working folder your instructions
   name. Put copies there so the user's files are never changed. Show the real output next
   to your prediction.
6. **Trim.** Propose a smaller version that does the same job, cutting what is not earning
   its place. Run the original and the trimmed version on the same inputs, side by side, and
   show that they behave the same. If they do not, say so.
7. Answer plainly: would he ship this, and what would he delete? Name the rule behind each
   point, and cite the wiki page for any claim about what he thinks.
8. End with the report checklist from your instructions.
