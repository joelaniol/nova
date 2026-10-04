# `nova.ui_restore_tabs_prompt_state`

> **Inspects whether a startup tab restoration prompt is active and previews saved session tabs.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_restore_tabs_prompt_state` reports whether Nova's "restore previous tabs?" startup prompt is currently open, and if so, previews the pending tab snapshot (tab count, which index was active, when it was saved, and each tab's URL) without answering the prompt. Use `nova.ui_restore_tabs_prompt_resolve` to actually answer it.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_restore_tabs_prompt_state",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "PromptOpen=True HasPendingSnapshot=True SnapshotTabCount=4"
    }
  ],
  "structuredContent": {
    "promptOpen": true,
    "hasPendingSnapshot": true,
    "snapshotTabCount": 4,
    "snapshotActiveTabIndex": 0,
    "snapshotSavedAtUtc": "2026-10-03T08:15:00Z",
    "snapshotTabs": [
      { "index": 0, "url": "https://app.example.com", "restorable": true }
    ]
  }
}
```
The `snapshotTabs` array above is shortened; a real call returns one entry per saved tab.

---

## 4. Operational Best Practices

* **Startup Check:** Run after Nova starts to see whether the restore-tabs prompt is open before deciding how to answer it with `nova.ui_restore_tabs_prompt_resolve`.

---

## 5. Related Tools

* [`nova.ui_restore_tabs_prompt_resolve`](nova-ui-restore-tabs-prompt-resolve.md)
