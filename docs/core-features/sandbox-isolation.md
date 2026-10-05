# Multi-Sandbox Session Isolation

> [!NOTE]
> Sandboxes let you stay signed in to the same website with different accounts at the same time. Each sandbox has its own browser profile with its own cookies, storage and cache, so a login in one sandbox does not affect another.

---

## 1. A Concrete Example: Two Accounts, Side by Side

Open your work account in sandbox A and your personal account on the same website in sandbox B. Each website session uses a different browser profile, so signing out in A does not sign out B. Tabs within A share A's profile and can use the same login.

The separation concerns browser sessions. A Nova sandbox is not an operating-system virtual machine or a security boundary for running untrusted native programs. [Outrider](outrider-boundary.md) provides a separate boundary for native process failures; [AAG](aag.md) checks agent-action prerequisites.

## 2. Why Separate Sessions?

Many workflows need several identities side by side:

* **Personal vs. work:** two accounts of the same web app, open at the same time.
* **Testing roles:** checking a web app as administrator and as customer in parallel.

Tabs using the same browser profile share cookies and persistent site storage. On sites that support only one account per session, signing in to another account changes the session for those tabs.

---

## 3. How Sandboxes Are Stored

Each sandbox is a separate WebView2 browser profile. All profiles live under one shared WebView2 data folder inside the Nova profile folder:

```
%LOCALAPPDATA%\nova-cognitive\Nova\
  ├── settings.json                        # Sandbox list (name, color, start URL, ...)
  └── UserData\Shared\EBWebView\
        ├── WV2Profile_<sandbox-uid>\      # One profile per sandbox
        └── WV2Profile_<sandbox-uid>\
```

Installations upgraded from older versions may still use `%LOCALAPPDATA%\NovaBrowser\` as the profile folder.

Sandboxes are addressed by a short ID (`A`, `B`, `C`, ...) and also carry a persistent internal ID that names their profile folder. Up to 100 sandboxes can exist; at least one always remains.

For agents, resolving the intended account is a routing decision: a service or intent hint helps choose a sandbox, but does not prove that it is currently signed in to the desired account. Inspect the selected target's actual session before acting.

```mermaid
flowchart TD
    Nova["Nova AI Workspace - one browser process"]
    Nova --> A["Sandbox A - own profile"]
    Nova --> B["Sandbox B - own profile"]
    A --> SA["Cookies, localStorage, IndexedDB, cache"]
    B --> SB["Cookies, localStorage, IndexedDB, cache"]
```

---

## 4. What Is Separated — and What Is Not

**Separated per sandbox:**

* Cookies, `localStorage`, `sessionStorage`, IndexedDB, cache and other profile data.
* Signing in in sandbox A has no effect on sandbox B.
* Fingerprint protection can be overridden per sandbox (see [Fingerprint Protection & Browser Identity](fingerprint-and-identity.md)).

**Shared by all sandboxes:**

* **One browser process and one proxy.** All sandboxes and browser tabs run in the same WebView2 browser process, which takes its proxy from the global setting. A separate proxy per sandbox is currently not possible; sandboxes that were set to their own proxy are switched to follow the global one. See [Proxy Routing & Network](proxy-and-network.md).
* **WebRTC and DNS protection.** "Protect WebRTC local IP leaks" (off by default) applies to the whole browser. With a SOCKS5 proxy it also routes DNS lookups through the proxy; if several SOCKS5 proxies are configured, this DNS protection covers only one of them.
* **Browser identity.** The user-agent preset set with `nova.identity_set` applies to all tabs.

> [!IMPORTANT]
> Sandboxes separate sessions; they do not give each sandbox its own network identity. Sites can still see the same IP address and the same browser engine across sandboxes.

---

## 5. Persistence & Recovery

Each sandbox profile folder contains a small metadata file. At startup Nova reconciles these profile identities with the sandbox list in `settings.json`:

* If the configured list is empty, surviving profiles can restore the list.
* An individually missing sandbox can also be reattached when its profile survives, it was not deleted, its short ID is free and the sandbox limit permits it.
* Conflicting identities or a full sandbox list require the recovery dialog rather than automatic attachment.

Deletion markers prevent intentional deletions from being restored by accident. This recovery uses surviving local profile data; it is not a backup and cannot undo deletion of that data.

---

## 6. MCP Tooling for Sandbox Management

| Tool | Purpose |
| :--- | :--- |
| `nova.sandbox_context` | Metadata and context of a sandbox. |
| `nova.resolve_sandbox` | Picks the best matching sandbox for an intent key (e.g. `email.compose`), with optional service and account hints. |
| `nova.sandbox_create` / `nova.sandbox_update` | Creates or changes a sandbox (name, color, start URL, purpose, account label, aliases, preferred intents; `update` can also pause it). |
| `nova.sandbox_delete` | Removes a sandbox and its profile data (`confirm: true` required). |
| `nova.cookie_list` / `nova.cookie_set` / `nova.cookie_delete` | Cookies of the target tab's or sandbox's profile. |
| `nova.storage_inspect` | `localStorage` or `sessionStorage` of the target page. |

---

## Related Documentation

* **[Site Data & Privacy Management](site-data-management.md)** — Cookies, storage and cache clearing.
* **[Proxy Routing & Network](proxy-and-network.md)** — Proxy profiles and WebRTC leak protection.
* **[Fingerprint Protection & Browser Identity](fingerprint-and-identity.md)** — Fingerprint protection levels and browser identity presets.
