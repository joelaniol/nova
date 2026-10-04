# `nova.pks_platform_list`

> **Lists supported platform UI frameworks and common component models.**

* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.pks_platform_list` lists platform-level vendor knowledge (e.g. consent-management-platform templates) previously registered via [`nova.pks_platform_seed`](nova-pks-platform-seed.md). Nova does not ship this store pre-seeded — the list is empty until something seeds it.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_pks_platform_list",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "2 platforms registered."
    }
  ],
  "structuredContent": {
    "count": 2,
    "platforms": [
      {
        "stableId": "onetrust",
        "displayName": "OneTrust",
        "status": "active",
        "migratedToStableId": null,
        "statusReasonJson": null,
        "description": "OneTrust consent-management-platform pattern.",
        "homepageUrl": "https://onetrust.com",
        "lastSeenAtUtc": "2026-10-02T20:10:00Z",
        "lastRevalidatedAtUtc": null,
        "patternCount": 1,
        "totalPatternCount": 1
      },
      {
        "stableId": "didomi",
        "displayName": "Didomi",
        "status": "active",
        "migratedToStableId": null,
        "statusReasonJson": null,
        "description": null,
        "homepageUrl": null,
        "lastSeenAtUtc": "2026-10-02T20:10:00Z",
        "lastRevalidatedAtUtc": null,
        "patternCount": 1,
        "totalPatternCount": 1
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Platform Identification:** Check which vendor templates are already registered before seeding a duplicate via `nova.pks_platform_seed`.

---

## 5. Related Tools

* [`nova.pks_platform_get`](nova-pks-platform-get.md)
* [`nova.pks_platform_seed`](nova-pks-platform-seed.md)
