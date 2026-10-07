# `nova.downloads_auto_open_set`

Bulk-replaces the list of file extensions that auto-open with the OS default application.

---

## 1. Overview

`nova.downloads_auto_open_set` updates the allowed auto-open file extensions. Any executable extensions in the request are automatically rejected for security.

* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `extensions` | `array` of `string` | Yes | — | — | Replacement list of extensions. Each entry is normalized (lowercase, leading dot). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
