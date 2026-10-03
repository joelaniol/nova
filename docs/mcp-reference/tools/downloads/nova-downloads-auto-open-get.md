# `nova.downloads_auto_open_get`

Retrieves the list of file extensions configured to open automatically upon download completion.

---

## 1. Overview

`nova.downloads_auto_open_get` inspects which file extensions are registered to trigger OS launch immediately after download, along with the hardcoded security blocklist of non-executable extensions.

* **Capability Bundle:** `app_shell_recovery`
* **Security Tier:** Tier 1 (Safe)
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
  "name": "nova.downloads_auto_open_get",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "2 auto-open extension(s) configured."
    }
  ],
  "structuredContent": {
    "extensions": [
      ".pdf",
      ".csv"
    ],
    "blockedExtensions": [
      ".bat",
      ".cmd",
      ".com",
      ".exe",
      ".msi",
      ".ps1",
      ".vbs"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Security Protection:** Executable extensions (`.exe`, `.bat`, `.ps1`, `.msi`) are permanently blocklisted and can never be added to auto-open.

---

## See Also

* [`nova.downloads_auto_open_set`](nova-downloads-auto-open-set.md) - Update auto-open extensions.
* [Downloads Management Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
