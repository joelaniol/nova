# `nova.plugin_request_permission`

> **Grant review-gated permissions or scopes for an installed plugin.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Grant review-gated permissions or scopes for an installed plugin. Use this after plugin_create/import/update when requested capabilities still show up as pending in plugin_inspect. This tool can grant requested runtime permissions including RequestFilter for manifest.network.rules, approve manifest.hostPermissions.matches for auto-activation, approve manifest.network.allow for nova.net.fetch, and grant manifest.mcpTools entries one by one before plugin-defined tools become visible in tools/list. It only grants capabilities already declared by the plugin manifest; it never invents new permissions or removes existing grants.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID whose requested permissions or scopes to grant. |
| `permissions` | `array` of `string` | No | — | — | Optional exact permission enum names to grant from the plugin's requestedPermissions list. Typical review-gated values are DomRead, OverlayWrite, MutationClassWrite, MutationStyleWrite, NetworkFetch, NotifySend, FrameMatchedSubframes, and RequestFilter. |
| `mcpTools` | `array` of `string` | No | — | — | Optional exact manifest.mcpTools names to grant for agent use. A plugin-defined MCP tool only appears in tools/list and becomes callable after the plugin is active and that specific declared tool name has been approved here. |
| `grantHostPermissions` | `boolean` | No | `false` | — | If true, approve the plugin's declared hostPermissions.matches patterns so it can auto-activate on matching pages. Exclude patterns remain manifest-owned and are not independently grantable. |
| `grantNetworkAccess` | `boolean` | No | `false` | — | If true, approve the plugin's declared network.allow rules so nova.net.fetch can reach those URLs. Timeout/redirect/size limits still come from the manifest and host policy. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request

```json
{
  "_meta": { "intent": "Grant review-gated DOM and host permissions after manual review" },
  "pluginId": "com.example.price-scanner",
  "permissions": [
    "DomRead",
    "OverlayWrite"
  ],
  "grantHostPermissions": true,
  "grantNetworkAccess": true,
  "mcpTools": [
    "get_active_price"
  ]
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "alreadyGranted": false,
  "denied": false,
  "denyReason": null,
  "pluginId": "com.example.price-scanner",
  "grantedPermissions": ["StorageReadWrite", "DomRead", "OverlayWrite"],
  "grantedHostMatches": ["https://shop.example.com/*"],
  "grantedNetworkRules": [],
  "grantedMcpTools": ["get_active_price"],
  "pendingPermissions": [],
  "pendingHostMatches": [],
  "pendingNetworkRules": [],
  "pendingMcpTools": [],
  "permissionReviewRequired": false,
  "grantHostPermissions": true,
  "grantNetworkAccess": false,
  "requestedMcpTools": ["get_active_price"],
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
    "pendingPermissions": [],
    "pendingHostMatches": [],
    "permissionReviewRequired": false
  }
}
```

If the user declines, the result has `ok: false`, `denied: true`, `reasonCode: "plugin.permission_denied"` and a `denyReason`; nothing new is granted.

`plugin` is the plugin snapshot, shortened here. It also carries the session fields (`currentSession`, `activeSessions`, `lastKnownSession`, `knownSessions`), frame access, content-script counts and the granted and pending host, network and MCP-tool scopes.

---

## 4. Operational Best Practices

* **Mandatory Intent Clause:** As a `high_impact` operation, `_meta.intent` must always be provided with an explicit rationale explaining why elevated scopes are warranted; calls without it are rejected immediately.
* **Manifest-Bound Verification:** Permissions requested here must be pre-declared in the plugin's manifest; the host will never grant capabilities outside the plugin's declared scope.
* **Granular Principle of Least Privilege:** Grant permissions incrementally (approving specific `mcpTools` or `permissions` one by one) rather than blanket approvals, minimizing attack surfaces across web origins.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
