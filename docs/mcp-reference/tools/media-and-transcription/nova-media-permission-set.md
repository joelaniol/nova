# `nova.media_permission_set`

Sets or clears persistent or session-based camera, mic, speaker, and geolocation permissions.

---

## 1. Overview

`nova.media_permission_set` configures origin-specific overrides for camera, microphone, speaker, screen-share, and geolocation permissions. Writes are either persistent (survive restart) or session-scoped grants that are cleared on app exit, after a time cap, or once the last tab closes.

* **Core Architecture Guide:** [Media Devices & Permissions](../../../core-features/media-intelligence/devices-and-permissions/README.md)

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
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
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
      "text": "Registered session grant(s) for https://meet.example.com: camera, microphone."
    }
  ],
  "structuredContent": {
    "status": "ok",
    "origin": "https://meet.example.com",
    "requestingOrigin": null,
    "lifetime": "session",
    "registered": ["camera", "microphone"],
    "note": "Session grants only apply to user-initiated getUserMedia calls. Automated JS timers cannot activate the grant without a user gesture."
  }
}
```

A persistent write (no `lifetime`, or `lifetime: "persistent"`) instead returns `{ "status": "ok", "origin": "...", "applied": ["microphone=allow", "camera=allow"] }` — `applied` entries read `"axis=cleared(ask)"` when a mode of `ask` removed the stored override rather than setting a value. `clearAll: true` returns `{ "status": "ok", "origin": "...", "cleared": true }`.

---

## 4. Operational Best Practices

* **Session Lifetime Preferred:** Use `lifetime: "session"` for testing to avoid leaving persistent microphone or camera grants enabled permanently. Note the guard in `note`: a session grant still only unblocks a user-initiated `getUserMedia` call, not an automated one.
* **Clear All:** Pass `clearAll: true` to purge all overrides for a domain and revert to global default behavior. Cannot be combined with `requestingOrigin` — use [`nova.site_permissions_reset_origin`](../site-data-and-identity/nova-site-permissions-reset-origin.md) for a full per-origin reset including iframe tuples.

---

## 5. Related Tools

* [`nova.media_permission_get`](nova-media-permission-get.md)
* [`nova.media_permissions_clear_session_grants`](nova-media-permissions-clear-session-grants.md)
