# `nova.ui_certificate_prompt_resolve`

> **Resolves an untrusted or invalid SSL/TLS server certificate security dialog.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Security Gate Resolution)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_certificate_prompt_resolve` allows automated workflows to proceed through self-signed certificate warnings in development environments or cancel unsafe requests.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `decision` | `string` | **Yes** | refuse: decline the connection (safe, unblocks browsing). proceed: continue with an unverified certificate for this session. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_certificate_prompt_resolve",
  "arguments": {
    "action": "proceed_once"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Proceeded past SSL certificate warning."
    }
  ],
  "structuredContent": {
    "ok": true,
    "action": "proceed_once",
    "bypassActive": true
  }
}
```

---

## 4. Operational Best Practices

* **Development Only:** Never bypass certificate warnings on external production websites.
* **Audit Trail:** Log all certificate bypass decisions with reasons.

---

## 5. Related Tools

* [`nova.ui_client_certificate_prompt_resolve`](nova-ui-client-certificate-prompt-resolve.md)
