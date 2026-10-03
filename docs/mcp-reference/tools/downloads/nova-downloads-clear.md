# `nova.downloads_clear`

Clears terminal download history from the UI and persistent storage.

---

## 1. Overview

`nova.downloads_clear` removes completed, cancelled, and failed download entries from the downloads manager history. Active transfers (queued, in progress, paused) are preserved and never cleared.

* **Capability Bundle:** `app_shell_recovery`
* **Security Tier:** Tier 2 (Cleanup)
* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`filter`** | `string` | No | `"all"` | History filter. Currently only `"all"` is supported. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
