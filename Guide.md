

```markdown
# Tor-Resources-Hub

This repository serves as a centralized directory for verified `.onion` addresses and essential guides related to the Tor Hidden Service network. 

## 🌐 What You Will Find
- **Verified Search Engines**: Direct links to active instances of Ahmia, DuckDuckGo (Darknet), Torch, and Chive.
- **Market Directories**: Catalogs of historically significant marketplaces with their latest known entry points.
- **Safety Guidelines**: Best practices for verifying addresses, using PGP encryption, and securing transactions via escrow.

## ⚠️ Note on Volatility
Since servers in the Tor network migrate frequently (e.g., from `v2.onion` to `v3.onion`) to evade censorship, this repo acts as a checkpoint list to cross-reference against official surface-web counterparts before visiting any hidden service. Always verify URLs before transacting sensitive data.

---
*Sources are dynamically managed; check the interface or documentation for updates.*
```

### `guide.md` (Separate File)

**How to Access .onion Sites Safely**

1.  **Install Tor Browser**: Ensure you have the latest version of [Tor Browser](https://www.torproject.org/) installed on your device. Standard browsers cannot access `.onion` links directly.
2.  **Verify Addresses**: Because `.onion` addresses change often, always compare them with their surface web counterpart (e.g., if a site is at `ahmia.fi`, check their current `.onion` address there). Look out for subtle typos like extra letters that indicate phishing sites.
3.  **Use HTTPS Inside Tor**: Even within the Darknet, prefer connections marked with "HTTPS" or a lock icon to ensure end-to-end encryption between you and the relay server.
4.  **Secure Transactions**: For markets, look for services supporting Multi-Signature (Multi-Sig) escrow and hardware-based 2FA (like YubiKey) rather than SMS verification, which can be intercepted on unstable networks.

**Common URL Structure**
A typical hidden service link looks like this:
```text
httpssso4e2z5p6s7y.onion[:PORT][/PATH]
```
- The part before `.onion` is a Base64-encoded public key derived from the service's private key. If this changes, the entire address must change.
