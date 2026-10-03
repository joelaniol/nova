# `nova.downloads_auto_open_set`

Bulk-replaces the list of file extensions that auto-open with the OS default application.

---

## 1. Overview

`nova.downloads_auto_open_set` updates the allowed auto-open file extensions. Any executable extensions in the request are automatically rejected for security.

* **Capability Bundle:** `app_shell_recovery`
* **Security Tier:** Tier 2 (Configuration)
* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`extensions`** | `array of strings` | Yes | `none` | Array of file extensions (max 64). Normalized to lowercase with leading dot. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.downloads_auto_open_set",
  "arguments": {
    "extensions": [
      ".pdf",
      ".xlsx",
      ".csv"
    ]
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "3 extension(s) saved."
    }
  ],
  "structuredContent": {
    "extensions": [
      ".pdf",
      ".xlsx",
      ".csv"
    ],
    "rejected": []
  }
}
```

---

## 4. Operational Best Practices

* **Normalization:** Extensions are automatically converted to lowercase with a single leading dot (`"pdf"` -> `".pdf"`).
* **Rejection Handling:** If an agent attempts to register an executable extension like `.exe`, it is placed in `rejected` and discarded.

---

## See Also

* [`nova.downloads_auto_open_get`](nova-downloads-auto-open-get.md) - Read current auto-open extensions.
* [Downloads Management Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
