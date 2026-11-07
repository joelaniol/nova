# `nova.plugin_rollback`

> **Restore an installed plugin to a specific snapshot from plugin_version_history.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Restore an installed plugin to a specific snapshot from plugin_version_history. Snapshots include the manifest, legacy entry-point source, and declared sourceFiles\[\] for contentScripts. Use plugin_inspect.versionHistory or plugin_get_version_code to choose the historyId first. Rollback snapshots the current manifest/source before restoring the historical entry, re-registers the plugin, and can optionally keep the restored version in Testing via deferActivation=true.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID to roll back. |
| `historyId` | `integer` | Yes | — | ≥ 1 | The history entry ID from plugin_inspect.versionHistory[].historyId to restore. |
| `changeNote` | `string` | No | — | — | Optional human-readable rollback note (max 500 chars). Stored on the snapshot that captures the current version before restore. |
| `deferActivation` | `boolean` | No | `false` | — | If true and the plugin is currently Installed, keep the restored version in Testing so it does not auto-activate again until a passing smoke run or plugin_enable promotes it. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "_meta": { "intent": "Revert to stable version after runtime exception" },
  "pluginId": "com.example.price-scanner",
  "historyId": 1,
  "changeNote": "Reverted 1.0.1 due to null selector exception",
  "deferActivation": true
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "pluginId": "com.example.price-scanner",
  "historyId": 1,
  "restoredVersion": "1.0.0",
  "restoredChangeNote": "Initial code via plugin_create",
  "restoredCreatedAtUtc": "2026-11-07T07:55:00.0000000Z",
  "sourceRestored": true,
  "sourceFileCount": 0,
  "sourceFilesRestored": 0,
  "deferActivation": true,
  "plugin": {
    "pluginId": "com.example.price-scanner",
    "name": "Price Scanner",
    "version": "1.0.0",
    "installState": "Testing",
    "runtimeState": "Inactive",
    "enabled": true,
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

* **Non-Destructive History:** Rolling back erases nothing. Before restoring, Nova saves the current manifest and source as a new history entry (with your `changeNote`), so the rollback itself can be undone.
* **Post-Rollback Safe Gating (`deferActivation: true`):** For an `Installed` plugin, `deferActivation: true` keeps the restored version in `Testing` until a passing smoke test or `nova.plugin_enable` promotes it.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
