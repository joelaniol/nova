# `nova.connector_create`

Creates an E-Mail account (IMAP/SMTP) or remote server connection (SFTP/FTP).

---

## 1. Overview

`nova.connector_create` provisions a new managed connector profile. Credentials (passwords, private key passphrases) are immediately encrypted using Windows DPAPI and stored in the Global Secret Store. Connection profiles can be scoped to specific workspaces.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 2 (Connector Configuration)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `displayName` | `string` | Yes | — | ≤ 120 characters | How the account is recognized (e.g. 'Work mail'). |
| `type` | `string` | Yes | — | `mail`, `sftp`, `ftp` | Connection type. |
| `username` | `string` | No | — | ≤ 320 characters | Username / e-mail address. Required for mail, SFTP, and FTP connectors. |
| `password` | `string` | No | — | — | Write-only password for mail, FTP, or SFTP authMode='password'. Stored DPAPI-encrypted; never returned. Omit to leave unset. |
| `passwordFromVault` | `string` | No | — | — | Instead of password: the id of a Nova vault entry (from nova.vault_list). Nova copies that entry's password into this connection internally - you never see it. The user confirms each copy in a dialog that shows the saved login next to this connection's servers, because a web login is not always the mail/server login. The user may answer 'always' for exactly this entry and these servers; then later copies of that pair (also unattended) need no prompt, while a different entry or server still asks. Mutually exclusive with password; needs authMode='password'. Without such an answer unattended runs are refused (-32033); a declined prompt returns -32029 and stores nothing. |
| `authMode` | `string` | No | — | `password`, `private_key` | sftp only: authentication method. Defaults to private_key when privateKeyPath is supplied, otherwise password. |
| `privateKeyPath` | `string` | No | — | ≤ 2048 characters | sftp + private_key only: write-only host path to an existing SSH private key. Stored inside the DPAPI-encrypted profile and never returned. |
| `keyPassphrase` | `string` | No | — | — | sftp + private_key only: optional write-only private-key passphrase. Stored DPAPI-encrypted and never returned; empty clears it on update. |
| `imapHost` | `string` | No | — | ≤ 253 characters | mail: incoming (IMAP) server host. |
| `imapPort` | `integer` | No | `993` | 1–65535 | mail: IMAP port. Default 993. |
| `imapSecurity` | `string` | No | — | `auto`, `ssl_on_connect`, `start_tls`, `none` | mail: IMAP transport security. Auto requires TLS. none is unencrypted debug/legacy mode and requires both the user option and allowInsecure=true. Default auto. |
| `imapAllowInvalidCertificate` | `boolean` | No | `false` | — | mail only: store an IMAP debug exception that accepts an invalid, mismatched, expired, or self-signed TLS certificate. Requires the user option and allowInsecure=true on this create and every use; cannot be true with imapSecurity='none'. |
| `signatureText` | `string` | No | — | ≤ 8192 characters | mail only: the signature TEXT BLOCK (name, company, phone - the sig block below a mail, NOT a cryptographic/S-MIME signature; Nova does not sign mails), appended below every sent mail and draft after the standard "-- " line (nova.mail_send includeSignature=false leaves it off). Empty string clears it; connector_list shows it. |
| `signatureHtml` | `string` | No | — | ≤ 32768 characters | mail only: the same signature text block as HTML for HTML mails (not a cryptographic signature); without it an HTML mail gets the text signature. Empty string clears it. |
| `smtpHost` | `string` | No | — | ≤ 253 characters | mail: outgoing (SMTP) server host. |
| `smtpPort` | `integer` | No | `587` | 1–65535 | mail: SMTP port. Default 587. |
| `smtpSecurity` | `string` | No | — | `auto`, `ssl_on_connect`, `start_tls`, `none` | mail: SMTP transport security. Auto requires TLS. none is unencrypted debug/legacy mode and requires both the user option and allowInsecure=true. Default auto. |
| `smtpAllowInvalidCertificate` | `boolean` | No | `false` | — | mail only: store an SMTP debug exception that accepts an invalid, mismatched, expired, or self-signed TLS certificate. Requires the user option and allowInsecure=true on this create and every use; cannot be true with smtpSecurity='none'. |
| `host` | `string` | No | — | ≤ 253 characters | sftp/ftp: server host. |
| `port` | `integer` | No | — | 1–65535 | Server port. SFTP defaults to 22; FTP/explicit FTPS defaults to 21. |
| `security` | `string` | No | — | `auto`, `ssl_on_connect`, `start_tls`, `none` | File-transfer transport. SFTP accepts only auto (SSH). FTP auto/start_tls means explicit FTPS, ssl_on_connect means implicit FTPS, and none means plaintext FTP. Auto never downgrades. |
| `allowInsecure` | `boolean` | No | `false` | — | Required as true on this call when any selected transport is none or a mail endpoint allows an invalid TLS certificate. It works only after the user separately enabled insecure connector connections in Settings. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.connector_create",
  "arguments": {
    "displayName": "Production IMAP",
    "type": "mail",
    "host": "imap.example.com",
    "port": 993,
    "username": "agent@example.com",
    "password": "secretPassword123"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Created mail connector 'conn-mail-01' (Production IMAP) with default capability grants."
    }
  ],
  "structuredContent": {
    "ok": true,
    "id": "conn-mail-01",
    "displayName": "Production IMAP",
    "type": "mail",
    "grants": {
      "read": "ask",
      "organize": "ask",
      "send": "ask"
    }
  }
}
```

---

## 4. Operational Best Practices

* **Secret Vault Integration:** Provide `passwordFromVault: true` to bind directly to a Vault credential without supplying plaintext passwords.
* **Capability Default:** New connections default all capabilities to `ask` mode, prompting the human user on first interactive use.
* **Security Profiles:** Always prefer TLS (`imapSecurity: "SslTls"`, `smtpSecurity: "StartTls"`) over plaintext protocols.

---

## 5. Related Tools

* [`nova.connector_list`](nova-connector-list.md)
* [`nova.connector_grant_set`](nova-connector-grant-set.md)
* [`nova.connector_delete`](nova-connector-delete.md)
