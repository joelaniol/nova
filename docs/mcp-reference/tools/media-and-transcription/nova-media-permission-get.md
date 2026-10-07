# `nova.media_permission_get`

Reads the effective and stored media permissions for a specific web origin.

---

## 1. Overview

`nova.media_permission_get` evaluates the active permission state for an origin, factoring in stored overrides, iframe requesting origins, and global browser defaults.

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `origin` | `string` | Yes | — | — | Absolute http/https top-level origin (e.g. 'https://meet.google.com'). |
| `requestingOrigin` | `string` | No | — | — | Optional iframe origin (P-4). When set and distinct from origin, the lookup tries tuple-match first, then falls back to top-level match. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "Override stored for https://meet.example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "origin": "https://meet.example.com",
    "requestingOrigin": null,
    "matchedTuple": false,
    "stored": {
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
    },
    "effective": {
      "camera": "ask",
      "microphone": "allow",
      "speaker": "ask",
      "screenCapture": "ask",
      "geolocation": "ask"
    },
    "sessionGrants": {
      "camera": false,
      "microphone": false,
      "speaker": false
    },
    "provenance": {
      "camera": { "state": "ask", "source": "AskUser", "lifetime": "onerequest", "reasonStack": ["site_grant:axis_unset:https://meet.example.com:Camera", "global_mode:Camera=Ask", "ask_user:default_terminal"] },
      "microphone": { "state": "allow", "source": "SiteGrant", "lifetime": "persistent", "reasonStack": ["site_grant:allow:https://meet.example.com:Microphone"] },
      "speaker": { "state": "ask", "source": "AskUser", "lifetime": "onerequest", "reasonStack": [] },
      "screenCapture": { "state": "ask", "source": "AskUser", "lifetime": "onerequest", "reasonStack": [] },
      "geolocation": { "state": "ask", "source": "AskUser", "lifetime": "onerequest", "reasonStack": [] }
    }
  }
}
```

`stored` is `null` when no override exists for the origin. `provenance` is only present when the server exposes the resolver's reason stack; otherwise it is `null` and only `effective`/`sessionGrants` can be used to explain the current decision.

---

## 4. Operational Best Practices

* **Origin Boundary Check:** Always evaluate permissions before attempting to interact with in-page media elements that trigger prompts.

---

## 5. Related Tools

* [`nova.media_permission_set`](nova-media-permission-set.md)
* [`nova.media_permissions_list`](nova-media-permissions-list.md)
