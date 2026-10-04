# `nova.traces_list`

Lists recent host operation traces with execution timing, phases, and outcome status for debugging.

---

## 1. Overview

`nova.traces_list` retrieves recent internal operation traces from Nova's host runtime. It exposes low-level lifecycle execution records, tool invocation durations, sub-phase timestamps, and error classifications, facilitating deep performance tuning and debugging.

* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `limit` | `integer` | No | `20` | 1–50 | Maximum traces to return. |
| `status` | `string` | No | — | `ok`, `failed`, `blocked`, `running` | Optional status filter. 'ok' returns successful traces, 'failed' returns tool/runtime failures, 'blocked' returns policy/claim/approval denials, and 'running' returns traces that have not completed yet. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.traces_list",
  "arguments": {
    "limit": 3,
    "status": "failed"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "1 trace(s), 0 metric observation(s).\nTraces:\n[...]\nMetrics:\n[]"
    }
  ],
  "structuredContent": {
    "count": 1,
    "traces": [
      {
        "opId": "a1b2c3d4",
        "traceId": "tr-09b4",
        "toolName": "nova.click_selector",
        "targetId": "tab-1",
        "subjectKey": null,
        "sourceKind": "mcp",
        "clientType": "claude-code",
        "sidecarSessionId": null,
        "startedAt": "2026-10-02T20:10:00Z",
        "elapsedMs": 5020,
        "phases": [
          {
            "name": "selector_resolve",
            "startMs": 0,
            "endMs": 5000,
            "details": "timed out"
          }
        ],
        "status": "failed",
        "reason": "Element #nonexistent-btn was not found within timeout",
        "failScreenshots": null
      }
    ],
    "metricCount": 0,
    "metricObservations": []
  }
}
```

Note this tool's result has no top-level `ok` field (unlike most other tools) — check `count`/`traces` directly. `metricObservations` is a separate, always-present list of recent OK-signal metric observations (unrelated to trace status); it is not limited by the `status` filter.

---

## 4. Operational Best Practices

* **Host Performance Tuning:** Use `nova.traces_list` to identify slow operations and diagnose whether latency occurred in a specific phase (`phases[].startMs`/`endMs`) of the call.
* **Failure Auditing:** Filter by `status: "failed"` to review recent tool invocation failures; `reason` carries the failure text and `failScreenshots` (base64 PNGs, up to 5) is populated only for `failed`/`blocked` traces when a screenshot could be captured.

---

## 5. Related Tools

* [`nova.session_record_events`](nova-session-record-events.md) — Inspect console and error streams.
* [`nova.session_record_status`](nova-session-record-status.md) — Monitor recording health.
