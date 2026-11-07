# `nova.plugin_css_reset`

> **Remove the plugin's host-owned injected stylesheet from active page sessions.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Remove the plugin's host-owned injected stylesheet from active page sessions. If class/inline-style ledger entries are still active, returns partial with unsupported_mutation_kinds instead of claiming rollback.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID whose CSS mutations to reset. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request

```json
{
  "_meta": { "intent": "Reset injected stylesheet on active page" },
  "pluginId": "com.example.price-scanner"
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "pluginId": "com.example.price-scanner",
  "status": "reverted",
  "revertedStylesheets": 1
}
```

---

## 4. Operational Best Practices

* **Surgical Stylesheet Purge:** Use `nova.plugin_css_reset` to remove host-managed `<style>` tags injected by a plugin without disturbing other extensions or host browser styles.
* **Partial Rollback Handling:** If the plugin also applied inline styles or mutated host element class lists directly, the tool returns a `partial` status with `unsupported_mutation_kinds`; full remediation then requires disabling the plugin via `nova.plugin_disable`.
* **Live Visual Recovery:** Call this tool if a misconfigured plugin stylesheet causes visual regressions or obscures core web page elements during automated workflows.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
