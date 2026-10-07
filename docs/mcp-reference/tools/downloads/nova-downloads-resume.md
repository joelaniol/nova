# `nova.downloads_resume`

Resumes a paused live WebView2-native download by ID.

---

## 1. Overview

`nova.downloads_resume` resumes transfer on a paused download. This differs fundamentally from `nova.downloads_retry`: `resume` continues an existing socket/range stream, whereas `retry` navigates to the original URL again.

* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | Yes | — | — | The download ID to resume (from nova.downloads_list). The item should have canResume=true. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
