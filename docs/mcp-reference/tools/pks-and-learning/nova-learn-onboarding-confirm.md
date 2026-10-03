# `nova.learn_onboarding_confirm`

> **Confirms that a learned onboarding flow step was successfully completed.**

* **Capability Bundle:** `pks_learning`
* **Security Tier:** Tier 2 (Onboarding Learning)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.learn_onboarding_confirm` marks a tutorial or tour step as verified, updating domain onboarding state in PKS.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `domain` | `string` | **Yes** | The domain the AAG gate fired against. Must match an active learn-mode activation for this session. |
| `paraphrase` | `string` | **Yes** | Your restatement of the onboarding contract in your own words. 80-800 characters, no boilerplate, at least 4 distinct content tokens. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_learn_onboarding_confirm",
  "arguments": {
    "domain": "app.example.com",
    "stepKey": "welcome_modal_dismissed"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Confirmed onboarding step welcome_modal_dismissed for app.example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "domain": "app.example.com",
    "stepKey": "welcome_modal_dismissed",
    "status": "Completed"
  }
}
```

---

## 4. Operational Best Practices

* **Tutorial Bypass:** Prevents repeated display of first-time user tutorials across sessions.

---

## 5. Related Tools

* [`nova.learn_onboarding_recall`](nova-learn-onboarding-recall.md)
