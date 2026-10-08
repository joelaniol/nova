# `nova.pks_platform_get`

> **Reads one stored platform entry with its pattern templates and aliases.**

* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/learning/phenomenological-knowledge-store-pks/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.pks_platform_get` returns a platform stored in the PKS (for example a cookie-consent vendor added with `nova.pks_platform_seed`): its metadata, status (`active`, `deprecated` or `merged`), pattern templates and lookup aliases. Platforms only exist once they have been seeded; an unknown ID returns `found: false`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `stableId` | `string` | Yes | — | ≥ 1 characters | Non-empty platform stable ID. The runtime trims and lowercases it before lookup. |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_pks_platform_get",
  "arguments": {
    "stableId": "cookiebot"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Platform 'cookiebot': Cookiebot, 0 active patterns (0 total), 1 aliases."
    }
  ],
  "structuredContent": {
    "found": true,
    "platform": {
      "stableId": "cookiebot",
      "displayName": "Cookiebot",
      "description": null,
      "homepageUrl": "https://www.cookiebot.com/",
      "status": "active",
      "migratedToStableId": null,
      "statusReasonJson": "{}",
      "lastSeenAtUtc": null,
      "lastReachableAtUtc": null,
      "lastRevalidatedAtUtc": null,
      "scoreComputedAtUtc": null,
      "patternCount": 0,
      "totalPatternCount": 0,
      "aliasCount": 1,
      "patterns": [],
      "aliases": [
        { "kind": "script_domain", "value": "consent.cookiebot.com", "confidence": 1.0 }
      ]
    }
  }
}
```

Not found: `{ "found": false, "stableId": "..." }` with the text "Platform '<id>' not found.". Each entry in `patterns` carries `stableId`, `type`, `fingerprint`, `playbook`, `applicability`, `health`, `deprecated` and `priority`.

---

## 4. Operational Best Practices

* **Reuse across sites:** A platform pattern applies to every site that embeds the vendor, so check the platform entry before writing the same consent or modal handling per domain.

---

## 5. Related Tools

* [`nova.pks_platform_list`](nova-pks-platform-list.md)
* [`nova.pks_platform_seed`](nova-pks-platform-seed.md)
