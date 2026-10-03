# `nova.scheduled_task_update`

Updates fields (prompt, schedule, budget, timeouts, chaining) of an existing scheduled task.

---

## 1. Overview

`nova.scheduled_task_update` modifies the configuration of a scheduled task. Only provided fields are updated; omitted fields retain their existing values. Updating the schedule recalculates the next execution timestamp immediately.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 2 (Task Mutation)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`taskId`** | `string` | Yes | `none` | The task ID to update. |
| **`displayName`** | `string` | No | `null` | New display name. |
| **`prompt`** | `string` | No | `null` | New instruction prompt or script. |
| **`cronExpression`** | `string` | No | `null` | New schedule expression. Pass `""` to clear. |
| **`intervalSeconds`** | `integer` | No | `null` | New interval in seconds (minimum 60). |
| **`timeoutSeconds`** | `integer` | No | `null` | New run timeout in seconds. |
| **`maxBudgetUsd`** | `number` | No | `null` | New cost cap per run in USD. |
| **`mcpAccess`** | `boolean` | No | `null` | Enable or disable MCP tool access. |
| **`triggerNextTaskId`** | `string` | No | `null` | Update downstream chained task ID. Pass `""` to clear. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_update",
  "arguments": {
    "taskId": "task-7c81a2f0",
    "timeoutSeconds": 240,
    "cronExpression": "daily 10:00"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Updated task task-7c81a2f0: timeoutSeconds=240, schedule='daily 10:00'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskId": "task-7c81a2f0",
    "updatedFields": [
      "timeoutSeconds",
      "cronExpression"
    ],
    "nextRunUtc": "2026-10-03T08:00:00Z"
  }
}
```

---

## 4. Operational Best Practices

* **Schedule Recalculation:** Changing `cronExpression`, `intervalSeconds`, or `timeZoneId` instantly updates the scheduler without requiring a restart.
* **Clearing Fields:** Supply an empty string `""` to remove optional fields like `triggerNextTaskId` or `watchPath`.

---

## 5. Related Tools

* [`nova.scheduled_task_get`](nova-scheduled-task-get.md) — View updated definition.
* [`nova.scheduled_task_disable`](nova-scheduled-task-disable.md) — Pause task without deleting.
