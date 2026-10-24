---
type: method
steps:
  - Start a new chat when you switch topic
  - Keep information related to the task
  - Treat the tokens in the window as a precious resource
sources: ["[[youtube-2025-02-27-how-i-use-llms]]"]
aliases: [new chat, start a new chat when switching topics, keep the context clean, context window hygiene]
---
# Start a new chat per topic
His habit of wiping the context window whenever he changes subject, because a chat is one token sequence that both sides write into and "new chat" resets it ([[youtube-2025-02-27-how-i-use-llms]] @06:48, @07:21, @16:14).

## Steps
1. **New topic, new chat.** He encourages you to start a new chat whenever you switch topic ([[youtube-2025-02-27-how-i-use-llms]] @16:14, @17:53).
2. **Keep what is related.** If earlier information is actually related to the task you may want to keep it in the window ([[youtube-2025-02-27-how-i-use-llms]] @17:53).
3. **Tokens are expensive.** He says to think of the tokens in the context window as a precious resource: old tokens can distract the model and lower its accuracy, and more tokens make sampling the next one slightly slower and more expensive ([[youtube-2025-02-27-how-i-use-llms]] @16:46, @17:20).

## Seen in
- [[youtube-2025-02-27-how-i-use-llms]]
- [[tokenization]] — the chat as a token sequence
- [[parameters-are-vague-recollection-context-is-working-memory]] — **Note:** the context window as working memory, from his previous lecture
