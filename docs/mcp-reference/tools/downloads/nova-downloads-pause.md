# `nova.downloads_pause`

Pauses an active WebView2-native download by ID.

---

## 1. Overview

`nova.downloads_pause` pauses a live download transfer. The download must report `canPause: true` in `nova.downloads_list`. HttpClient fallback downloads and completed items cannot be paused.

* **Capability Bundle:** `app_shell_recovery`
* **Security Tier:** Tier 2 (Control)
* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`id`** | `string` | Yes | `none` | Download ID to pause. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.downloads_pause",
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
      "text": "Download dl-4f8a19bc pause requested."
    }
  ],
  "structuredContent": {
    "paused": true,
    "id": "dl-4f8a19bc",
    "reason": null
  }
}
```

---

## 4. Operational Best Practices

* **Capability Pre-check:** Check `canPause` in `nova.downloads_list` before calling. If unsupported by the underlying HTTP server or transfer mode, returns `reason: "not_eligible"`.

---

## See Also

* [`nova.downloads_resume`](nova-downloads-resume.md) - Resume paused transfer.
* [`nova.downloads_pause_all`](nova-downloads-pause-all.md) - Pause all live transfers.
* [Downloads Management Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
