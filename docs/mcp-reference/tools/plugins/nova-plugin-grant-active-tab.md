# `nova.plugin_grant_active_tab`

> **Start an installed plugin on the current browser tab with temporary activeTab-style access.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Start an installed plugin on the current browser tab with temporary activeTab-style access. This is a session-only grant for the chosen tab and expires on the next top-level navigation. It never persists hostPermissions or network.allow approvals. Use it when a plugin needs page-scoped access on the current tab without granting permanent auto-activation.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The installed plugin ID to start with temporary activeTab access. |
| `targetId` | `string` | No | — | — | Optional browser-tab target. Defaults to the active browser tab. Accepts a tab ID or active-browser aliases like 'activeBrowserTab'. |
| `permissions` | `array` of `string` | No | — | — | Optional exact permission enum names to enable for this temporary session. Omit to grant all activeTab-compatible page permissions requested by the manifest. Allowed values are limited to DomRead, OverlayWrite, MutationClassWrite, and MutationStyleWrite. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## See Also

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins.md)
