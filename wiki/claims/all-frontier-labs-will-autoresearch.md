---
type: claim
stated_on: 2026-03-09
confidence: stated
sources: ["[[x-2026-03-09-autoresearch-tuning-nanochat]]", "[[talk-2026-03-20-skill-issue]]"]
topic: "[[llm-self-improvement]]"
---
# All LLM frontier labs will do autoresearch, which he calls the final boss battle
> "All LLM frontier labs will do this." — [[x-2026-03-09-autoresearch-tuning-nanochat]] #1

## Context
He makes the prediction right after reporting his first autoresearch round on nanochat; see [[autoresearch-found-real-improvements-to-nanochat]] ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1). He calls it "the final boss battle" and grants it is a lot more complex at scale, since there is not a single `train.py` to tune, but says doing it is "just engineering" and it is going to work ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1). His picture is a swarm of agents that collaborate to tune smaller models, with the most promising ideas promoted to increasingly larger scales and humans optionally contributing on the edges ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1). More generally, he says any metric that is reasonably efficient to evaluate, or that has more efficient proxies such as training a smaller network, "can be autoresearched by an agent swarm", and suggests readers ask whether their problem is in that bucket ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1).

**In the Skill Issue interview (2026-03-20).** He says training GPT-2-size models is for him a little playground, and what he is fundamentally interested in is recursive self-improvement, the extent to which LLMs can improve LLMs; all the frontier labs, he says, "they're all trying to recursively self-improve roughly speaking" ([[talk-2026-03-20-skill-issue]] @17:32, @18:04). With GPU clusters of tens of thousands, it is easy to imagine them automating exploration on smaller models and extrapolating with scaling laws, and he says that is probably what they are working on ([[talk-2026-03-20-skill-issue]] @19:08, @19:40). He says lab researchers are actively automating themselves away, and recalls telling people at OpenAI that if they succeeded they would all be out of a job ([[talk-2026-03-20-skill-issue]] @43:40, @44:12). He also imagines an untrusted swarm of agents on the internet contributing commits that trusted workers verify, cheap to check but expensive to find, like Folding@home, and says that "who knows" it might even run circles around the frontier labs ([[talk-2026-03-20-skill-issue]] @33:53, @34:57, @35:28, @36:01).

## Related claims
- None set. **Note:** the post gives no horizon; "it's going to work" is not dated, so it is not set against [[there-is-a-massive-gap-between-demo-and-product]] ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1).
