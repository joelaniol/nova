# `nova.plugin_uninstall`

> **Uninstall a plugin.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Uninstall a plugin. Marks it as uninstalled in the database and optionally deletes all plugin files and data from disk.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID to uninstall. |
| `deleteData` | `boolean` | No | `false` | — | If true, also delete plugin files and data directory from disk. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request

```json
{
  "_meta": { "intent": "Uninstall obsolete scraper and clean storage" },
  "pluginId": "com.example.old-scraper",
  "deleteData": true
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "pluginId": "com.example.old-scraper",
  "status": "uninstalled",
  "dataDeleted": true
}
```

---

## 4. Operational Best Practices

* **Mandatory Intent Clause:** Because `nova.plugin_uninstall` is classified as `high_impact`, passing `_meta.intent` is strictly required by the host runtime; missing intent results in immediate call rejection.
* **Data Retention vs. Purge (`deleteData`):** By default (`deleteData: false`), plugin configuration, logs, and database records are retained so re-installation preserves state. Use `deleteData: true` only when permanently decommissioning the extension.
* **Cascading Cleanup:** Uninstallation immediately shuts down running engine instances, deregisters dynamic MCP tools (`plugin.{pluginId}.*`), and rolls back any active DOM/CSS injections recorded in the mutation ledger.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
