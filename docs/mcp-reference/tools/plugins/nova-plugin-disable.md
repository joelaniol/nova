# `nova.plugin_disable`

> **Disable a plugin.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Disable a plugin. Stops the runtime if active, reverts all DOM/CSS mutations, and persists the disabled state.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID to disable. |
| `reason` | `string` | No | — | — | Optional human-readable reason for disabling. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "_meta": { "intent": "Disable scanner during portal redesign" },
  "pluginId": "com.example.price-scanner",
  "reason": "Temporary deactivation while site DOM is restructured"
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "pluginId": "com.example.price-scanner",
  "status": "disabled",
  "state": "disabled",
  "terminatedInstances": 1
}
```

---

## 4. Operational Best Practices

* **Immediate Instance Teardown:** Disabling immediately terminates all active Jint sandbox engines, unregisters event listeners, and unbinds dynamic MCP tools (`plugin.{pluginId}.*`).
* **Automatic Mutation Rollback:** All DOM classes, styles, and open Shadow DOM overlays injected by the disabled plugin are cleanly rolled back via Nova's `PluginMutationLedger`.
* **Auditability via `reason`:** Always supply a human-readable `reason` to record why the plugin was deactivated in the audit ledger.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
