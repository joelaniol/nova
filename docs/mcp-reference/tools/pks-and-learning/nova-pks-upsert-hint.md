# `nova.pks_upsert_hint`

> **Attaches or updates a human operator guidance hint on a phenomenon pattern.**

* **Security Tier:** Tier 2 (Operator Guidance)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.pks_upsert_hint` binds operator annotations (e.g. "Wait 2 seconds after click for React state settlement") to a phenomenon.

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
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_pks_upsert_hint",
  "arguments": {
    "phenomenonId": "phenom-cart-flow-01",
    "hint": "Requires 500ms settlement after selecting shipping address."
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Attached guidance hint to phenom-cart-flow-01."
    }
  ],
  "structuredContent": {
    "ok": true,
    "phenomenonId": "phenom-cart-flow-01",
    "hintsCount": 1
  }
}
```

---

## 4. Operational Best Practices

* **Human Knowledge Injection:** Record non-obvious site quirks for future agent runs.

---

## 5. Related Tools

* [`nova.pks_patch`](nova-pks-patch.md)
