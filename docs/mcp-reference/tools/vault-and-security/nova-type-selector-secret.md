# `nova.type_selector_secret`

Types a vault password into a target form field using an ephemeral `SecretRef` token, setting the value through the field's native value setter and dispatching input/change events, without exposing plaintext secrets to the agent.

---

## 1. Overview

`nova.type_selector_secret` is the counterpart to [`nova.vault_prepare_fill`](nova-vault-prepare-fill.md). It receives an opaque `SecretRef` token, verifies that the target tab's active origin matches the token's cryptographic grant, ensures the token has not expired or already been redeemed, and sets the password into the designated input field through its native value setter (not simulated keystrokes), then dispatches `input`/`change` events.

* **Zero Plaintext Leakage:** Neither the agent nor the MCP JSON-RPC protocol messages ever handle the plaintext password.
* **Granular Failure Codes:** Distinguishes `secretref_not_found`, `secretref_expired`, `secretref_origin_mismatch`, and `secretref_already_used` (returned as both a `reason` string and a `vault.`-prefixed `reasonCode`) so agents make intelligent retry decisions.
* **Field Reset (`clear: true`):** Automatically clears any placeholder or residual characters in the password input prior to typing.
* **Native Autofill Warning:** Detects when native browser autofill popovers might overlay the input and notifies the agent via `autofillPopupWarning`.

---

## 2. Token Redemption Lifecycle

1. `nova.vault_prepare_fill` issues a `SecretRef`: bound to the target origin, valid for 2 hours, usable once.
2. `nova.type_selector_secret` redeems it. Nova checks, in this order of outcome:
   - **expired** (`secretref_expired`): request a new one with `nova.vault_prepare_fill`.
   - **already used** (`secretref_already_used`): request a new one.
   - **different origin** (`secretref_origin_mismatch`): nothing was typed; the same reference still works on the origin it is bound to, or request a new one.
3. On success Nova types the password into the field; the agent never sees it.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | — | — | Tab ID or 'active'. |
| `selector` | `string` | Yes | — | — | CSS selector for the password input field. |
| `secretRef` | `string` | Yes | — | — | SecretRef token from nova.vault_prepare_fill. |
| `clear` | `boolean` | No | `true` | — | Clear field before typing. Default: true. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `vault_auth` (load it with `nova.tools_bundle(bundle='vault_auth')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 4. Example Call

```json
{
  "_meta": { "intent": "Submitting user login credentials" },
  "selector": "input#login_field_password",
  "secretRef": "A819B02FE4918237C1894D2FF009988",
  "clear": true
}
```

---

## 5. Return Value Structure

```json
{
  "ok": true,
  "selector": "input#login_field_password",
  "targetId": "tab-101",
  "actionDispatched": true,
  "autofillPopupWarning": null,
  "autofillFieldRole": null
}
```

`autofillPopupWarning` is a text warning (not a boolean) when native password-manager UI may overlay the field, and `null` otherwise; `autofillFieldRole` names the detected field role when known.

---

## 6. Common Errors & Troubleshooting

| reasonCode / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `aag:safety.perceive_first` | The Automated Actions Guard (AAG) requires visual page perception before sensitive input. | Call [`nova.perceive`](../dom-and-reading/nova-perceive.md) on the target tab, then retry with the **same** unredeemed `secretRef`. |
| `vault.secretref_origin_mismatch` | Tab navigated away from the origin where `vault_prepare_fill` was requested. | Use the same token back on its bound origin, or mint a fresh token. |
| `vault.secretref_already_used` | Token was already redeemed in a previous call. | Request a new token via [`nova.vault_prepare_fill`](nova-vault-prepare-fill.md). |
| `vault.secretref_expired` | More than 120 minutes elapsed since the token was issued. | Request a fresh token. |
| `vault.entry_missing` | The vault entry behind the token was deleted after the token was issued. | Request a new token via [`nova.vault_prepare_fill`](nova-vault-prepare-fill.md). |

---

## 7. Related Tools & Documentation

* [`nova.vault_prepare_fill`](nova-vault-prepare-fill.md) — Request the ephemeral `SecretRef` token.
* [`nova.type_selector`](../browser-automation/nova-type-selector.md) — For typing non-secret fields (usernames, emails).
* [`nova.click_selector`](../browser-automation/nova-click-selector.md) — Click submit buttons after typing credentials.
* [Automated Actions Guide (AAG)](../../../core-features/agent-awareness-gates-aag/README.md) — Guardrails for automated credential submission.
