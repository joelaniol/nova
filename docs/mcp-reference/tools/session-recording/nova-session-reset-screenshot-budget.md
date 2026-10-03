# `nova.session_reset_screenshot_budget`

Resets the session screenshot budget counter to allow fresh visual captures.

---

## 1. Overview

`nova.session_reset_screenshot_budget` clears the in-memory screenshot budget accumulator for the active MCP session. Nova enforces a bounded visual capture budget to prevent infinite visual capture loops or memory exhaustion; this tool re-arms the budget during extended testing sessions.

* **Capability Bundle:** `session_recording`, `visual_evidence`
* **Security Tier:** Tier 1 (Session Budget Control)
* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.session_reset_screenshot_budget",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Screenshot budget reset for the active MCP session."
    }
  ],
  "structuredContent": {
    "ok": true,
    "budgetLimit": 50,
    "consumed": 0,
    "remaining": 50
  }
}
```

---

## 4. Operational Best Practices

* **Post-Exhaustion Recovery:** Call when a multi-step test intentionally exhausts visual capture limits and requires fresh captures for subsequent phases.
* **Session-Scoped:** Only affects the current MCP client session; does not alter global configuration.

---

## 5. Related Tools

* [`nova.capture_screenshot`](../visual-evidence/nova-capture-screenshot.md) — Capture visual evidence.
* [`nova.screenshot_diff`](../visual-evidence/nova-screenshot-diff.md) — Pixel diffing.
