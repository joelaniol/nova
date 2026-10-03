# `nova.clipboard_write`

> **Writes plain text to the Windows OS system clipboard.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (OS Integration)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.clipboard_write` places a specified string into the system clipboard, enabling subsequent paste actions into native or web applications.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional metadata. Provide _meta.intent (a short reason) for high-impact tools. A tool's annotations.intentRequired in tools/list tells you up front: 'always' means intent is mandatory, 'conditional' means it becomes mandatory for certain arguments (e.g. includeValues=true), absent means never. |
| `text` | `string` | **Yes** | Required text payload to write into the clipboard. Must be a JSON string; explicit null is invalid. Empty or whitespace-only strings intentionally clear/overwrite the current clipboard text. The runtime sanitizes dangerous invisible/control characters before writing and rejects payloads longer than 65536 characters. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_clipboard_write",
  "arguments": {
    "text": "Automated workflow payload 2026-Q4"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Wrote 33 characters to Windows clipboard."
    }
  ],
  "structuredContent": {
    "ok": true,
    "length": 33
  }
}
```

---

## 4. Operational Best Practices

* **Simulate Pastes:** Pair with `nova.input_shortcut` (`Ctrl+V`) for rich text areas that reject direct DOM typing.

---

## 5. Related Tools

* [`nova.clipboard_read`](nova-clipboard-read.md)
