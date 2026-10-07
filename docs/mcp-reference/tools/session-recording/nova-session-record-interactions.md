# `nova.session_record_interactions`

Reads the chronological interaction timeline (clicks, typing, form submits) from a recording.

---

## 1. Overview

`nova.session_record_interactions` reconstructs the sequence of physical and programmatic interactions executed during a session. It unifies both user-driven DOM inputs (`source: "user_dom"`) and agent MCP tool calls (`source: "mcp"`), providing an audit trail of actions leading up to any event.

* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording/README.md)

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

Capability bundle: `session_recording` (load it with `nova.tools_bundle(bundle='session_recording')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
      "text": "Recording rec-9b21f04a: interactions returned 2 of 2 matching entry/entries."
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordingId": "rec-9b21f04a",
    "totalMatchCount": 2,
    "count": 2,
    "entries": [
      {
        "ts": "2026-10-02T20:16:05Z",
        "source": "mcp",
        "type": "nova.click_selector",
        "targetSelector": "#checkout-btn",
        "argsRedacted": "{\"selector\":\"#checkout-btn\"}"
      },
      {
        "ts": "2026-10-02T20:17:10Z",
        "source": "user_dom",
        "type": "click",
        "targetSelector": ".submit-payment",
        "role": "button",
        "value": null,
        "viewportX": 510,
        "viewportY": 820
      }
    ]
  }
}
```

Note the top-level field is `entries`, not `interactions`; `source: "mcp"` rows carry `argsRedacted` (the tool's arguments with sensitive values replaced), while `source: "user_dom"` rows carry `role`/`value`/`viewportX`/`viewportY` instead.

---

## 4. Operational Best Practices

* **Playbook Generation:** Use interaction sequences from successful human sessions to inform PKS phenomenon fast-paths.
* **Reproduction Steps:** Review agent and human actions sequentially to reproduce race conditions or intermittent failures.
* **Redaction Assurance:** A typed value that exactly matches a secret already stored in Nova's vault is replaced with a `[redacted:vault-fingerprint:<hash>]` token. This is a whole-value vault match, not a blanket password-field filter — a value that isn't in the vault is not redacted by this mechanism.

---

## 5. Related Tools

* [`nova.session_record_events`](nova-session-record-events.md) — Inspect console and system logs.
* [`nova.pks_upsert`](../pks-and-learning/nova-pks-upsert.md) — Learn interaction playbooks.
