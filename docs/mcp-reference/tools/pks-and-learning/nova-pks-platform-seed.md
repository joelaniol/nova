# `nova.pks_platform_seed`

> **Seeds the platform knowledge base with pre-trained platform component models.**

* **Capability Bundle:** `pks_learning`
* **Security Tier:** Tier 2 (Platform Seeding)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.pks_platform_seed` imports pre-packaged platform heuristics and selector models into the local PKS database.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `aliases` | `array` | No | Aliases for vendor/script domain lookups. When provided, the array must contain at least one entry. |
| `description` | `string` | No | Optional platform description. Whitespace-only values are normalized to null. |
| `displayName` | `string` | **Yes** | Human-readable non-empty platform name. Leading and trailing whitespace are trimmed before persistence. |
| `homepageUrl` | `string` | No | Optional homepage URL. Whitespace-only values are normalized to null. |
| `patterns` | `array` | No | Pattern templates to upsert. When provided, the array must contain at least one entry. |
| `stableId` | `string` | **Yes** | Unique non-empty platform identifier. The runtime trims whitespace, stores it in canonical lowercase form (for example 'onetrust' or 'cookiebot'), and rejects the reserved legacy test-only pattern 'platform-{32hex}'. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_pks_platform_seed",
  "arguments": {
    "platformId": "shopify",
    "overwrite": false
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Seeded Shopify platform models (12 components)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "platformId": "shopify",
    "componentsLoaded": 12
  }
}
```

---

## 4. Operational Best Practices

* **Initialization:** Run during workstation onboarding to prime agent capabilities.

---

## 5. Related Tools

* [`nova.pks_platform_get`](nova-pks-platform-get.md)
