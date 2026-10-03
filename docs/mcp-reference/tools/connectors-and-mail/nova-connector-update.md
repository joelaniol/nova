# `nova.connector_update`

Updates configuration, endpoints, credentials, or signatures of an existing connection.

---

## 1. Overview

`nova.connector_update` modifies settings for a previously registered connector. Only specified fields are updated; omitted fields retain their existing values.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 2 (Connector Mutation)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`allowInsecure`** | `boolean` | No | `false` | Required as true when the resulting profile uses security=none or allows an invalid mail TLS certificate; the user's separate Settings option must also be enabled. |
| **`authMode`** | `string` | No | `null` | sftp only: new authentication method. |
| **`displayName`** | `string` | No | `null` | New display name. |
| **`host`** | `string` | No | `null` | sftp/ftp: server host. |
| **`id`** | `string` | Yes | `null` | Connector id (from nova.connector_list). |
| **`imapAllowInvalidCertificate`** | `boolean` | No | `null` | mail only: whether this IMAP endpoint accepts an invalid TLS certificate as an explicitly gated debug exception. false restores strict validation; cannot be true with imapSecurity='none'. |
| **`imapHost`** | `string` | No | `null` | mail: incoming (IMAP) server host. |
| **`imapPort`** | `integer` | No | `null` | mail: IMAP port. |
| **`imapSecurity`** | `string` | No | `null` | mail: IMAP transport security. none is the explicitly gated unencrypted mode. |
| **`keyPassphrase`** | `string` | No | `null` | sftp + private_key only: write-only replacement passphrase; empty clears it. Never returned. |
| **`password`** | `string` | No | `null` | Write-only. Replaces the stored password; never returned. |
| **`passwordFromVault`** | `string` | No | `null` | Instead of password: the id of a Nova vault entry (from nova.vault_list). Nova copies that entry's password into this connection internally - you never see it. The user confirms each copy in a dialog that shows the saved login next to this connection's servers, because a web login is not always the mail/server login. The user may answer 'always' for exactly this entry and these servers; then later copies of that pair (also unattended) need no prompt, while a different entry or server still asks. Mutually exclusive with password; needs authMode='password'. Without such an answer unattended runs are refused (-32033); a declined prompt returns -32029 and stores nothing. |
| **`port`** | `integer` | No | `null` | sftp/ftp: port. |
| **`privateKeyPath`** | `string` | No | `null` | sftp + private_key only: new write-only host path to a private key; never returned. |
| **`security`** | `string` | No | `null` | File-transfer transport. SFTP accepts only auto; FTP auto/start_tls is explicit FTPS, ssl_on_connect is implicit FTPS, and none is plaintext FTP. |
| **`signatureHtml`** | `string` | No | `null` | mail only: the same signature text block as HTML for HTML mails (not a cryptographic signature); without it an HTML mail gets the text signature. Empty string clears it. |
| **`signatureText`** | `string` | No | `null` | mail only: the signature TEXT BLOCK (name, company, phone - the sig block below a mail, NOT a cryptographic/S-MIME signature; Nova does not sign mails), appended below every sent mail and draft after the standard "-- " line (nova.mail_send includeSignature=false leaves it off). Empty string clears it; connector_list shows it. |
| **`smtpAllowInvalidCertificate`** | `boolean` | No | `null` | mail only: whether this SMTP endpoint accepts an invalid TLS certificate as an explicitly gated debug exception. false restores strict validation; cannot be true with smtpSecurity='none'. |
| **`smtpHost`** | `string` | No | `null` | mail: outgoing (SMTP) server host. |
| **`smtpPort`** | `integer` | No | `null` | mail: SMTP port. |
| **`smtpSecurity`** | `string` | No | `null` | mail: SMTP transport security. none is the explicitly gated unencrypted mode. |
| **`username`** | `string` | No | `null` | New username / e-mail address. |

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
      "text": "Updated connection conn-mail-01."
    }
  ],
  "structuredContent": {
    "ok": true,
    "id": "conn-mail-01",
    "updatedFields": [
      "displayName",
      "smtpHost"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Type Immutability:** Connector type (`mail`, `sftp`, `ftp`) cannot be changed after creation; create a new connector if switching protocol families.
* **Password Rotation:** Supplying a new `password` re-encrypts the secret under DPAPI and preserves existing capability grants.

---

## 5. Related Tools

* [`nova.connector_list`](nova-connector-list.md)
* [`nova.connector_delete`](nova-connector-delete.md)
