# `nova.clipboard_read`

> **Reads the current plain text contents from the Windows OS system clipboard.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.clipboard_read` reads the current plain-text contents of the OS clipboard. If the clipboard is empty or holds no text, the response says so instead of returning an error.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
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
      "text": "https://login.example.com/oauth/token"
    }
  ],
  "structuredContent": {
    "hasText": true,
    "text": "https://login.example.com/oauth/token"
  }
}
```
When the clipboard has no text, `hasText` is `false`, `text` is an empty string, and the text block reads `"(clipboard is empty or has no text)"`.

---

## 4. Operational Best Practices

* **Data Sanitization:** Be cautious when clipboard contains sensitive tokens or passwords.
* **Timing:** Allow short delays when reading clipboard immediately after triggering in-page copy buttons.

---

## 5. Related Tools

* [`nova.clipboard_write`](nova-clipboard-write.md)
* [`nova.input_shortcut`](../browser-automation/nova-input-shortcut.md)
