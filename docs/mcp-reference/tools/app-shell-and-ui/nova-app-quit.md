# `nova.app_quit`

> **Gracefully terminates the Nova host application process and all child WebView2 runtimes.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 3 (Host Process Control)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.app_quit` triggers an orderly application shutdown: flushes pending SQLite transactions, unregisters MCP endpoints, releases Outrider child processes, and exits.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Metadata. Provide _meta.intent (a short reason) — required for this high-impact tool. |
| `force` | `boolean` | No | Exit immediately even if the UI thread is unresponsive (shortens the internal shutdown watchdog). Normal shutdown still runs cleanup; only set this if a graceful quit appears to hang. |
| `reason` | `string` | No | Optional free-text reason recorded in the app log for diagnostics. |

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
      "text": "Application termination initiated."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ShuttingDown"
  }
}
```

---

## 4. Operational Best Practices

* **Final Step Only:** Only invoke when task objectives require full process teardown.
* **Pending State:** Ensure background downloads and tasks are finished or paused prior to quitting.

---

## 5. Related Tools

* [`nova.ui_get_state`](nova-ui-get-state.md)
