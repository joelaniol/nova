# `nova.plugin_create`

> **Create and install a new agent-authored plugin from a manifest JSON string.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Create and install a new agent-authored plugin from a manifest JSON string. Required manifest fields: id (regex \[a-z\]\[a-z0-9._-\]{1,62}\[a-z0-9\]), version (semver), name, entryPoint (JS filename). Optional: requestedPermissions (DomRead, OverlayWrite, MutationClassWrite, MutationStyleWrite, StorageReadWrite, NetworkFetch, NotifySend, BadgeWrite, FrameMatchedSubframes, RequestFilter), hostPermissions.matches (Chrome-style globs like 'https://example.com/\*' for auto-activation) plus hostPermissions.frameAccess (TopLevelOnly or MatchedSubframes) with optional allFrames/frameIds subframe targeting, contentScripts\[\] (optional src-relative JS files with matches/excludeMatches/runAt/allFrames/frameIds), network.allow (HTTPS-only allowlist for nova.net.fetch), network.rules (declarative page request Block/Allow/UpgradeScheme filters, requires RequestFilter), lifecycle (timeouts/memory + runAt: documentStart\|documentEnd\|documentIdle), storage (quota), ui (allowOverlay), mcpTools (max 10, declares custom MCP tools the agent can call as 'plugin.{pluginId}.{toolName}' once active — plugin JS must call nova.tools.register(name, handler) to bind each one). Install now starts with auto-grant permissions only (for example StorageReadWrite/BadgeWrite when requested); review-gated permissions plus host/network scopes stay pending until nova.plugin_request_permission approves them. Provide 'code' for the entry-point JS and/or 'files' for additional src-relative source files. Read nova.reference_doc_read(docId='plugins') for the full schema and bridge API reference (nova.dom incl. observe/unobserve, nova.overlay, nova.mutation, nova.storage local/sync/session/managed scopes, nova.diag, nova.net, nova.on, nova.alarms).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `manifest` | `string` | Yes | — | — | Full plugin manifest as a JSON string. Must include id, version, name, and entryPoint. |
| `code` | `string` | No | — | — | Optional initial entry-point JavaScript source. If provided, written immediately after install (equivalent to plugin_create + plugin_update in one call). |
| `files` | `object` | No | — | — | Optional map of src-relative JavaScript file paths to source strings. Use this for manifest.contentScripts[] files such as {'code/content.js':'...'}; paths must stay inside the plugin src directory. |
| `deferActivation` | `boolean` | No | `false` | — | If true, create the plugin in Testing state instead of Installed so it cannot auto-activate on matching pages until a passing smoke test promotes it via activateAfterPass=true or plugin_enable. |
| `agentId` | `string` | No | — | — | Optional agent identifier for tracking which agent created this plugin. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "_meta": { "intent": "Install pricing extraction extension" },
  "manifest": "{\n  \"id\": \"com.example.price-scanner\",\n  \"version\": \"1.0.0\",\n  \"name\": \"Price Scanner\",\n  \"entryPoint\": \"index.js\",\n  \"requestedPermissions\": [\"DomRead\", \"StorageReadWrite\"],\n  \"hostPermissions\": { \"matches\": [\"https://shop.example.com/*\"] }\n}",
  "code": "var handles = JSON.parse(nova.dom.querySelectorAll('.price', 1));\nif (handles.length > 0) {\n  nova.storage.local.set('lastPrice', nova.dom.getTextContent(handles[0]));\n}",
  "deferActivation": true
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "pluginId": "com.example.price-scanner",
  "installState": "Testing",
  "installPath": "...\\plugins\\com.example.price-scanner",
  "deferActivation": true,
  "codeWritten": true,
  "sourceFileCount": 0,
  "warning": null,
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

* **Staged Activation Pattern (`deferActivation: true`):** Always create new plugins with `deferActivation: true`. This initializes the extension in the `Testing` state, preventing unvetted code from running automatically on live user tabs until verified via [`nova.plugin_test`](nova-plugin-test.md).
* **Two-Tier Permission Model:** Installation grants only Auto-Grant permissions (such as `StorageReadWrite` or `BadgeWrite`). Review-gated permissions (such as `DomRead`, `NetworkFetch`, or `OverlayWrite`) and host permissions remain `pending` until approved via [`nova.plugin_request_permission`](nova-plugin-request-permission.md).
* **Reverse-DNS Identifier Constraint:** Plugin IDs must match regex `[a-z][a-z0-9._-]{1,62}[a-z0-9]` (e.g. `com.vendor.workflow-helper`). Malformed IDs fail immediately with `-32602`.
* **Mandatory Intent Field:** Calls to `plugin_create` require `_meta.intent`. Omission results in pre-dispatch validation rejection.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
