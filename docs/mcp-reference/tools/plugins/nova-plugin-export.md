# `nova.plugin_export`

> **Export a plugin as a base64-encoded .novaplugin ZIP bundle containing manifest, source code, and optionally persistent KV storage data (including typed storage.local / storage.sync snapshots).**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Export a plugin as a base64-encoded .novaplugin ZIP bundle containing manifest, source code, and optionally persistent KV storage data (including typed storage.local / storage.sync snapshots).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID to export. |
| `includeKvData` | `boolean` | No | `false` | — | If true, include the plugin's persistent key-value storage snapshot in the bundle, including typed storage.local / storage.sync data. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request

```json
{
  "_meta": { "intent": "Export plugin bundle including persistent KV storage" },
  "pluginId": "com.example.price-scanner",
  "includeKvData": true
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "pluginId": "com.example.price-scanner",
  "bundleBase64": "UEsDBBQAAAAIA...",
  "bundleSizeBytes": 24576
}
```

---

## 4. Operational Best Practices

* **Portable Bundle Archive:** The `.novaplugin` bundle is a base64-encoded ZIP with the manifest and the source code, and with `includeKvData: true` also the persistent storage snapshot (`storage.local` / `storage.sync`). Restore it with [`nova.plugin_import`](nova-plugin-import.md).
* **Data Privacy in Exports (`includeKvData`):** Keep `includeKvData: false` when distributing plugins to other users or version control to prevent leaking sensitive API keys, cached credentials, or user-specific records.
* **Automated Backup & Disaster Recovery:** Use `nova.plugin_export` before executing major multi-file updates or schema migrations to capture an out-of-band recovery snapshot.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
