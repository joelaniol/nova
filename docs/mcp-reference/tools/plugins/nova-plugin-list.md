# `nova.plugin_list`

> **List all installed agent-authored plugins with their install state, runtime state, permissions, and error/crash counts.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

List all installed agent-authored plugins with their install state, runtime state, permissions, and error/crash counts.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `includeUninstalled` | `boolean` | No | `false` | — | If true, also include previously uninstalled plugins from the database. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request

```json
{
  "_meta": { "intent": "List all active and uninstalled plugins" },
  "includeUninstalled": true
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "pluginCount": 1,
  "plugins": [
    {
      "pluginId": "com.example.price-scanner",
      "name": "Price Scanner",
      "version": "1.2.0",
      "installState": "Installed",
      "runtimeState": "Active",
      "enabled": true,
      "errorCount": 0,
      "crashCount": 0
    }
  ]
}
```

Each entry is a plugin snapshot (shortened here). With `includeUninstalled: true`, uninstalled plugins appear with `installState: "Uninstalled"` and `runtimeState: "Inactive"`.

---

## 4. Operational Best Practices

* **Initial Catalog Discovery:** Call `nova.plugin_list` at the start of a session to see the installed plugins, their versions, `installState` (`Testing`, `Installed`, `Disabled`, ...) and `runtimeState` (`Inactive`, `Active`, `Crashed`, ...).
* **Stability Monitoring:** Periodically check the `crashCount` field across listed plugins; plugins with non-zero crash counts should be inspected and tested in isolation before continuing production flows.
* **Tombstone Auditing:** Set `includeUninstalled: true` when checking whether a previously removed extension can be revived or if its ID is already registered in historical records.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
