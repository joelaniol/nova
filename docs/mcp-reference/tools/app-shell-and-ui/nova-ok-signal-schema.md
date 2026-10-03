# `nova.ok_signal_schema`

> **Lists the canonical Operational Knowledge signal keys accepted by nova.ok_observe.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 1 (Read-Only Schema)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ok_signal_schema` returns all valid telemetry keys, parameter constraints, and description semantics for semantic page reporting.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional metadata. Provide _meta.intent (a short reason) for high-impact tools. A tool's annotations.intentRequired in tools/list tells you up front: 'always' means intent is mandatory, 'conditional' means it becomes mandatory for certain arguments (e.g. includeValues=true), absent means never. |
| `includeDeprecated` | `boolean` | No | Whether deprecated canonical keys should be included. |
| `maxEntries` | `integer` | No | Maximum number of schema entries returned. |
| `namespace` | `string,null` | No | Optional canonical namespace filter, for example 'core'. Use null or omit to list all namespaces. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ok_signal_schema",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Accepted signal keys: 18 canonical keys returned."
    }
  ],
  "structuredContent": {
    "ok": true,
    "keys": [
      "modal_blocker_detected",
      "captcha_challenge_active",
      "infinite_scroll_exhausted",
      "spa_route_transitioning"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Schema Validation:** Always reference this schema before generating programmatic observations.

---

## 5. Related Tools

* [`nova.ok_observe`](nova-ok-observe.md)
