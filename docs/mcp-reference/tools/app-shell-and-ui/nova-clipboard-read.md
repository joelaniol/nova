# `nova.clipboard_read`

> **Reads the current plain text contents from the Windows OS system clipboard.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 1 (Read-Only OS Integration)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.clipboard_read` accesses the OS clipboard buffer securely, retrieving copied snippets, URLs, or tokens generated during automation.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional metadata. Provide _meta.intent (a short reason) for high-impact tools. A tool's annotations.intentRequired in tools/list tells you up front: 'always' means intent is mandatory, 'conditional' means it becomes mandatory for certain arguments (e.g. includeValues=true), absent means never. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_clipboard_read",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Clipboard content: 'https://login.example.com/oauth/token'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "text": "https://login.example.com/oauth/token",
    "length": 42
  }
}
```

---

## 4. Operational Best Practices

* **Data Sanitization:** Be cautious when clipboard contains sensitive tokens or passwords.
* **Timing:** Allow short delays when reading clipboard immediately after triggering in-page copy buttons.

---

## 5. Related Tools

* [`nova.clipboard_write`](nova-clipboard-write.md)
* [`nova.input_shortcut`](../browser-automation/nova-input-shortcut.md)
