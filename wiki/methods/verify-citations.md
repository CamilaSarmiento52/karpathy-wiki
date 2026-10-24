---
type: method
steps:
  - Check facts against primary sources
  - Follow the citations to the pages
  - Treat reports as a first draft
  - Read the code it ran
  - Have it transcribe images to text first
sources: ["[[youtube-2025-02-27-how-i-use-llms]]"]
aliases: [check primary sources, treat it as a first draft, treat deep research reports as a first draft, scrutinize the code, transcribe before asking, LLM code tools need a user who can verify the code]
---
# Verify citations
How he checks what an LLM tells him, since even a direct answer is the model's vague recollection of the internet and he does not always fully trust what comes out ([[youtube-2025-02-27-how-i-use-llms]] @13:58, @15:06). Asking directly without tools is fine for him when the knowledge is common and not recent, as with the caffeine in an Americano, and he still checks ([[youtube-2025-02-27-how-i-use-llms]] @13:25, @13:58). **Note:** not the same as [[verify-against-a-reference-implementation]], which is about matching code outputs ([[youtube-2025-02-27-how-i-use-llms]] @13:58).

## Steps
1. **Primary sources.** He checked the caffeine figure against primary sources and a cold medicine's ingredients against the box ([[youtube-2025-02-27-how-i-use-llms]] @13:58, @15:06).
2. **Follow the citations.** Search answers come with citations you can visit to check for hallucinations ([[youtube-2025-02-27-how-i-use-llms]] @35:12). With deep research any part can be hallucinated, fabricated or misunderstood, so the citations matter, and he reads the papers to see whether the model understood them ([[youtube-2025-02-27-how-i-use-llms]] @48:26).
3. **First draft.** He says to treat a deep research report as a first draft and as papers to look at ([[youtube-2025-02-27-how-i-use-llms]] @48:26). His table of US LLM labs missed one lab and included others it should not have; he calls it hit and miss and does not fully trust the numbers ([[youtube-2025-02-27-how-i-use-llms]] @50:06, @50:39). Medical results he treats as a good first draft and something to talk over with a doctor ([[youtube-2025-02-27-how-i-use-llms]] @1:44:24, @1:44:58).
4. **Read the code.** He would always encourage you to scrutinize the code Advanced Data Analysis writes: in his example it silently filled in a value for a missing year and misreported an extrapolated number ([[youtube-2025-02-27-how-i-use-llms]] @1:05:46, @1:06:19, @1:06:53). He calls it like a very junior data analyst, and is hesitant to recommend it to people who cannot read and verify the code ([[youtube-2025-02-27-how-i-use-llms]] @1:06:19, @1:08:01, @1:08:33).
5. **Transcribe first.** For an image of, for example, a supplement's ingredient list or test results, he first asks for a transcription into text so he can check the model read the values correctly, then asks his questions ([[youtube-2025-02-27-how-i-use-llms]] @1:42:10, @1:43:50).

## Seen in
- [[youtube-2025-02-27-how-i-use-llms]]
- [[use-llms-as-tools-and-check-their-work]] — the stance this method carries out
- [[llm-hallucinations]] — why the checks are needed
- [[llm-tool-use]] — search, deep research and the interpreter
