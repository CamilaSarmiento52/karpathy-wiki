---
type: method
steps:
  - Count FLOPs per token and parameters with explicit formulas
  - Fix a FLOP budget and train several depths to exactly that budget
  - Find the depth with the lowest loss at that budget
  - Repeat for a few budgets and fit the optima
  - Read the optimal tokens-to-parameters ratio off the fit and set training length from it
  - Check that the resulting family's curves do not cross
sources: ["[[github-2026-01-07-nanochat-miniseries-v1]]", "[[github-2026-01-31-nanochat-beating-gpt-2]]"]
aliases: [scaling-law sweep, compute-optimal sweep, measure your own Chinchilla ratio]
---
# Fit your own scaling law
How he decides how long to train each nanochat model: rather than ask how many iterations a d12 needs, he fixes a FLOP budget, finds the model size that reaches the lowest loss for it, and derives the compute-optimal tokens-to-parameters ratio from his own runs ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws)). He frames the goal as optimising a family of models controlled by one dial, the compute you wish to spend, which is what gives confidence that the extrapolation to "the big run" will work ([[github-2026-01-07-nanochat-miniseries-v1]] §intro (Why miniseries)).

## Steps
1. **Count FLOPs and parameters explicitly.** FLOPs per token are 6 × the non-embedding parameters plus 12·l·h·q·t for attention's key-query matmuls, which his code comment puts about 1% off Chinchilla's exact formulas; parameters are all parameters, counted Chinchilla's way, because, his comment says, his own nanochat experiments confirm "the Chinchilla approach gives the much cleaner scaling law" ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws)).
2. **Fix the budget, vary the depth.** With `--target_flops` fixed, e.g. 3e18 (setting), the training script scales the iterations so every depth costs exactly that budget: small depths train long, large depths train short ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws)).
3. **Find the minimum.** At 3e18 FLOPs one depth in between, d16 (measured), struck the right balance and reached the lowest loss; that model size and training length is compute optimal ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws)).
4. **Repeat and fit.** Repeating for a few budgets gives what he calls surprisingly nice U shapes; a quadratic fit to the optima gives 137M parameters and 1.12B tokens at 1e18 FLOPs, 240M and 1.88B at 3e18, and 330M and 2.71B at 6e18, ratios of 8.2, 8.1 and 8.5 (measured, fit) ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws)).
5. **Set the training length from the ratio.** With equal exponents the optimal ratio is a constant; nanochat's fits give about 8 against Chinchilla's 20 (comparison), so training length follows as tokens = 8 × parameters divided by the batch of about 0.5M tokens; "We're now only training compute optimal models." ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws)). He says the lower constant might come from nanochat specifics such as Muon or from the small model sizes ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws)).
6. **Check the family.** If code, architecture, optimisation and scaling laws are right, the loss curves of the series should not intersect, each being the unique compute-optimal way to its target loss ([[github-2026-01-07-nanochat-miniseries-v1]] §intro (Miniseries v1)).

The table that extrapolates the series to GPT-2 and GPT-3 is headed "12:1 D:N ratio" while the text gives 8; both are reported as the post gives them ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Miniseries v1 CORE scores), §Details (Scaling laws)).

On 2026-01-31 he lists the scaling-law measurement among what worked for the GPT-2 record: the optimal tokens-to-parameters ratio measured at about 10, with "It's important to do the actual experiment on your own network." ([[github-2026-01-31-nanochat-beating-gpt-2]] §What Worked). The record run's script uses 10.5 for compute optimal and 12 for the speedrun (settings) ([[github-2026-01-31-nanochat-beating-gpt-2]] §Training Script). **Note:** about 8 on 2026-01-07 and about 10 on 2026-01-31 come from different code states; neither post calls the second a revision of the first ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws); [[github-2026-01-31-nanochat-beating-gpt-2]] §What Worked).

## Seen in
- [[nanochat]] — the miniseries trained this way
- [[scaling-laws]] — Chinchilla and Kaplan as he reports them
- [[nanochat-reproduces-chinchillas-equal-scaling-of-parameters-and-tokens]]
