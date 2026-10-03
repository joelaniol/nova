# `nova.media_permissions_list`

Lists all stored per-origin permission overrides along with global default policies.

---

## 1. Overview

`nova.media_permissions_list` retrieves all configured domain permissions across camera, microphone, speaker, and screenCapture axes, including global defaults.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`axis`** | `string` | No | `null` | Filter by axis. Combine with mode to find rows where that axis equals the mode. |
| **`limit`** | `integer` | No | `null` | Max results. Default 100. |
| **`mode`** | `string` | No | `null` | Filter by mode. Without axis, matches rows where any axis carries the mode. |
| **`offset`** | `integer` | No | `null` | Pagination offset. |
| **`origin`** | `string` | No | `null` | Filter by origin prefix (e.g. 'https://meet'). |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_permissions_list",
  "arguments": {
    "limit": 20
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Loaded 2 stored media permission overrides."
    }
  ],
  "structuredContent": {
    "ok": true,
    "total": 2,
    "globalDefaults": {
      "camera": "ask",
      "microphone": "ask"
    },
    "overrides": [
      {
        "origin": "https://meet.example.com",
        "microphone": "allow"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Global Policy Audits:** Check `globalDefaults` to understand standard prompt behavior across unconfigured origins.

---

## 5. Related Tools

* [`nova.media_permission_get`](nova-media-permission-get.md)
* [`nova.media_permission_set`](nova-media-permission-set.md)
