# `nova.downloads_preview`

Opens a completed download inline in a new browser tab using a secure file:// URL.

---

## 1. Overview

`nova.downloads_preview` renders images, PDFs, videos, audio, and structured text files directly inside a new browser tab without launching external applications. For security, SVG and HTML files are strictly excluded to prevent script injection.

* **Security Tier:** Tier 1 (Safe Preview)
* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | Yes | — | — | The download ID (from nova.downloads_list). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.downloads_preview",
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
      "text": "Download dl-4f8a19bc preview opened in new tab (pdf)."
    }
  ],
  "structuredContent": {
    "previewed": true,
    "id": "dl-4f8a19bc",
    "kind": "pdf",
    "targetId": "tab-5",
    "reason": null
  }
}
```

---

## 4. Operational Best Practices

* **Supported File Formats:** Image (`jpg`, `png`, `gif`, `webp`, `bmp`, `ico`), Document (`pdf`), Media (`mp4`, `webm`, `mov`, `mp3`, `wav`), and Text (`txt`, `md`, `log`, `csv`, `json`, `xml`).
* **Sandbox Isolation:** The preview tab opens with an opaque origin, ensuring local files cannot leak data into existing sandbox sessions.

---

## See Also

* [`nova.downloads_wait`](nova-downloads-wait.md) - Wait for download completion.
* [`nova.downloads_open_file`](nova-downloads-open-file.md) - Open with native OS app.
* [Downloads Management Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
