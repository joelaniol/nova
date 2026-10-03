# `nova.downloads_open_folder`

Reveals the downloaded file in Windows Explorer with the item selected.

---

## 1. Overview

`nova.downloads_open_folder` opens Windows File Explorer at the target directory and selects the downloaded file, allowing human operators to locate and manage files quickly.

* **Capability Bundle:** `app_shell_recovery`
* **Security Tier:** Tier 1 (Safe Host Inspection)
* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | Yes | — | — | The download ID (from nova.downloads_list). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.downloads_open_folder",
  "arguments": {
    "id": "dl-4f8a19bc"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Download dl-4f8a19bc revealed in folder: C:\\Users\\GNetwork\\Downloads."
    }
  ],
  "structuredContent": {
    "opened": true,
    "id": "dl-4f8a19bc",
    "filePath": "C:\\Users\\GNetwork\\Downloads\\archive.tar.gz",
    "folderPath": "C:\\Users\\GNetwork\\Downloads",
    "reason": null
  }
}
```

---

## 4. Operational Best Practices

* **Locating Assets:** Excellent for human handoff prompts: "I have downloaded the report to your Downloads folder and highlighted it in Explorer."

---

## See Also

* [`nova.downloads_open_file`](nova-downloads-open-file.md) - Open file directly.
* [`nova.downloads_list`](nova-downloads-list.md) - Inspect file paths.
* [Downloads Management Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
