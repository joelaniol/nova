# `nova.media_permissions_clear_session_grants`

Drops all temporary session permissions and halts any live media tracks relying on them.

---

## 1. Overview

`nova.media_permissions_clear_session_grants` purges all in-memory "Allow once" decisions across all browser tabs and forcibly terminates any live audio/video tracks running under temporary grants.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 2 (Session Clearance)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_permissions_clear_session_grants",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Cleared all session grants and terminated active media tracks."
    }
  ],
  "structuredContent": {
    "ok": true,
    "clearedCount": 2,
    "tracksTerminated": 1
  }
}
```

---

## 4. Operational Best Practices

* **Session Teardown:** Call at the end of automated workflows to guarantee zero lingering temporary media access.

---

## 5. Related Tools

* [`nova.media_stop_all`](nova-media-stop-all.md)
* [`nova.media_permission_set`](nova-media-permission-set.md)
