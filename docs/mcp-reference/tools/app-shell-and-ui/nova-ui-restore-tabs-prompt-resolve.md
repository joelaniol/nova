# `nova.ui_restore_tabs_prompt_resolve`

> **Resolves the startup tab restoration prompt modal after an abnormal browser termination.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Session Recovery)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_restore_tabs_prompt_resolve` instructs Nova whether to restore previous browser tabs (`restore`), start fresh (`discard`), or postpone (`not_now`).

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `decision` | `string` | **Yes** | Decision for the currently open startup restore-tabs prompt. 'restore' reopens the saved session, 'discard' drops the saved session, 'not_now' dismisses the prompt for now without restoring tabs. |

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
