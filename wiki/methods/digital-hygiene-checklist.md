---
type: method
steps:
  - Use a password manager with a unique password per site
  - Guard critical accounts with two or three hardware security keys
  - Use biometrics where available
  - Answer security questions with random strings
  - Turn on disk encryption
  - Avoid smart devices
  - Message on Signal with disappearing messages
  - Use a privacy-first browser and search engine
  - Mint a card per merchant
  - Give merchants a virtual mail address
  - Never click email links; block remote images
  - Turn on a VPN selectively
  - Block ads and trackers at the DNS level
  - Watch which apps call home
  - Keep personal accounts off work computers
sources: ["[[blog-2025-03-17-digital-hygiene]]"]
aliases: [digital hygiene, digital hygiene tips, privacy and security checklist]
---
# Digital hygiene checklist
The privacy and security practices he follows himself, listed from the most basic to the more niche; the product names are his choices as of 2025-03-17 ([[blog-2025-03-17-digital-hygiene]] §intro). He says a secure digital life is not trivial but can be approached with determination and discipline ([[blog-2025-03-17-digital-hygiene]] §intro (closing)).

## Steps
1. **Password manager.** Mint a new, unique, hard password for every service and autofill it with a browser extension; he uses 1Password ([[blog-2025-03-17-digital-hygiene]] §intro (Password manager)). This stops passwords being guessed or one leak opening many doors, and makes the manager the one thing to secure ([[blog-2025-03-17-digital-hygiene]] §intro (Password manager)).
2. **Hardware keys.** Secure the most critical services with two or three YubiKeys stored in different places; see [[use-hardware-security-keys-not-sms-as-a-second-factor]] ([[blog-2025-03-17-digital-hygiene]] §intro (Hardware security key)).
3. **Biometrics.** On iOS he recommends FaceID basically everywhere, for example to open the 1Password app ([[blog-2025-03-17-digital-hygiene]] §intro (Biometrics)).
4. **Security questions.** They are effectively passwords that are easy to research, so generate random answers and store them in the password manager ([[blog-2025-03-17-digital-hygiene]] §intro (Security questions)).
5. **Disk encryption.** Turn it on, FileVault on a Mac, so a stolen computer's disk cannot be read ([[blog-2025-03-17-digital-hygiene]] §intro (Disk encryption)).
6. **No smart devices.** He calls them insecure internet-connected computers that gather data, get hacked often and send data home for analytics ([[blog-2025-03-17-digital-hygiene]] §intro (Internet of Things)).
7. **Signal.** Use it instead of text messages because it is end-to-end encrypted and does not store metadata like many other apps, and turn on disappearing messages, for example after 90 days ([[blog-2025-03-17-digital-hygiene]] §intro (Messaging)).
8. **Browser and search.** He uses Brave, Chromium-based so Chrome extensions work, and Brave Search, which has its own index; he characterises DuckDuckGo as basically a skin for Bing, citing an article, and falls back to Google with "!g" ([[blog-2025-03-17-digital-hygiene]] §intro (Browser), §intro (Search engine)).
9. **A card per merchant.** He mints one card per merchant through privacy.com, with per-card limits and a random name and address in the billing details ([[blog-2025-03-17-digital-hygiene]] §intro (Credit cards)).
10. **Virtual mail address.** A virtual mail service scans your post; he uses Earth Class Mail and is looking to switch ([[blog-2025-03-17-digital-hygiene]] §intro (Address)).
11. **Email.** He never clicks links in emails, since sender addresses are easy to spoof, and navigates to the service himself; he disables image loading, since embedded images track opens and can hide scam content ([[blog-2025-03-17-digital-hygiene]] §intro (Email)).
12. **VPN.** Mullvad, off by default and on for services he trusts less ([[blog-2025-03-17-digital-hygiene]] §intro (VPN)).
13. **DNS blocker.** NextDNS, or a pi-hole for tinkerers ([[blog-2025-03-17-digital-hygiene]] §intro (DNS-based blocker)).
14. **Network monitor.** Little Snitch on his MacBook shows which apps call home; an app that communicates too much is suspect ([[blog-2025-03-17-digital-hygiene]] §intro (Network monitor)).
15. **Work-life separation.** Keep personal services off work computers, which likely log activity extensively ([[blog-2025-03-17-digital-hygiene]] §intro (Work-life separation)).

Not yet on his list: a VoIP burner phone service and a unique email address per service, both of which he says he is interested in ([[blog-2025-03-17-digital-hygiene]] §intro (What's not on the list)).

## Seen in
- [[blog-2025-03-17-digital-hygiene]]
- [[user-hostile-technology]] — what the checklist defends against
- [[he-prefers-to-pay-and-be-the-customer]]
