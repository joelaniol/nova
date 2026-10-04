# `nova.ui_auth_prompt_resolve`

> **Answers Nova's HTTP sign-in dialog with a stored vault entry, or cancels it.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_auth_prompt_resolve` answers the sign-in dialog Nova shows when a server asks for HTTP authentication. The agent never passes a password: with `decision: "use_vault"`, Nova looks up the vault entries stored for the dialog's origin and sends the matching one itself. If the origin has several entries, pass `username` to choose one; Nova does not guess. `cancel` declines the sign-in; the request fails and browsing is unblocked.

The agent gets one attempt per origin and session: if the server asks again after credentials were sent, further `use_vault` calls for that origin return `status: "blocked"` (`auth.retry_budget_exhausted`) and the dialog stays open for the user, because repeated failed sign-ins can get the IP address banned. Other outcomes without sign-in: `not_found` (`auth.vault_entry_not_found`), `ambiguous` (`auth.vault_entry_ambiguous`), `error` (`auth.vault_unavailable`) and `noop` (`auth.no_prompt_open`).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `decision` | `string` | Yes | — | `use_vault`, `cancel` | use_vault: sign in with a stored entry for this origin. cancel: decline the challenge and unblock browsing. |
| `username` | `string` | No | — | ≤ 256 characters | Optional. Selects one vault entry when the origin has several. Ignored for 'cancel'. A name that matches no stored entry fails with 'auth.vault_entry_not_found' rather than falling back to another entry. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_auth_prompt_resolve",
  "arguments": {
    "decision": "use_vault",
    "username": "admin"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Sign-in prompt resolved (use_vault, status=submitted)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "decision": "use_vault",
    "status": "submitted",
    "reasonCode": "none",
    "message": "Credentials were sent. The server has not confirmed them yet; a repeat challenge for this origin means they were refused, and the agent path then closes for the session.",
    "promptWasOpen": true,
    "origin": "https://intranet.example.com",
    "vaultEntryUsed": true,
    "usedUserName": "admin",
    "vaultMatchCount": 1,
    "failedAttempts": 0
  }
}
```

---

## 4. Operational Best Practices

* **Store the entry first:** The vault must hold an entry for the origin; save one with `nova.vault_set` and check with `nova.vault_list`.
* **Recognise the dialog:** While the dialog is open, other tool calls are blocked and their result names this tool under `nextActions`.
* **Name the account:** Pass `username` whenever more than one entry exists for the origin, so the single attempt is not spent on the wrong account.

---

## 5. Related Tools

* [`nova.ui_get_state`](nova-ui-get-state.md)
* [`nova.vault_list`](../vault-and-security/nova-vault-list.md)
* [`nova.vault_set`](../vault-and-security/nova-vault-set.md)
