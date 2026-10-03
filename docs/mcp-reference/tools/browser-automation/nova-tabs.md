# `nova.tabs`

Lists all open tabs, WebViews, and sandbox surfaces across the workspace with filtering, claim status, and ownership details.

---

## 1. Overview

`nova.tabs` gives AI agents visibility into all active browser surfaces in the running Nova AI Workspace instance. It allows agents to choose targets, inspect current page URLs, check multi-agent claim leases, and avoid operating in the user's personal tabs.

* **Capability Bundle:** `browser_automation`
* **Target Scope:** Global workspace inventory.
* **Token Optimization:** Supports `outputDetail: "minimal"` to return a lean inventory without bloating the LLM context.

---

## 2. Key Capabilities & Features

### A. Agent Isolation (`mine: true`)
When collaborating on a machine where a human user or other AI agents are active:
* Passing `mine: true` filters the returned list to only show tabs claimed or created by your `agentId`.
* This ensures you never accidentally close, navigate, or click inside a tab that the human operator is currently reading.

### B. Multi-Agent Lease Auditing
Each tab in the response reports:
* `claimed`: Whether a lease is active.
* `claimOwner`: The `agentId` currently holding the write lock.
* `leaseRemainingMs`: Milliseconds before the lease expires and becomes available for other agents.

### C. Output Formats
* **`minimal` (Recommended):** Returns only `targetId`, `title`, `url`, `active`, and `claimOwner`.
* **`full`:** Returns comprehensive metadata, WebErrorStatus, sandbox bindings, private browsing indicators, and process IDs.

---

## 3. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`outputDetail`** | `string` | No | `"full"` | `"minimal"`, `"compact"`, or `"full"`. Use `"minimal"` in automated loops to conserve tokens. |
| **`mine`** | `boolean` | No | `false` | When `true`, returns only tabs owned or claimed by `agentId`. |
| **`agentId`** | `string` | No | `"default"` | Identity of the calling agent for ownership resolution. |
| **`activeOnly`** | `boolean` | No | `false` | When `true`, returns only the currently focused/active tab. |
| **`domain`** | `string` | No | `null` | Filter tabs matching a specific host or domain. |
| **`claimedBy`** | `string` | No | `null` | Filter tabs claimed by a specific agent. |
| **`kind`** | `string` | No | `null` | Filter by surface kind (e.g. `"browser"`, `"sandbox"`). |
| **`targetIds`** | `array` | No | `null` | Specific list of tab IDs to inspect. |

---

## 4. Example Calls

### Querying All Tabs with Minimal Detail
```json
{
  "name": "nova.tabs",
  "arguments": {
    "outputDetail": "minimal"
  }
}
```

### Sample Response (Minimal)
```json
{
  "tabs": [
    {
      "targetId": "tab-1",
      "title": "GitHub � Where software is built",
      "url": "https://github.com/",
      "active": true,
      "sandbox": "A",
      "claimed": false
    },
    {
      "targetId": "tab-2",
      "title": "Hacker News",
      "url": "https://news.ycombinator.com/",
      "active": false,
      "sandbox": "A",
      "claimed": true,
      "claimOwner": "research-agent-1",
      "leaseRemainingMs": 184000
    }
  ],
  "activeTargetId": "tab-1"
}
```

---

## 5. Best Practices & Common Traps

* **Never hardcode `"tab-1"`:** Target IDs are assigned dynamically as tabs open and close. Always run `nova.tabs(outputDetail="minimal")` before starting a multi-step workflow.
* **Auto-Claim on Mutation:** While `nova.tabs` is read-only, mutating tools (`click_selector`, `navigate`) can auto-claim an unclaimed tab for your session. Use explicit `nova.tab_claim` when you need an ironclad multi-step lease.

---

## See Also

* [`nova.tab_claim`](nova-tab-claim.md) � Claim exclusive write access to a tab.
* [`nova.tab_new`](nova-tab-new.md) � Open a new tab.
* [`nova.tab_close`](nova-tab-close.md) � Close a tab.
* [Core Feature: Multi-Sandbox Isolation](../../../core-features/sandbox-isolation.md)
