# `nova.clipboard_read`

> **Reads the current plain text contents from the Windows OS system clipboard.**

* **Security Tier:** Tier 1 (Read-Only OS Integration)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.clipboard_read` accesses the OS clipboard buffer securely, retrieving copied snippets, URLs, or tokens generated during automation.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
<!-- /generated:parameters -->

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
