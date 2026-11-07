# `nova.plugin_managed_storage_get`

> **Read host-controlled managed storage for an installed plugin.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Read host-controlled managed storage for an installed plugin. This is the read-only data surfaced inside plugin JS as nova.storage.managed. Without 'key', returns the full managed key/value object; with 'key', returns just that single projected typed JSON value.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID whose managed storage to inspect. |
| `key` | `string` | No | — | — | Optional single managed storage key to read. Omit to return the full managed key/value object. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request

```json
{
  "_meta": { "intent": "Read managed configuration for enterprise compliance" },
  "pluginId": "com.example.price-scanner",
  "key": "apiEndpoint"
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "pluginId": "com.example.price-scanner",
  "key": "apiEndpoint",
  "exists": true,
  "value": "https://api.example.com/v1"
}
```

Without `key`, the result has `keyCount` and `values` (the whole managed key/value object) instead of `key`, `exists` and `value`.

---

## 4. Operational Best Practices

* **Host-Controlled Policy Inspection:** Use this tool to inspect enterprise policies or administrative configurations that are injected into the plugin runtime as read-only data (`nova.storage.managed`).
* **Selective vs. Full Retrieval:** Omit the `key` parameter to retrieve the complete managed key/value dictionary, or pass a specific `key` for targeted single-value lookup.
* **Immutable from Plugin JS:** Managed storage cannot be modified from the plugin's own JavaScript runtime; it serves as a secure one-way control channel from the host agent to the extension.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
