# Digest: Finding the Best Sleep Tracker
- raw: raw/blog/finding-the-best-sleep-tracker.md · published: 2025-03-24 · medium: blog · words: 1829
- source slug: blog-2025-03-24-best-sleep-tracker

## Source page
```
---
type: source
raw_path: raw/blog/finding-the-best-sleep-tracker.md
published: 2025-03-24
medium: blog
summary: "His two-month comparison of four sleep trackers worn at once (Oura, Whoop, 8Sleep, Apple Watch with AutoSleep), finding Oura and Whoop best and AutoSleep near random, and his view that sleep strongly tracks his work quality."
url: https://karpathy.bearblog.dev/finding-the-best-sleep-tracker/
title: Finding the Best Sleep Tracker
---
# Finding the Best Sleep Tracker
Raw: [[raw/blog/finding-the-best-sleep-tracker]] · Original: https://karpathy.bearblog.dev/finding-the-best-sleep-tracker/

The post has no headings; some paragraphs open with a label. Citations use `§intro (<label>)` for Qualitative assessment, Matters of Heart Rate, Yes, sleep matters and Shopping recommendations, and plain `§intro` for the paragraphs before the first label.

## Summary
After a Bryan Johnson video on sleep habits, which he says he watched about two months before writing, he resolved to improve his sleep and first to measure it, so he wore four trackers at once, Oura, Whoop, an 8Sleep Pod 4 Ultra and an Apple Watch with AutoSleep, and logged their numbers each morning in a published spreadsheet (§intro). After about two months he rates Oura and Whoop as "Tier 1", 8Sleep as ok, and Apple Watch with AutoSleep as really terrible, its scores nearly random (§intro (Qualitative assessment)). Score histograms show AutoSleep and 8Sleep saturating near 100, Whoop somewhat, and Oura with the most dynamic range; pairwise score correlations are highest for Whoop and Oura (0.65) and lowest for Whoop and AutoSleep (0.14) (§intro (Qualitative assessment)). Resting heart rate agrees closely across trackers, does not clearly correlate with sleep score, and, with his regular Zone 2 and HIIT exercise, fell slightly over the 60 days while HRV rose (§intro (Matters of Heart Rate)). He says with absolute certainty that his sleep scores correlate strongly with the quality of his work that day, and recommends Whoop for convenient tracking and Oura for the best tracking if the ring suits you (§intro (Yes, sleep matters), (Shopping recommendations)).

## Key points
- Oura and Whoop best, 8Sleep ok, AutoSleep near random → [[oura-and-whoop-were-the-best-sleep-trackers-he-tested]]
- Sleep score tracks the quality of his work; accumulated sleep debt matters more than one night → [[his-sleep-score-tracks-his-work-quality]]
- How he compared the trackers: wear all, log every morning, histograms, pairwise correlations → [[compare-measuring-devices-head-to-head]]

## Fed pages
- [[oura-and-whoop-were-the-best-sleep-trackers-he-tested]]
- [[his-sleep-score-tracks-his-work-quality]]
- [[compare-measuring-devices-head-to-head]]
```

## Candidates
### claim: oura-and-whoop-were-the-best-sleep-trackers-he-tested
- existing: no
- title: "In his two-month test, Oura and Whoop were the best sleep trackers and AutoSleep was near random"
- confidence: stated
- quote: "AutoSleep is basically a random number generator." (§intro (Shopping recommendations))
- statements:
  - After about two months he judged Oura and Whoop "Tier 1", fairly similar and high quality, with scores that mostly matched how he felt in the morning; 8Sleep ok; Apple Watch with AutoSleep really terrible, scores almost random and swinging wildly (§intro (Qualitative assessment))
  - Histograms: AutoSleep and 8Sleep give very high scores pushing against 100, Whoop is a little too easy to please, and Oura is the hardest to please with a roughly gaussian spread and the most dynamic range, which he counts in its favour; his best Oura score was 92 while he gets 100 on Whoop fairly regularly (§intro (Qualitative assessment))
  - Sorted score correlations: Whoop–Oura 0.65, Oura–8Sleep 0.59, Oura–AutoSleep 0.47, 8Sleep–AutoSleep 0.42, Whoop–8Sleep 0.38, Whoop–AutoSleep 0.14; if Whoop is good, which he thinks it is, AutoSleep looks almost like a noise generator (§intro (Qualitative assessment))
  - Oura: excellent app with a single dense overview pane; but the ring is thick, interferes with his grip at the gym, needs correct sizing and rotation, and must come off to charge (§intro (Shopping recommendations))
  - Whoop: excellent, comprehensive app that takes more clicking; a neat LLM integration; a Community feature he likes but finds undercooked; saturates at 100 fairly easily; a much better wrist form factor and a charger that attaches so it never comes off (§intro (Shopping recommendations))
  - 8Sleep's scores did not make as much sense to him and did not correlate strongly with Whoop or Oura; for AutoSleep, "Do not use", though there may be a better Apple Watch app he has not found (§intro (Shopping recommendations))
  - His advice: Whoop for 9.5/10 reliable, convenient tracking; Oura for 10/10 tracking if you are ok with the ring (§intro (Shopping recommendations))
- relation to existing claims: none.

### claim: his-sleep-score-tracks-his-work-quality
- existing: no
- title: "His sleep scores correlate strongly with the quality of his work that day"
- confidence: stated
- quote: "my sleep scores correlate strongly with the quality of work" (§intro (Yes, sleep matters))
- statements:
  - He says with absolute certainty that Bryan [Johnson] is basically right, and that his sleep scores correlate strongly with the quality of work he can do that day (§intro (Yes, sleep matters))
  - With a low score he lacks agency, courage and creativity; with a high one he can power through anything, and on his best days work 14 hours barely noticing time pass (§intro (Yes, sleep matters))
  - The effect depends on accumulated sleep debt over the last few days, not a single night: one bad night is usually ok, a few in a row are bad (§intro (Yes, sleep matters))
  - He has not yet seen a dramatic improvement in his own sleep over the two months, which were mixed up with parties, injuries, experiments and a rough week obsessing over a technical problem; he treats it as a year-long project (§intro (Matters of Heart Rate))
- relation to existing claims: none. The position on sleep is attributed to Bryan Johnson first; he endorses it. Keep the endorsement as his, the habits as Bryan's.

### method: compare-measuring-devices-head-to-head
- existing: no (nearest existing: [[verify-against-a-reference-implementation]], which cross-checks code against a trusted implementation; not the same procedure, and here no device is the reference. No link unless as a **Note:**.)
- aliases: [sleep tracker comparison, head-to-head tracker comparison]
- one source only; merge may fold it into the source page if a single-use procedure is not worth a method page.
- steps:
  1. Wear every candidate device at once
  2. Log each device's numbers every morning
  3. Note how you felt on waking
  4. Plot each device's score histogram
  5. Correlate the devices pairwise
  6. Test expected relations, read them as correlation only
- statements:
  - He wore Oura, Whoop, 8Sleep and Apple Watch with AutoSleep together for about two months (§intro)
  - He logged sleep stages (Light, REM, Deep, Awake), resting heart rate, HRV and each app's sleep score in a simple spreadsheet every day right after waking, to compare them and relate them to how he felt that morning; the raw data is linked (§intro)
  - He plotted histograms of each tracker's scores to see saturation and dynamic range (§intro (Qualitative assessment))
  - He plotted pairwise correlation scatter plots to see which trackers agree most (§intro (Qualitative assessment))
  - He checked resting heart rate agreement across trackers and its correlation with sleep score, warning it is only correlation and he does not know whether the apps use RHR in their score (§intro (Matters of Heart Rate))
  - He checked whether his exercise showed up in Whoop–Oura averaged RHR and HRV (§intro (Matters of Heart Rate))
- relation to existing pages: none.

### Not a candidate: topic sleep-tracking / personal health tracking
- Only this source discusses sleep. The nearest existing page is [[calorie]] (his calorie-deficit tracker, `github-2024-05-30-calorie-readme`): both are him tracking a personal health number daily, but the calorie README says nothing about sleep, measurement quality or devices. That is my reading, not a recurrence of the same idea. Proposed instead: an optional labelled **Note:** on [[calorie]] citing this source in `context`, e.g. "**Note:** another personal tracking project of his is a two-month comparison of sleep trackers ([[blog-2025-03-24-best-sleep-tracker]])."

## Quotes
- "Its scores are basically almost random and they swing around wildly" (§intro (Qualitative assessment))
- "Oura is the most difficult to please" (§intro (Qualitative assessment))
- "Whoop vs Oura: 0.65" (§intro (Qualitative assessment))
- "AutoSleep looks almost like a noise generator." (§intro (Qualitative assessment))
- "Keep in mind that this is just correlation analysis" (§intro (Matters of Heart Rate))
- "I love to see exercise adaptations in the data." (§intro (Matters of Heart Rate))
- "my sleep scores correlate strongly with the quality of work" (§intro (Yes, sleep matters))
- "When my sleep score is high, I can power through anything." (§intro (Yes, sleep matters))
- "So in other words a single bad night is usually ok." (§intro (Yes, sleep matters))
- "Listen to Bryan." (§intro (Yes, sleep matters))
- "AutoSleep is basically a random number generator." (§intro (Shopping recommendations))
- "Get Oura for 10/10 tracking, if you're ok with the ring form factor." (§intro (Shopping recommendations))

## Notes for merge
- Locations: no markdown headings. Labelled paragraphs: "Qualitative assessment.", "Matters of Heart Rate.", "Yes, sleep matters.", "Shopping recommendations."; the correlation list and histogram discussion fall between the first two labels and are cited `§intro (Qualitative assessment)`. The exercise and "not seeing a dramatic increase" paragraphs sit after "Matters of Heart Rate" and before "Yes, sleep matters".
- Numbers, exactly as in the raw: score correlations above; RHR improved "a bit less than 3 bpm" over 60 days ("from ~51 bpm -> 48 ~bpm"); HRV "from ~49 -> 54"; Whoop HRV about 5 above Oura, which he cannot explain; Whoop RHR–score correlation "~0.13", Oura none; exercise about 30 minutes of Zone 2 a day on average plus a 4x4x4 HIIT twice a week; best Oura score 92.
- Heart-rate matrix: he says all trackers except 8Sleep agree quite highly and 8Sleep is worst because it is a mattress without a direct heart-rate measurement, yet the printed matrix gives 8Sleep 0.947 with AutoSleep and with Oura, and the lowest pair is Whoop–8Sleep 0.879. Report his words and, if the numbers are used, the numbers; do not reconcile them.
- "About 2 months ago" is relative to the post; per CLAUDE.md §2 write it as his words ("about two months before the post"), not a computed date.
- Bryan Johnson's habits and claims are his, not Karpathy's; Karpathy only endorses that sleep matters.
- The images (him wearing the devices, plots, app screenshots) are not in the raw.
- Product verdicts are his as of 2025-03-24, not the wiki's.
