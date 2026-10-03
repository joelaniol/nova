# `nova.downloads_resume`

Resumes a paused live WebView2-native download by ID.

---

## 1. Overview

`nova.downloads_resume` resumes transfer on a paused download. This differs fundamentally from `nova.downloads_retry`: `resume` continues an existing socket/range stream, whereas `retry` navigates to the original URL again.

* **Capability Bundle:** `app_shell_recovery`
* **Security Tier:** Tier 2 (Control)
* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`id`** | `string` | Yes | `none` | Download ID to resume. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.downloads_resume",
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
      "text": "Download dl-4f8a19bc resume requested."
    }
  ],
  "structuredContent": {
    "resumed": true,
    "id": "dl-4f8a19bc",
    "reason": null
  }
}
```

---

## 4. Operational Best Practices

* **Verify `canResume`:** Ensure `canResume: true` was reported in `nova.downloads_list`. If the server does not support HTTP Range requests, resumption will fail.

---

## See Also

* [`nova.downloads_pause`](nova-downloads-pause.md) - Pause active transfer.
* [`nova.downloads_retry`](nova-downloads-retry.md) - Retry failed download.
* [Downloads Management Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
