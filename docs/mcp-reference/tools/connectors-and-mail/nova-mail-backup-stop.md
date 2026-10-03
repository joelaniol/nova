# `nova.mail_backup_stop`

Gracefully stops an in-flight mail backup job, committing all downloaded messages.

---

## 1. Overview

`nova.mail_backup_stop` signals a running mail backup job to halt. In-flight message downloads are cleanly committed so no downloaded progress is lost.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 2 (Job Control)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `jobId` | `string` | Yes | — | — | Job id returned by nova.mail_backup_start. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.mail_backup_stop",
  "arguments": {
    "jobId": "job-mb-819a"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Stopped backup job job-mb-819a."
    }
  ],
  "structuredContent": {
    "ok": true,
    "jobId": "job-mb-819a",
    "status": "stopped"
  }
}
```

---

## 4. Operational Best Practices

* **Safe Resumption:** Subsequent backup runs will resume incrementally from the committed watermark.

---

## 5. Related Tools

* [`nova.mail_backup_start`](nova-mail-backup-start.md)
* [`nova.mail_backup_status`](nova-mail-backup-status.md)
