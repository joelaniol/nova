# `nova.memory_add_candidate`

Proposes a lightweight candidate memory claim for the currently claimed task and tab.

---

## 1. Overview

`nova.memory_add_candidate` records a one-line candidate claim for the currently claimed tab in the Learning Candidate Journal (LCJ). The target tab must already be claimed (`nova.tab_claim`) before a candidate can be added.

* **Core Architecture Guide:** [Agent Learning Pipeline (ALP) & Learning Candidate Journal (LCJ)](../../../core-features/learning/agent-learning-pipeline-alp/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Claimed target tab ID (or active/activeBrowserTab). |
| `agentId` | `string` | No | `"default"` | — | Agent identity. Must match claim owner. Defaults to 'default'. |
| `component` | `string` | Yes | — | — | Specific component key (e.g. 'mcp-locks', 'ui-automation'). |
| `claim` | `string` | Yes | — | — | One-line reusable insight (max 280 chars). |
| `status` | `string` | No | `"unverified"` | `unverified`, `verified`, `disproven` | Claim verification status. 'unverified' stores a fresh claim that still needs confirmation, 'verified' marks a claim that was reproduced or proven true, and 'disproven' records a claim that was checked and found false, outdated, or no longer applicable. |
| `confidence` | `number` | No | `0.65` | — | Confidence score 0.0-1.0. Default 0.65. |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "LCJ candidate created: #42 (unverified)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "taskId": "task-9b10a",
    "ownerAgentId": "default",
    "candidateId": 42,
    "created": true,
    "status": "unverified",
    "confidence": 0.65,
    "updatedAtUtc": "2026-08-15T09:30:00Z"
  }
}
```

`candidateId` is an integer. `created` is `false` when the call updated an existing candidate for the same claim context instead of inserting a new one.

---

## 4. Operational Best Practices

* **Actor-Side Claims:** Use during exploratory tasks to suggest procedural knowledge without directly mutating verified PKS stores.

---

## 5. Related Tools

* [`nova.tab_claim`](../browser-automation/nova-tab-claim.md)
* [`nova.memory_stats`](nova-memory-stats.md)
