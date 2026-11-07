# `nova.plugin_icons_list`

> **List all plugin icon names known to the host (used in manifest.ui.icon).**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

List all plugin icon names known to the host (used in manifest.ui.icon). Returns an array of names like 'chart-line', 'bell', 'cog', 'bookmark', etc. Each name resolves to a bundled Fluent SVG asset for the plugin menu. Unknown names fall back to a default puzzle icon.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request

```json
{
  "_meta": { "intent": "Discover available Fluent UI icons for plugin manifest" }
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "count": 55,
  "icons": ["alert", "bell", "bookmark", "chart-bar", "chart-line", "cog"]
}
```

The list is cut short here; call the tool for all names.

---

## 4. Operational Best Practices

* **Pre-Manifest Validation:** Query `nova.plugin_icons_list` before authoring or updating `manifest.ui.icon` to select a recognized Fluent asset name.
* **Graceful Fallback:** Any icon name not present in the returned list gracefully falls back to the default host puzzle-piece icon in browser UI menus.
* **Zero Parameters:** The tool takes no arguments; callers can invoke it with an empty object or include `_meta.intent` for call tracing.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
