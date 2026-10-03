# `nova.site_permissions_reset_origin`

One-click reset of all stored permissions (media, notifications, geolocation) for an origin.

---

## 1. Overview

`nova.site_permissions_reset_origin` provides a comprehensive single-call purge of all permissions configured for a web domain: camera, microphone, speaker, screen sharing, desktop notifications, and geolocation.

* **Security Tier:** Tier 2 (Permission Reset)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `origin` | `string` | Yes | — | — | Absolute http/https origin (no path/query). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
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
      "text": "Reset all stored site permissions for https://meet.example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "origin": "https://meet.example.com",
    "resetAxes": [
      "camera",
      "microphone",
      "speaker",
      "notifications",
      "geolocation"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Pristine State Testing:** Ideal for QA test runners verifying first-time user consent prompts.

---

## 5. Related Tools

* [`nova.media_permission_set`](../media-and-transcription/nova-media-permission-set.md)
* [`nova.notifications_permission_set`](../notifications/nova-notifications-permission-set.md)
