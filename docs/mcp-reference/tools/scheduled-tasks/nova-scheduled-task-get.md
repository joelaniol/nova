# `nova.scheduled_task_get`

Retrieves full details of a scheduled task including prompt, schedule, chaining, and budget settings.

---

## 1. Overview

`nova.scheduled_task_get` returns the complete configuration for a specific background task. It exposes the prompt text, executor arguments, timezone, retry behavior, workspace path, and chaining dependencies.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`taskId`** | `string` | Yes | `none` | The task ID to retrieve. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_get",
  "arguments": {
    "taskId": "task-7c81a2f0"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Loaded scheduled task 'Competitor Price Tracker' (task-7c81a2f0)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskId": "task-7c81a2f0",
    "displayName": "Competitor Price Tracker",
    "status": "Enabled",
    "prompt": "Check https://store.example.com/item/101 and write the current price to shared/price.json",
    "executorKind": "ClaudeCode",
    "cronExpression": "daily 09:00",
    "timeZoneId": "Europe/Berlin",
    "timeoutSeconds": 180,
    "mcpAccess": true,
    "workspacePath": "ScheduledTasks/task-7c81a2f0",
    "concurrencyPolicy": "Skip"
  }
}
```

---

## 4. Operational Best Practices

* **Pre-Update Verification:** Call `get` before [`nova.scheduled_task_update`](nova-scheduled-task-update.md) to inspect current configurations.
* **Workspace Location:** Use `workspacePath` to determine where persistent shared files and run logs reside.

---

## 5. Related Tools

* [`nova.scheduled_task_update`](nova-scheduled-task-update.md) — Update task configuration.
* [`nova.scheduled_task_workspace`](nova-scheduled-task-workspace.md) — Inspect task workspace.
