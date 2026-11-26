# `nova.purchase_budget_status`

> **Upcoming release:** this tool ships with the next Nova version and is not in the published setup yet.

Shows the purchase budget the user set for agents: whether buying on their own is switched on, the currency, and how much is left.

---

## 1. Overview

The user decides in Nova's settings whether agents may buy on their own and sets a budget in one currency for it. Within that budget a purchase step (a click on the pay button, or a card fill that registers the pay button) goes ahead without a dialog; anything the budget does not cover asks the user as before. Only the user refills the budget.

Use this tool to plan before you shop: it returns `enabled`, `currency` and the amounts `total`, `available`, `reserved`, `committed` and `unresolved` in major units of that currency (for example `12.50`). The figures are a snapshot, not an authorization: Nova checks the order again at the click, and a price that changed in between is checked against the budget once more.

When no budget is set or buying on their own is switched off, every purchase asks the user. `budgetReadable: false` means Nova could not read its budget file; buying on their own is then off until the user sets a new budget. The tool also answers while a checkout tab is locked after a card fill.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `vault_auth` (load it with `nova.tools_bundle(bundle='vault_auth')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Example Call

```json
{
  "_meta": { "intent": "Check the purchase budget before ordering" }
}
```
