# `nova.plugin_test`

> **Execute or smoke-test a JS script in a plugin's Jint runtime.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Execute or smoke-test a JS script in a plugin's Jint runtime. If no 'script' is provided, loads and executes the plugin's entry-point file from disk. The script has access to all nova.\* bridges (see plugin_update for the full API). mode='execute' targets the live runtime and therefore requires the plugin to already be active (for example via auto-activation on a matching page). mode='smoke' starts a temporary isolated verification runtime, reuses the last remembered live plugin context when available, reports that as livePageContext=true, and otherwise falls back to a synthetic test context (reported as syntheticContext=true). mode='execute' returns the legacy { ok, returnValue, error, elapsedMs }; mode='smoke' returns { passed, executionOk, errors, warnings, securityEvents, domChanges, elapsedMs, isolated, syntheticContext, livePageContext, applyWrites, applyWritesActive, activateAfterPass, activationApplied } for the agent verify loop. Class/style/css domChanges stay preview-only by default; with applyWrites=true and livePageContext=true, the smoke harness applies those mutations to the real page and rolls them back automatically before the session ends. With activateAfterPass=true, a passing smoke run can also promote a Testing/disabled plugin back to Installed. The smoke harness can also register live dom.observe/overlay.onEvent hooks, verify their delivery with temporary smoke probes, and temporarily mount smoke-owned overlays that are cleaned up automatically after the session. Timeouts and memory violations mark the plugin as crashed.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID to test. |
| `script` | `string` | No | — | — | Optional JS script to execute. If omitted, the plugin's entry-point file is loaded. |
| `mode` | `string` | No | `"execute"` | `execute`, `smoke` | Test mode. 'execute' preserves the legacy live-runtime dry-run response and requires an active plugin runtime. 'smoke' runs an isolated verification session, captures pass/fail issues, warnings, security events, and domChanges, and reports whether a remembered live page context was available for live hook registration plus delivery probes (`livePageContext`) or whether it had to fall back to a synthetic test context (`syntheticContext`). |
| `applyWrites` | `boolean` | No | `false` | — | Smoke-only opt-in for applying class/style/css mutations to the real remembered page before automatically rolling them back at session end. Requires mode='smoke' plus a remembered live page context with epoch tracking; otherwise the smoke report fails closed with applyWritesActive=false and a harness error. |
| `activateAfterPass` | `boolean` | No | `false` | — | Smoke-only opt-in for promoting a plugin from Testing or Disabled back to Installed after a passing smoke run. Use this together with plugin_create/plugin_update deferActivation=true to keep new or freshly edited plugins from auto-activating before verification passes. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "_meta": { "intent": "Smoke test price scanner on live shop page" },
  "pluginId": "com.example.price-scanner",
  "mode": "smoke",
  "activateAfterPass": true
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "passed": true,
  "mode": "smoke",
  "pluginId": "com.example.price-scanner",
  "executionOk": true,
  "returnValue": null,
  "error": null,
  "elapsedMs": 84,
  "errors": [],
  "warnings": [],
  "securityEvents": [],
  "domChanges": [],
  "isolated": true,
  "syntheticContext": false,
  "livePageContext": true,
  "applyWrites": false,
  "applyWritesActive": false,
  "activateAfterPass": true,
  "activationApplied": true,
  "plugin": {
    "pluginId": "com.example.price-scanner",
    "name": "Price Scanner",
    "version": "1.0.0",
    "installState": "Installed",
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

A failed smoke run returns `ok: false` and `passed: false` with the reasons in `errors[]` (each `{ code, message }`); `activationApplied` then stays `false`.
`plugin` is the plugin snapshot, shortened here. It also carries the session fields (`currentSession`, `activeSessions`, `lastKnownSession`, `knownSessions`), frame access, content-script counts and the granted and pending host, network and MCP-tool scopes.

---

## 4. Operational Best Practices

* **Smoke Verification Pipeline (`mode: "smoke"`):** Use `mode: "smoke"` for pre-flight validation. It runs the code in a temporary isolated runtime and reports errors, warnings, security events and DOM changes. `livePageContext: true` means it reused the last real page context; `syntheticContext: true` means it fell back to a test context.
* **Automated Promotion (`activateAfterPass: true`):** For a plugin in `Testing` or `Disabled`, pass `activateAfterPass: true`. If the smoke test passes, the plugin is promoted to `Installed`; `activationApplied` says whether that happened.
* **Reversible Test Mutations:** By default, class, style and CSS changes stay preview-only. `applyWrites: true` applies them to the remembered live page and rolls them back when the smoke session ends; without a live page context the run fails closed with `applyWritesActive: false`.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
