# `nova.downloads_pause_all`

Pauses all in-progress WebView2-native downloads that support pausing.

---

## 1. Overview

`nova.downloads_pause_all` iterates through all currently active downloads and dispatches pause commands to those supporting suspension, providing bandwidth relief for critical foreground operations.

* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.downloads_pause_all",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Pause requested: 2 dispatched, 1 skipped."
    }
  ],
  "structuredContent": {
    "paused": [
      "dl-1",
      "dl-2"
    ],
    "skipped": [
      {
        "id": "dl-3",
        "reason": "not_eligible"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Bandwidth Prioritization:** Call before large media transcription model downloads or heavy web crawls to dedicate full socket capacity to the priority task.

---

## See Also

* [`nova.downloads_resume_all`](nova-downloads-resume-all.md) - Resume all paused transfers.
* [`nova.downloads_pause`](nova-downloads-pause.md) - Pause a single download.
* [Downloads Management Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
