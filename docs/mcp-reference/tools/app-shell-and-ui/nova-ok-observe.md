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

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional metadata. Provide _meta.intent (a short reason) for high-impact tools. A tool's annotations.intentRequired in tools/list tells you up front: 'always' means intent is mandatory, 'conditional' means it becomes mandatory for certain arguments (e.g. includeValues=true), absent means never. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `claims` | `array` | **Yes** | Structured observations about the current page state. |
| `perceptionId` | `string,null` | No | Optional perception/trace ID to group claims from the same observation moment. Use null or omit when no trace grouping is available. |
| `targetId` | `string,null` | No | Tab ID, sandbox ID, or 'active'. Use null or omit for default 'active'. |

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
