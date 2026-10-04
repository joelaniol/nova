# `nova.revalidate`

> **Checks stale PKS phenomena of a domain against the live page in a tab and records the outcome.**

* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.revalidate` picks up to `limit` phenomena of the domain that are due for a check (stale or recently failing) and tests their fingerprint selectors on the page currently loaded in `targetId`, without clicking anything. Each result gets a verdict (`healthy`, `drift`, `gone`, `error` or `unknown`); healthy and drift results are written back as telemetry, so a phenomenon that keeps drifting can be demoted or deprecated. When the learned selectors no longer match but an element with the same text anchor is found, the result carries a `repairCandidate` and an entry in `pksAdviceItems`; it is never applied automatically. Without `scope`, the domain of the tab's current URL is used. Checks are rate-limited by a revalidation budget (`budgetRemaining`, `reasonCode: "revalidate.budget_exhausted"`).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | No | — | — | Domain scope to revalidate (e.g. 'example.com'). If omitted, revalidation is scoped to the current target host. |
| `limit` | `integer` | No | — | 1–5 | Max phenomena to check (default 3, max 5). |
| `targetId` | `string` | Yes | — | — | Tab/sandbox to run DOM checks in. |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_revalidate",
  "arguments": {
    "targetId": "tab-1",
    "scope": "example.com",
    "limit": 3
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Revalidated 1 phenomena for 'example.com':\n  cookie-banner-accept: healthy (2/2 selectors)\nBudget remaining: 17 global"
    }
  ],
  "structuredContent": {
    "ok": true,
    "reasonCode": null,
    "scope": "example.com",
    "targetScope": "example.com",
    "scopeDerivedFromTarget": false,
    "checked": 1,
    "results": [
      {
        "scope": "example.com",
        "stableId": "cookie-banner-accept",
        "verdict": "healthy",
        "selectorExists": true,
        "fingerprintMatchRatio": 1.0,
        "signalsChecked": 2,
        "signalsMatched": 2,
        "error": null,
        "repairCandidate": null,
        "telemetryScope": "example.com",
        "telemetryOutcome": "silent_verify_ok",
        "telemetryRecorded": true,
        "telemetrySkippedReason": null,
        "telemetryError": null
      }
    ],
    "pksAdviceItems": [],
    "telemetryRecorded": 1,
    "telemetryFailed": 0,
    "budgetRemaining": 17,
    "denied": []
  }
}
```

If nothing is due, the result is `checked: 0` with the text "No stale phenomena found for '<scope>'.".

---

## 4. Operational Best Practices

* **Open the right page first:** The check runs on what `targetId` currently shows; navigate to the page where the phenomenon appears before calling.
* **Verify repair candidates:** A `repairCandidate` is derived from the page and can be planted by a hostile site; confirm it before updating the phenomenon with `nova.pks_patch`.

---

## 5. Related Tools

* [`nova.phenomenon_apply`](nova-phenomenon-apply.md)
* [`nova.pks_get`](nova-pks-get.md)
