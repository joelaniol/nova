# `nova.ui_client_certificate_prompt_resolve`

> **Selects a client certificate or cancels a mutual TLS (mTLS) authentication prompt.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Security Gate Resolution)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_client_certificate_prompt_resolve` selects a specific installed X.509 client certificate to satisfy an mTLS handshake challenge.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `decision` | `string` | **Yes** | send_none: identify with no certificate. send: present the certificate named by 'subject'. |
| `subject` | `string` | No | Required for 'send'. Matched case-insensitively against the subject of the offered certificates; the failure response lists them. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_client_certificate_prompt_resolve",
  "arguments": {
    "action": "select",
    "certificateThumbprint": "9A7B31F2E8C04..."
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Selected client certificate for mTLS."
    }
  ],
  "structuredContent": {
    "ok": true,
    "action": "select",
    "certificateThumbprint": "9A7B31F2E8C04..."
  }
}
```

---

## 4. Operational Best Practices

* **mTLS Authentication:** Provide valid certificate thumbprint registered in the Windows Personal certificate store.

---

## 5. Related Tools

* [`nova.ui_certificate_prompt_resolve`](nova-ui-certificate-prompt-resolve.md)
