# `nova.plugin_import`

> **Import a plugin from a base64-encoded .novaplugin ZIP bundle.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins.md)
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

## See Also

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins.md)
