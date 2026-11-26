# `nova.vault_card_fill`

> **Upcoming release:** this tool ships with the next Nova version and is not in the published setup yet.

Fills a stored payment card into a checkout form, including card fields inside an embedded payment frame of another site.

---

## 1. Overview

You name the card fields and their roles (`number`, `expiry` or `expMonth`/`expYear`, `cvc`, `holder`) with a CSS selector and, for fields inside a frame, the `frameId` from `nova.perceive(deep=true)`. Nova checks the fields itself, asks the user to approve the fill with their Nova PIN, and types the values. The card number, expiry and security code never reach the agent.

From the moment the user is asked, the checkout tab gives agents nothing: no screenshot, page text, DOM, network data or script results. Close it with `nova.tab_close` when you are done and read the order result in a new tab of the same sandbox. With `submit` you register the pay button: the user approves "fill and pay" in one dialog, and [`nova.vault_card_submit`](nova-vault-card-submit.md) then clicks exactly that button.

When the user has set a purchase budget (see [`nova.purchase_budget_status`](nova-purchase-budget-status.md)) and it covers the order total, a fill with `submit` needs no PIN and no dialog; only a security code that is not stored is still asked. An order the budget does not cover goes to the dialog with the reason.

The answer names the roles that were filled and a `status` (`completed`, `partial`, `refused`) with a `reasonCode`, never values. A fill is refused while a screen recording runs and for a card that has expired (`card.expired`).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | — | — | Tab ID of the checkout, or 'active'. The tab is locked for agents from the approval on. |
| `cardId` | `string` | No | — | — | Card id from nova.vault_card_list. Optional when exactly one card is stored. |
| `fields` | `array` of `object` | Yes | — | 1–6 items | The card fields of the form. Each role once; a number field is required; all embedded fields must belong to one payment provider. |
| `submit` | `object` | No | — | — | Optional pay button to register. The user approves 'fill and pay' in one dialog; afterwards nova.vault_card_submit clicks exactly this button (twice at most; once when the purchase budget covers the order). |
| `submit.selector` | `string` | Yes | — | — | CSS selector of the pay button (button, input type=submit, or link). |
| `submit.frameId` | `string` | No | — | — | Frame of the button, when it sits in a frame. |
| `submit.label` | `string` | No | — | — | The button's visible text, shown to the user in the dialog (e.g. 'Jetzt kaufen'). |
| `agentId` | `string` | No | — | — | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `vault_auth` (load it with `nova.tools_bundle(bundle='vault_auth')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Example Call

```json
{
  "_meta": { "intent": "Pay the order the user asked for" },
  "targetId": "tab-7",
  "cardId": "3f2a9c...",
  "fields": [
    { "role": "number", "selector": "#credit-card-number", "frameId": "F1" },
    { "role": "expiry", "selector": "#expiration", "frameId": "F2" },
    { "role": "cvc", "selector": "#cvv", "frameId": "F3" }
  ],
  "submit": { "selector": "button.pay-now", "label": "Jetzt kaufen" }
}
```
