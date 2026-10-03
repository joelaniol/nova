# `nova.media_permissions_list`

Lists all stored per-origin permission overrides along with global default policies.

---

## 1. Overview

`nova.media_permissions_list` retrieves all configured domain permissions across camera, microphone, speaker, and screenCapture axes, including global defaults.

* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

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
