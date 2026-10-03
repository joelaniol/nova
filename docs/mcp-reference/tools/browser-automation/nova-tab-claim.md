# `nova.tab_claim`

Claims exclusive write ownership (lease) over a specified browser tab to prevent multi-agent collisions and race conditions.

---

## 1. Overview

In modern multi-agent systems (e.g. Claude Code subagents, OpenAI Codex, or Antigravity swarms), multiple AI agents often execute in parallel on the same workstation. Without coordination, Agent A may click a button while Agent B is typing into a form on the same page.

`nova.tab_claim` establishes a **Hardware-Enforced Lease Lock** on a tab. While a claim is active, Nova's Agent Awareness Gates (AAG) reject mutating actions (`click_selector`, `type_selector`, `navigate`) from any agent whose `agentId` does not match the claim owner.

* **Capability Bundle:** `browser_automation`
* **Target Scope:** Tab-specific (`targetId` required).
* **Expiration Policy:** Every lease has a finite TTL (default: 5 minutes / 300,000 ms) to prevent permanent deadlocks if an agent crashes.

---

## 2. Key Capabilities & Features

### A. Mutual Exclusion
* While `targetId` is claimed by Agent A:
  * Agent A can execute clicks, navigation, typing, and form submissions freely.
  * Agent B's attempts to mutate the tab are immediately rejected with `-32002: Tab is locked by another agent lease`.
  * Read-only tools (`nova.tabs`, `nova.read_dom`, `nova.read_text_structured`) remain accessible to other agents.

### B. Cooperative Reclaiming (`reclaimReason`)
If a previous session or crashed subagent left an active lease, a coordinator agent can reclaim the tab before the TTL expires by supplying an explicit `reclaimReason`. Nova logs the reclamation event in the audit trail.

---

## 3. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`targetId`** | `string` | **Yes** | � | Target tab ID to claim (e.g. `"tab-1"`). |
| **`agentId`** | `string` | No | `"default"` | Unique identity of the calling agent claiming the lease. |
| **`ttlMs`** | `integer` | No | `300000` | Lease duration in milliseconds (default: 5 minutes). Max: 3,600,000 ms (1 hour). |
| **`agentRole`** | `string` | No | `null` | Role description (e.g. `"MarketResearcher"`, `"CheckoutAuditor"`). |
| **`reclaimReason`** | `string` | No | `null` | Required only when overriding an existing active claim held by another agent. |
| **`debugLabel`** | `string` | No | `null` | Human-readable label displayed in the host UI claim overlay. |

---

## 4. Example Calls

### Claiming a Tab for 3 Minutes
```json
{
  "name": "nova.tab_claim",
  "arguments": {
    "targetId": "tab-2",
    "agentId": "subagent-pricing-1",
    "ttlMs": 180000,
    "debugLabel": "Extracting product pricing matrix"
  }
}
```

### Sample Response
```json
{
  "ok": true,
  "targetId": "tab-2",
  "claimed": true,
  "claimOwner": "subagent-pricing-1",
  "leaseRemainingMs": 180000,
  "expiresAtUtc": "2026-10-02T21:35:00Z"
}
```

---

## 5. Best Practices & Common Traps

* **Always Release When Done:** Call `nova.tab_release` immediately after your task completes so other subagents or human operators can use the tab without waiting for the lease to expire.
* **Auto-Claim on First Mutation:** If a tab is currently unclaimed, calling a mutating action like `nova.click_selector` will automatically claim the tab for your session. Calling `nova.tab_claim` explicitly is recommended when coordinating long multi-step workflows.

---

## See Also

* [`nova.tab_release`](nova-tab-release.md) � Release an active lease.
* [`nova.tabs`](nova-tabs.md) � Check claim owners and lease remaining time.
* [Core Feature: Agent Awareness Gates (AAG)](../../../core-features/aag.md)
