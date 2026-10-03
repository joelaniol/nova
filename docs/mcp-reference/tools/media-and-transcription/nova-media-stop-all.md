# `nova.media_stop_all`

Emergency kill switch terminating all active camera, microphone, and screen-sharing tracks browser-wide.

---

## 1. Overview

`nova.media_stop_all` acts as an emergency cutoff for active hardware media streams. It shuts down camera sensors, microphone capture loops, and desktop capture sessions across all WebViews immediately.

* **Security Tier:** Tier 2 (Emergency Kill Switch)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | No | — | `all`, `origin` | 'all' (default) or 'origin'. |
| `origin` | `string` | No | — | — | Required when scope='origin'. Absolute http/https origin. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_stop_all",
  "arguments": {
    "scope": "all"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Emergency stop executed: all active camera/mic tracks terminated."
    }
  ],
  "structuredContent": {
    "ok": true,
    "scope": "all",
    "terminatedStreamsCount": 1
  }
}
```

---

## 4. Operational Best Practices

* **Fail-Safe Clean Slate:** Execute `nova.media_stop_all` whenever an agent detects unexpected device activity or an automation script crashes.

---

## 5. Related Tools

* [`nova.media_activity_status`](nova-media-activity-status.md)
* [`nova.media_permissions_clear_session_grants`](nova-media-permissions-clear-session-grants.md)
