# `nova.pks_upsert`

Stores or updates a verified phenomenon, behavioral playbook, and detection fingerprint in the Phenomenological Knowledge Store (PKS).

---

## 1. Overview

`nova.pks_upsert` persists empirical web knowledge so future agents can navigate recurring domain phenomena deterministically. Because PKS is a shared memory system, Nova enforces strict **Empirical Verification**, **Polarity Invariants**, and **Scope Boundaries** to prevent hallucinated or malicious entries from polluting the store.

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

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | Yes | — | — | Domain scope (e.g. 'spiegel.de'). |
| `context` | `object` | No | — | — | Optional: set/update domain-level context keys describing the current browsing environment. |
| `context.device` | `string` | No | — | `desktop`, `mobile`, `tablet` | Device type for this browsing environment. |
| `context.locale` | `string` | No | — | — | e.g. 'de-DE' |
| `context.auth` | `string` | No | — | `anonymous`, `logged_in`, `unknown` | Authentication state. 'anonymous' = not signed in, 'logged_in' = signed in, 'unknown' = not enough evidence to classify. |
| `context.domainCapabilities` | `object` | No | — | — | Optional: set domain capabilities (login surface, feature inventories). Used to describe which features exist before and after login. |
| `context.trustedStateDetectors` | `object` | No | — | — | Optional trusted state detector configs. Each property name is a detector/state key such as logged_in or sidebar_open. |
| `context.classification` | `object` | No | — | — | Domain-level service classification. Tags are merged by kind+value instead of replacing the full set. |
| `trust` | `string` | No | — | `unknown`, `low`, `medium`, `high` | Optional domain trust level. Trust level. 'unknown' = not reviewed yet, 'low' = weak or unstable evidence, 'medium' = usable but still needs confirmation, 'high' = repeatedly verified and reliable. |
| `phenomenon` | `object` | Yes | — | — | Phenomenon to upsert (matched by id if existing). |
| `phenomenon.id` | `string` | No | — | — | Phenomenon ID. Omit to auto-generate. |
| `phenomenon.type` | `string` | No | — | `consent_cmp`, `modal`, `paywall`, `login_wall`, `layout_shift`, `native_dialog`, `popover_open`, `custom` | Phenomenon type. 'consent_cmp' = cookie/consent manager surface, 'modal' = generic blocking overlay or dialog, 'paywall' = subscription/payment gate, 'login_wall' = sign-in gate, 'layout_shift' = disruptive UI shift without a classic overlay, 'native_dialog' = browser/native prompt such as permission or file picker, 'popover_open' = anchored popover/dropdown surface, 'custom' = uncategorized site-specific phenomenon. |
| `phenomenon.fingerprint` | `object` | No | — | — | Fingerprint signals used to detect the phenomenon later. |
| `phenomenon.playbook` | `object` | No | — | — | Structured response plan for the phenomenon, including execution and verification. |
| `phenomenon.context` | `object` | No | — | — | Optional phenomenon-level context override. Missing keys fallback to domain context keys. When updating an existing phenomenon, the deprecated flag is automatically cleared (reactivated). |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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

`action` is `"created"` for a brand-new phenomenon, `"updated"` for an existing non-deprecated one, or `"reactivated"` when the existing entry was deprecated (upserting always clears the deprecated flag). New phenomena always start at `LearningLevel: Shadow` — check `nova.pks_get` or `nova.explain` to see the resulting level/gates, the response itself does not return a learning level.

```json
{
  "action": "created",
  "scope": "example.com",
  "phenomenonId": "example-cmp-reject"
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `reasonCode: "pks.scope_not_open"` (ok: false, no `-326xx` code; the tool returns normally) | Attempted to register PKS knowledge for a domain not currently open in any tab or sandbox. | Navigate to the target domain first, then retry. |
| `-32602: Invariant violation: wildcard selector` | Provided selector uses unanchored wildcards (`[class*=...]`). | Provide exact CSS class, ID, or specific attribute selector. |
| `-32602: Polarity mismatch` | Button text contradicts the declared action polarity. | Align `declaredPolarity` with the visible button text. |
| `-32602: domain already has 200 phenomena` | Domain hit the per-domain phenomenon cap on a new (non-matching) `phenomenon.id`. | Deprecate unused phenomena via `nova.pks_deprecate` before adding new ones. |

---

## 7. Related Tools & Documentation

* [`nova.telemetry_report`](nova-telemetry-report.md) — Report interaction outcomes to graduate phenomena.
* [`nova.pks_get`](nova-pks-get.md) — Retrieve existing domain phenomena.
* [`nova.pks_match`](nova-pks-match.md) — Match current page signals against stored phenomena.
* [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md) — Comprehensive guide to PKS levels and lifecycle.
