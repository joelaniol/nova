# `nova.ui_restore_tabs_prompt_resolve`

> **Resolves the startup tab restoration prompt modal after an abnormal browser termination.**

* **Security Tier:** Tier 2 (Session Recovery)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_restore_tabs_prompt_resolve` instructs Nova whether to restore previous browser tabs (`restore`), start fresh (`discard`), or postpone (`not_now`).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `decision` | `string` | Yes | — | `restore`, `discard`, `not_now` | Decision for the currently open startup restore-tabs prompt. 'restore' reopens the saved session, 'discard' drops the saved session, 'not_now' dismisses the prompt for now without restoring tabs. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_restore_tabs_prompt_resolve",
  "arguments": {
    "action": "restore"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Restored 4 tabs from previous session snapshot."
    }
  ],
  "structuredContent": {
    "ok": true,
    "action": "restore",
    "tabsRestored": 4
  }
}
```

---

## 4. Operational Best Practices

* **Automated Recovery:** Check `nova.ui_restore_tabs_prompt_state` at launch and resolve programmatically to unblock test harnesses.

---

## 5. Related Tools

* [`nova.ui_restore_tabs_prompt_state`](nova-ui-restore-tabs-prompt-state.md)
