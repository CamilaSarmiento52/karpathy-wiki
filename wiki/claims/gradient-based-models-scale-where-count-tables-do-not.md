---
type: claim
stated_on: 2022-09-07
confidence: stated
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]"]
topic: "[[bigram-language-model]]"
---
# Gradient-based models scale to longer contexts where count tables do not
> "But the gradient-based approach is significantly more flexible." — [[youtube-2022-09-07-makemore-1-bigram]] @1:45:39

## Context
Counting works for bigrams only because the setup is so simple that probabilities can be estimated directly in a table ([[youtube-2022-09-07-makemore-1-bigram]] @1:45:39). The gain of the gradient approach is that it can be expanded and the neural net complexified with more previous characters ([[youtube-2022-09-07-makemore-1-bigram]] @1:45:39, @1:46:12). It is not obvious how to extend the counting approach to many input characters because the tables get too large for all combinations; he calls it a fundamentally unscalable approach ([[youtube-2022-09-07-makemore-1-bigram]] @1:46:46, @1:47:19). With the last 10 characters as input you cannot keep everything in a table, while the neural approach is more scalable and improvable ([[youtube-2022-09-07-makemore-1-bigram]] @1:47:19).

## Related claims
- In the next lecture he quantifies the table blow-up that motivates the MLP: 27 contexts for one character, 729 for two, about 20,000 for three, with too few counts per row, and then builds the gradient-trained model that takes three characters of context ([[youtube-2022-09-12-makemore-2-mlp]] @01:06, @01:40, @09:28).
