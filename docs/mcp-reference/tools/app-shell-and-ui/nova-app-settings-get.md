# `nova.app_settings_get`

> **Reads Nova's app preferences and tells the agent which of them it may change.**

* **User Guide:** [Settings](../../../user-guide/settings/README.md)
* **Architecture Guide:** [Agent Settings Governance & MCP](../../../user-guide/settings/agent-governance-and-mcp.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.app_settings_get` lists Nova's own preferences: whether the last tabs reopen at startup, what closing the window does, where links from other programs open, the search engine, sleeping tabs and a few more. Each entry carries its current `value`, `type`, `allowedValues`, `writable`, `settingsLocation` (where the user finds it in Settings) and a `description`.

Settings that guard the user against agents — agent remote control, approval prompts, agent visits in history, developer options, the password vault, media and update protections — are listed too, with `writable: false` and a `readOnlyReason`. Only the user changes them.

The list is curated (`coverage: "curated"`), not every Nova setting. Permissions, auto-reload, the terminal and download auto-open have their own tools.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `keys` | `array` of `string` | No | — | — | Optional: only these setting keys (as returned by a call without keys). Omit for all. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_app_settings_get",
  "arguments": { "keys": ["continueWhereLeftOff", "mcpRemoteControlEnabled"] }
}
```

### JSON-RPC Response
```json
{
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "settings": [
      {
        "key": "continueWhereLeftOff",
        "value": false,
        "type": "boolean",
        "allowedValues": null,
        "writable": true,
        "readOnlyReason": null,
        "settingsLocation": "Settings > General > Startup and closing",
        "description": "Reopen the last session's tabs without asking at the next start after a normal exit. ..."
      },
      {
        "key": "mcpRemoteControlEnabled",
        "value": true,
        "type": "boolean",
        "allowedValues": null,
        "writable": false,
        "readOnlyReason": "Agent access itself is the user's decision.",
        "settingsLocation": "Settings > AI & agents",
        "description": "Whether agents may control Nova over MCP at all."
      }
    ],
    "coverage": "curated",
    "note": "Curated list, not every Nova setting. ..."
  }
}
```

---

## 4. Operational Best Practices

* **Read before you write:** take the key and an entry of `allowedValues` from here, then change it with `nova.app_settings_set`.
* **A missing setting is not absent:** the list is curated. Search with `nova.tools_bundle(query='...')` for a dedicated tool before telling the user it cannot be changed.

---

## 5. Related Tools

* [`nova.app_settings_set`](nova-app-settings-set.md)
* [`nova.permission_center_get`](nova-permission-center-get.md)
