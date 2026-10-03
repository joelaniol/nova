# `nova.type_selector_secret`

Types a vault password into a target form field using an ephemeral `SecretRef` token, injecting keystrokes directly via CDP without exposing plaintext secrets to the agent.

---

## 1. Overview

`nova.type_selector_secret` is the counterpart to [`nova.vault_prepare_fill`](nova-vault-prepare-fill.md). It receives an opaque `SecretRef` token, verifies that the target tab's active origin matches the token's cryptographic grant, ensures the token has not expired or already been redeemed, and injects the password keystrokes into the designated input field.

* **Capability Bundle:** `vault_and_security`, `form_submission`
* **Zero Plaintext Leakage:** Neither the agent nor the MCP JSON-RPC protocol messages ever handle the plaintext password.
* **Granular Failure Codes:** Distinguishes `not_found`, `expired`, `origin_mismatch`, and `already_used` so agents make intelligent retry decisions.
* **Field Reset (`clear: true`):** Automatically clears any placeholder or residual characters in the password input prior to typing.
* **Native Autofill Warning:** Detects when native browser autofill popovers might overlay the input and notifies the agent via `autofillPopupWarning`.

---

## 2. Token Redemption Lifecycle

```
[vault_prepare_fill]
        ?
        ? (issues SecretRef: origin-bound, TTL=120m, single-use)
[Agent calls type_selector_secret]
        ?
   +--------------------------------+
   ? Check: Has target origin changed?? --? [origin_mismatch: Hard Error]
   +--------------------------------+
        ?
   +--------------------------------+
   ? Check: Has 120m expired?       ? --? [expired: Request New Token]
   +--------------------------------+
        ?
   +--------------------------------+
   ? Check: Already redeemed?       ? --? [already_used: Single-use violation]
   +--------------------------------+
        ?
   +--------------------------------+
   ? Check: AAG perceive_first set? ? --? [Blocked: Call perceive, then retry token]
   +--------------------------------+
        ?
        ? (All Valid)
   Inject Keystrokes via CDP --? Invalidate SecretRef --? Success
```

---

## 3. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`selector`** | `string` | **Yes** | ? | CSS selector for the password input field. Supports ` >>> `. |
| **`secretRef`** | `string` | **Yes** | ? | Ephemeral token obtained from `nova.vault_prepare_fill`. |
| **`clear`** | `boolean` | No | `true` | Clear existing field contents before typing. |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs`, or `"active"`. |
| **`_meta.intent`**| `string` | **Conditional**| ? | Audit trail statement explaining password injection. |
| **`agentId`** | `string` | No | `"default"` | Agent identity for claim lease verification. |

---

## 4. Example Call

```json
{
  "_meta": { "intent": "Submitting user login credentials" },
  "selector": "input#login_field_password",
  "secretRef": "sref_a819b02fe4918237c1894d",
  "clear": true
}
```

---

## 5. Return Value Structure

```json
{
  "success": true,
  "selector": "input#login_field_password",
  "targetId": "tab-101",
  "cleared": true,
  "charactersInjected": 16,
  "autofillPopupWarning": false
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `safety.perceive_first blocked` | The Automated Actions Guard (AAG) requires visual page perception before sensitive input. | Call [`nova.perceive`](../dom-and-reading/nova-perceive.md) on the target tab, then retry with the **same** unredeemed `secretRef`. |
| `origin_mismatch` | Tab navigated away from the origin where `vault_prepare_fill` was requested. | Re-navigate to correct URL and mint a fresh token. |
| `already_used` | Token was already redeemed in a previous call. | Request a new token via [`nova.vault_prepare_fill`](nova-vault-prepare-fill.md). |
| `expired` | More than 120 minutes elapsed since the token was issued. | Request a fresh token. |

---

## 7. Related Tools & Documentation

* [`nova.vault_prepare_fill`](nova-vault-prepare-fill.md) ? Request the ephemeral `SecretRef` token.
* [`nova.type_selector`](../browser-automation/nova-type-selector.md) ? For typing non-secret fields (usernames, emails).
* [`nova.click_selector`](../browser-automation/nova-click-selector.md) ? Click submit buttons after typing credentials.
* [Automated Actions Guide (AAG)](../../../core-features/aag.md) ? Guardrails for automated credential submission.
