# `nova.plugin_security_log`

> **Read recent security policy violations recorded by the bridge enforcement layer (permission_denied, quota_exceeded, url_blocked, script_blocked, redirect_blocked, oversize_attempt).**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Read recent security policy violations recorded by the bridge enforcement layer (permission_denied, quota_exceeded, url_blocked, script_blocked, redirect_blocked, oversize_attempt). Auto-disable gate triggers when 10+ events occur within 5 minutes — use this tool to debug why a plugin was auto-disabled and to discover which manifest grants or network.allow rules need to be added.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID whose security log to query. |
| `limit` | `integer` | No | `50` | 1–200 | Maximum number of log entries to return (newest first). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
<!-- /generated:parameters -->

---

## See Also

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins.md)
