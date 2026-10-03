# `nova.media_permission_get`

Reads the effective and stored media permissions for a specific web origin.

---

## 1. Overview

`nova.media_permission_get` evaluates the active permission state for an origin, factoring in stored overrides, iframe requesting origins, and global browser defaults.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`origin`** | `string` | Yes | `null` | Absolute http/https top-level origin (e.g. 'https://meet.google.com'). |
| **`requestingOrigin`** | `string` | No | `null` | Optional iframe origin (P-4). When set and distinct from origin, the lookup tries tuple-match first, then falls back to top-level match. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_permission_get",
  "arguments": {
    "origin": "https://meet.example.com"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Effective permissions for https://meet.example.com: microphone=allow, camera=ask."
    }
  ],
  "structuredContent": {
    "ok": true,
    "origin": "https://meet.example.com",
    "effective": {
      "microphone": "allow",
      "camera": "ask",
      "speaker": "allow",
      "screenCapture": "ask"
    }
  }
}
```

---

## 4. Operational Best Practices

* **Origin Boundary Check:** Always evaluate permissions before attempting to interact with in-page media elements that trigger prompts.

---

## 5. Related Tools

* [`nova.media_permission_set`](nova-media-permission-set.md)
* [`nova.media_permissions_list`](nova-media-permissions-list.md)
