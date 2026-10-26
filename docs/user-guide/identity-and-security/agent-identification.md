# Agent Identification

> [!NOTE]
> Available from 1.0.0-alpha.21 (not published yet).

Some websites ask software that acts on your behalf to say so in every request. Amazon's conditions of use, for example, ask an AI agent shopping for you to add an agent name to the browser's identification (the *user agent*). Nova can do this for you, but only where you allow it and only when your agent asks for it.

---

## What changes, and what does not

* A tab only identifies as an agent when an agent asks for it **on that tab**; there is no global switch. Your other tabs keep their identification, with one exception for sites with a service worker (below).
* It only works on the sites listed in Settings. Amazon is listed from the start.
* The tab adds `Agent/NovaAIWorkspace` to the browser identification it already sends. Everything else the site sees about your browser stays the same, so the browser does not look like a different one.
* When the tab moves on to a site that is not on the list, Nova removes the addition again. The very first request of that page can still carry it.
* Requests the listed site makes to other sites (images, scripts, payment providers) carry the addition too.
* Many sites (Amazon among them) run a background helper, a *service worker*, that all their open tabs share. While one tab identifies as an agent, requests this helper makes for **your other tabs of the same site** carry the addition too, until that tab stops identifying or closes. Nova tells the agent which of your tabs this concerns, so it can move to a private tab with its own session; if you shop on the same site yourself at the same time, you can also ask it to work in a private tab from the start.
* While the tab identifies as an agent, the agent cannot use Nova's human-like mouse movement there. An announced agent should not pretend to be a person, and Amazon's conditions forbid exactly that.

> [!IMPORTANT]
> Announcing an agent is a choice with consequences. A site can treat an announced agent differently, for example limit it or ask for extra checks. Sites protected by bot walls (such as Cloudflare) may block tabs that say they are an agent, which is why Nova never does it on its own and never on sites you did not list.

---

## Where to change the list

Open **Menu → Settings → Privacy & Security → Privacy** and find the card **Agent identification**.

1. In **Allowed sites**, enter the sites separated by commas, for example `amazon.*, example.com`.
2. `amazon.*` stands for every Amazon country site (`amazon.de`, `amazon.com`, `amazon.co.uk`, ...). `example.com` covers that site and its subdomains.
3. Click outside the field. Nova tidies the list (lowercase, no `www.`, no duplicates) and saves it.

To stop identification everywhere, empty the field. Agents can read this list but cannot change it.

---

## Asking your agent

Tell your agent in your own words, for example:

> Shop on amazon.de for me. Identify this tab as an agent while you are on Amazon.

The agent turns it on for its tab once that tab shows a listed site. If the site is not listed, Nova refuses and tells the agent where you can add it. While a tab identifies as an agent, the device button in the address bar shows **Agent**. Click it to see why, to stop the identification for that tab, or to edit the list of sites.

A tab that simulates another device or browser (device emulation) cannot identify as an agent at the same time, and neither can a browser whose identity you changed under **Browser ID** in the same settings area: the addition is only ever made to the browser's own identification.

---

## Related Documentation

* **[Identity & Security](README.md)** — Overview of Nova's identity and security features.
* **[Website & Agent Permissions](permissions.md)** — What agents may do and when Nova asks you.
* **[Device emulation](../../core-features/device-emulation/README.md)** — Simulating phones, tablets and other browsers.

---

[Back to Identity & Security](README.md)
