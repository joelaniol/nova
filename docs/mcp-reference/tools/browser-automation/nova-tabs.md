# `nova.tabs`

Lists all open tabs, WebViews, and sandbox surfaces across the workspace with filtering, claim status, and ownership details.

---

## 1. Overview

`nova.tabs` gives AI agents visibility into all active browser surfaces in the running Nova AI Workspace instance. It allows agents to choose targets, inspect current page URLs, check multi-agent claim leases, and avoid operating in the user's personal tabs.

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

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `activeOnly` | `boolean` | No | `false` | — | When true, return only the active target. |
| `kind` | `string` | No | — | `sandbox`, `browserTab` | Optional exact target-kind filter. |
| `domain` | `string` | No | — | 1–253 characters | Optional hostname filter. Matches the exact URL host and its subdomains. |
| `claimedBy` | `string` | No | — | 1–256 characters | Optional exact claim-owner agentId filter. Expired claims do not match. |
| `mine` | `boolean` | No | `false` | — | Return only targets that belong to you: claimed by your agentId, or created by it via nova.tab_new. Use it to stay out of tabs the user or another agent is working in. The response echoes mineAgentId so an empty list can be told apart from a wrong agentId. |
| `agentId` | `string` | No | — | 1–256 characters | Your agent identity, used by mine=true. Defaults to 'default'. |
| `targetIds` | `array` of `string` | No | — | ≤ 100 items | Optional set of target IDs to include, bounded to 100 items. |
| `outputDetail` | `string` | No | `"full"` | `minimal`, `summary`, `full` | Projection size. minimal returns targetId, url, isActive, isPrivate/privateSessionId, and a short claim block; summary adds core identity/readiness fields; full preserves all tab diagnostics. Every size reports isPrivate, so a target can be picked without a second call. |

Capability bundles: `browser_automation`, `page_read_debug`, `visual_evidence`.
<!-- /generated:parameters -->

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
      "title": "GitHub — Where software is built",
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

* [`nova.tab_claim`](nova-tab-claim.md) — Claim exclusive write access to a tab.
* [`nova.tab_new`](nova-tab-new.md) — Open a new tab.
* [`nova.tab_close`](nova-tab-close.md) — Close a tab.
* [Core Feature: Multi-Sandbox Isolation](../../../core-features/sandbox-isolation.md)
