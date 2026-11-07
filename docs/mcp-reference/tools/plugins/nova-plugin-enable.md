# `nova.plugin_enable`

> **Activate a plugin that is either disabled or waiting in Testing state.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Activate a plugin that is either disabled or waiting in Testing state. Resets crash/security counters and allows the plugin to be started again.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID to enable. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "_meta": { "intent": "Enable verified price scanner" },
  "pluginId": "com.example.price-scanner"
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "pluginId": "com.example.price-scanner",
  "status": "enabled",
  "state": "installed",
  "activeInstances": 1
}
```

---

## 4. Operational Best Practices

* **Transition from Testing to Installed:** Use `plugin_enable` to transition a plugin from `Testing` (created via `deferActivation: true`) or `Disabled` into the active `Installed` state.
* **Auto-Activation Gating:** Once enabled, the plugin automatically evaluates against matching pages declared in `hostPermissions.matches` and registers custom dynamic MCP tools.
* **Pre-Flight Smoke Verification:** Never enable a plugin without first confirming clean execution via [`nova.plugin_test`](nova-plugin-test.md).

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
