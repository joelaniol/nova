# `nova.plugin_inspect`

> **Detailed inspection of a plugin: full state snapshot, manifest details, granted permissions, contentScriptInventory for static/dynamic scripts vs active/known live frames, plugin storage key counts (persistent KV plus host-managed keys), active mutation count, and recent mutations.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
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

## 3. Protocol Usage

### JSON-RPC Request

```json
{
  "_meta": { "intent": "Inspect plugin runtime state and permissions" },
  "pluginId": "com.example.price-scanner"
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "pluginId": "com.example.price-scanner",
  "state": "enabled",
  "version": "1.2.0",
  "grantedPermissions": [
    "DomRead",
    "OverlayWrite"
  ],
  "activeMutations": 2,
  "storageKeyCount": 5,
  "contentScriptInventory": {
    "staticScripts": [
      "content.js"
    ],
    "activeFrames": 1
  }
}
```

---

## 4. Operational Best Practices

* **Pre-Flight Health Audit:** Use `nova.plugin_inspect` before performing updates or sensitive workflow steps to verify current permissions, active content script frames, and runtime execution state.
* **Resource Leak Detection:** Monitor `activeMutations` and `storageKeyCount` across workflow cycles to ensure the plugin is not leaving abandoned DOM nodes or accumulating unbounded storage keys.
* **History & Snapshot Verification:** Review the detailed manifest and version metadata to identify target `historyId` records prior to initiating rollbacks via `nova.plugin_rollback`.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
