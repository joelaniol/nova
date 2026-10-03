# `nova.media_stop_all`

Emergency kill switch terminating all active camera, microphone, and screen-sharing tracks browser-wide.

---

## 1. Overview

`nova.media_stop_all` acts as an emergency cutoff for active hardware media streams. It shuts down camera sensors, microphone capture loops, and desktop capture sessions across all WebViews immediately.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 2 (Emergency Kill Switch)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`origin`** | `string` | No | `null` | Required when scope='origin'. Absolute http/https origin. |
| **`scope`** | `string` | No | `null` | 'all' (default) or 'origin'. |

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
