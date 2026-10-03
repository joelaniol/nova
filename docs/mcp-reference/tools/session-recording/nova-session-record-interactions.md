# `nova.session_record_interactions`

Reads the chronological interaction timeline (clicks, typing, form submits) from a recording.

---

## 1. Overview

`nova.session_record_interactions` reconstructs the sequence of physical and programmatic interactions executed during a session. It unifies both user-driven DOM inputs (`source: "user_dom"`) and agent MCP tool calls (`source: "mcp"`), providing an audit trail of actions leading up to any event.

* **Capability Bundle:** `session_recording`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `recordingId` | `string` | Yes | — | — | Recording ID (the dir under %LOCALAPPDATA%/NovaBrowser/Recordings). |
| `source` | `string` | No | — | `mcp`, `user_dom` | Filter by source: 'mcp' (agent-driven), 'user_dom' (native), or omit for both. |
| `type` | `string` | No | — | — | Filter by interaction type (e.g. 'click', 'submit', 'nova.click_selector'). Exact match. |
| `targetSelectorMatch` | `string` | No | — | — | Case-insensitive regex applied to targetSelector. Invalid regex disables the filter. |
| `sinceMs` | `integer` | No | — | — | Filter timestamp >= Unix-ms (ISO-8601 string also accepted). |
| `untilMs` | `integer` | No | — | — | Filter timestamp <= Unix-ms (ISO-8601 string also accepted). |
| `limit` | `integer` | No | `200` | 1–5000 | Max events returned. |
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.session_record_interactions",
  "arguments": {
    "recordingId": "rec-9b21f04a",
    "type": "click"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Loaded 2 click interactions from rec-9b21f04a."
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordingId": "rec-9b21f04a",
    "count": 2,
    "interactions": [
      {
        "sequence": 1,
        "timestampUtc": "2026-10-02T20:16:05Z",
        "source": "mcp",
        "action": "nova.click_selector",
        "targetSelector": "#checkout-btn",
        "coordinates": {
          "x": 420,
          "y": 780
        }
      },
      {
        "sequence": 2,
        "timestampUtc": "2026-10-02T20:17:10Z",
        "source": "user_dom",
        "action": "click",
        "targetSelector": ".submit-payment",
        "coordinates": {
          "x": 510,
          "y": 820
        }
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Playbook Generation:** Use interaction sequences from successful human sessions to inform PKS phenomenon fast-paths.
* **Reproduction Steps:** Review agent and human actions sequentially to reproduce race conditions or intermittent failures.
* **Redaction Assurance:** Sensitive password input values in interaction records are replaced with `[REDACTED_SECRET]` tokens.

---

## 5. Related Tools

* [`nova.session_record_events`](nova-session-record-events.md) — Inspect console and system logs.
* [`nova.pks_upsert`](../pks-and-learning/nova-pks-upsert.md) — Learn interaction playbooks.
