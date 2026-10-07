# `nova.connector_update`

Updates configuration, endpoints, credentials, or signatures of an existing connection.

---

## 1. Overview

`nova.connector_update` modifies settings for a previously registered connector. Only specified fields are updated; omitted fields retain their existing values. Changing the server, login, auth mode, key path, or transport-security policy without supplying a matching new credential detaches the stale stored credential (`credentialCleared: true` in the result).

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | Yes | — | — | Connector id (from nova.connector_list). |
| `displayName` | `string` | No | — | ≤ 120 characters | New display name. |
| `username` | `string` | No | — | ≤ 320 characters | New username / e-mail address. |
| `password` | `string` | No | — | — | Write-only. Replaces the stored password; never returned. |
| `passwordFromVault` | `string` | No | — | — | Instead of password: the id of a Nova vault entry (from nova.vault_list). Nova copies that entry's password into this connection internally - you never see it. The user confirms each copy in a dialog that shows the saved login next to this connection's servers, because a web login is not always the mail/server login. The user may answer 'always' for exactly this entry and these servers; then later copies of that pair (also unattended) need no prompt, while a different entry or server still asks. Mutually exclusive with password; needs authMode='password'. Without such an answer unattended runs are refused (-32033); a declined prompt returns -32036 and stores nothing. |
| `authMode` | `string` | No | — | `password`, `private_key` | sftp only: new authentication method. |
| `privateKeyPath` | `string` | No | — | ≤ 2048 characters | sftp + private_key only: new write-only host path to a private key; never returned. |
| `keyPassphrase` | `string` | No | — | — | sftp + private_key only: write-only replacement passphrase; empty clears it. Never returned. |
| `imapHost` | `string` | No | — | ≤ 253 characters | mail: incoming (IMAP) server host. |
| `imapPort` | `integer` | No | — | 1–65535 | mail: IMAP port. |
| `imapSecurity` | `string` | No | — | `auto`, `ssl_on_connect`, `start_tls`, `none` | mail: IMAP transport security. none is the explicitly gated unencrypted mode. |
| `imapAllowInvalidCertificate` | `boolean` | No | — | — | mail only: whether this IMAP endpoint accepts an invalid TLS certificate as an explicitly gated debug exception. false restores strict validation; cannot be true with imapSecurity='none'. |
| `signatureText` | `string` | No | — | ≤ 8192 characters | mail only: the signature TEXT BLOCK (name, company, phone - the sig block below a mail, NOT a cryptographic/S-MIME signature; Nova does not sign mails), appended below every sent mail and draft after the standard "-- " line (nova.mail_send includeSignature=false leaves it off). Empty string clears it; connector_list shows it. |
| `signatureHtml` | `string` | No | — | ≤ 32768 characters | mail only: the same signature text block as HTML for HTML mails (not a cryptographic signature); without it an HTML mail gets the text signature. Empty string clears it. |
| `smtpHost` | `string` | No | — | ≤ 253 characters | mail: outgoing (SMTP) server host. |
| `smtpPort` | `integer` | No | — | 1–65535 | mail: SMTP port. |
| `smtpSecurity` | `string` | No | — | `auto`, `ssl_on_connect`, `start_tls`, `none` | mail: SMTP transport security. none is the explicitly gated unencrypted mode. |
| `smtpAllowInvalidCertificate` | `boolean` | No | — | — | mail only: whether this SMTP endpoint accepts an invalid TLS certificate as an explicitly gated debug exception. false restores strict validation; cannot be true with smtpSecurity='none'. |
| `host` | `string` | No | — | ≤ 253 characters | sftp/ftp: server host. |
| `port` | `integer` | No | — | 1–65535 | sftp/ftp: port. |
| `security` | `string` | No | — | `auto`, `ssl_on_connect`, `start_tls`, `none` | File-transfer transport. SFTP accepts only auto; FTP auto/start_tls is explicit FTPS, ssl_on_connect is implicit FTPS, and none is plaintext FTP. |
| `allowInsecure` | `boolean` | No | `false` | — | Required as true when the resulting profile uses security=none or allows an invalid mail TLS certificate; the user's separate Settings option must also be enabled. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.connector_update",
  "arguments": {
    "id": "conn-mail-01",
    "displayName": "Primary Work Email",
    "smtpHost": "smtp.example.com"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Connector 'Primary Work Email' updated (id=conn-mail-01). The password is stored encrypted and never returned."
    }
  ],
  "structuredContent": {
    "id": "conn-mail-01",
    "action": "updated",
    "displayName": "Primary Work Email",
    "type": "mail",
    "username": "agent@example.com",
    "host": "imap.example.com:993",
    "hasPassword": true,
    "authenticationMode": null,
    "hasPrivateKey": false,
    "hasKeyPassphrase": false,
    "usesInsecureTransport": false,
    "allowsInvalidTlsCertificate": false,
    "signature": { "available": false, "text": null, "html": null },
    "credentialCleared": false,
    "changed": true,
    "status": "updated",
    "reasonCode": null
  }
}
```

---

## 4. Operational Best Practices

* **Type Immutability:** Connector type (`mail`, `sftp`, `ftp`) cannot be changed after creation; create a new connector if switching protocol families.
* **Credential Replacement:** Supplying a new `password`/`keyPassphrase` re-encrypts it under DPAPI; capability grants are untouched by an update. Existing capability grants stay in place.
* **Watch `credentialCleared`:** changing the server/login/auth mode/key path/transport policy without also sending the matching new credential detaches the old one — the result's `credentialCleared` flag and message say so.

---

## 5. Related Tools

* [`nova.connector_list`](nova-connector-list.md)
* [`nova.connector_delete`](nova-connector-delete.md)
