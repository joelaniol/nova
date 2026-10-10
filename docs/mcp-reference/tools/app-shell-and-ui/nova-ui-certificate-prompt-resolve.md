# `nova.ui_certificate_prompt_resolve`

> **Answers Nova's dialog for a server certificate it could not verify: refuse the connection or proceed for this session.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

When a site presents a server certificate that cannot be verified (for example a self-signed certificate on an internal or development server), Nova asks before continuing. `nova.ui_certificate_prompt_resolve` answers that dialog for the agent. `refuse` declines the connection and unblocks browsing. `proceed` continues with the unverified certificate; the exception covers this one certificate for the rest of the session and is recorded in Nova's log with the certificate fingerprint.

If no dialog is open, the call returns `ok: false` with `reasonCode: "certificate.no_prompt_open"`; a second answer to a dialog that is already closing returns `certificate.already_answered`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `decision` | `string` | Yes | — | `proceed`, `refuse` | refuse: decline the connection (safe, unblocks browsing). proceed: continue with an unverified certificate for this session. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_certificate_prompt_resolve",
  "arguments": {
    "decision": "proceed"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Certificate prompt resolved (proceed, status=accepted)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "decision": "proceed",
    "status": "accepted",
    "reasonCode": "none",
    "message": "The connection continues with a certificate Nova could not verify. It may be read or altered in transit. The exception covers this one certificate for the rest of the session.",
    "promptWasOpen": true,
    "host": "dev.internal.example",
    "fingerprint": "3FA81C0B92D47E65",
    "exceptionGranted": true
  }
}
```

With `decision: "refuse"` the result reports `status: "refused"` and `exceptionGranted: false`.

---

## 4. Operational Best Practices

* **Development Only:** Proceed only for hosts you control or know, such as internal or development servers. Refuse on public websites.
* **Check the host:** Compare `host` in the result with the server the task targets.

---

## 5. Related Tools

* [`nova.ui_client_certificate_prompt_resolve`](nova-ui-client-certificate-prompt-resolve.md)
