# `nova.plugin_get_version_code`

> **Read a specific historical snapshot of a plugin's code + manifest from plugin_version_history.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Read a specific historical snapshot of a plugin's code + manifest from plugin_version_history. Use plugin_inspect.versionHistory to discover historyIds. Returns the full manifest_json, legacy source_code, sourceFiles\[\] for declared entryPoint/contentScripts files, and change_note that was captured before that update — essential for rollback, side-by-side comparison, or recovering from a bad update.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID whose version history to read. |
| `historyId` | `integer` | Yes | — | ≥ 1 | The history entry ID from plugin_inspect.versionHistory[].historyId. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
<!-- /generated:parameters -->

---

## See Also

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins.md)
