# `nova.scheduled_task_secret_list`

Lists registered secret key names for a task without exposing plaintext secret values.

---

## 1. Overview

`nova.scheduled_task_secret_list` returns the names of all secrets currently configured for a task. In accordance with zero-trust security guidelines, plaintext secret values are never disclosed in the response.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`taskId`** | `string` | Yes | `none` | The task ID. |
| **`limit`** | `integer` | No | `100` | Maximum keys to return (1-500). |
| **`offset`** | `integer` | No | `0` | Pagination offset. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_secret_list",
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
      "text": "Task task-7c81a2f0 has 1 registered secret key: OPENAI_API_KEY."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskId": "task-7c81a2f0",
    "secretKeys": [
      "OPENAI_API_KEY"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Pre-Flight Credential Auditing:** Check secret keys before triggering a task to ensure all required external API keys are configured.
* **Missing Secrets:** If a required key is absent, use [`nova.scheduled_task_secret_set`](nova-scheduled-task-secret-set.md) to supply it.

---

## 5. Related Tools

* [`nova.scheduled_task_secret_set`](nova-scheduled-task-secret-set.md) — Set encrypted secret.
* [`nova.scheduled_task_get`](nova-scheduled-task-get.md) — View task details.
