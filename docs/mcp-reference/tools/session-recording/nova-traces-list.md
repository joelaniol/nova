# `nova.traces_list`

Lists recent host operation traces with execution timing, phases, and outcome status for debugging.

---

## 1. Overview

`nova.traces_list` retrieves recent internal operation traces from Nova's host runtime. It exposes low-level lifecycle execution records, tool invocation durations, sub-phase timestamps, and error classifications, facilitating deep performance tuning and debugging.

* **Capability Bundle:** `session_recording`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`limit`** | `integer` | No | `20` | Maximum number of traces to return (max 100). |
| **`status`** | `string` | No | `null` | Optional status filter: `"ok"`, `"failed"`, or null for all. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
