# `nova.plugin_get_version_code`

> **Read a specific historical snapshot of a plugin's code + manifest from plugin_version_history.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Read a specific historical snapshot of a plugin's code + manifest from plugin_version_history. Use plugin_inspect.versionHistory to discover historyIds. Returns the full manifest_json, legacy source_code, sourceFiles\[\] for declared entryPoint/contentScripts files, and change_note that was captured before that update — essential for rollback, side-by-side comparison, or recovering from a bad update.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID whose version history to read. |
| `historyId` | `integer` | Yes | — | ≥ 1 | The history entry ID from plugin_inspect.versionHistory[].historyId. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "_meta": { "intent": "Inspect historical version before rollback" },
  "pluginId": "com.example.price-scanner",
  "historyId": 1
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "pluginId": "com.example.price-scanner",
  "historyId": 1,
  "version": "1.0.0",
  "manifestJson": "{ \"id\": \"com.example.price-scanner\", ... }",
  "sourceCode": "var handles = JSON.parse(nova.dom.querySelectorAll('.price', 1)); ...",
  "sourceFileCount": 0,
  "sourceFiles": [],
  "changeNote": "Initial code via plugin_create",
  "createdAtUtc": "2026-11-07T08:00:00.0000000Z"
}
```

---

## 4. Operational Best Practices

* **History ID Retrieval:** The parameter is `historyId` (integer), not a semver version string. Obtain valid `historyId` integers from [`nova.plugin_inspect`](nova-plugin-inspect.md) under `versionHistory[].historyId`.
* **Pre-Rollback Diff Verification:** Retrieve the historical source code to verify exactly what logic will be reinstated before invoking [`nova.plugin_rollback`](nova-plugin-rollback.md).

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
