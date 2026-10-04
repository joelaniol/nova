# `nova.measure_web_vitals`

Measures Core Web Vitals (LCP, a simplified CLS, INP, FCP, plus TTFB and load timings) for the active page, rating LCP/CLS/INP/FCP as `good`, `needs-improvement`, or `poor` for automated performance gating.

---

## 1. Overview

Frontend performance regressions directly damage SEO rankings and user retention. `nova.measure_web_vitals` installs in-browser `PerformanceObserver` listeners (backfilled with entries recorded since initial document navigation) to report accurate, standardized Core Web Vitals metrics without external lab proxies.

* **Google's Published Thresholds:** LCP/CLS/INP/FCP are each scored `"good"`, `"needs-improvement"`, or `"poor"` against Google's published Core Web Vitals cut-offs.
* **Settlement Window (`durationMs`):** Allows page fonts, hero images, and layout shifts to settle (recommended `≥ 2000 ms`).
* **Before / After Reset (`reset: true`):** Resets shift/interaction accumulators to measure the exact layout impact of an individual interaction. LCP is the page-load value and is never reset.
* **Simplified CLS:** CLS here is the sum of layout-shift values that had no recent user input — the simple approximation, not Google's windowed/session CLS algorithm. The `good`/`poor` thresholds (0.1 / 0.25) are Google's, but the running total they are applied to is simpler than the official metric.

---

## 2. Core Web Vitals Metrics

| Metric | Full Name | `good` threshold | `poor` threshold (above = poor) | Description |
| :--- | :--- | :---: | :---: | :--- |
| **LCP** | Largest Contentful Paint | `≤ 2500 ms` | `> 4000 ms` | Render time of the largest image or text block visible in the viewport. |
| **CLS** | Cumulative Layout Shift (simplified, see above) | `≤ 0.10` | `> 0.25` | Sum of non-input layout-shift values during the measurement window. |
| **INP** | Interaction to Next Paint (max observed, not p98) | `≤ 200 ms` | `> 500 ms` | Longest single event duration observed during the window; `null` if no interaction happened. |
| **FCP** | First Contentful Paint | `≤ 1800 ms` | `> 3000 ms` | Timestamp of the first `first-contentful-paint` paint entry. |
| **TTFB** | Time to First Byte | — | — | `navigation.responseStart` in milliseconds. Reported but **not rated** — there is no `good`/`poor` value for it in the response. |

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `durationMs` | `integer` | No | `2000` | 0–10000 | Measurement window in milliseconds: how long to let LCP/CLS settle and interactions register after installing the observers. 0 = collect immediately (may miss late LCP shifts). |
| `reset` | `boolean` | No | `true` | — | If true (default), CLS/INP accumulators are zeroed at the start of this call so it measures fresh — use for independent before/after measurements. false keeps accumulating across calls on the same tab (e.g. cumulative-since-load CLS). LCP is the page-load value and is never reset. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Standard Post-Navigation Performance Audit
```json
{
  "durationMs": 3000
}
```

### Measure Layout Shift of an Expandable Accordion Interaction
```json
{
  "durationMs": 1500,
  "reset": true
}
```

---

## 5. Return Value Structure

```json
{
  "targetId": "tab-101",
  "ok": true,
  "durationMs": 3000,
  "reset": true,
  "result": {
    "ok": true,
    "url": "https://example.com/shop",
    "observed": true,
    "metrics": {
      "lcpMs": 1420.5,
      "cls": 0.024,
      "inpMs": 48.0,
      "fcpMs": 680.2,
      "ttfbMs": 185.0,
      "domContentLoadedMs": 850.0,
      "loadMs": 1210.0
    },
    "ratings": {
      "lcp": "good",
      "cls": "good",
      "inp": "good",
      "fcp": "good"
    },
    "sampleCounts": { "layoutShifts": 2, "lcpCandidates": 1 },
    "note": null
  }
}
```

There is no overall/aggregate `rating` — read the per-metric values under `ratings`. `note` is non-null (explaining that INP needs an interaction) whenever `metrics.inpMs` is `null`.

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `metrics.inpMs: null`, `note` explains it | No interaction event (above the 16ms duration threshold) occurred during the measurement window. | Perform an interaction (e.g. [`nova.click_selector`](../browser-automation/nova-click-selector.md)) while measuring. |
| `-32002: PerformanceObserver is not available in this page` | The page's JS context does not support `PerformanceObserver` (rare). | Nothing to retry — vitals cannot be measured on this page. |
| `-32002: Web-vitals observer install/collect failed: ...` | The in-page probe threw. | Retry; if persistent, the page may block `performance.*` APIs. |

---

## 7. Related Tools & Documentation

* [`nova.detect_overflow`](nova-detect-overflow.md) — Identify visual overflow and layout shifts.
* [`nova.measure_elements`](nova-measure-elements.md) — Measure bounding rectangles across multiple elements.
* [`nova.audit_accessibility`](nova-audit-accessibility.md) — Run WCAG accessibility audits.
