# `nova.media_permission_set`

Sets or clears persistent or session-based camera, mic, speaker, and geolocation permissions.

---

## 1. Overview

`nova.media_permission_set` configures origin-specific overrides for media and hardware devices. Supports persistent storage or session-scoped grants with automatic expiration upon tab closure.

* **Security Tier:** Tier 2 (Permission Mutation)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `origin` | `string` | Yes | — | — | Absolute http/https top-level origin. |
| `requestingOrigin` | `string` | No | — | — | Optional iframe origin (P-4). When set and distinct from origin, writes a tuple-specific override (an iframe-only entry that does not affect the top-level grant). Omit for classic top-level writes. |
| `camera` | `string` | No | — | `ask`, `allow`, `deny` | Camera mode. |
| `microphone` | `string` | No | — | `ask`, `allow`, `deny` | Microphone mode. |
| `speaker` | `string` | No | — | `ask`, `allow`, `deny` | Speaker / audio output routing mode. |
| `screenCapture` | `string` | No | — | `ask`, `allow`, `deny` | Screen sharing (getDisplayMedia) per-site override. lifetime='session' is not supported for this axis. |
| `geolocation` | `string` | No | — | `ask`, `allow`, `deny` | Geolocation (navigator.geolocation) per-site override. lifetime='session' is not supported for this axis. |
| `lifetime` | `string` | No | — | `persistent`, `session` | How long the grant lives. 'persistent' (default) survives restart; 'session' is in-memory only and only valid for camera/microphone/speaker. |
| `clearAll` | `boolean` | No | — | — | Remove the entire stored override for this origin. Cannot be combined with axis modes or lifetime. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
<!-- /generated:parameters -->

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
