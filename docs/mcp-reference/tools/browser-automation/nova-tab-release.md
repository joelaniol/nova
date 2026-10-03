# `nova.tab_release`

Releases an active exclusive lease on a browser tab, optionally logging finalization decisions, task outcomes, or coverage status.

---

## 1. Overview

`nova.tab_release` relinquishes write ownership of a tab previously acquired via `nova.tab_claim` or an implicit auto-claim. Releasing a tab makes it immediately available for interaction by other AI agents or the human operator without waiting for the lease TTL to expire.

* **Capability Bundle:** `browser_automation`
* **Target Scope:** Tab-specific (`targetId` required).
* **Audit Trail:** Supports attaching finalization tokens, task success decisions, and coverage exhaustion notes to Nova's evidence ledger.

---

## 2. Key Capabilities & Features

### A. Instant Lock Removal
Clears the `claimOwner` entry in Nova's target registry and resets the lease countdown to zero.

### B. Task & ETM Finalization
When releasing a tab as part of an **Episodic Task Memory (ETM)** workflow:
* Pass `finalizeDecision: "success"` or `"aborted"`.
* Pass `finalizeReasonCode: "task_completed"` or a descriptive reason.
* If performing URL audits, pass `coverageExhausted: true` to certify that all planned URLs on the domain have been verified.

---

## 3. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`targetId`** | `string` | **Yes** | � | Target tab ID to release (e.g. `"tab-1"`). |
| **`agentId`** | `string` | No | `"default"` | Identity of the calling agent holding the claim. |
| **`finalizeDecision`** | `string` | No | `null` | Finalization outcome (e.g. `"success"`, `"aborted"`). |
| **`finalizeReasonCode`**| `string` | No | `null` | Structured reason code (e.g. `"order_confirmed"`). |
| **`finalizeReasonText`**| `string` | No | `null` | Human-readable explanation of why the tab was released. |
| **`coverageExhausted`** | `boolean` | No | `false` | Indicates exhaustive URL exploration was completed. |

---

## 4. Example Call

```json
{
  "name": "nova.tab_release",
  "arguments": {
    "targetId": "tab-2",
    "agentId": "subagent-pricing-1",
    "finalizeDecision": "success",
    "finalizeReasonCode": "extraction_complete"
  }
}
```

### Sample Response
```json
{
  "ok": true,
  "targetId": "tab-2",
  "claimed": false,
  "releasedBy": "subagent-pricing-1"
}
```

---

## See Also

* [`nova.tab_claim`](nova-tab-claim.md) � Claim an exclusive write lease.
* [`nova.tabs`](nova-tabs.md) � Inspect active tab claims.
* [Core Feature: Agent Awareness Gates (AAG)](../../../core-features/aag.md)
