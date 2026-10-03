# `nova.ok_signal_schema`

> **Lists the canonical Operational Knowledge signal keys accepted by nova.ok_observe.**

* **Security Tier:** Tier 1 (Read-Only Schema)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ok_signal_schema` returns all valid telemetry keys, parameter constraints, and description semantics for semantic page reporting.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `namespace` | `string or null` | No | — | — | Optional canonical namespace filter, for example 'core'. Use null or omit to list all namespaces. |
| `includeDeprecated` | `boolean` | No | `false` | — | Whether deprecated canonical keys should be included. |
| `maxEntries` | `integer` | No | `200` | 1–500 | Maximum number of schema entries returned. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
<!-- /generated:parameters -->

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
