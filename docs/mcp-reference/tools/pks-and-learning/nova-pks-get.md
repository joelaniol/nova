# `nova.pks_get`

Retrieves domain-scoped Phenomenological Knowledge Store (PKS) entries, playbooks, interaction fingerprints, and contextual environment markers.

---

## 1. Overview

The **Phenomenological Knowledge Store (PKS)** is Nova's shared, self-learning domain memory. Instead of forcing autonomous agents to rediscover cookie consent banners, modal dialogs, paywalls, or multi-step checkout flows repeatedly from scratch, PKS preserves proven behavioral playbooks and detection fingerprints per domain.

`nova.pks_get` fetches registered phenomena for a domain scope. It supports lightweight existence checks (`outputDetail: "summary"`) or full extraction (`outputDetail: "full"`), with optional filtering by individual phenomenon ID.

* **Two Detail Levels:** `"summary"` returns compact IDs, types, and health stats (~90% token reduction); `"full"` returns playbooks, action sequences, and fingerprint signals.
* **Context Compatibility Checks:** Compares the active agent context (device, locale, auth state) against the stored domain context, reporting mismatches transparently.
* **Single Phenomenon Querying (`phenomenonId`):** Retrieve only the needed phenomenon without downloading the entire domain scope.

---

## 2. Key Capabilities & Features

### A. Summary vs Full Inspection
* **`outputDetail: "summary"`**: Useful when an agent enters a domain and wants to know: *"Are there any known cookie banners or login walls on this site?"* Only phenomena at `Active` level are listed by name (Shadow/Candidate phenomena are counted but not itemized); each listed entry reports its type, whether it has ever run (`verified`), its 30-day success rate, and total attempts.
* **`outputDetail: "full"`**: Delivers concrete execution steps (`playbook.actions`), post-action assertions (`playbook.verify`), and fallback selectors.

### B. Context Applicability Reporting
Websites frequently behave differently across devices or authentication states (e.g. desktop vs mobile, or logged-in vs anonymous). When calling `nova.pks_get`, passing `context` checks whether the stored phenomenon applies:
```json
{
  "scope": "github.com",
  "context": {
    "auth": "logged_in",
    "device": "desktop",
    "locale": "en-US"
  }
}
```
The response indicates `contextMatch: true` or details specific divergences.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | Yes | — | — | Domain scope (e.g. 'spiegel.de'). |
| `phenomenonId` | `string` | No | — | — | Optional: filter to a single phenomenon by ID (e.g. 'model-selector'). Case-insensitive match. Returns only that phenomenon instead of the full domain payload. If not found, returns phenomenonFound=false with availableIds. If deprecated, returns deprecated=true with deprecatedReason. |
| `outputDetail` | `string` | No | — | `full`, `summary` | Response detail level. 'summary' returns only IDs, types, and health stats (much smaller payload). 'full' returns complete phenomena with playbooks and fingerprints. Default: 'full'. |
| `context` | `object` | No | — | — | Optional context for applicability diagnostics against stored domain context keys. |
| `context.device` | `any` | No | — | — | Device type for context-specific filtering. Use null or omit to leave the device filter unset. |
| `context.locale` | `string or null` | No | — | ≥ 1 characters | Optional locale filter such as 'de-DE'. Use null or omit to leave the locale filter unset. |
| `context.auth` | `any` | No | — | — | Authentication state. 'anonymous' = not signed in, 'logged_in' = signed in, 'unknown' = not enough evidence to classify. Use null or omit to leave the auth filter unset. |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Lightweight Summary Check for Domain
```json
{
  "scope": "spiegel.de",
  "outputDetail": "summary"
}
```

### Retrieve Full Playbook for Cookie Consent Banner
```json
{
  "scope": "spiegel.de",
  "phenomenonId": "spiegel-cmp-reject",
  "outputDetail": "full"
}
```

---

## 5. Return Value Structure (Summary Mode)

```json
{
  "found": true,
  "scope": "spiegel.de",
  "trust": "high",
  "updatedAtUtc": "2026-10-02T20:10:00Z",
  "contextMatch": null,
  "mismatches": [],
  "phenomenonCount": 2,
  "activePhenomenonCount": 2,
  "totalPhenomenaCount": 2,
  "deprecatedCount": 0,
  "domainHintCount": 0,
  "phenomena": [
    {
      "id": "spiegel-cmp-reject",
      "type": "consent_cmp",
      "verified": true,
      "successRate30d": 0.993,
      "totalAttempts": 420
    },
    {
      "id": "spiegel-paywall-gate",
      "type": "paywall",
      "verified": true,
      "successRate30d": 0.977,
      "totalAttempts": 85
    }
  ]
}
```

`phenomenonCount`/`activePhenomenonCount` only count phenomena at `Active` level; `totalPhenomenaCount` includes Shadow and Candidate entries too. `contextMatch`/`mismatches` are only populated when a `context` filter was passed in the request.

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `phenomenonFound: false` | Specified `phenomenonId` does not exist for the domain. | Check `availableIds` in the response or call with `outputDetail: "summary"`. |
| `deprecated: true` | Phenomenon was deprecated due to repeated execution failures. | Inspect `deprecatedReason`. Verify current DOM and reactivate via [`nova.pks_upsert`](nova-pks-upsert.md). |

---

## 7. Related Tools & Documentation

* [`nova.pks_upsert`](nova-pks-upsert.md) — Store or update verified phenomena in PKS.
* [`nova.pks_match`](nova-pks-match.md) — Match live DOM observations against known fingerprints.
* [`nova.telemetry_report`](nova-telemetry-report.md) — Report execution outcome for health scoring.
* [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md) — Architecture, lifecycle levels, and invariant rules.
