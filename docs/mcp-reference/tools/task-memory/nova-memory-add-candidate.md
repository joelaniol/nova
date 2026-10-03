# `nova.memory_add_candidate`

Proposes a lightweight candidate memory claim for the currently claimed task and tab.

---

## 1. Overview

`nova.memory_add_candidate` records an unverified hypothesis or observation during task execution for subsequent offline verification.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 2 (Memory Ingestion)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`claim`** | `string` | Yes | `null` | One-line reusable insight (max 280 chars). |
| **`component`** | `string` | Yes | `null` | Specific component key (e.g. 'mcp-locks', 'ui-automation'). |
| **`confidence`** | `number` | No | `0.65` | Confidence score 0.0-1.0. Default 0.65. |
| **`status`** | `string` | No | `"unverified"` | Claim verification status. 'unverified' stores a fresh claim that still needs confirmation, 'verified' marks a claim that was reproduced or proven true, and 'disproven' records a claim that was checked and found false, outdated, or no longer applicable. |
| **`targetId`** | `string` | Yes | `null` | Claimed target tab ID (or active/activeBrowserTab). |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.memory_add_candidate",
  "arguments": {
    "targetId": "tab-1",
    "component": "login_form",
    "claim": "Requires CSRF token in header X-XSRF-TOKEN"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Added memory candidate for login_form."
    }
  ],
  "structuredContent": {
    "ok": true,
    "candidateId": "cand-09a",
    "component": "login_form",
    "status": "PendingVerification"
  }
}
```

---

## 4. Operational Best Practices

* **Actor-Side Claims:** Use during exploratory tasks to suggest procedural knowledge without directly mutating verified PKS stores.

---

## 5. Related Tools

* [`nova.memory_note`](nova-memory-note.md)
* [`nova.memory_stats`](nova-memory-stats.md)
