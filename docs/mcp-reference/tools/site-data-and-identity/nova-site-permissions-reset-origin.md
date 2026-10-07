# `nova.site_permissions_reset_origin`

One-click reset of all stored permissions (media, notifications, geolocation) for an origin.

---

## 1. Overview

`nova.site_permissions_reset_origin` provides a single-call purge of all stored permissions for a web origin: camera, microphone, speaker, screen sharing, and geolocation (one combined row), desktop notifications (a separate row), and remembered per-site device preferences. It also unconditionally drops any in-memory session grants, active clipboard-read and advanced-hardware decisions, and stops active media streams for that origin — even if no persisted row existed. Clipboard-read and advanced-hardware only have a global default, not a per-site override, so there is nothing persisted to remove for those two.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `origin` | `string` | Yes | — | — | Absolute http/https origin (no path/query). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.site_permissions_reset_origin",
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
      "text": "Reset all permissions for https://meet.example.com (media=True, notifications=True, devicePrefs=False)."
    }
  ],
  "structuredContent": {
    "status": "ok",
    "origin": "https://meet.example.com",
    "anyRemoved": true,
    "removed": {
      "media": true,
      "notifications": true,
      "devicePreferences": false
    },
    "note": "Clipboard-read and advanced-hardware axes use global defaults only; their per-site behaviour reverts automatically. Device label cache is preserved as non-consent UX metadata."
  }
}
```

`removed.media` covers camera, microphone, speaker, screen sharing, and geolocation together — the response does not break that row down further. This response has no `ok` field; use `status`/`anyRemoved` instead. If nothing was stored for the origin, the call still succeeds with `anyRemoved: false` and all `removed.*` set to `false`.

---

## 4. Operational Best Practices

* **Pristine State Testing:** Ideal for QA test runners verifying first-time user consent prompts.

---

## 5. Related Tools

* [`nova.media_permission_set`](../media-and-transcription/nova-media-permission-set.md)
* [`nova.notifications_permission_set`](../notifications/nova-notifications-permission-set.md)
