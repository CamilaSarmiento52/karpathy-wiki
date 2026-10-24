---
type: artifact
repo_url: https://github.com/karpathy/calorie
language: JavaScript (one index.html)
status: active
sources: ["[[github-2024-05-30-calorie-readme]]"]
aliases: [calorie tracker, calorie deficit tracker]
---
# calorie
His calorie deficit tracking web app, a personal project outside his AI work ([[github-2024-05-30-calorie-readme]] §intro).

## What it demonstrates
- **The model behind it.** As he explains it, you burn calories at a base metabolic rate just by living, roughly 2000 kcal/day for him; food adds calories, exercise burns them, and a net deficit means weight loss ([[github-2024-05-30-calorie-readme]] §intro). His goal might be a 500 kcal/day deficit, which he works out as 7 × 500 = 3500 kcal a week, roughly a pound of fat ([[github-2024-05-30-calorie-readme]] §intro).
- **How it works.** Two counters show the current deficit next to the goal; you press +100 kcal per hundred calories eaten (a Big Mac is five presses for him) and -100 kcal per hundred burned (a 30-minute treadmill run at about 400 kcal is four) ([[github-2024-05-30-calorie-readme]] §intro).
- **How he uses it.** He leaves it open in a corner of his screen; it shows how much he can eat and stay on goal, or how much running a planned 1000 kcal meal would take, and the aim is to keep the number green, not red ([[github-2024-05-30-calorie-readme]] §intro).
- **Setup.** Edit two constants in `index.html`, `hourlyCalorieBurn` and `hourlyCalorieTargetDeficit` (daily values divided by 24), then open the file in a browser; it is MIT licensed ([[github-2024-05-30-calorie-readme]] §intro, §License).
- `status: active` because the README has no deprecation notice; `language` reflects the JavaScript constants in its single `index.html` ([[github-2024-05-30-calorie-readme]] §intro).

## Related
- [[github-2024-05-30-calorie-readme]]
