# `nova.downloads_open_file`

Opens a completed download using the operating system default application.

---

## 1. Overview

`nova.downloads_open_file` launches the downloaded file via the Windows shell association (e.g. opening a `.docx` in Word or `.pdf` in Acrobat). It requires the download to be in status `completed` with a verified file on disk.

* **Capability Bundle:** `app_shell_recovery`
* **Security Tier:** Tier 2 (Host Interaction)
* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`id`** | `string` | Yes | `none` | Download identifier. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.downloads_open_file",
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
      "text": "Download dl-4f8a19bc file opened: C:\\Users\\GNetwork\\Downloads\\invoice.pdf."
    }
  ],
  "structuredContent": {
    "opened": true,
    "id": "dl-4f8a19bc",
    "filePath": "C:\\Users\\GNetwork\\Downloads\\invoice.pdf",
    "reason": null
  }
}
```

---

## 4. Operational Best Practices

* **Host Application Launch:** This opens an external Windows process. If an agent only needs to inspect file contents without launching a third-party app, prefer `nova.downloads_preview` or direct script reads.
* **File Missing Detection:** Returns `reason: "file_missing"` if the user moved or deleted the file after download.

---

## See Also

* [`nova.downloads_open_folder`](nova-downloads-open-folder.md) - Reveal in Explorer.
* [`nova.downloads_preview`](nova-downloads-preview.md) - Preview inline in a browser tab.
* [Downloads Management Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
