# `nova.ui_restore_tabs_prompt_resolve`

> **Resolves the startup tab restoration prompt modal after an abnormal browser termination.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts/README.md)
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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_restore_tabs_prompt_resolve",
  "arguments": {
    "decision": "restore"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Restore-tabs prompt resolved (restore, status=restored)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "decision": "restore",
    "status": "restored",
    "reasonCode": "restored_from_snapshot",
    "promptWasOpen": true,
    "hadPendingSnapshot": true,
    "snapshotTabCount": 4,
    "restored": true,
    "discarded": false
  }
}
```

---

## 4. Operational Best Practices

* **Automated Recovery:** Check `nova.ui_restore_tabs_prompt_state` at launch and resolve the prompt programmatically to unblock test harnesses.
* **No open prompt:** If the prompt is not open, the call returns `ok: false`, `status: "noop"` and `reasonCode: "prompt_not_open"`; if no saved session exists, `reasonCode` is `no_pending_snapshot`.

---

## 5. Related Tools

* [`nova.ui_restore_tabs_prompt_state`](nova-ui-restore-tabs-prompt-state.md)
