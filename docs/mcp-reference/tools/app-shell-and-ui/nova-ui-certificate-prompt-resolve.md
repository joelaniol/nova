# `nova.ui_certificate_prompt_resolve`

> **Resolves an untrusted or invalid SSL/TLS server certificate security dialog.**

* **Security Tier:** Tier 2 (Security Gate Resolution)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_certificate_prompt_resolve` allows automated workflows to proceed through self-signed certificate warnings in development environments or cancel unsafe requests.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `decision` | `string` | Yes | — | `proceed`, `refuse` | refuse: decline the connection (safe, unblocks browsing). proceed: continue with an unverified certificate for this session. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
<!-- /generated:parameters -->

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
