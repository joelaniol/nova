# `nova.plugin_import`

> **Import a plugin from a base64-encoded .novaplugin ZIP bundle.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Import a plugin from a base64-encoded .novaplugin ZIP bundle. Validates manifest, installs the plugin with auto-grant permissions only, and optionally restores persistent KV data such as typed storage.local / storage.sync snapshots. Review-gated permissions plus host/network scopes remain pending until nova.plugin_request_permission approves them.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `bundleBase64` | `string` | Yes | — | — | Base64-encoded .novaplugin ZIP bundle. |
| `overwrite` | `boolean` | No | `false` | — | If true, overwrite an existing plugin with the same ID. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request

```json
{
  "_meta": { "intent": "Import trusted pricing assistant bundle" },
  "bundleBase64": "UEsDBBQAAAAIA...",
  "overwrite": true
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
    "installState": "Installed",
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

* **Mandatory Intent Clause:** As a `high_impact` operation, `_meta.intent` must always be provided with a concise explanation; calls missing it are rejected immediately.
* **Two-Stage Activation Pipeline:** Imported plugins start with auto-grant permissions only; review-gated permissions (e.g. `DomRead`), host and network scopes and MCP tools stay pending until granted via [`nova.plugin_request_permission`](nova-plugin-request-permission.md). A storage snapshot in the bundle is restored with the plugin.
* **Safeguarded Overwrites (`overwrite`):** By default (`overwrite: false`), importing fails if a plugin with the same ID already exists, guarding against accidental state clobbering. Set `overwrite: true` only during intentional version replacements.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
