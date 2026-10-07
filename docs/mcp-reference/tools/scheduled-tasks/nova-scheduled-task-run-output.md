# `nova.scheduled_task_run_output`

Memory-safe tail reader for stdout and stderr log streams of a specific task run.

---

## 1. Overview

`nova.scheduled_task_run_output` reads log streams produced during task execution. For files over 1 MB it streams from the end of the file instead of loading it fully, to avoid out-of-memory errors on large outputs, and returns the requested tail along with line-range metadata (`startLine`, `endLine`, `hasEarlier`). If the run has no log file for the requested stream yet, it reports zero lines rather than an error. The response also includes `structuredResult` — the run's parsed structured-result JSON, if the executor wrote one — alongside the raw log lines.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `runId` | `string` | Yes | — | — | The run ID to read output from. |
| `stream` | `string` | No | `"stdout"` | `stdout`, `stderr` | Which stream to read: 'stdout' or 'stderr'. Default: 'stdout'. |
| `maxLines` | `integer` | No | `500` | 1–10000 | Maximum lines to return (tail). Default: 500. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_run_output",
  "arguments": {
    "runId": "8f14e45fceea167a5a36dedd4bea2543",
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
      "text": "[INFO] Navigating to https://store.example.com/item/101...\n[INFO] Element #price resolved: $49.99\n[INFO] Written to shared/price.json. Run finished."
    }
  ],
  "structuredContent": {
    "runId": "8f14e45fceea167a5a36dedd4bea2543",
    "stream": "stdout",
    "totalLines": 3,
    "truncated": false,
    "mode": "tail",
    "maxLines": 50,
    "returnedCount": 3,
    "startLine": 1,
    "endLine": 3,
    "hasEarlier": false,
    "hasMore": false,
    "nextStartLine": null,
    "lines": [
      "[INFO] Navigating to https://store.example.com/item/101...",
      "[INFO] Element #price resolved: $49.99",
      "[INFO] Written to shared/price.json. Run finished."
    ],
    "structuredResult": null
  }
}
```

---

## 4. Operational Best Practices

* **Error Streams First:** When investigating failed runs, query `stream: "stderr"` first to see exception stack traces.
* **Bounded Output:** Default 500 lines protects client context from token overflow on verbose shell tasks; check `hasEarlier` to know if output was cut off at the start.

---

## 5. Related Tools

* [`nova.scheduled_task_runs`](nova-scheduled-task-runs.md) — Find run IDs.
* [`nova.scheduled_task_run_cancel`](nova-scheduled-task-run-cancel.md) — Cancel stuck run.
