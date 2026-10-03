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

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `domain` | `string` | No | — | — | Optional. When omitted, the session's currently activated learn-mode domain is used. |
<!-- /generated:parameters -->

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
