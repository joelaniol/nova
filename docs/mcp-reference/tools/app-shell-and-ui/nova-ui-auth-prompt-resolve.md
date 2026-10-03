# `nova.ui_auth_prompt_resolve`

> **Resolves an active HTTP 401 Basic or Digest authentication challenge dialog.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Modal & Dialog Resolution)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_auth_prompt_resolve` injects credentials into or cancels Nova's native HTTP authentication prompt modal.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `decision` | `string` | **Yes** | use_vault: sign in with a stored entry for this origin. cancel: decline the challenge and unblock browsing. |
| `username` | `string` | No | Optional. Selects one vault entry when the origin has several. Ignored for 'cancel'. A name that matches no stored entry fails with 'auth.vault_entry_not_found' rather than falling back to another entry. |

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
