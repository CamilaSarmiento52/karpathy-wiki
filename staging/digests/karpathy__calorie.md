# Digest: calorie README
- raw: raw/github/karpathy__calorie.md · published: 2024-05-30 · medium: github · words: 371
- source slug: github-2024-05-30-calorie-readme

## Source page
```
---
type: source
raw_path: raw/github/karpathy__calorie.md
published: 2024-05-30
medium: github
summary: "README of calorie, his single-page personal web app that tracks a running calorie deficit against a daily goal with +100 and -100 kcal buttons."
url: https://github.com/karpathy/calorie
title: calorie README
---
# calorie README
Raw: [[raw/github/karpathy__calorie]] · Original: https://github.com/karpathy/calorie

Dated by the README's last commit (a3c5d0d). A personal project, not part of his AI work.

## Summary
calorie is a calorie-deficit tracking web app (§intro). He explains the model behind it: you burn calories at a base metabolic rate just by living (roughly 2000 kcal/day for him), eating adds calories, exercise burns them, and a net deficit loses weight; his goal might be a 500 kcal/day deficit, which he works out as roughly a pound of fat a week (§intro). The app shows two counters, the current deficit next to the goal; you press +100 kcal per hundred calories eaten and -100 kcal per hundred burned exercising (§intro). He keeps it open in a corner of his screen to see how much he can still eat, or how much he would need to run off before a big meal, and the aim is to keep the number green rather than red (§intro). Configuration is two constants edited directly in `index.html`, and you run it by opening that file in a browser (§intro).

## Key points
- What the app does, how he uses it, and how it is configured → [[calorie]]

## Fed pages
- [[calorie]]
```

## Candidates
### artifact: calorie
- existing: no
- aliases: [calorie tracker, calorie deficit tracker]
- frontmatter: repo_url https://github.com/karpathy/calorie · language JavaScript (single `index.html`) · status active (no deprecation in the README)
- statements:
  - A calorie deficit tracking web app (§intro)
  - The model: base metabolic rate burns calories continuously (he gives roughly 2000 kcal/day for himself and points to online calculators); food adds, exercise subtracts; a net deficit means weight loss (§intro)
  - A daily deficit goal, e.g. 500 kcal/day for him, which he computes as 7 × 500 = 3500 kcal a week, roughly 1 pound of fat (§intro)
  - Two counters show the current deficit next to the goal; +100 kcal per press for food (a Big Mac is five presses for him), -100 kcal per press for exercise (a 30-minute treadmill run at about 400 kcal is four) (§intro)
  - He leaves it open in a corner of his screen; it shows how much he may eat to stay on goal, or how much running a planned 1000 kcal meal would need (§intro)
  - The goal is to keep the number green (deficit in line with goal), not red (§intro)
  - Setup is editing `hourlyCalorieBurn` and `hourlyCalorieTargetDeficit` (daily values divided by 24) in `index.html`, then opening the file in a browser (§intro)
  - MIT licence (§License)
- relation to existing pages: none.

No topic candidate: calorie tracking does not recur anywhere in the wiki. No claim candidate:
he describes how he uses the app, not a position. No method: it is not how he builds,
debugs, explains or evaluates.

## Quotes
- "Calorie deficit tracking web app." (§intro)
- "I leave this little web app always open at the corner of my screen." (§intro)
- "Losing weight then becomes as simple as making sure that your number stays green" (§intro)

## Notes for merge
- Locations: text under `# calorie` is `§intro`; the only other heading is `§License`.
- The nutrition arithmetic (BMR, 3500 kcal ≈ 1 lb) is his statement in the README; attribute it to him and do not present it as health advice or extend it.
- His own numbers (BMR, deficit goal, Big Mac, treadmill) are personal details he published; fine to paraphrase briefly, no need to dwell.
- The artifact's only inbound link will be this source page, which satisfies invariant 4. A **Note:** connection to [[small-hackable-educational-code]] (one file, no dependencies) would be my reading, not his; I do not propose it.
- `language`: GitHub would likely report HTML; the README shows JavaScript constants in `index.html`. Either is defensible; merge picks one.
