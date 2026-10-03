# `nova.scheduled_task_var_set`

Sets a persistent key-value state variable for a task that survives across runs.

---

## 1. Overview

`nova.scheduled_task_var_set` stores lightweight persistent state for a task. Variables are retained across runs and browser restarts, enabling tasks to track watermarks, last-seen timestamps, pagination cursors, and running counters without creating extra files.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 2 (State Mutation)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`taskId`** | `string` | Yes | `none` | The task ID. |
| **`key`** | `string` | Yes | `none` | Variable name (alphanumeric + underscore, max 64 chars). |
| **`value`** | `string` | Yes | `none` | Variable value (max 64 KB). Use JSON strings for structured data. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_var_set",
  "arguments": {
    "taskId": "task-7c81a2f0",
    "key": "last_scraped_id",
    "value": "10482"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Set variable 'last_scraped_id' for task task-7c81a2f0."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskId": "task-7c81a2f0",
    "key": "last_scraped_id",
    "valueLength": 5
  }
}
```

---

## 4. Operational Best Practices

* **Watermark Tracking:** Store high-water marks (e.g. `last_processed_email_id`) so recurring runs process only new delta items.
* **Structured State:** Serialize small state objects as JSON strings within the 64 KB limit.

---

## 5. Related Tools

* [`nova.scheduled_task_var_get`](nova-scheduled-task-var-get.md) — Read variable value.
* [`nova.scheduled_task_var_list`](nova-scheduled-task-var-list.md) — List all variables.
