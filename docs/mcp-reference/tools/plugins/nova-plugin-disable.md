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
  "plugin": {
    "pluginId": "com.example.price-scanner",
    "name": "Price Scanner",
    "version": "1.0.0",
    "installState": "Disabled",
    "runtimeState": "Inactive",
    "enabled": false,
    "errorCount": 0,
    "crashCount": 0,
    "permissions": ["StorageReadWrite"],
    "pendingPermissions": ["DomRead"],
    "pendingHostMatches": ["https://shop.example.com/*"],
    "permissionReviewRequired": true
  }
}
```

`plugin` is the plugin snapshot, shortened here. It also carries the session fields (`currentSession`, `activeSessions`, `lastKnownSession`, `knownSessions`), frame access, content-script counts and the granted and pending host, network and MCP-tool scopes.

---

## 4. Operational Best Practices

* **Immediate Instance Teardown:** Disabling sends the plugin a `disable` event for its own best-effort cleanup, then stops every running instance. Plugin-defined MCP tools (`plugin.{pluginId}.*`) are only listed while the plugin is active.
* **Tracked Changes Are Closed:** All page changes Nova tracked for the plugin are marked as reverted. To clean a page while the plugin keeps running, use [`nova.plugin_css_reset`](nova-plugin-css-reset.md) or [`nova.plugin_inject_reset`](nova-plugin-inject-reset.md) instead.
* **Auditability via `reason`:** Supply a short `reason`; it is logged and passed to the plugin's `disable` event.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
