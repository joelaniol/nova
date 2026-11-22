# `nova.vault_card_list`

> **Upcoming release:** this tool ships with the next Nova version and is not in the published setup yet.

Lists the payment cards stored in Nova without their numbers.

---

## 1. Overview

Use it to pick the `cardId` for [`nova.vault_card_fill`](nova-vault-card-fill.md). Each card comes with its label, brand, last 4 digits, expiry and whether a security code is stored. The card number and the security code are never returned. An empty list means the user has not stored a card yet; they add cards in Nova's settings.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `vault_auth` (load it with `nova.tools_bundle(bundle='vault_auth')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Example Call

```json
{
  "_meta": { "intent": "Pick the card for the checkout" }
}
```
