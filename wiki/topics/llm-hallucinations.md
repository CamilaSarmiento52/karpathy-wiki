---
type: topic
aliases: [Hallucinations, hallucination, LLM hallucinations, confabulation, "I don't know", model self-knowledge, self-knowledge, knowledge of self, model identity, "who built you", factuality, making stuff up, LLM psychology]
first_seen: 2025-02-05
last_updated: 2026-02-12
sources: ["[[youtube-2025-02-05-deep-dive-into-llms]]", "[[blog-2026-02-12-microgpt]]"]
related: ["[[jagged-intelligence]]", "[[llm-tool-use]]", "[[pretraining-and-finetuning]]"]
context: ["[[youtube-2025-06-19-software-is-changing]]"]
---
# LLM hallucinations
Hallucination, in his framing, is when an LLM fabricates information; he opens his section on "LLM psychology", the emergent cognitive effects of the training pipeline, with it ([[youtube-2025-02-05-deep-dive-into-llms]] @1:20:31).

## What he says
**Why it happens.** Training conversations answer questions of the form "who is X" confidently, because the labeler writing the answer knows the person or researches them, so at test time the model imitates that confident style and gives its statistically most likely guess rather than saying it doesn't know ([[youtube-2025-02-05-deep-dive-into-llms]] @1:21:36, @1:22:09, @1:22:42). He shows this with a name he made up: an old model, Falcon 7B, gives a different fabricated biography each time it is resampled, while a current ChatGPT says it does not know the person ([[youtube-2025-02-05-deep-dive-into-llms]] @1:23:15, @1:23:48, @1:25:29).

**Mitigation one: train on "I don't know".** He describes the procedure from Meta's Llama 3 paper, not his own: use an LLM to generate questions from training documents, interrogate the model several times, have an LLM judge compare its answers with the correct ones, and where it gets them wrong add training conversations whose correct answer is that it doesn't know ([[youtube-2025-02-05-deep-dive-into-llms]] @1:26:02, @1:27:39, @1:28:14, @1:29:20, @1:30:30, @1:31:03). He presumes some neuron in the network represents uncertainty, and those examples let the model wire it to saying it doesn't know; he calls this a large mitigation ([[youtube-2025-02-05-deep-dive-into-llms]] @1:26:33, @1:27:06, @1:31:37).

**Mitigation two: tools.** Letting the model search the web refreshes its working memory instead of relying on recollection ([[youtube-2025-02-05-deep-dive-into-llms]] @1:32:43, @1:33:17). How search works mechanically is on [[llm-tool-use]] ([[youtube-2025-02-05-deep-dive-into-llms]] @1:33:53).

**Still there.** He says hallucinations have gotten better over time and will keep improving, but models still hallucinate ([[youtube-2025-02-05-deep-dive-into-llms]] @3:08:39).

**Self-knowledge.** Asking a model what it is and who built it is, he says, a little nonsensical, since it has no persistent existence and restarts every conversation ([[youtube-2025-02-05-deep-dive-into-llms]] @1:41:37, @1:42:11). Falcon saying it was built by OpenAI is not evidence it trained on OpenAI data; more likely it is a hallucinated label picked up from internet text about ChatGPT ([[youtube-2025-02-05-deep-dive-into-llms]] @1:42:44, @1:43:55). Developers override identity with hardcoded conversations, OLMo's SFT mixture has 240 of them, or with a hidden system message; he calls both cooked up and bolted on ([[youtube-2025-02-05-deep-dive-into-llms]] @1:44:27, @1:44:59, @1:45:33, @1:46:07, @1:46:42).

**Note:** [[jagged-intelligence]] lists hallucination and missing self-knowledge among the deficits he names in the 2025-06-19 YC talk; this page is his account of the cause ([[youtube-2025-06-19-software-is-changing]] @16:04; [[youtube-2025-02-05-deep-dive-into-llms]] @1:20:31).

**Plausible, not true (microgpt, 2026-02-12).** The model samples tokens from a probability distribution; "It has no concept of truth", only what sequences are statistically plausible given the training data ([[blog-2026-02-12-microgpt]] §FAQ). He says microgpt "hallucinating" a name like "karia" is the same phenomenon as ChatGPT confidently stating a false fact: both are plausible-sounding completions that happen not to be real ([[blog-2026-02-12-microgpt]] §FAQ). **Note:** [[hallucinations-come-from-imitating-confident-answers]] explains why models answer confidently; this explains hallucination as plausible sampling; both can hold and no relation is set ([[blog-2026-02-12-microgpt]] §FAQ).

## Claims
- [[hallucinations-come-from-imitating-confident-answers]]
- [[parameters-are-vague-recollection-context-is-working-memory]] — why looking things up helps

## Related
- [[jagged-intelligence]] — hallucination as one of the holes
- [[llm-tool-use]] — search as the second mitigation
- [[pretraining-and-finetuning]] — the labeler conversations the confident style comes from
- [[chatgpt-answers-simulate-a-human-data-labeler]]
