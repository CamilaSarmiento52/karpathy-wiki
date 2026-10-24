---
type: topic
aliases: [RLVR, Reinforcement Learning from Verifiable Rewards, reinforcement learning stage, RL for LLMs, thinking models, reasoning models, DeepSeek-R1, o1, o3, chains of thought, verifiable domains, practice problems]
first_seen: 2025-02-05
last_updated: 2025-12-19
sources: ["[[blog-2025-12-19-year-in-review-2025]]", "[[youtube-2025-02-05-deep-dive-into-llms]]", "[[github-2025-10-13-nanochat-discussion-introducing]]"]
related: ["[[jagged-intelligence]]"]
---
# RLVR
Reinforcement Learning from Verifiable Rewards: training LLMs against automatically checkable rewards such as math and code puzzles, which he calls the major new stage of 2025 ([[blog-2025-12-19-year-in-review-2025]] §1).

## What he says
Before 2025 the production recipe was pretraining, supervised finetuning and RLHF ([[blog-2025-12-19-year-in-review-2025]] §1). Under RLVR, models develop strategies that look like reasoning, because they must find what works for them through optimisation rather than imitate traces ([[blog-2025-12-19-year-in-review-2025]] §1).

Unlike the short SFT and RLHF stages, RLVR allows long optimisation against non-gameable rewards, and it took compute that labs had meant for pretraining ([[blog-2025-12-19-year-in-review-2025]] §1). It also added a new knob, test-time compute, scaled by letting models think longer ([[blog-2025-12-19-year-in-review-2025]] §1). He names o1 as the first RLVR model and o3 as the point where the difference became obvious ([[blog-2025-12-19-year-in-review-2025]] §1).

**RL on practice problems (Deep Dive, 2025-02-05).** In this lecture he does not use the term RLVR; he calls the third major stage reinforcement learning, still under post-training, and likens it to practice problems with a final answer but no worked solution ([[youtube-2025-02-05-deep-dive-into-llms]] @2:09:57, @2:13:19, @2:13:53). The procedure: sample many solutions per prompt, up to thousands or more, find those that reach the correct answer and train on them, across tens of thousands of prompts ([[youtube-2025-02-05-deep-dive-into-llms]] @2:20:28, @2:21:34, @2:23:13, @2:24:20). He calls it basically a guess and check, with SFT still useful as an initialisation near correct solutions ([[youtube-2025-02-05-deep-dive-into-llms]] @2:25:25, @2:25:58). In verifiable domains a candidate is scored against a concrete answer, by checking a boxed answer or with an LLM judge, with no humans in the loop ([[youtube-2025-02-05-deep-dive-into-llms]] @2:48:14, @2:48:47).

The high-level idea is simple but the details are hard; companies experimented internally without talking publicly, which he says is why the DeepSeek-R1 paper was such a big deal ([[youtube-2025-02-05-deep-dive-into-llms]] @2:28:11, @2:28:46, @2:29:18). In that paper, as he reads it, accuracy climbs with training steps and the average response grows longer ([[youtube-2025-02-05-deep-dive-into-llms]] @2:29:50, @2:30:24). That o1, o3-mini and similar ChatGPT models were trained with RL similar to R1's he reports from public statements by OpenAI employees; GPT-4o and the free tier, he says, are mostly SFT models ([[youtube-2025-02-05-deep-dive-into-llms]] @2:37:07, @2:37:40). OpenAI shows summaries rather than raw chains of thought, he thinks partly over the risk of distillation ([[youtube-2025-02-05-deep-dive-into-llms]] @2:38:14, @2:38:46). He judges OpenAI's top paid models and DeepSeek-R1 roughly on par, with evaluation hard to read ([[youtube-2025-02-05-deep-dive-into-llms]] @2:38:46, @2:39:19). As of 2025-02-05 Google offered an experimental thinking model and Anthropic did not yet ([[youtube-2025-02-05-deep-dive-into-llms]] @2:41:02, @2:41:35).

Frontier research, he says, is building large, diverse prompt distributions, game environments for every domain of knowledge ([[youtube-2025-02-05-deep-dive-into-llms]] @2:47:40). Whether thinking learned in verifiable domains transfers to unverifiable ones is unknown in the field, and these models will mostly shine in verifiable domains like math and code ([[youtube-2025-02-05-deep-dive-into-llms]] @3:28:45, @3:29:18, @3:29:50). His claim that models discover their own ways of thinking this way is [[rl-lets-models-discover-their-own-thinking-strategies]] ([[youtube-2025-02-05-deep-dive-into-llms]] @2:32:04). **Note:** the 2025-02-05 lecture and the 2025-12-19 review describe the same stage in different words; the dates are given, not an order of discovery ([[youtube-2025-02-05-deep-dive-into-llms]] @2:13:19; [[blog-2025-12-19-year-in-review-2025]] §1).

**GRPO on GSM8K (nanochat launch post, 2025-10-13).** He does not use the term RLVR in this post. Of nanochat's datasets GSM8K has a clear, objective reward, the correct answer, so the optional RL stage interleaves sampling and training to hill-climb it ([[github-2025-10-13-nanochat-discussion-introducing]] §Reinforcement Learning (RL)). His GRPO is highly simplified: no trust region (no reference model or KL), on-policy (no PPO ratios or clipping), token-level normalisation and advantage as reward minus the mean, closer to REINFORCE while keeping the group-relative advantage ([[github-2025-10-13-nanochat-discussion-introducing]] §Reinforcement Learning (RL)). Reward, pass@1 and pass@8 rise over the default run of about 1.5 hours (measured), and pass@8 well above pass@1 suggests more to gain from more RL; he says gains are larger on bigger models and that he ran up to d30, without giving numbers ([[github-2025-10-13-nanochat-discussion-introducing]] §Reinforcement Learning (RL)). It is off by default because it is not well tuned, gives a GSM-specific model and there is no full general RLHF; why it runs so long is [[rl-sucks-supervision-bits-through-a-straw]] ([[github-2025-10-13-nanochat-discussion-introducing]] §Reinforcement Learning (RL)).

## Claims
- [[rl-lets-models-discover-their-own-thinking-strategies]]
- [[rl-sucks-supervision-bits-through-a-straw]] — why the RL stage runs long

## Related
- [[llm-self-improvement]] — the AlphaGo comparison he draws
- [[system-1-and-system-2-thinking]] — thinking models and longer responses
- [[jagged-intelligence]] — RLVR makes capability spike near verifiable domains
