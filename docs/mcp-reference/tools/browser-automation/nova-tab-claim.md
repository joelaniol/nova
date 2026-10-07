# `nova.tab_claim`

Claims exclusive write ownership (lease) over a specified browser tab to prevent multi-agent collisions and race conditions.

---

## 1. Overview

In modern multi-agent systems (e.g. Claude Code subagents, OpenAI Codex, or Antigravity swarms), multiple AI agents often execute in parallel on the same workstation. Without coordination, Agent A may click a button while Agent B is typing into a form on the same page.

`nova.tab_claim` gives one agent a time-limited lease on a tab. While the claim is active, Nova refuses calls on that tab from any agent whose `agentId` does not match the claim owner.

* **Target Scope:** Tab-specific (`targetId` required).
* **Expiration Policy:** Every lease expires (`ttlMs`, default 120 s, 5 s to 30 min), so a crashed agent cannot block a tab for good. Claiming again extends it.

---

## 2. Key Capabilities & Features

### A. Mutual Exclusion
* While `targetId` is claimed by Agent A:
  * Agent A can execute clicks, navigation, typing, and form submissions freely.
  * Agent B's calls on the tab are refused with error code `-32040` (`claim.owner_mismatch`); the message names the owning `agentId`.

### B. Cooperative Reclaiming (`reclaimReason`)
If a previous session or crashed subagent left an active lease, a coordinator agent can reclaim the tab before the TTL expires by supplying an explicit `reclaimReason`. The previous owner gets a one-time notice with that reason on its next call.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Tab to claim (tabId, sandboxId like 'A', or 'active'). |
| `agentId` | `string` | No | `"default"` | — | Agent identity. Defaults to 'default'. |
| `agentRole` | `string` | No | — | `actor`, `archivist`, `mcp` | Optional role hint. 'actor' performs live tab work and cannot override finalize decisions, 'archivist' is allowed to finalize/curate completed work, and 'mcp' is the privileged server/operator role. If provided, the value must match the role inferred from agentId. |
| `ttlMs` | `integer` | No | `120000` | 5000–1800000 | Lease duration in ms. Defaults to 120s. Must be between 5s and 30min; out-of-range values fail with -32602 before a claim is created or extended. |
| `debugLabel` | `string` | No | — | — | Optional label for logging/debugging. On a same-owner re-claim, a non-empty value updates the existing metadata; omission or blank input preserves the current label. |
| `reclaimReason` | `string` | No | — | — | Force-reclaim reason. When provided and another agent holds the tab, the existing claim is force-released and the displaced owner receives a one-shot AAG block notification with this reason. Omit to get the default owner-mismatch error. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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

* [`nova.tab_release`](nova-tab-release.md) — Release an active lease.
* [`nova.tabs`](nova-tabs.md) — Check claim owners and lease remaining time.
* [Core Feature: Agent Awareness Gates (AAG)](../../../core-features/agent-awareness-gates-aag/README.md)
