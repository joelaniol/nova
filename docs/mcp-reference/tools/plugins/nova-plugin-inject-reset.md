# `nova.plugin_inject_reset`

> **Unmount all overlay elements injected by a plugin.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Unmount all overlay elements injected by a plugin. Marks overlay mutations as reverted in the ledger.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID whose overlay injections to reset. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request

```json
{
  "_meta": { "intent": "Unmount all injected overlay elements" },
  "pluginId": "com.example.price-scanner"
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "status": "reset",
  "pluginId": "com.example.price-scanner",
  "reasonCode": null,
  "activeMutationCount": 0,
  "activePageSessionCount": 1,
  "cleanupAttemptedSessions": 1,
  "cleanupSucceededSessions": 1,
  "pageCleanupCount": 1,
  "revertedCount": 1,
  "unsupportedMutationCount": 0,
  "warning": null
}
```

`status` is `reset` after a real page cleanup, `partial` when the cleanup could not be fully applied (see `reasonCode`), and `noop` when there was nothing to reset.

---

## 4. Operational Best Practices

* **Overlay Teardown:** Removes the overlays the plugin mounted on its active pages. Injected CSS is handled by [`nova.plugin_css_reset`](nova-plugin-css-reset.md).
* **Honest Result:** The tracked overlay changes are only marked as reverted after a real page cleanup ran; otherwise the result is `partial` or `noop`. `nova.plugin_inspect` then shows the updated `activeMutationCount`.
* **Non-Destructive Execution:** Unlike disabling or uninstalling, resetting injections preserves the running plugin state, event listeners, and storage, making it ideal for temporary DOM cleanups.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
