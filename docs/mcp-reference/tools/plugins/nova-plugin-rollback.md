# `nova.plugin_rollback`

> **Restore an installed plugin to a specific snapshot from plugin_version_history.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Restore an installed plugin to a specific snapshot from plugin_version_history. Snapshots include the manifest, legacy entry-point source, and declared sourceFiles\[\] for contentScripts. Use plugin_inspect.versionHistory or plugin_get_version_code to choose the historyId first. Rollback snapshots the current manifest/source before restoring the historical entry, re-registers the plugin, and can optionally keep the restored version in Testing via deferActivation=true.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID to roll back. |
| `historyId` | `integer` | Yes | — | ≥ 1 | The history entry ID from plugin_inspect.versionHistory[].historyId to restore. |
| `changeNote` | `string` | No | — | — | Optional human-readable rollback note (max 500 chars). Stored on the snapshot that captures the current version before restore. |
| `deferActivation` | `boolean` | No | `false` | — | If true and the plugin is currently Installed, keep the restored version in Testing so it does not auto-activate again until a passing smoke run or plugin_enable promotes it. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## See Also

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
