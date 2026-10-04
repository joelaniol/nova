# `nova.downloads_clear`

Clears terminal download history from the UI and persistent storage.

---

## 1. Overview

`nova.downloads_clear` removes completed, cancelled, and failed download entries from the downloads manager history. Active transfers (queued, in progress, paused) are preserved and never cleared.

* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `filter` | `string` | No | — | `all` | Filter: only 'all' is currently supported (default). Clears all terminal entries (completed/cancelled/failed). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.downloads_clear",
  "arguments": {
    "filter": "all"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Download history cleared."
    }
  ],
  "structuredContent": {
    "cleared": true,
    "filter": "all"
  }
}
```

---

## 4. Operational Best Practices

* **Active Job Safety:** Never interrupts ongoing transfers; only tidies finished or failed historical records.

---

## See Also

* [`nova.downloads_list`](nova-downloads-list.md) - View current download history.
* [Downloads Management Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
