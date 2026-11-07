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
  "plugin": {
    "pluginId": "com.example.price-scanner",
    "name": "Price Scanner",
    "version": "1.0.0",
    "installState": "Installed",
    "runtimeState": "Active",
    "enabled": true,
    "errorCount": 0,
    "crashCount": 0,
    "permissions": ["StorageReadWrite"],
    "pendingPermissions": ["DomRead"],
    "pendingHostMatches": ["https://shop.example.com/*"],
    "permissionReviewRequired": true
  },
  "currentSession": null,
  "activeSessions": [],
  "storageKeyCount": 5,
  "managedStorageKeyCount": 0,
  "errorCount": 0,
  "activeMutationCount": 2,
  "recentMutations": [
    { "kind": "ClassAdd", "selector": ".price", "createdAtUtc": "2026-11-07T08:00:00.0000000Z", "reverted": false }
  ],
  "versionHistory": [
    { "historyId": 1, "version": "1.0.0", "changeNote": "Initial code via plugin_create", "sourceFileCount": 0, "sourceStored": true, "createdAtUtc": "2026-11-07T07:55:00.0000000Z" }
  ],
  "contentScriptInventory": { "...": "declared and dynamic content scripts vs. live frames" },
  "manifest": { "id": "com.example.price-scanner", "version": "1.0.0", "entryPoint": "index.js", "...": "..." },
  "permissions": ["StorageReadWrite"],
  "pendingPermissions": ["DomRead"],
  "permissionReviewRequired": true
}
```

Shortened. The full result also lists `lastKnownSession`, `knownSessions`, `requestFilter` and every granted and pending host, network and MCP-tool scope.

---

## 4. Operational Best Practices

* **Pre-Flight Health Audit:** Use `nova.plugin_inspect` before performing updates or sensitive workflow steps to verify current permissions, active content script frames, and runtime execution state.
* **Resource Leak Detection:** Watch `activeMutationCount` and `storageKeyCount` across workflow cycles to see whether the plugin leaves page changes behind or keeps growing its storage.
* **History & Snapshot Verification:** Review the detailed manifest and version metadata to identify target `historyId` records prior to initiating rollbacks via `nova.plugin_rollback`.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
