# `nova.scheduled_task_export`

Exports all scheduled task definitions as a portable JSON array (excluding secrets and history).

---

## 1. Overview

`nova.scheduled_task_export` dumps all task definitions into a portable JSON array string. It captures prompts, schedules, executor configurations, budget caps, and chaining rules while omitting ephemeral runtime state, run history, and DPAPI-encrypted secrets.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_export",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Exported 2 task definitions as JSON."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskCount": 2,
    "tasksJson": "[{\"displayName\":\"Competitor Price Tracker\",\"prompt\":\"...\",\"cronExpression\":\"daily 09:00\"}]"
  }
}
```

---

## 4. Operational Best Practices

* **Version Control Integration:** Commit exported task configurations into Git repositories to manage scheduled automations as code.
* **Disaster Recovery:** Store JSON exports before major migrations or system updates.

---

## 5. Related Tools

* [`nova.scheduled_task_import`](nova-scheduled-task-import.md) — Restore exported tasks.
* [`nova.scheduled_task_list`](nova-scheduled-task-list.md) — List active tasks.
