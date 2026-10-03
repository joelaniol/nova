# `nova.pks_upsert`

Stores or updates a verified phenomenon, behavioral playbook, and detection fingerprint in the Phenomenological Knowledge Store (PKS).

---

## 1. Overview

`nova.pks_upsert` persists empirical web knowledge so future agents can navigate recurring domain phenomena deterministically. Because PKS is a shared memory system, Nova enforces strict **Empirical Verification**, **Polarity Invariants**, and **Scope Boundaries** to prevent hallucinated or malicious entries from polluting the store.

* **Capability Bundle:** `pks_and_learning`, `domain_knowledge`
* **Mandatory Verification Workflow:** Never guess selectors. The agent must:
  1. Execute the interaction on the live page.
  2. Verify that the interaction succeeded.
  3. Call `nova.pks_upsert` followed by `nova.telemetry_report(outcome="success")`.
* **Open Tab Constraint:** Writes are rejected unless `scope` matches a currently active tab or sandbox host.
* **Shadow-Level Graduation:** New phenomena enter at `LearningLevel: Shadow` and graduate to `Active` after passing empirical health gates.
* **Fallback Selectors:** Actions support up to 5 verified fallback selectors for the same UI intent to withstand minor site updates.

---

## 2. Hard Consent CMP Polarity Invariants

For `consent_cmp` phenomena (cookie banners), Nova enforces four non-negotiable safety rules to prevent accidental or malicious consent hijacking. Violating any invariant immediately returns error `-32602`:

1. **Declared Polarity:** Every mutating action must explicitly declare its polarity: `reject`, `accept`, `manage`, `navigate`, or `noop`.
2. **Exact Selectors Only:** Selectors must be exact (`id`, `class`, or exact attribute matches). Wildcards (`*`, `[class*=]`, `[id*=]`) are strictly rejected because DOM shifts could flip the button's meaning.
3. **Text-Polarity Agreement:** When `targetVisibleText` is provided, it must agree with `declaredPolarity` (e.g. a button reading "Accept All" cannot be declared as `reject`).
4. **Vendor API Agreement:** If a vendor API call is declared (e.g. `__tcfapi`), its method must agree with the declared polarity.

---

## 3. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`scope`** | `string` | **Yes** | ? | Domain scope (e.g. `"spiegel.de"`). Must match an open tab host. |
| **`phenomenon`** | `object` | **Yes** | ? | Phenomenon definition containing `id`, `type`, `fingerprint`, and `playbook`. |
| **`phenomenon.type`**| `string` | **Yes**| ? | Type: `consent_cmp`, `modal`, `paywall`, `login_wall`, `layout_shift`, `native_dialog`, `popover_open`, or `custom`. |
| **`phenomenon.fingerprint`**| `object`| No | `null` | Array of structured detection signals (`dom`, `text`, `layout`, `vendor`, `interaction`). |
| **`phenomenon.playbook`**| `object` | No | `null` | Action sequence (`actions[]`), policy, and postcondition checks (`verify[]`). |
| **`context`** | `object` | No | `null` | Domain environment markers: `{ auth, device, locale, classification }`. |
| **`trust`** | `string` | No | `"unknown"`| Trust level: `"unknown"`, `"low"`, `"medium"`, or `"high"`. |
| **`agentId`** | `string` | No | `"default"`| Agent identity for claim lease verification. |

---

## 4. Example Call: Registering a Verified Reject Playbook

```json
{
  "scope": "example.com",
  "phenomenon": {
    "id": "example-cmp-reject",
    "type": "consent_cmp",
    "fingerprint": {
      "minConfidence": 0.9,
      "signals": [
        { "kind": "dom", "match": "#sp-consent-container" },
        { "kind": "text", "match": "We value your privacy" }
      ]
    },
    "playbook": {
      "policy": "reject_preferred",
      "actions": [
        {
          "type": "click",
          "selector": "button#btn-reject-all",
          "fallbackSelectors": ["button[data-action='reject-all']"],
          "timeoutMs": 2000
        }
      ],
      "verify": [
        {
          "type": "absent",
          "selector": "#sp-consent-container",
          "timeoutMs": 3000
        },
        {
          "type": "scroll_unlocked"
        }
      ]
    }
  }
}
```

---

## 5. Return Value Structure

```json
{
  "success": true,
  "scope": "example.com",
  "phenomenonId": "example-cmp-reject",
  "learningLevel": "Shadow",
  "reactivated": false,
  "storedAtUtc": "2026-10-02T20:10:00Z"
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `Domain scope must match an open tab` | Attempted to register PKS knowledge for a closed or unvisited domain. | Navigate to the target domain first. |
| `-32602: Invariant violation: wildcard selector` | Provided selector uses unanchored wildcards (`[class*=...]`). | Provide exact CSS class, ID, or specific attribute selector. |
| `-32602: Polarity mismatch` | Button text contradicts the declared action polarity. | Align `declaredPolarity` with the visible button text. |

---

## 7. Related Tools & Documentation

* [`nova.telemetry_report`](nova-telemetry-report.md) ? Report interaction outcomes to graduate phenomena.
* [`nova.pks_get`](nova-pks-get.md) ? Retrieve existing domain phenomena.
* [`nova.pks_match`](nova-pks-match.md) ? Match current page signals against stored phenomena.
* [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md) ? Comprehensive guide to PKS levels and lifecycle.
