# `nova.pks_upsert_hint`

> **Creates or updates a domain hint: CSS selectors that mark ad containers, noise regions or result items on a site.**

* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/phenomenological-knowledge-store-pks/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.pks_upsert_hint` stores a domain hint in the PKS of one domain. A hint is not a free-text note; it is a set of CSS selectors with a `kind`: `content_filter.ad_container` and `noise_region` mark areas that page reading and call-to-action scoring should down-rank or skip (`effect`), `content_container.result_item` marks repeating result entries that Nova can enumerate (`extract`, `enumerateMax`). A hint with an existing `id` is updated (or reactivated if it was deprecated); without `id` Nova generates one. The domain must be open in a tab or sandbox, otherwise the call is rejected with `reasonCode: "pks.scope_not_open"`. For free-text operator guidance use `nova.domain_note`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | Yes | — | — | Domain scope (e.g. 'youtube.com'). |
| `domainHint` | `object` | Yes | — | — | Domain hint to upsert (matched by id if existing). |
| `domainHint.id` | `string` | No | — | — | Hint ID (stable across updates). Omit to auto-generate. |
| `domainHint.kind` | `string` | Yes | — | `content_filter.ad_container`, `noise_region`, `content_container.result_item` | Hint kind. |
| `domainHint.mode` | `string` | No | `"ancestor"` | `ancestor`, `item_root` | ancestor (el.closest check) \| item_root (enumerate matching elements). |
| `domainHint.selectors` | `array` of `string` | Yes | — | 1–10 items | CSS selectors (1..10, each non-empty string). For ancestor mode: checked via el.closest(). For item_root: enumerated via querySelectorAll(). |
| `domainHint.effect` | `object` | No | — | — | Effect when hint matches (ad_container/noise_region only). |
| `domainHint.extract` | `object` | No | — | — | Extraction config (result_item only). |
| `domainHint.enumerateMax` | `integer` | No | `8` | 1–50 | Max instances to enumerate for result_item hints during Perceive/CTA scanning. Defaults to 8 when omitted. |
| `domainHint.confidence` | `number` | No | `0.5` | 0–1 | Confidence 0.0-1.0 used as a ranking weight for this hint during Perceive/CTA scoring. Defaults to 0.5. |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_pks_upsert_hint",
  "arguments": {
    "scope": "example.com",
    "domainHint": {
      "id": "promo-rail",
      "kind": "noise_region",
      "mode": "ancestor",
      "selectors": ["aside.sponsored", "[data-testid='promo-rail']"]
    }
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "DomainHint 'promo-rail' (noise_region) created for example.com."
    }
  ],
  "structuredContent": {
    "action": "created",
    "scope": "example.com",
    "hintId": "promo-rail",
    "kind": "noise_region",
    "mode": "ancestor",
    "selectorCount": 2,
    "warnings": null
  }
}
```

`action` is `created`, `updated` or `reactivated`. Selectors that look auto-generated (hashed class suffixes) are still stored, but listed in `warnings` with `type: "unstable_selector"`.

---

## 4. Operational Best Practices

* **Stable selectors:** Prefer `data-*` attributes or semantic selectors; hashed class names tend to change on the next deploy.
* **Stable IDs:** Pass the same `id` when refining a hint so it is updated instead of duplicated.

---

## 5. Related Tools

* [`nova.pks_patch`](nova-pks-patch.md)
