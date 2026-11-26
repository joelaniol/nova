# `nova.vault_card_submit`

> **Upcoming release:** this tool ships with the next Nova version and is not in the published setup yet.

Clicks the pay button that was registered with a card fill and approved by the user.

---

## 1. Overview

Only the button named in `submit` of [`nova.vault_card_fill`](nova-vault-card-fill.md) can be clicked, only if it is still the same element, and only by the agent session that filled the card.

- **The user approved "fill and pay":** at most two clicks. The answer is always `status: accepted` and says nothing about what happened, because the checkout tab gives agents no content.
- **The user's purchase budget covered the order** (see [`nova.purchase_budget_status`](nova-purchase-budget-status.md)): one click. Nova reads the total again right before it. The answer is `status: accepted`, or `status: refused` with a `reasonCode` when Nova did not click, for example because the order changed, the budget no longer covers it, or the pay button changed. After a refusal do not retry and do not pay another way; tell the user.

Close the tab afterwards and check the order in a new tab of the same sandbox.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | — | — | Tab ID of the checkout, or 'active'. |
| `agentId` | `string` | No | — | — | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `vault_auth` (load it with `nova.tools_bundle(bundle='vault_auth')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Example Call

```json
{
  "_meta": { "intent": "Complete the approved payment" },
  "targetId": "tab-7"
}
```
