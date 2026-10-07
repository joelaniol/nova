# `nova.connector_grant_set`

Sets capability access modes (ask, always, blocked) for a connector.

---

## 1. Overview

`nova.connector_grant_set` configures fine-grained capability gates for a connector. Grants control what operations an AI agent can execute autonomously without human prompts.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | Connector id (from nova.connector_list). |
| `capability` | `string` | Yes | — | — | Capability wire name: 'read'/'organize'/'send' (mail), 'read'/'full' (sftp/ftp), 'process.exec' (sftp command execution; inherits 'full' when unset), or 'process.stdin' (interactive input into a running ssh_run_start session; opt-in only, never inherited). |
| `mode` | `string` | Yes | — | `ask`, `always`, `blocked` | Access mode for this capability. |
| `scope` | `string` | No | `"global"` | `global`, `workspace` | Where the grant applies. 'workspace' requires Nova's host-verified current terminal/task context; the caller never supplies an id. |
| `allowedMailFolders` | `array` of `string` | No | — | ≤ 200 items | Mail read + always only: exact IMAP folder names this grant may read. Omit to preserve this axis; pass [] to allow all folders. No wildcard or regex syntax. |
| `allowedMailSenders` | `array` of `string` | No | — | ≤ 200 items | Mail read + always only: sender addresses or bare domains this grant may read. Omit to preserve this axis; pass [] to allow all senders. No wildcard or regex syntax. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.connector_grant_set",
  "arguments": {
    "profileId": "conn-mail-01",
    "capability": "read",
    "mode": "always",
    "scope": "global"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Grant set: 'read' = always (global) for connector 'conn-mail-01'."
    }
  ],
  "structuredContent": {
    "profileId": "conn-mail-01",
    "capability": "read",
    "mode": "always",
    "scope": "global",
    "changed": true,
    "status": "updated",
    "reasonCode": null
  }
}
```

---

## 4. Operational Best Practices

* **Least Privilege:** Keep sensitive capabilities like `send` (mail) or `full` (sftp/ftp) in `ask` mode so human operators approve outbound messages or write/delete actions.
* **Folder Scoping:** Restrict `allowedMailFolders` (e.g. `["INBOX", "Archive"]`) to prevent autonomous access to sensitive mail folders.

---

## 5. Related Tools

* [`nova.connector_list`](nova-connector-list.md)
* [`nova.connector_recipient_set`](nova-connector-recipient-set.md)
