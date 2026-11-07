# `nova.plugin_grant_active_tab`

> **Start an installed plugin on the current browser tab with temporary activeTab-style access.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Start an installed plugin on the current browser tab with temporary activeTab-style access. This is a session-only grant for the chosen tab and expires on the next top-level navigation. It never persists hostPermissions or network.allow approvals. Use it when a plugin needs page-scoped access on the current tab without granting permanent auto-activation.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The installed plugin ID to start with temporary activeTab access. |
| `targetId` | `string` | No | — | — | Optional browser-tab target. Defaults to the active browser tab. Accepts a tab ID or active-browser aliases like 'activeBrowserTab'. |
| `permissions` | `array` of `string` | No | — | — | Optional exact permission enum names to enable for this temporary session. Omit to grant all activeTab-compatible page permissions requested by the manifest. Allowed values are limited to DomRead, OverlayWrite, MutationClassWrite, and MutationStyleWrite. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request

```json
{
  "_meta": { "intent": "Temporarily grant active tab DOM access for price check" },
  "pluginId": "com.example.price-scanner",
  "targetId": "active",
  "permissions": [
    "DomRead",
    "OverlayWrite"
  ]
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "pluginId": "com.example.price-scanner",
  "targetId": "tab-8472",
  "url": "https://shop.example.com/item/42",
  "origin": "https://shop.example.com",
  "temporaryPermissions": ["DomRead", "OverlayWrite"],
  "expiresOnNextNavigation": true,
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
  }
}
```

`plugin` is the plugin snapshot, shortened here. It also carries the session fields (`currentSession`, `activeSessions`, `lastKnownSession`, `knownSessions`), frame access, content-script counts and the granted and pending host, network and MCP-tool scopes.

---

## 4. Operational Best Practices

* **Ephemeral Session-Only Access:** Grants issued via `nova.plugin_grant_active_tab` exist only for the specified tab and automatically expire on the next top-level navigation, preventing unintended cross-site privilege leakage.
* **Scoped Permission Subset:** Only page-scoped permissions (`DomRead`, `OverlayWrite`, `MutationClassWrite`, `MutationStyleWrite`) are allowed, and only those the manifest requests. Omit `permissions` to get all of them; host and network approvals are never granted this way.
* **Target Identification:** Without `targetId` the grant goes to the active browser tab. Pass a tab ID to target another tab without changing focus.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
