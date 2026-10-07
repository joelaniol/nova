# `nova.tab_new`

Creates a new browser tab with optional immediate navigation, private (incognito) browsing isolation, and automatic lease claiming.

---

## 1. Overview

`nova.tab_new` instantiates a fresh browser tab inside Nova AI Workspace. It supports opening URLs immediately, selecting the host sandbox, spawning ephemeral private sessions that leave zero disk footprints, and claiming the tab in a single atomic operation.

* **Target Scope:** Creates a new target and returns its `targetId`.
* **Atomicity:** Combines creation, sandbox routing, navigation, and claiming into one call.

---

## 2. Key Capabilities & Features

### A. Ephemeral Private Tabs (`private: true`)
When researching paywalled sites, public landing pages, or testing unauthenticated flows:
* Passing `private: true` opens an in-memory incognito tab with a completely empty cookie jar.
* All cookies, cache, and session tokens are permanently discarded the moment the tab is closed.
* **Never log out of existing tabs:** Destroying the user's live session to inspect a logged-out view is forbidden; use `private: true` instead.

### B. Sandbox Placement (`sandbox`)
Specify which sandbox profile the tab should run in (e.g. `sandbox: "B"`).
* If omitted, the new tab inherits the currently active sandbox context.
* Cookies and storage are partitioned according to the designated sandbox.

### C. Atomic Claiming (`claim: true`)
By passing `claim: true`, Nova assigns the new tab's write lease directly to your `agentId` upon creation, eliminating race conditions with other agents.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `url` | `string` | No | — | — | Optional absolute initial URL. Empty/omitted => New Tab page. Browser targets support allowed schemes such as https:// and trusted local file:// review pages. |
| `activate` | `boolean` | No | `true` | — | If true (default), switch to the new tab immediately. |
| `waitForLoad` | `boolean` | No | `false` | — | If true and url is provided, wait for page load before returning. |
| `waitForLoadTimeoutMs` | `integer` | No | `10000` | 0–30000 | Max ms to wait for load (0-30000). Only used when waitForLoad=true. |
| `waitForSettlement` | `boolean` | No | `false` | — | If true, wait for SPA DOM settlement after readyState=complete. Implies waitForLoad=true. |
| `settlementTimeoutMs` | `integer` | No | `5000` | 1000–15000 | Max ms to wait for settlement (1000-15000). Only used when waitForSettlement=true. |
| `includeScreenshot` | `boolean` | No | `false` | — | If true and load completes, include a screenshot in the response. Screenshot delivery is an optional sidecar: if capture fails, this result stays authoritative and structuredContent.screenshotStatus/screenshotReasonCode/screenshotRetryable/screenshotError describe the capture-only failure - do not repeat the action to get the image. |
| `screenshotMaxWidth` | `integer` | No | — | — | Max screenshot width in pixels. |
| `screenshotMaxHeight` | `integer` | No | — | — | Max screenshot height in pixels. |
| `screenshotFormat` | `string` | No | `"png"` | `png`, `jpeg`, `auto` | Screenshot format. Use 'auto' to fall back to the tool-intent default. |
| `screenshotQuality` | `integer` | No | `80` | 1–100 | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `outputDetail` | `string` | No | `"full"` | `full`, `compact`, `minimal` | Response verbosity. 'full' (default) is the unchanged payload. 'compact' drops the advisory blocks you did not ask for (pks/pksMeta, discoverySignals, routingHint, taskDiscoveryWarning, byte accounting) and keeps everything you did - state, screenshot, settlement. 'minimal' is the lean envelope: core contract (ok/status/reasonCode/stage/retryable), the navigation proof (url/requestedUrl/loadCompleted/navigationFailed/webErrorStatus/settlement), target and page info, claim/private state, screenshot sidecar status, and the never-suppressible safety warnings. No setting can hide a warning. |
| `pksInclude` | `string` | No | `"auto"` | `auto`, `off`, `summary`, `full` | PKS payload detail level in structuredContent.pks. Default is server setting (initial: auto). |
| `sandbox` | `string` | No | — | — | Open the tab inside this sandbox (its letter id, e.g. 'A'), so it shares that sandbox's cookies and session — the way a link that opens a new window behaves inside a sandbox. Use it to continue a flow that belongs to a logged-in sandbox (verification, sign-in, checkout, account settings) instead of landing in the shared browser-tab profile where that session does not exist. Omit for an ordinary browser tab. Mutually exclusive with private. The tab reports isSandboxTab=true and its sandboxId in nova.tabs. |
| `private` | `boolean` | No | `false` | — | Open an ephemeral private (incognito) tab: starts logged out with an empty cookie jar, and keeps nothing after the tab closes — no browsing history, no download history, no saved password prompt, no new page-knowledge or notes. Reading existing knowledge still works. All private tabs share one session by default, like a single incognito window; pass isolate=true for a separate one. Local diagnostic logs still record tool calls. |
| `isolate` | `boolean` | No | `false` | — | Only valid with private=true (otherwise -32602). Gives this tab its own private session instead of the shared one, so two agents can hold two independent logged-out contexts at the same time. The session and its data are discarded when the last tab using it closes. |
| `claim` | `object` | No | — | — | Optional auto-claim. When present, the server claims the new tab immediately after creation (equivalent to a separate nova.tab_claim call). Result appears in structuredContent.claim with tri-state: claimed/failed/unknown. Success responses stay canonical on leaseMs/leaseRemainingMs and also mirror ttlMs/ttlRemainingMs for round-trip claim helpers. Claim failure is non-fatal — the tab is still created. |
| `claim.agentId` | `string` | No | `"default"` | — | Agent identifier for the claim. Optional — if omitted, nova.tab_new reuses the top-level agentId when present and otherwise falls back to 'default'. Recommended: pass explicitly for non-default ownership. |
| `claim.ttlMs` | `integer` | No | `120000` | 5000–1800000 | Lease duration in ms. Defaults to 120s. Must be between 5s and 30min; out-of-range values fail with -32602 before the tab is created. |

**`_meta.intent` is required for certain arguments.** Passing a short reason in `_meta.intent` is always safe; a rejected call names the argument that made it required.

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Creating an Ephemeral Private Tab for Scraping
```json
{
  "name": "nova.tab_new",
  "arguments": {
    "url": "https://example.com/pricing",
    "private": true,
    "claim": {},
    "waitForLoad": true
  }
}
```

`claim` is an object, not a boolean — pass `{}` to auto-claim with default settings, or `{"agentId": "...", "ttlMs": ...}` to be explicit.

### Sample Response (abbreviated)
```json
{
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "targetId": "tab-5",
    "tabId": "tab-5",
    "isPrivate": true,
    "privateSessionId": "default",
    "activated": true,
    "created": true,
    "url": "https://example.com/pricing",
    "pageUrl": "https://example.com/pricing",
    "claim": {
      "requested": true,
      "state": "claimed",
      "resolvedAgentId": "research-agent-1",
      "leaseMs": 120000,
      "leaseRemainingMs": 120000
    }
  }
}
```
The full payload also carries navigation, settlement, PKS and screenshot-sidecar fields; this is a trimmed excerpt.

---

## 5. Best Practices & Common Traps

* **One Call Instead of Two:** Always pass `url` directly to `nova.tab_new` instead of calling `tab_new` followed by `navigate`.
* **Close Private Tabs Promptly:** Since private tabs live in memory, close them via `nova.tab_close` as soon as your extraction or audit is complete to release system memory.

---

## See Also

* [`nova.tab_close`](nova-tab-close.md) — Close a tab.
* [`nova.tab_claim`](nova-tab-claim.md) — Manage tab leases.
* [`nova.navigate`](nova-navigate.md) — Navigate an existing tab.
* [Core Feature: Multi-Sandbox Isolation](../../../core-features/sandbox-isolation/README.md)
