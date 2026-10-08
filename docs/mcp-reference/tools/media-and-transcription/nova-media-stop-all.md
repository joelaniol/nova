# `nova.media_stop_all`

Emergency kill switch terminating all active camera, microphone, and screen-sharing tracks browser-wide.

---

## 1. Overview

`nova.media_stop_all` acts as an emergency cutoff for active hardware media streams. It stops live camera, microphone, and screen-sharing tracks across all tabs (or within one origin, with `scope: "origin"`). It does not clear stored or session permission grants — a stopped site can start a new stream again without a fresh prompt if it already holds Allow. Use [`nova.media_permissions_clear_session_grants`](nova-media-permissions-clear-session-grants.md) to also drop in-memory "Allow once" grants.

* **Core Architecture Guide:** [Media Devices & Permissions](../../../core-features/media-intelligence/devices-and-permissions/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | No | — | `all`, `origin` | 'all' (default) or 'origin'. |
| `origin` | `string` | No | — | — | Required when scope='origin'. Absolute http/https origin. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Stopped 1 live media track(s)."
    }
  ],
  "structuredContent": {
    "status": "ok",
    "scope": "all",
    "origin": null,
    "stoppedTrackCount": 1
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
