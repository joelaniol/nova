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
  "violationCount": 1,
  "autoDisableThreshold": 10,
  "violations": [
    {
      "timestamp": "2026-11-07T08:02:10Z",
      "kind": "url_blocked",
      "target": "https://unauthorized.tracker.example.com/collect",
      "reason": "Host not allowed by manifest.network.allow"
    }
  ]
}
```

---

## 4. Operational Best Practices

* **Auto-Disable Prevention:** The host automatically disables any plugin that triggers 10 or more security policy violations within 5 minutes. Periodically review `nova.plugin_security_log` during development to catch boundary rejections early.
* **Violation Taxonomy:** Inspect the `kind` field to distinguish between `permission_denied` (calling ungranted APIs), `quota_exceeded` (exceeding memory or storage limits), `url_blocked` (unauthorized fetch origins), and `oversize_attempt`.
* **Remediation Strategy:** When `url_blocked` or `permission_denied` appears in the log, update `manifest.json` and grant the required permissions via `nova.plugin_request_permission` rather than attempting to bypass host policies.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
