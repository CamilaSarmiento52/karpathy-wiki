# Digest: Digital hygiene
- raw: raw/blog/digital-hygiene.md · published: 2025-03-17 · medium: blog · words: 1985
- source slug: blog-2025-03-17-digital-hygiene

## Source page
```
---
type: source
raw_path: raw/blog/digital-hygiene.md
published: 2025-03-17
medium: blog
summary: "A guide to the basic privacy and security practices he follows in day-to-day computing, from a password manager and hardware security keys to per-merchant cards, a virtual mail address and a network monitor."
url: https://karpathy.bearblog.dev/digital-hygiene/
title: Digital hygiene
---
# Digital hygiene
Raw: [[raw/blog/digital-hygiene]] · Original: https://karpathy.bearblog.dev/digital-hygiene/

The post has no headings; each tip is a paragraph that opens with a bold-style label. Citations use `§intro (<label>)`, e.g. `§intro (Hardware security key)`; the paragraph after the tips is `§intro (closing)`.

## Summary
He opens with the internet's fraud apparatus: tech companies build profiles of you to monetise or sell to data brokers, and breaches feed your data into an underground industry of phishing, ransomware and identity theft (§intro). The guide lists the basic practices he follows, most basic first: a password manager with unique passwords, two or three hardware security keys as a second factor instead of SMS, biometrics, random answers to security questions, and disk encryption (§intro (Password manager), (Hardware security key), (Biometrics), (Security questions), (Disk encryption)). He tells readers to avoid "smart" devices, and names the services he uses for messaging, browsing, search, per-merchant credit cards, a virtual mail address, email, VPN, DNS-level blocking and network monitoring (§intro (Internet of Things) through (Network monitor)). He advises keeping personal services off work computers (§intro (Work-life separation)). He says he wants products that leak only the necessary information and prefers paying for software so that incentives are aligned and he is the customer (§intro (Search engine), (closing)). He ends with what he has not yet done, such as still using Gmail and X for convenience (§intro (What's not on the list)).

## Key points
- The fraud apparatus, smart devices, and paying to be the customer → [[user-hostile-technology]]
- The practices he follows, in his order → [[digital-hygiene-checklist]]
- Hardware security keys, not phone numbers, as the second factor → [[use-hardware-security-keys-not-sms-as-a-second-factor]]
- He pays for services because he prefers to be the customer, not the product → [[he-prefers-to-pay-and-be-the-customer]]

## Fed pages
- [[user-hostile-technology]]
- [[digital-hygiene-checklist]]
- [[use-hardware-security-keys-not-sms-as-a-second-factor]]
- [[he-prefers-to-pay-and-be-the-customer]]
```

## Candidates
### topic: user-hostile-technology
- existing: no (new; shared with `blog-2024-09-08-i-love-calculator`)
- aliases: [digital hygiene, digital privacy, privacy and security, internet of shit, dependency footprint, the calculator ideal]
- recurrence with the calculator post, in his words: the same CO2 monitor anecdote (here: bought "in my younger and naive years", from China, it wanted to know everything about him and his precise location before reporting CO2; calculator post: demanded an account, an app and precise location) (§intro (Internet of Things)); the same @internetofshit link (§intro (Internet of Things)); the same preference for paying/owning over being monetised (§intro (Search engine), (closing)).
- statements (this source):
  - He describes a fraud apparatus: tech companies are incentivised to build comprehensive profiles of you to monetise for advertising or sell to data brokers, who enrich, de-anonymise and resell them (§intro)
  - Regular data breaches collect your information into dark-web archives that feed an underground industry of hacks, phishing, ransomware, card fraud and identity theft (§intro)
  - He calls smart devices incredibly insecure internet-connected computers that gather data, get hacked often and send data back for analytics, and says they should be avoided (§intro (Internet of Things))
  - He wants a secure digital life with products that leak only the necessary information, and wishes to pay for software so incentives are aligned and he is the customer (§intro (closing))
  - He says this is not trivial but can be approached with determination and discipline (§intro (closing))
  - He trades sovereignty for convenience in places: he still mostly uses Gmail/GSuite and X (§intro (What's not on the list))

### method: digital-hygiene-checklist
- existing: no
- aliases: [digital hygiene tips, privacy and security checklist]
- he follows these himself ("I use and like…" throughout); the post orders them "starting with the most basic to a bit more niche" (§intro)
- steps (short imperatives, his order):
  1. Use a password manager with a unique password per site
  2. Guard critical accounts with 2–3 hardware security keys
  3. Use biometrics where available
  4. Answer security questions with random strings
  5. Turn on disk encryption
  6. Avoid smart devices
  7. Message on Signal with disappearing messages
  8. Use a privacy-first browser and search engine
  9. Mint a card per merchant
  10. Give merchants a virtual mail address
  11. Never click email links; block remote images
  12. Turn on a VPN selectively
  13. Block ads and trackers at the DNS level
  14. Watch which apps call home
  15. Keep personal accounts off work computers
- statements:
  - Password manager: mint new, unique, hard passwords for every service, with a browser extension to autofill; he uses 1Password; this stops passwords being guessed or one leak opening many doors, and makes the manager the thing to secure (§intro (Password manager))
  - Hardware key: secure the most critical services (e.g. Google, 1Password) with a second factor; he uses YubiKey; set up 2–3 keys stored in different places to avoid lockout; prefer U2F, fall back on TOTP stored on the YubiKey (§intro (Hardware security key))
  - Biometrics: on iOS he recommends FaceID basically everywhere, e.g. for the 1Password app (§intro (Biometrics))
  - Security questions are effectively passwords that are easy to research; treat them as passwords, generate random answers and store them in the password manager (§intro (Security questions))
  - Disk encryption (FileVault on Macs) so a stolen computer's disk cannot be read (§intro (Disk encryption))
  - Messaging: Signal instead of text messages, because it is end-to-end encrypted and does not store metadata like many other apps; turn on disappearing messages (e.g. 90 days), which he sees as a vulnerability with no significant upside otherwise (§intro (Messaging))
  - Browser: Brave, Chromium-based so Chrome extensions work, without Google seeing your digital life (§intro (Browser))
  - Search: Brave Search, with its own index; he says DuckDuckGo is basically a skin for Bing; he pays $3/mo for Brave Premium; about 95% of his queries are simple website lookups; prepend "!g" to fall back to Google (§intro (Search engine))
  - Credit cards: one card per merchant via privacy.com, with per-card limits and random name/address in billing details (§intro (Credit cards))
  - Address: a virtual mail service that scans your mail; he uses Earth Class Mail, is a bit embarrassed by it, and is looking to switch to Virtual Post Mail (§intro (Address))
  - Email: he still uses Gmail and partly Proton Mail; never click links in emails since sender addresses are easy to spoof, navigate to the service yourself; disable image loading because embedded images track opens and hide scam content (§intro (Email))
  - VPN: Mullvad, off by default, on for services he trusts less (§intro (VPN))
  - DNS blocker: NextDNS; pi-hole as the physical alternative for tinkerers (§intro (DNS-based blocker))
  - Network monitor: Little Snitch on his MacBook, to see which apps call home; an app that communicates too much is suspect (§intro (Network monitor))
  - Work-life separation: avoid personal services on work computers, which likely log activity extensively (§intro (Work-life separation))
  - Not yet done: a VoIP burner phone service and unique email addresses per service, both of which he says he is interested in (§intro (What's not on the list))
- relation to existing pages: none. ([[llm-security]] is about attacks on LLMs; this post never mentions LLMs. No link.)

### claim: use-hardware-security-keys-not-sms-as-a-second-factor
- existing: no
- title: "Secure critical accounts with hardware security keys, not a phone number"
- confidence: stated
- quote: "Therefore, purchase and set up hardware security keys - the industrial strength protection standard." (§intro (Hardware security key))
- statements:
  - The most common second factor, a phone number with an SMS pin, is much better than none but known to be extremely insecure because of SIM swap attacks; he says many of his friends have been victims (§intro (Hardware security key))
  - Keys keep the private key in the device's secure element, never on a general-purpose computer like a laptop; he says you should not trust general-purpose computing devices (§intro (Hardware security key))
  - He estimates your risk of being compromised drops by about 1000X, and strongly recommends 2–3 YubiKeys (§intro (Hardware security key))
- relation to existing claims: none.

### claim: he-prefers-to-pay-and-be-the-customer
- existing: no (shared with `blog-2024-09-08-i-love-calculator`; this post is the primary, direct statement)
- title: "He prefers to pay for products and be the customer, not the product"
- confidence: stated
- quote: "I prefer to be the customer, not the product in my digital life" (§intro (Search engine))
- statements:
  - He pays $3/mo for Brave Premium, as with all services on his list, because he prefers to be the customer (§intro (Search engine))
  - He wishes to pay for the software he uses so that incentives are aligned and he is the customer (§intro (closing))
- relation to existing claims: none in the wiki. The calculator post `supports` it within this batch ("You paid for it and now it is yours."); same page, two sources.

## Quotes
- "Your risk of getting pwned has just decreased by about 1000X." (§intro (Hardware security key))
- "Therefore, purchase and set up hardware security keys - the industrial strength protection standard." (§intro (Hardware security key))
- "you should not trust general purpose computing devices" (§intro (Hardware security key))
- "the use of a phone number is known to be extremely insecure" (§intro (Hardware security key))
- "Always ensure that your computers use disk encryption." (§intro (Disk encryption))
- "I prefer to be the customer, not the product in my digital life" (§intro (Search engine))
- "Never click on any link inside any email you receive." (§intro (Email))
- "Any app that communicates too much is sus" (§intro (Network monitor))
- "I just want to live a secure digital life" (§intro (closing))
- "I wish to pay for the software I use so that incentives are aligned" (§intro (closing))
- "trading off sovereignty for convenience" (§intro (What's not on the list))
- "The journey continues." (§intro (What's not on the list))

## Notes for merge
- Locations: the raw has no markdown headings; the tip labels ("Password manager.", "Hardware security key.", …) are inline paragraph openers. `§intro (<label>)` follows the convention used for the llm.c Discussions. Labels: Password manager, Hardware security key, Biometrics, Security questions, Disk encryption, Internet of Things, Messaging, Browser, Search engine, Credit cards, Address, Email, VPN, DNS-based blocker, Network monitor, Work-life separation; then an unlabelled closing paragraph, then "Finally, what's not on the list."
- Product names are his choices as of 2025-03-17. Write them as "he uses/recommends", not as the wiki's endorsement.
- "Do not be a noob and mint new, unique, hard passwords" literally reads as "do not … mint"; context clearly means "don't be a noob: mint unique passwords". Paraphrase, do not quote.
- "about 1000X" is his rough figure; keep "about".
- Raw typos to leave out of quotes: "maidan name", "much strong commitments", "for it be sold" (the last is in the calculator post).
- The CO2 monitor here is "from China" and bought "in my younger and naive years"; the calculator post adds the "thousands of positive reviews" and the account/app demand. Same device presumably, but he does not say so; write "a CO2 monitor" in each post's own terms.
- The DuckDuckGo/Microsoft remark is his characterisation backed by a linked article; attribute it.
