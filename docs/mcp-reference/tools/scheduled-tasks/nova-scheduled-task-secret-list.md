# `nova.scheduled_task_secret_list`

Lists registered secret key names for a task without exposing plaintext secret values.

---

## 1. Overview

`nova.scheduled_task_secret_list` returns the names of all secrets currently configured for a task. The tool is write-only by design on the other side (`nova.scheduled_task_secret_set`): plaintext secret values are never disclosed in this or any other response.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID. |
| `limit` | `integer` | No | `100` | 1–500 | Maximum secret keys to return (1-500). Default: 100. |
| `offset` | `integer` | No | `0` | ≥ 0 | Number of secret keys to skip before returning this page. Default: 0. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "Secrets for task 'task-7c81a2f0': OPENAI_API_KEY."
    }
  ],
  "structuredContent": {
    "taskId": "task-7c81a2f0",
    "keys": [
      "OPENAI_API_KEY"
    ],
    "returnedCount": 1,
    "limit": 100,
    "offset": 0,
    "truncated": false,
    "nextOffset": null
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
