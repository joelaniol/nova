# `nova.learn_onboarding_recall`

> **Recalls learned onboarding tutorial dismissal steps for a domain.**

* **Capability Bundle:** `pks_learning`
* **Security Tier:** Tier 1 (Read-Only Learning)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.learn_onboarding_recall` queries stored onboarding sequences to automatically skip tours and welcome wizards upon page load.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `domain` | `string` | No | Optional. When omitted, the session's currently activated learn-mode domain is used. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_learn_onboarding_recall",
  "arguments": {
    "domain": "app.example.com"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 2 completed onboarding steps."
    }
  ],
  "structuredContent": {
    "ok": true,
    "domain": "app.example.com",
    "completedSteps": [
      "welcome_modal_dismissed",
      "feature_tour_skipped"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Check at Navigation:** Call immediately after `nova.navigate` on complex web apps.

---

## 5. Related Tools

* [`nova.learn_onboarding_confirm`](nova-learn-onboarding-confirm.md)
