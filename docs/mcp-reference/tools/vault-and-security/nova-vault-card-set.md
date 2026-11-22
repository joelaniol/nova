# `nova.vault_card_set`

> **Upcoming release:** this tool ships with the next Nova version and is not in the published setup yet.

Adds a payment card to Nova or changes a stored one.

---

## 1. Overview

Works only when the user allowed agents to manage payment cards in Nova's settings (off by default). Every add or change also needs the user's approval in a Nova dialog that shows brand, last 4 digits and expiry. Nova checks the number (digits, length, check digit) and refuses an expiry in the past. The answer is the card summary, never the number. A change voids every approval that was kept for the card.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `cardId` | `string` | No | — | — | Change this card. Omit to add a new one. |
| `label` | `string` | No | — | — | Name shown to the user, e.g. 'Visa private'. Default: brand and last 4 digits. |
| `holder` | `string` | No | — | — | Name on the card. |
| `number` | `string` | No | — | — | Card number, 12-19 digits; spaces and dashes are ignored. Required when adding. |
| `expMonth` | `integer` | No | — | 1–12 | Expiry month 1-12. Required when adding. |
| `expYear` | `integer` | No | — | — | Expiry year, four digits or two (28 = 2028). Required when adding. |
| `cvc` | `string` | No | — | — | Optional security code (3-4 digits) to keep with the card. Without it the user types the CVC into Nova's dialog at each fill. |
| `removeCvc` | `boolean` | No | `false` | — | On a change: forget the stored CVC. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `vault_auth` (load it with `nova.tools_bundle(bundle='vault_auth')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Example Call

```json
{
  "_meta": { "intent": "Store the card the user gave me" },
  "label": "Visa private",
  "holder": "Alex Example",
  "number": "4111 1111 1111 1111",
  "expMonth": 12,
  "expYear": 2028
}
```
