# `nova.media_activity_audit`

Retrieves an audit trail of stored media permissions joined with recent decision records per origin.

---

## 1. Overview

`nova.media_activity_audit` compiles stored per-site media permissions joined with timestamped decisions from Nova's in-memory permission activity log.

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `kind` | `string` | No | — | `camera`, `microphone`, `speaker`, `screenCapture`, `geolocation` | Filter to entries that have an explicit setting on this axis. |
| `limit` | `integer` | No | — | 1–500 | Max entries returned. Default 100. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_activity_audit",
  "arguments": {
    "limit": 10
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "1 site(s) with stored media permissions."
    }
  ],
  "structuredContent": {
    "count": 1,
    "limit": 10,
    "entries": [
      {
        "origin": "https://meet.example.com",
        "camera": "allow",
        "microphone": "allow",
        "speaker": null,
        "screenCapture": null,
        "geolocation": null,
        "lifetime": "persistent",
        "devicePreferenceKnown": false,
        "storedAtUtc": "2026-10-02T19:00:00Z",
        "lastDecisionAtUtc": "2026-10-02T19:00:00Z",
        "lastDecisionState": "allow",
        "lastDecisionSource": "SiteGrant"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Compliance Auditing:** Review granted permissions across all domains to identify outdated or overly permissive media grants.

---

## 5. Related Tools

* [`nova.media_permission_get`](nova-media-permission-get.md)
* [`nova.media_permissions_list`](nova-media-permissions-list.md)
