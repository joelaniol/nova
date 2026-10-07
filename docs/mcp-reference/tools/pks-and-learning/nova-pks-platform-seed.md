# `nova.pks_platform_seed`

> **Creates or updates a platform entry (for example a cookie-consent vendor) with pattern templates and lookup aliases.**

* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/phenomenological-knowledge-store-pks/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.pks_platform_seed` writes a platform to the PKS: a vendor or product that appears on many sites, such as a consent manager. A platform carries pattern templates (`patterns`: type `consent_cmp`, `modal`, `paywall` or `login_wall`, with fingerprint, playbook, applicability and priority) and aliases (`aliases`: kind `vendor_marker`, `script_domain` or `dom_id` plus a value) that let Nova recognise the platform on a page. When `nova.pks_match` finds no domain-specific phenomenon, it falls back to matching platform patterns. At least one pattern or one alias is required. Existing entries with the same `stableId` are updated; an alias that already belongs to another platform is rejected.

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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_pks_platform_seed",
  "arguments": {
    "stableId": "cookiebot",
    "displayName": "Cookiebot",
    "homepageUrl": "https://www.cookiebot.com/",
    "aliases": [
      { "kind": "script_domain", "value": "consent.cookiebot.com" }
    ]
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Platform 'cookiebot' seeded: 0 patterns, 1 aliases."
    }
  ],
  "structuredContent": {
    "ok": true,
    "platformId": 12,
    "stableId": "cookiebot",
    "patternsUpserted": 0,
    "aliasesUpserted": 1
  }
}
```

`platformId` is Nova's internal numeric ID of the platform entry; use `stableId` to refer to the platform in other calls.

---

## 4. Operational Best Practices

* **Check first:** Use `nova.pks_platform_list` to see which platforms already exist before creating a new `stableId`.
* **Descriptive IDs:** Use the vendor name in lowercase (`onetrust`, `cookiebot`); the test-only pattern `platform-{32hex}` is rejected.

---

## 5. Related Tools

* [`nova.pks_platform_get`](nova-pks-platform-get.md)
