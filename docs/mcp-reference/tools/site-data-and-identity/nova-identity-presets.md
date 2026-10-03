# `nova.identity_presets`

Lists available browser identity presets and selectable browser engine versions.

---

## 1. Overview

`nova.identity_presets` returns the catalog of pre-configured browser identity presets, detailing platform OS, browser families, and verified User-Agent strings.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| *(none)* | — | — | — | No parameters accepted. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.identity_presets",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Loaded 4 browser identity presets."
    }
  ],
  "structuredContent": {
    "ok": true,
    "presets": [
      {
        "preset": "ChromeWindows",
        "description": "Standard Google Chrome on Windows 11",
        "supportedVersions": [
          "128.0.0.0",
          "127.0.0.0"
        ]
      },
      {
        "preset": "EdgeWindows",
        "description": "Microsoft Edge on Windows 11"
      },
      {
        "preset": "SafariMac",
        "description": "Apple Safari on macOS Sequoia"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Catalog Selection:** Use preset names directly in [`nova.identity_set`](nova-identity-set.md).

---

## 5. Related Tools

* [`nova.identity_get`](nova-identity-get.md)
* [`nova.identity_set`](nova-identity-set.md)
