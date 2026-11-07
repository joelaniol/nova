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
  "pluginId": "com.example.price-scanner",
  "status": "reverted",
  "unmountedOverlays": 2
}
```

---

## 4. Operational Best Practices

* **Complete Overlay Teardown:** Unmounts all active floating badges, custom sidebars, and shadow root containers created by the plugin, restoring the host DOM tree.
* **Ledger Synchronization:** Clears corresponding entries in `PluginMutationLedger` and marks mutations as reverted, ensuring accurate state in subsequent calls to `nova.plugin_inspect`.
* **Non-Destructive Execution:** Unlike disabling or uninstalling, resetting injections preserves the running plugin state, event listeners, and storage, making it ideal for temporary DOM cleanups.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
