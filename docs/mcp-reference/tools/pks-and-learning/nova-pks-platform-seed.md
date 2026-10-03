# `nova.pks_platform_seed`

> **Seeds the platform knowledge base with pre-trained platform component models.**

* **Security Tier:** Tier 2 (Platform Seeding)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.pks_platform_seed` imports pre-packaged platform heuristics and selector models into the local PKS database.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `stableId` | `string` | Yes | — | ≥ 1 characters | Unique non-empty platform identifier. The runtime trims whitespace, stores it in canonical lowercase form (for example 'onetrust' or 'cookiebot'), and rejects the reserved legacy test-only pattern 'platform-{32hex}'. |
| `displayName` | `string` | Yes | — | ≥ 1 characters | Human-readable non-empty platform name. Leading and trailing whitespace are trimmed before persistence. |
| `description` | `string` | No | — | — | Optional platform description. Whitespace-only values are normalized to null. |
| `homepageUrl` | `string` | No | — | — | Optional homepage URL. Whitespace-only values are normalized to null. |
| `patterns` | `array` of `object` | No | — | ≥ 1 items | Pattern templates to upsert. When provided, the array must contain at least one entry. |
| `aliases` | `array` of `object` | No | — | ≥ 1 items | Aliases for vendor/script domain lookups. When provided, the array must contain at least one entry. |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
<!-- /generated:parameters -->

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
