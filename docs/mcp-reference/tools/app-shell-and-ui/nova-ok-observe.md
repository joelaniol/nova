# `nova.ok_observe`

> **Pushes a structured Operational Knowledge (OK) signal about page state, blocking patterns, or layout shifts.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Telemetry Ingestion)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ok_observe` feeds semantic telemetry into Nova's heuristic adaptation engine. Informs the browser about detected captchas, dynamic layouts, or slow loading triggers.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string or null` | No | `"active"` | — | Tab ID, sandbox ID, or 'active'. Use null or omit for default 'active'. |
| `perceptionId` | `string or null` | No | — | — | Optional perception/trace ID to group claims from the same observation moment. Use null or omit when no trace grouping is available. |
| `claims` | `array` of `object` | Yes | — | ≥ 1 items | Structured observations about the current page state. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ok_observe",
  "arguments": {
    "targetId": "tab-1",
    "signalKey": "modal_blocker_detected",
    "confidence": 0.95,
    "metadata": {
      "selector": ".newsletter-modal"
    }
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Ingested OK signal: modal_blocker_detected."
    }
  ],
  "structuredContent": {
    "ok": true,
    "signalKey": "modal_blocker_detected",
    "accepted": true
  }
}
```

---

## 4. Operational Best Practices

* **Signal Keys:** Query `nova.ok_signal_schema` first to verify canonical signal names.
* **Confidence Weight:** Only submit signals with confidence >= 0.8 to prevent telemetry noise.

---

## 5. Related Tools

* [`nova.ok_signal_schema`](nova-ok-signal-schema.md)
* [`nova.dismiss_blockers`](../browser-automation/nova-dismiss-blockers.md)
