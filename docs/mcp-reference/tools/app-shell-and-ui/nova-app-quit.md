# `nova.app_quit`

> **Gracefully terminates the Nova host application process and all child WebView2 runtimes.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.app_quit` requests a shutdown of the Nova host application. The response is returned to the caller before the process actually exits, so a dropped connection right after this call is expected. This programmatic close skips the "Close Nova?" confirmation prompt that a human closing the window would see; it does not restore tabs on the next launch.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `force` | `boolean` | No | `false` | — | Exit immediately even if the UI thread is unresponsive (shortens the internal shutdown watchdog). Normal shutdown still runs cleanup; only set this if a graceful quit appears to hang. |
| `reason` | `string` | No | — | — | Optional free-text reason recorded in the app log for diagnostics. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_app_quit",
  "arguments": {
    "reason": "Scheduled maintenance complete."
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Nova shutdown initiated. The connection will drop as the app exits."
    }
  ],
  "structuredContent": {
    "ok": true,
    "force": false,
    "shuttingDown": true
  }
}
```

---

## 4. Operational Best Practices

* **Final Step Only:** Only invoke when task objectives require full process teardown; this is a clean exit and does not trigger tab restoration on the next launch.
* **Pending State:** Ensure background downloads and tasks are finished or paused prior to quitting.

---

## 5. Related Tools

* [`nova.ui_get_state`](nova-ui-get-state.md)
