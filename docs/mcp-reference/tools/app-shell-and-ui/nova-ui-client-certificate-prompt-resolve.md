# `nova.ui_client_certificate_prompt_resolve`

> **Answers Nova's client-certificate dialog: send a named certificate or continue without one.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

When a server asks the browser for a client certificate (mutual TLS), Nova shows a dialog with the certificates on offer. `nova.ui_client_certificate_prompt_resolve` answers it for the agent. `send_none` continues without a certificate and the site decides how to proceed. `send` presents the certificate whose subject contains the given `subject` text (case-insensitive); there is no fallback to another certificate.

If `subject` is missing or matches nothing, the call returns `ok: false` with `status: "not_found"` (`client_certificate.subject_required` or `client_certificate.subject_not_found`), lists the offered subjects in `availableSubjects`, and leaves the dialog open. If no dialog is open, the reason code is `client_certificate.no_prompt_open`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `decision` | `string` | Yes | — | `send`, `send_none` | send_none: identify with no certificate. send: present the certificate named by 'subject'. |
| `subject` | `string` | No | — | ≤ 512 characters | Required for 'send'. Matched case-insensitively against the subject of the offered certificates; the failure response lists them. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_client_certificate_prompt_resolve",
  "arguments": {
    "decision": "send",
    "subject": "CN=build-agent-01"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Client-certificate prompt resolved (send, status=sent)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "decision": "send",
    "status": "sent",
    "reasonCode": "none",
    "message": "The certificate was sent; the server now knows this identity.",
    "promptWasOpen": true,
    "availableCount": 2,
    "sentSubject": "CN=build-agent-01, O=Example Corp",
    "availableSubjects": []
  }
}
```

---

## 4. Operational Best Practices

* **Name the identity:** Sending a certificate tells the server who you are. Pass a `subject` that identifies exactly the certificate the task requires; a failed match lists the offered subjects so you can choose.

---

## 5. Related Tools

* [`nova.ui_certificate_prompt_resolve`](nova-ui-certificate-prompt-resolve.md)
