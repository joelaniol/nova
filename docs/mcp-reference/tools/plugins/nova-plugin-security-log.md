# `nova.plugin_security_log`

> **Read recent security policy violations recorded by the bridge enforcement layer (permission_denied, quota_exceeded, url_blocked, script_blocked, redirect_blocked, oversize_attempt).**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
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
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request

```json
{
  "_meta": { "intent": "Inspect security violations causing auto-disable" },
  "pluginId": "com.example.price-scanner",
  "limit": 50
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "pluginId": "com.example.price-scanner",
  "eventCount": 1,
  "recentCount": 1,
  "autoDisableThreshold": 10,
  "recentWindowMinutes": 5,
  "entries": [
    {
      "entryId": 3,
      "kind": "url_blocked",
      "detail": "https://tracker.example.net/collect",
      "createdAtUtc": "2026-11-07T08:02:10.0000000Z"
    }
  ]
}
```

---

## 4. Operational Best Practices

* **Auto-Disable Prevention:** The host automatically disables any plugin that triggers 10 or more security policy violations within 5 minutes. Periodically review `nova.plugin_security_log` during development to catch boundary rejections early.
* **Violation Taxonomy:** The `kind` field tells the cause, for example `permission_denied` (an API without the grant), `quota_exceeded`, `url_blocked` (a fetch outside `network.allow`), `redirect_blocked`, `script_blocked` and `oversize_attempt`.
* **Remediation Strategy:** When `url_blocked` or `permission_denied` appears, declare the missing scope in the manifest via [`nova.plugin_update`](nova-plugin-update.md) and grant it via [`nova.plugin_request_permission`](nova-plugin-request-permission.md).

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
