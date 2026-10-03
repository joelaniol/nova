# `nova.scheduled_task_run_cancel`

Cancels an in-flight background task run asynchronously.

---

## 1. Overview

`nova.scheduled_task_run_cancel` sends a graceful termination signal to the executor process of a running task. If the process does not terminate within a safety grace window, Nova forces a process tree kill to prevent hung background workers.

* **Security Tier:** Tier 2 (Process Control)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `runId` | `string` | Yes | — | — | ID of the run to cancel. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_run_cancel",
  "arguments": {
    "runId": "run-8120c"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Cancellation signal sent to run-8120c."
    }
  ],
  "structuredContent": {
    "ok": true,
    "runId": "run-8120c",
    "status": "Cancelling"
  }
}
```

---

## 4. Operational Best Practices

* **Asynchronous Drain:** Cancellation is non-blocking; verify termination via [`nova.scheduled_task_active_runs`](nova-scheduled-task-active-runs.md).
* **Resource Recovery:** Clean cancellation ensures file handles and WebView instances bound to the run are safely released.

---

## 5. Related Tools

* [`nova.scheduled_task_active_runs`](nova-scheduled-task-active-runs.md) — Check active runs.
* [`nova.scheduled_task_trigger`](nova-scheduled-task-trigger.md) — Start a run.
