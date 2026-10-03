# `nova.connector_list`

Lists configured E-Mail accounts and remote file transfer server connections.

---

## 1. Overview

`nova.connector_list` retrieves all active connector profiles available to the current workspace or global session. It reports connection IDs, types, host endpoints, usernames, and granted capability permissions without disclosing secrets.

* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `type` | `string` | No | — | `mail`, `sftp`, `ftp` | Optional: only list connectors of this type. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.connector_list",
  "arguments": {
    "type": "mail"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 1 configured mail connector for the current workspace."
    }
  ],
  "structuredContent": {
    "ok": true,
    "connectors": [
      {
        "id": "conn-mail-01",
        "displayName": "Work Email",
        "type": "mail",
        "host": "imap.example.com",
        "username": "agent@example.com",
        "grants": {
          "read": "allow",
          "send": "ask"
        }
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Workspace Resolution:** Passwords and credentials are resolved strictly against the calling workspace context.
* **Filtered Scanning:** Use `type: "mail"`, `type: "sftp"`, or `type: "ftp"` to narrow results when managing specific automation tasks.

---

## 5. Related Tools

* [`nova.connector_create`](nova-connector-create.md)
* [`nova.connector_update`](nova-connector-update.md)
