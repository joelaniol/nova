# `nova.media_permission_set`

Sets or clears persistent or session-based camera, mic, speaker, and geolocation permissions.

---

## 1. Overview

`nova.media_permission_set` configures origin-specific overrides for media and hardware devices. Supports persistent storage or session-scoped grants with automatic expiration upon tab closure.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 2 (Permission Mutation)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`camera`** | `string` | No | `null` | Camera mode. |
| **`clearAll`** | `boolean` | No | `null` | Remove the entire stored override for this origin. Cannot be combined with axis modes or lifetime. |
| **`geolocation`** | `string` | No | `null` | Geolocation (navigator.geolocation) per-site override. lifetime='session' is not supported for this axis. |
| **`lifetime`** | `string` | No | `null` | How long the grant lives. 'persistent' (default) survives restart; 'session' is in-memory only and only valid for camera/microphone/speaker. |
| **`microphone`** | `string` | No | `null` | Microphone mode. |
| **`origin`** | `string` | Yes | `null` | Absolute http/https top-level origin. |
| **`requestingOrigin`** | `string` | No | `null` | Optional iframe origin (P-4). When set and distinct from origin, writes a tuple-specific override (an iframe-only entry that does not affect the top-level grant). Omit for classic top-level writes. |
| **`screenCapture`** | `string` | No | `null` | Screen sharing (getDisplayMedia) per-site override. lifetime='session' is not supported for this axis. |
| **`speaker`** | `string` | No | `null` | Speaker / audio output routing mode. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_permission_set",
  "arguments": {
    "origin": "https://meet.example.com",
    "microphone": "allow",
    "camera": "allow",
    "lifetime": "session"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Updated permissions for https://meet.example.com: microphone=allow, camera=allow (session)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "origin": "https://meet.example.com",
    "microphone": "allow",
    "camera": "allow",
    "lifetime": "session"
  }
}
```

---

## 4. Operational Best Practices

* **Session Lifetime Preferred:** Use `lifetime: "session"` for testing to avoid leaving persistent microphone or camera grants enabled permanently.
* **Clear All:** Pass `clearAll: true` to purge all overrides for a domain and revert to global default behavior.

---

## 5. Related Tools

* [`nova.media_permission_get`](nova-media-permission-get.md)
* [`nova.media_permissions_clear_session_grants`](nova-media-permissions-clear-session-grants.md)
