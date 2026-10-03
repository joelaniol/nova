# `nova.traces_list`

Lists recent host operation traces with execution timing, phases, and outcome status for debugging.

---

## 1. Overview

`nova.traces_list` retrieves recent internal operation traces from Nova's host runtime. It exposes low-level lifecycle execution records, tool invocation durations, sub-phase timestamps, and error classifications, facilitating deep performance tuning and debugging.

* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `limit` | `integer` | No | `20` | 1–50 | Maximum traces to return. |
| `status` | `string` | No | — | `ok`, `failed`, `blocked`, `running` | Optional status filter. 'ok' returns successful traces, 'failed' returns tool/runtime failures, 'blocked' returns policy/claim/approval denials, and 'running' returns traces that have not completed yet. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
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
      "text": "Retrieved 1 failed operation trace from recent history."
    }
  ],
  "structuredContent": {
    "ok": true,
    "count": 1,
    "traces": [
      {
        "traceId": "tr-09b4",
        "tool": "nova.click_selector",
        "durationMs": 5020,
        "status": "failed",
        "error": "Element #nonexistent-btn was not found within timeout",
        "timestampUtc": "2026-10-02T20:10:00Z",
        "phases": [
          {
            "name": "selector_resolve",
            "durationMs": 5000,
            "ok": false
          }
        ]
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Host Performance Tuning:** Use `nova.traces_list` to identify slow operations and diagnose whether latency occurred in DOM resolution, network waits, or process IPC.
* **Failure Auditing:** Filter by `status: "failed"` to review recent tool invocation failures across all connected subagents.

---

## 5. Related Tools

* [`nova.session_record_events`](nova-session-record-events.md) — Inspect console and error streams.
* [`nova.session_record_status`](nova-session-record-status.md) — Monitor recording health.
