# `nova.learn_suggest`

> **Suggests alternative interaction selectors based on historical pattern performance.**

* **Capability Bundle:** `pks_learning`
* **Security Tier:** Tier 1 (Read-Only Suggestions)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.learn_suggest` queries PKS historical execution data to recommend robust fallback selectors when a primary CSS selector breaks.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | No | — | — | Domain scope to filter suggestions for (e.g. 'github.com'). If omitted, returns cross-domain opportunities. |
| `limit` | `integer` | No | `5` | 1–20 | Maximum number of suggestions to return (1-20). Default 5. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_learn_suggest",
  "arguments": {
    "scope": "shop.example.com",
    "targetSelector": "button#buy-now"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Suggested 2 fallback selectors: button[data-testid=\"checkout-btn\"], .btn-checkout."
    }
  ],
  "structuredContent": {
    "ok": true,
    "suggestions": [
      "button[data-testid=\"checkout-btn\"]",
      ".btn-checkout"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Self-Healing Scripts:** Call when `nova.click_selector` fails to find an element.

---

## 5. Related Tools

* [`nova.pks_match`](nova-pks-match.md)
* [`nova.revalidate`](nova-revalidate.md)
