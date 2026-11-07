# `nova.plugin_managed_storage_update`

> **Create, update, or delete host-controlled managed storage values for an installed plugin.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Create, update, or delete host-controlled managed storage values for an installed plugin. Plugins can read these values through nova.storage.managed.get/keys but cannot write them themselves. Updates also emit storage.onChanged events with areaName='managed' into already running plugin runtimes.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID whose managed storage to change. |
| `values` | `object` | No | — | — | Optional object of managed storage values to upsert. Each property value may be any JSON-compatible plain data and is projected back to plugin JS as typed data. |
| `deleteKeys` | `array` of `string` | No | — | — | Optional exact managed storage keys to delete. Keys that also appear in values are updated, not deleted. |
| `clearExisting` | `boolean` | No | `false` | — | If true, delete all existing managed keys first except any keys being re-written in values. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request

```json
{
  "_meta": { "intent": "Update enterprise backend URL and clear obsolete flags" },
  "pluginId": "com.example.price-scanner",
  "values": {
    "apiEndpoint": "https://api-prod.internal.example.com/v2",
    "telemetryEnabled": true
  },
  "deleteKeys": [
    "betaFeatures"
  ],
  "clearExisting": false
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "pluginId": "com.example.price-scanner",
  "changedKeyCount": 3,
  "updatedKeys": ["apiEndpoint", "refreshMinutes"],
  "deletedKeys": ["betaFeatures"],
  "keyCount": 2
}
```

---

## 4. Operational Best Practices

* **One Call per Configuration Change:** Combine `values`, `deleteKeys` and `clearExisting` in a single call. A key that is in both `values` and `deleteKeys` is updated, not deleted.
* **Reactive Event Dispatch:** Updates automatically emit `storage.onChanged` events with `areaName='managed'` into running plugin engines, enabling live configuration reloads without restarting the plugin.
* **Complete Overwrites:** Set `clearExisting: true` when enforcing a pristine policy state, purging any obsolete or stray configuration keys previously written.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
