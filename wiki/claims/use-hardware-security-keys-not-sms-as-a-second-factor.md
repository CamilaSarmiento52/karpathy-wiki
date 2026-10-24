---
type: claim
stated_on: 2025-03-17
confidence: stated
sources: ["[[blog-2025-03-17-digital-hygiene]]"]
topic: "[[user-hostile-technology]]"
---
# Secure critical accounts with hardware security keys, not a phone number
> "the use of a phone number is known to be extremely insecure" — [[blog-2025-03-17-digital-hygiene]] §intro (Hardware security key)

## Context
For the most critical services, his examples being Google and 1Password, he says to add a second factor ([[blog-2025-03-17-digital-hygiene]] §intro (Hardware security key)). The most common one, a phone number receiving an SMS pin, is much better than none but extremely insecure because of SIM swap attacks, which he says many of his friends have fallen victim to ([[blog-2025-03-17-digital-hygiene]] §intro (Hardware security key)). Hardware keys keep the private key in the device's secure element, never on a general-purpose computer such as a laptop, and he says you should not trust general-purpose computing devices ([[blog-2025-03-17-digital-hygiene]] §intro (Hardware security key)). He estimates the risk of being compromised drops by about 1000X, and strongly recommends two or three YubiKeys kept in different places so that losing one does not lock you out, preferring U2F and falling back on TOTP stored on the key ([[blog-2025-03-17-digital-hygiene]] §intro (Hardware security key)).

## Related claims
- **Note:** no relation to another claim; the step sits in [[digital-hygiene-checklist]] ([[blog-2025-03-17-digital-hygiene]] §intro (Hardware security key)).
