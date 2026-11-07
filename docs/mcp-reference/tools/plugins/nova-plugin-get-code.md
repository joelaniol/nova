# `nova.plugin_get_code`

> **Read the declared JavaScript source files of an installed plugin.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Read the declared JavaScript source files of an installed plugin. Returns the legacy entry-point source plus sourceFiles\[\] for entryPoint and manifest.contentScripts\[\] files. Essential for the agent to debug, refactor, or improve existing plugins. Returns null source for missing files. Read nova.reference_doc_read(docId='plugins') for the plugin architecture.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID whose declared source files to read. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "_meta": { "intent": "Audit active scanner implementation" },
  "pluginId": "com.example.price-scanner"
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "pluginId": "com.example.price-scanner",
  "entryPoint": "index.js",
  "source": "var handles = JSON.parse(nova.dom.querySelectorAll('.price', 1)); ...",
  "sizeBytes": 312,
  "contentScripts": [],
  "sourceFiles": [
    {
      "path": "index.js",
      "exists": true,
      "source": "var handles = JSON.parse(nova.dom.querySelectorAll('.price', 1)); ...",
      "sizeBytes": 312,
      "roles": ["entryPoint"],
      "error": null
    }
  ]
}
```

---

## 4. Operational Best Practices

* **Inspection Before Editing:** Always retrieve active source code before executing `nova.plugin_update` to prevent overwriting auxiliary content scripts or losing existing event listener logic.
* **Multi-File Bundle Awareness:** The entry point comes back as `source`; every declared file, including the `contentScripts[]` files, comes back in `sourceFiles[]` with its `roles`. Inspect all of them before an update.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
