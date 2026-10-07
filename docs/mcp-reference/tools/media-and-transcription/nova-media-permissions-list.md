# `nova.media_permissions_list`

Lists all stored per-origin permission overrides along with global default policies.

---

## 1. Overview

`nova.media_permissions_list` retrieves all configured domain permissions across camera, microphone, speaker, and screenCapture axes, including global defaults.

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `axis` | `string` | No | — | `camera`, `microphone`, `speaker`, `screenCapture`, `geolocation` | Filter by axis. Combine with mode to find rows where that axis equals the mode. |
| `mode` | `string` | No | — | `ask`, `allow`, `deny` | Filter by mode. Without axis, matches rows where any axis carries the mode. |
| `origin` | `string` | No | — | — | Filter by origin prefix (e.g. 'https://meet'). |
| `limit` | `integer` | No | — | 1–500 | Max results. Default 100. |
| `offset` | `integer` | No | — | ≥ 0 | Pagination offset. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "1 media permission entry/entries."
    }
  ],
  "structuredContent": {
    "permissions": [
      {
        "origin": "https://meet.example.com",
        "requestingOrigin": null,
        "camera": "ask",
        "microphone": "allow",
        "speaker": null,
        "screenCapture": null,
        "geolocation": null,
        "lifetime": "persistent",
        "devicePreferenceKnown": false,
        "updatedAtUtc": "2026-10-02T19:00:00Z"
      }
    ],
    "count": 1,
    "limit": 20,
    "offset": 0,
    "globalDefaults": {
      "camera": "ask",
      "microphone": "ask",
      "speaker": "ask"
    }
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
