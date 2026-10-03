# `nova.ui_auth_prompt_resolve`

> **Resolves an active HTTP 401 Basic or Digest authentication challenge dialog.**

* **Security Tier:** Tier 2 (Modal & Dialog Resolution)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_auth_prompt_resolve` injects credentials into or cancels Nova's native HTTP authentication prompt modal.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `decision` | `string` | Yes | — | `use_vault`, `cancel` | use_vault: sign in with a stored entry for this origin. cancel: decline the challenge and unblock browsing. |
| `username` | `string` | No | — | ≤ 256 characters | Optional. Selects one vault entry when the origin has several. Ignored for 'cancel'. A name that matches no stored entry fails with 'auth.vault_entry_not_found' rather than falling back to another entry. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_auth_prompt_resolve",
  "arguments": {
    "action": "confirm",
    "username": "admin",
    "password": "secretpassword123"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Resolved HTTP authentication challenge."
    }
  ],
  "structuredContent": {
    "ok": true,
    "resolved": true,
    "action": "confirm"
  }
}
```

---

## 4. Operational Best Practices

* **Prompt Inspection:** Inspect dialog state with `nova.ui_get_state` first to confirm an auth dialog is waiting.
* **Credential Security:** Use ephemeral credentials or fetch secrets securely from `nova.vault_get`.

---

## 5. Related Tools

* [`nova.ui_get_state`](nova-ui-get-state.md)
* [`nova.vault_get`](../vault-and-security/nova-vault-get.md)
