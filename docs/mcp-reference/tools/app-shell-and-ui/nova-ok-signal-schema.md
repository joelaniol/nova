# `nova.ok_signal_schema`

> **Lists the canonical Operational Knowledge signal keys accepted by nova.ok_observe.**

* **Core Feature Guide:** [Operational Knowledge](../../../core-features/operational-knowledge-ok/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ok_signal_schema` lists the canonical `core.*` signal keys that `nova.ok_observe` accepts, each with its namespace, value type, description, and an example value. Platform-specific `vendor.*` keys are accepted by `nova.ok_observe` without being registered here.

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
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
      "text": "OK signal schema: 14 key(s)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "namespaceFilter": null,
    "includeDeprecated": false,
    "maxEntries": 200,
    "count": 14,
    "truncated": false,
    "keys": [
      {
        "signalKey": "core.login_state",
        "namespace": "core",
        "valueType": "string",
        "description": "Login state of the service",
        "exampleJson": "\"logged_in\"",
        "deprecated": false
      },
      {
        "signalKey": "core.plan.tier",
        "namespace": "core",
        "valueType": "string",
        "description": "Normalized plan tier",
        "exampleJson": "\"pro\"",
        "deprecated": false
      }
    ]
  }
}
```

This example shortens `keys` to two entries; the real response lists every matching canonical key (account, model, plan, session, page, UI, subscription, and feature signals, among others).

---

## 4. Operational Best Practices

* **Schema Validation:** Always reference this schema before generating programmatic observations.

---

## 5. Related Tools

* [`nova.ok_observe`](nova-ok-observe.md)
