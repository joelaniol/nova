# `nova.pks_platform_get`

> **Retrieves pre-trained platform-level UI pattern definitions (Shopify, WordPress, Jira).**

* **Capability Bundle:** `pks_learning`
* **Security Tier:** Tier 1 (Read-Only Platform Models)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.pks_platform_get` returns canonical component models and selectors for widespread web application platforms.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `stableId` | `string` | **Yes** | Non-empty platform stable ID. The runtime trims and lowercases it before lookup. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_pks_platform_get",
  "arguments": {
    "platformId": "shopify"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Retrieved Shopify platform pattern definition."
    }
  ],
  "structuredContent": {
    "ok": true,
    "platformId": "shopify",
    "componentModels": [
      "cart_drawer",
      "checkout_button",
      "variant_selector"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Platform Leveraging:** Utilize pre-trained platform models to avoid reinventing selectors across e-commerce stores.

---

## 5. Related Tools

* [`nova.pks_platform_list`](nova-pks-platform-list.md)
* [`nova.pks_platform_seed`](nova-pks-platform-seed.md)
