# `nova.plugin_inspect`

> **Detailed inspection of a plugin: full state snapshot, manifest details, granted permissions, contentScriptInventory for static/dynamic scripts vs active/known live frames, plugin storage key counts (persistent KV plus host-managed keys), active mutation count, and recent mutations.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Detailed inspection of a plugin: full state snapshot, manifest details, granted permissions, contentScriptInventory for static/dynamic scripts vs active/known live frames, plugin storage key counts (persistent KV plus host-managed keys), active mutation count, and recent mutations.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID to inspect. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## See Also

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins.md)
