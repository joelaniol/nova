# `nova.plugin_export`

> **Export a plugin as a base64-encoded .novaplugin ZIP bundle containing manifest, source code, and optionally persistent KV storage data (including typed storage.local / storage.sync snapshots).**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Export a plugin as a base64-encoded .novaplugin ZIP bundle containing manifest, source code, and optionally persistent KV storage data (including typed storage.local / storage.sync snapshots).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID to export. |
| `includeKvData` | `boolean` | No | `false` | — | If true, include the plugin's persistent key-value storage snapshot in the bundle, including typed storage.local / storage.sync data. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
<!-- /generated:parameters -->

---

## See Also

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins.md)
