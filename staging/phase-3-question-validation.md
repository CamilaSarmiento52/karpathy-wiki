# Phase 3 fresh-reader question and citation validation

Date: 2026-10-23. Scope: the compiled wiki available during this check.

## Method and limits

This check used a fresh isolated subagent, rather than a separate user-opened session. The subagent first read `CLAUDE.md`, `specs/phases/phase-3-compile-the-wiki/validation.md`, and `wiki/index.md`, then followed the relevant compiled topic, claim, artifact, and source pages. Answers below were formed only from compiled wiki content. Raw files were opened afterward solely to verify the selected citations; no uncompiled raw material was used to fill answer gaps. Wiki and raw files were read-only.

This report is deliberately outside `staging/verify/`: question-level citation spot checks must not count as whole-source batch verification.

## 1. How does he explain backpropagation, and what does he build to teach it?

He explains backpropagation as recursively applying the chain rule backward through an expression graph: the gradient arriving at each operation is multiplied by its local derivatives to obtain gradients for its inputs. The machinery applies to mathematical expressions generally, including neural networks ([[youtube-2022-08-16-micrograd]] @03:14, @04:51, @50:37).

To teach it, he starts from a blank notebook and rebuilds micrograd, a scalar autograd engine, then builds neurons, layers, and an MLP and trains a small neural net. The engine and neural-net library together are about 150 lines; the scalar implementation makes the mathematics explicit ([[youtube-2022-08-16-micrograd]] @00:00, @00:32, @05:24, @07:03, @07:35; source Summary @1:44:26, @1:52:43, @2:05:30).

Wiki route: `wiki/topics/backpropagation.md`, `wiki/artifacts/micrograd.md`, `wiki/claims/backpropagation-is-more-general-than-neural-networks.md`, and `wiki/sources/youtube-2022-08-16-micrograd.md`.

Citation verification:

| Citation | Raw passage | Supported paraphrase | Result |
|---|---|---|---|
| `youtube-2022-08-16-micrograd` @03:14 | [raw/youtube/VMj-3S1tku0.md:24](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/VMj-3S1tku0.md:24>) | Starting at the output, backprop goes backward through the expression graph and recursively uses the chain rule to obtain internal-node and input derivatives. | Correct |
| `youtube-2022-08-16-micrograd` @50:37 | [raw/youtube/VMj-3S1tku0.md:196](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/VMj-3S1tku0.md:196>) | Each operation supplies local derivatives, which multiply the derivative arriving from downstream; the process is recursive. | Correct |
| `youtube-2022-08-16-micrograd` @00:00–@00:32 | [raw/youtube/VMj-3S1tku0.md:12–14](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/VMj-3S1tku0.md:12>) | The lecture starts from a blank notebook and rebuilds micrograd step by step to expose neural-network training. | Correct |
| `youtube-2022-08-16-micrograd` @07:03–@07:35 | [raw/youtube/VMj-3S1tku0.md:38–40](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/VMj-3S1tku0.md:38>) | The roughly 100-line engine plus neuron/layer/MLP library is about 150 lines in total. | Correct |

Coverage: sufficient for this question. These selected citations are correct; this is not a full audit of every sentence in the linked pages.

## 2. How did his view of LLM agents change between 2023 and 2026?

Partial answer only: the compiled wiki does not establish his 2023 view of agents, and its only timeline is about vibe coding. It therefore cannot support a complete 2023-to-2026 account or establish a reversal of opinion.

The compiled dated evidence supports a narrower account. In June 2025 he cautions that agent progress will take a decade, using the long development of self-driving as an analogy, and says humans should remain in the loop ([[youtube-2025-06-19-software-is-changing]] @26:35, @27:09, @27:44). In December 2025 he calls Claude Code the first convincing agent demonstration, describing extended problem solving through repeated tool use and reasoning, and values its access to the developer's existing computer, environment, and context ([[blog-2025-12-19-year-in-review-2025]] §4). By April 2026 the compiled wiki documents his practical use of LLMs to build and maintain knowledge wikis and his provision of CLI tools for larger queries; that is an application of LLM tooling, not sufficient evidence of a changed overall agent forecast ([[x-2026-04-02-llm-knowledge-bases]] §Data ingest, §Extra tools).

Wiki route: `wiki/claims/this-is-the-decade-of-agents.md`, `wiki/claims/claude-code-is-the-first-convincing-llm-agent.md`, `wiki/topics/building-for-agents.md`, and `wiki/topics/llm-knowledge-bases.md`.

Citation verification:

| Citation | Raw passage | Supported paraphrase | Result |
|---|---|---|---|
| `youtube-2025-06-19-software-is-changing` @26:35–@27:44 | [raw/youtube/LCEmiRjPEtQ.md:108–112](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/LCEmiRjPEtQ.md:108>) | A perfect 2013 driving demo did not imply autonomy was finished; he expects a decade of agents and calls for human oversight. | Correct |
| `blog-2025-12-19-year-in-review-2025` §4 | [raw/blog/year-in-review-2025.md:60–62](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/blog/year-in-review-2025.md:60>) | Claude Code demonstrates an agent's reasoning/tool loop, with particular value in the local machine's existing environment and context. | Correct |
| `x-2026-04-02-llm-knowledge-bases` §Data ingest, §Extra tools | [raw/x/2039805659525644595.md:16–17,31–32](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/x/2039805659525644595.md:16>) | He has an LLM compile a linked markdown wiki and hands it a CLI search tool for larger queries. | Correct |

Coverage: incomplete. Citation correctness passes for the limited answer; the required 2023 baseline, agent-specific timeline, and supported longitudinal change account are missing from the compiled wiki. No uncompiled sources were consulted to supply them.

## 3. What does he say about tokenization being a source of LLM problems?

Partial answer only: the compiled wiki explains tokenization mechanics and tradeoffs, but does not compile the tokenizer lecture or related claims explaining tokenization as a source of LLM problems. It cannot answer that central premise from its current coverage.

What it does support is that tokenization maps text into integer sequences according to a vocabulary ([[youtube-2023-01-17-gpt-from-scratch]] @09:31). The compiled GPT lecture contrasts character and subword tokenization: vocabulary size trades off against sequence length, and he keeps a simple character tokenizer for teaching despite its long sequences ([[youtube-2023-01-17-gpt-from-scratch]] @11:43, @12:16). That is a supported tradeoff, not evidence for a broader list of tokenization-caused failures.

Wiki route: `wiki/topics/tokenization.md`, `wiki/sources/youtube-2023-01-17-gpt-from-scratch.md`, and `wiki/sources/github-2023-01-08-mingpt-readme.md`. The minGPT README's compiled BPE description adds implementation context, not the missing failure analysis.

Citation verification:

| Citation | Raw passage | Supported paraphrase | Result |
|---|---|---|---|
| `youtube-2023-01-17-gpt-from-scratch` @09:31 | [raw/youtube/kCc8FmEb1nY.md:46](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/kCc8FmEb1nY.md:46>) | Tokenizing means converting a text string into integers using a vocabulary; the lecture uses characters. | Correct |
| `youtube-2023-01-17-gpt-from-scratch` @11:43 | [raw/youtube/kCc8FmEb1nY.md:54](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/kCc8FmEb1nY.md:54>) | GPT-2 uses a much larger vocabulary, shortening the example's integer sequence; vocabulary and sequence length trade off. | Correct |
| `youtube-2023-01-17-gpt-from-scratch` @12:16 | [raw/youtube/kCc8FmEb1nY.md:56](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/kCc8FmEb1nY.md:56>) | He chooses a character tokenizer for simplicity and accepts long sequences, while subword encoding is common in practice. | Correct |

Coverage: incomplete. The checked mechanics citations are correct, but the requested explanation of tokenization-caused LLM problems is absent from the compiled wiki. No failure examples were inferred from general knowledge or uncompiled raw.

## 4. What does he recommend for pruning apple trees?

The wiki has nothing on this.

Negative-control verification: the index has no relevant topic or source, and a case-insensitive search for `apple|prun` over `wiki/` returned no matches. This is a statement about compiled-wiki coverage, not proof that he has never discussed pruning anywhere. There are no substantive answer citations to check; the two-citation requirement is inapplicable to a correctly refused negative control.

Coverage: expected negative-control behavior passes.

## Gate result

| Dimension | Result |
|---|---|
| Question 1 coverage | Sufficient |
| Question 2 coverage | Incomplete: missing 2023 baseline and agent timeline/change account |
| Question 3 coverage | Incomplete: missing tokenizer-problems lecture/claims |
| Question 4 negative control | Correctly says the wiki has nothing on this |
| Selected substantive citations checked against raw | All checked citations support the limited answers |
| Literal fresh user-opened session requirement | Not completed; isolated fresh subagent used instead |
| User clicks two citations per answer and confirms | Pending; automated raw checks do not substitute for user confirmation |
| Phase gate 3 → 4 | Not passed by this validation |

This report validates selected citations and exposes coverage gaps. It does not mark any source wholly verified, does not resolve other Phase 3 completion requirements, and does not satisfy the user's still-pending manual citation-click confirmation.
