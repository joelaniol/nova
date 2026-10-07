# `nova.connector_list`

Lists configured E-Mail accounts and remote file transfer server connections.

---

## 1. Overview

`nova.connector_list` reports every configured mail/SFTP/FTP connection, resolved for Nova's host-verified current workspace when one is bound, otherwise globally. Per connector it reports id, type, host, username, transport-security flags, the capabilities that are ready to use (`capabilities`) and the ones still missing with a reason (`capabilitiesMissing`, each `mode` is `ask` or `blocked`). Secrets are never returned.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `type` | `string` | No | — | `mail`, `sftp`, `ftp` | Optional: only list connectors of this type. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
      "text": "1 connector(s) available. 'capabilities' are ready at the account layer; 'capabilitiesMissing' lists what still needs an account grant or prompt. mail_send also obeys Nova's independent global MutatingRemote policy. Secrets are never returned - agents use accounts, never see passwords."
    }
  ],
  "structuredContent": {
    "connectors": [
      {
        "id": "conn-mail-01",
        "displayName": "Work Email",
        "type": "mail",
        "username": "agent@example.com",
        "host": "imap.example.com:993",
        "secondaryHost": "smtp.example.com:587",
        "hasPassword": true,
        "authenticationMode": null,
        "hasPrivateKey": false,
        "hasKeyPassphrase": false,
        "usesInsecureTransport": false,
        "allowsInvalidTlsCertificate": false,
        "requiresAllowInsecure": false,
        "signature": { "available": false, "text": null, "html": null },
        "capabilities": ["read"],
        "capabilitiesMissing": [
          { "capability": "send", "mode": "ask", "reason": "No grant set yet; the agent will be prompted on first use." }
        ],
        "allowedRecipients": null,
        "mailReadFilter": { "restricted": false, "allowedFolders": [], "allowedSenders": [] },
        "lastConnectOkUtc": "2026-10-03T08:00:00Z",
        "lastConnectError": null
      }
    ],
    "returnedCount": 1,
    "contextScope": "global",
    "workspaceBound": false,
    "insecureConnectionsAllowed": false
  }
}
```

---

## 4. Operational Best Practices

* **Secrets never appear here:** `hasPassword`/`hasPrivateKey`/`hasKeyPassphrase` are booleans only; no secret value is ever part of this or any other connector response.
* **Filtered Scanning:** Use `type: "mail"`, `type: "sftp"`, or `type: "ftp"` to narrow results when managing specific automation tasks.
* **Plaintext needs the user's switch:** `insecureConnectionsAllowed` mirrors the Settings option for plaintext mail/FTP and disabled mail certificate checks. When it is `false`, a connector with `requiresAllowInsecure: true` cannot be created, changed or used; ask the user to enable it instead of retrying.
* **Check `capabilitiesMissing` before acting:** a capability not listed under `capabilities` will either prompt the user or fail, depending on whether the call is interactive or unattended; the `reason` text says which.

---

## 5. Related Tools

* [`nova.connector_create`](nova-connector-create.md)
* [`nova.connector_update`](nova-connector-update.md)
