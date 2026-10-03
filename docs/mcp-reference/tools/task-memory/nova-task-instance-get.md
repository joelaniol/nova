# `nova.task_instance_get`

Loads a task instance snapshot for session-crossing resume and progress inspection.

---

## 1. Overview

`nova.task_instance_get` retrieves the full state of a task instance: current revision, completed work units, pending mandatory checks, and execution logs.

* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `instanceId` | `string` | Yes | — | — | The instance ID to load. |
| `includePendingUnits` | `boolean` | No | `false` | — | Legacy alias for includeDiscoveredUnitsPreview. Include a preview of units still in status 'discovered'. Default: false. |
| `pendingUnitsLimit` | `integer` | No | `20` | 1–200 | Legacy alias for discoveredUnitsPreviewLimit. Max discovered units to return. Default: 20. |
| `includeDiscoveredUnitsPreview` | `boolean` | No | `false` | — | Canonical flag. Include a preview of units that are still in status 'discovered'. Default: false. |
| `discoveredUnitsPreviewLimit` | `integer` | No | `20` | 1–200 | Canonical limit for discoveredUnitsPreview. Default: 20. |
| `includeRecentEvents` | `boolean` | No | `false` | — | Include recent event log entries. Default: false. |
| `recentEventLimit` | `integer` | No | `10` | 1–100 | Max recent events to return. Default: 10. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_instance_get",
  "arguments": {
    "instanceId": "inst-881a"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Loaded task instance inst-881a (status: InProgress, rev: 3)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "instanceId": "inst-881a",
    "status": "InProgress",
    "currentRev": 3,
    "completedUnits": 8,
    "pendingChecksCount": 1
  }
}
```

---

## 4. Operational Best Practices

* **Resume Workflows:** Call `get` to inspect remaining work when resuming an existing task in a fresh agent conversation.

---

## 5. Related Tools

* [`nova.task_instance_progress`](nova-task-instance-progress.md)
* [`nova.task_instance_complete`](nova-task-instance-complete.md)
