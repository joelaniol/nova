# `nova.tab_new`

Creates a new browser tab with optional immediate navigation, private (incognito) browsing isolation, and automatic lease claiming.

---

## 1. Overview

`nova.tab_new` instantiates a fresh browser tab inside Nova AI Workspace. It supports opening URLs immediately, selecting the host sandbox, spawning ephemeral private sessions that leave zero disk footprints, and claiming the tab in a single atomic operation.

* **Capability Bundle:** `browser_automation`
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

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`url`** | `string` | No | `"about:blank"`| Initial URL to navigate to immediately upon creation. |
| **`private`** | `boolean` | No | `false` | When `true`, opens an ephemeral private browsing tab with a clean session. |
| **`isolate`** | `boolean` | No | `false` | When `true`, forces a distinct, isolated container partition. |
| **`sandbox`** | `string` | No | `null` | Target sandbox identifier (e.g. `"A"`, `"B"`). Defaults to active sandbox. |
| **`claim`** | `boolean` | No | `false` | Immediately claim exclusive write lease for calling agent. |
| **`activate`** | `boolean` | No | `true` | Bring the new tab into foreground focus. |
| **`waitForLoad`** | `boolean` | No | `false` | Block until document load completes. |
| **`waitForSettlement`** | `boolean` | No | `false` | Block until SPA DOM quietness and network idle. |
| **`outputDetail`** | `string` | No | `"full"` | `"minimal"`, `"compact"`, or `"full"`. |
| **`agentId`** | `string` | No | `"default"` | Identity of the calling agent. |

---

## 4. Example Calls

### Creating an Ephemeral Private Tab for Scraping
```json
{
  "name": "nova.tab_new",
  "arguments": {
    "url": "https://example.com/pricing",
    "private": true,
    "claim": true,
    "waitForLoad": true,
    "outputDetail": "minimal"
  }
}
```

### Sample Response
```json
{
  "targetId": "tab-5",
  "url": "https://example.com/pricing",
  "private": true,
  "claimed": true,
  "claimOwner": "research-agent-1",
  "leaseRemainingMs": 300000,
  "status": "ok"
}
```

---

## 5. Best Practices & Common Traps

* **One Call Instead of Two:** Always pass `url` directly to `nova.tab_new` instead of calling `tab_new` followed by `navigate`.
* **Close Private Tabs Promptly:** Since private tabs live in memory, close them via `nova.tab_close` as soon as your extraction or audit is complete to release system memory.

---

## See Also

* [`nova.tab_close`](nova-tab-close.md) — Close a tab.
* [`nova.tab_claim`](nova-tab-claim.md) — Manage tab leases.
* [`nova.navigate`](nova-navigate.md) — Navigate an existing tab.
* [Core Feature: Multi-Sandbox Isolation](../../../core-features/sandbox-isolation.md)
