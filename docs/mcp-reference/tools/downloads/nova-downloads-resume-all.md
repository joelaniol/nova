# `nova.downloads_resume_all`

Resumes all paused downloads, and interrupted ones that can continue where they stopped, when their underlying WebView2 operation supports resumption.

---

## 1. Overview

`nova.downloads_resume_all` bulk-resumes paused transfers once priority tasks finish, and continues downloads a network drop interrupted once connectivity is restored.

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
  "name": "nova.downloads_resume_all",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Resume requested: 2 dispatched, 0 skipped."
    }
  ],
  "structuredContent": {
    "resumed": [
      "dl-1",
      "dl-2"
    ],
    "skipped": []
  }
}
```

---

## 4. Operational Best Practices

* **Resume After Bulk Work:** Pair with `nova.downloads_pause_all` to temporarily suspend transfers during latency-sensitive operations.

---

## See Also

* [`nova.downloads_pause_all`](nova-downloads-pause-all.md) - Pause all transfers.
* [`nova.downloads_resume`](nova-downloads-resume.md) - Resume a single download.
* [Downloads Management Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
