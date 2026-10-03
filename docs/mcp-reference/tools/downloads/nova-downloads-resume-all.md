# `nova.downloads_resume_all`

Resumes all paused downloads whose underlying WebView2 operation supports resumption.

---

## 1. Overview

`nova.downloads_resume_all` bulk-resumes paused transfers once priority tasks finish or network connectivity is restored.

* **Capability Bundle:** `app_shell_recovery`
* **Security Tier:** Tier 2 (Bulk Control)
* **Core Architecture Guide:** [Native Dialogs & Download Prompts](../../../core-features/native-dialogs-and-prompts.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
      "text": "resume requested: 2 dispatched, 0 skipped."
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
