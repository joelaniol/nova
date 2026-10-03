# `nova.scheduled_task_run_output`

Memory-safe tail reader for stdout and stderr log streams of a specific task run.

---

## 1. Overview

`nova.scheduled_task_run_output` reads log streams produced during task execution. It reads from the tail of the log file to prevent out-of-memory errors on large outputs, returning line slices and pagination metadata.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`runId`** | `string` | Yes | `none` | The run ID to read output from. |
| **`stream`** | `string` | No | `"stdout"` | Which stream to read: `"stdout"` or `"stderr"`. |
| **`maxLines`** | `integer` | No | `500` | Maximum lines to return from the end of the log. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_run_output",
  "arguments": {
    "runId": "run-8120c",
    "stream": "stdout",
    "maxLines": 50
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "[stdout] Loaded 3 lines for run-8120c."
    }
  ],
  "structuredContent": {
    "ok": true,
    "runId": "run-8120c",
    "stream": "stdout",
    "totalLines": 3,
    "lines": [
      "[INFO] Navigating to https://store.example.com/item/101...",
      "[INFO] Element #price resolved: $49.99",
      "[INFO] Written to shared/price.json. Run finished."
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Error Streams First:** When investigating failed runs, query `stream: "stderr"` first to see exception stack traces.
* **Bounded Output:** Default 500 lines protects client context from token overflow on verbose shell tasks.

---

## 5. Related Tools

* [`nova.scheduled_task_runs`](nova-scheduled-task-runs.md) — Find run IDs.
* [`nova.scheduled_task_run_cancel`](nova-scheduled-task-run-cancel.md) — Cancel stuck run.
