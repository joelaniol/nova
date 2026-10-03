# `nova.pks_get`

Retrieves domain-scoped Phenomenological Knowledge Store (PKS) entries, playbooks, interaction fingerprints, and contextual environment markers.

---

## 1. Overview

The **Phenomenological Knowledge Store (PKS)** is Nova's shared, self-learning domain memory. Instead of forcing autonomous agents to rediscover cookie consent banners, modal dialogs, paywalls, or multi-step checkout flows repeatedly from scratch, PKS preserves proven behavioral playbooks and detection fingerprints per domain.

`nova.pks_get` fetches registered phenomena for a domain scope. It supports lightweight existence checks (`outputDetail: "summary"`) or full extraction (`outputDetail: "full"`), with optional filtering by individual phenomenon ID.

* **Capability Bundle:** `pks_and_learning`, `domain_knowledge`
* **Two Detail Levels:** `"summary"` returns compact IDs, types, and health stats (~90% token reduction); `"full"` returns playbooks, action sequences, and fingerprint signals.
* **Context Compatibility Checks:** Compares the active agent context (device, locale, auth state) against the stored domain context, reporting mismatches transparently.
* **Single Phenomenon Querying (`phenomenonId`):** Retrieve only the needed phenomenon without downloading the entire domain scope.

---

## 2. Key Capabilities & Features

### A. Summary vs Full Inspection
* **`outputDetail: "summary"`**: Useful when an agent enters a domain and wants to know: *"Are there any known cookie banners or login walls on this site?"*
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

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`scope`** | `string` | **Yes** | ? | Domain scope (e.g. `"spiegel.de"`, `"github.com"`). |
| **`outputDetail`** | `string` | No | `"full"` | Detail level: `"summary"` (compact IDs/health) or `"full"` (complete playbooks). |
| **`phenomenonId`** | `string` | No | `null` | Filter to a single phenomenon ID (e.g. `"consent-banner"`). Case-insensitive. |
| **`context`** | `object` | No | `null` | Environment context: `{ auth?: string, device?: string, locale?: string }`. |

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
  "scope": "spiegel.de",
  "trust": "high",
  "phenomenaCount": 2,
  "phenomena": [
    {
      "id": "spiegel-cmp-reject",
      "type": "consent_cmp",
      "learningLevel": "Active",
      "healthScore": 0.98,
      "successCount": 420,
      "failureCount": 3
    },
    {
      "id": "spiegel-paywall-gate",
      "type": "paywall",
      "learningLevel": "Active",
      "healthScore": 0.95,
      "successCount": 85,
      "failureCount": 2
    }
  ]
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `phenomenonFound: false` | Specified `phenomenonId` does not exist for the domain. | Check `availableIds` in the response or call with `outputDetail: "summary"`. |
| `deprecated: true` | Phenomenon was deprecated due to repeated execution failures. | Inspect `deprecatedReason`. Verify current DOM and reactivate via [`nova.pks_upsert`](nova-pks-upsert.md). |

---

## 7. Related Tools & Documentation

* [`nova.pks_upsert`](nova-pks-upsert.md) ? Store or update verified phenomena in PKS.
* [`nova.pks_match`](nova-pks-match.md) ? Match live DOM observations against known fingerprints.
* [`nova.telemetry_report`](nova-telemetry-report.md) ? Report execution outcome for health scoring.
* [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md) ? Architecture, lifecycle levels, and invariant rules.
