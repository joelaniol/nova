# `nova.app_settings_set`

> **Changes Nova's app preferences the same way as the Settings page.**

* **User Guide:** [Settings](../../../user-guide/settings/README.md)
* **Architecture Guide:** [Agent Settings Governance & MCP](../../../user-guide/settings/agent-governance-and-mcp.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.app_settings_set` takes `values`, a map of setting key to new value (keys and allowed values come from `nova.app_settings_get`). The values are saved and the running app applies them at once, exactly as after a change in Settings. A call is applied completely or not at all.

The result lists every key with `previous`, `value` (read back after saving, not copied from the request) and `changed`. When every value was already set, `status` is `noop`.

Settings that guard the user against agents are read-only. A call that includes one is refused with `reasonCode: "app_settings.protected"`, names the setting with its `settingsLocation`, and writes nothing — also not the other values of that call. Tell the user where to change it instead.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `values` | `object` | Yes | — | — | Setting key -> new value, e.g. {"continueWhereLeftOff": true, "closeBehavior": "minimizeToTray"}. Keys and allowed values: nova.app_settings_get. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_app_settings_set",
  "arguments": { "values": { "continueWhereLeftOff": true, "closeBehavior": "minimizeToTray" } }
}
```

### JSON-RPC Response
```json
{
  "structuredContent": {
    "ok": true,
    "status": "applied",
    "applied": [
      { "key": "continueWhereLeftOff", "previous": false, "value": true, "changed": true },
      { "key": "closeBehavior", "previous": "ask", "value": "minimizeToTray", "changed": true }
    ]
  }
}
```

### Refused (protected setting)
```json
{
  "structuredContent": {
    "ok": false,
    "status": "refused",
    "reasonCode": "app_settings.protected",
    "message": "These settings guard the user against agents and can only be changed by the user in Settings. Nothing was written, also not the other values of this call.",
    "refused": [
      { "key": "recordAgentBrowsingInHistory", "reason": "The agent's trail in history is how the user sees what agents did.", "settingsLocation": "Settings > Privacy & Security" }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Change only what the user asked for:** these are the user's preferences; a change stays after the task.
* **Check `changed`, not just `ok`:** `noop` means the value was already in effect.

---

## 5. Related Tools

* [`nova.app_settings_get`](nova-app-settings-get.md)
* [`nova.permission_center_set`](nova-permission-center-set.md)
