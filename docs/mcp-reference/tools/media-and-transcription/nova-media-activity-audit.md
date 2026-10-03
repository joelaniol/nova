# `nova.media_activity_audit`

Retrieves an audit trail of stored media permissions joined with recent decision records per origin.

---

## 1. Overview

`nova.media_activity_audit` compiles stored per-site media permissions joined with timestamped decisions from Nova's in-memory permission activity log.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 1 (Read-Only Audit)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`kind`** | `string` | No | `null` | Filter to entries that have an explicit setting on this axis. |
| **`limit`** | `integer` | No | `null` | Max entries returned. Default 100. |

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
      "text": "Loaded audit trail for 2 origins."
    }
  ],
  "structuredContent": {
    "ok": true,
    "auditRecords": [
      {
        "origin": "https://meet.example.com",
        "camera": "allow",
        "microphone": "allow",
        "lastDecisionUtc": "2026-10-02T19:00:00Z"
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
