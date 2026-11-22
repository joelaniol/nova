# `nova.vault_card_delete`

> **Upcoming release:** this tool ships with the next Nova version and is not in the published setup yet.

Deletes a stored payment card.

---

## 1. Overview

Works only when the user allowed agents to manage payment cards in Nova's settings, and needs the user's approval in a Nova dialog. A deleted card's id is never used again.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `cardId` | `string` | Yes | — | — | Card id from nova.vault_card_list. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `vault_auth` (load it with `nova.tools_bundle(bundle='vault_auth')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Example Call

```json
{
  "_meta": { "intent": "Remove the expired card" },
  "cardId": "3f2a9c..."
}
```
