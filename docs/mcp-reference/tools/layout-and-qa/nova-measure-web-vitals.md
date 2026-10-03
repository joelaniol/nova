# `nova.measure_web_vitals`

Measures live Google Core Web Vitals (LCP, CLS, INP, FCP, TTFB) for the active page, providing categorized ratings (`good`, `needs-improvement`, or `poor`) for automated performance gating.

---

## 1. Overview

Frontend performance regressions directly damage SEO rankings and user retention. `nova.measure_web_vitals` installs in-browser `PerformanceObserver` listeners (backfilled with entries recorded since initial document navigation) to report accurate, standardized Core Web Vitals metrics without external lab proxies.

* **Capability Bundle:** `layout_and_qa`, `quality_inspection`
* **Official Google Thresholds:** Scores metrics as `"good"`, `"needs-improvement"`, or `"poor"`.
* **Settlement Window (`durationMs`):** Allows page fonts, hero images, and layout shifts to settle (recommended `≥ 2000 ms`).
* **Before / After Reset (`reset: true`):** Resets shift accumulators to measure the exact layout impact of an individual interaction.

---

## 2. Core Web Vitals Metrics

| Metric | Full Name | Target ("Good") | Description |
| :--- | :--- | :---: | :--- |
| **LCP** | Largest Contentful Paint | `≤ 2500 ms` | Render time of the largest image or text block visible in the viewport. |
| **CLS** | Cumulative Layout Shift | `≤ 0.10` | Sum of unexpected layout movement vectors during the measurement window. |
| **INP** | Interaction to Next Paint | `≤ 200 ms` | Longest latency between a user interaction (click/key) and the next rendered frame. |
| **FCP** | First Contentful Paint | `≤ 1800 ms` | Timestamp when the browser renders the first piece of DOM content. |
| **TTFB** | Time to First Byte | `≤ 800 ms` | Milliseconds elapsed until the initial server response packet arrives. |

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `durationMs` | `integer` | No | `2000` | 0–10000 | Measurement window in milliseconds: how long to let LCP/CLS settle and interactions register after installing the observers. 0 = collect immediately (may miss late LCP shifts). |
| `reset` | `boolean` | No | `true` | — | If true (default), CLS/INP accumulators are zeroed at the start of this call so it measures fresh — use for independent before/after measurements. false keeps accumulating across calls on the same tab (e.g. cumulative-since-load CLS). LCP is the page-load value and is never reset. |
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
  "url": "https://example.com/shop",
  "rating": "good",
  "metrics": {
    "lcp": {
      "valueMs": 1420.5,
      "rating": "good",
      "elementSelector": "img.hero-banner-image"
    },
    "cls": {
      "value": 0.024,
      "rating": "good",
      "shiftCount": 2
    },
    "inp": {
      "valueMs": 48.0,
      "rating": "good"
    },
    "fcp": {
      "valueMs": 680.2,
      "rating": "good"
    },
    "ttfb": {
      "valueMs": 185.0,
      "rating": "good"
    }
  },
  "lifecycle": {
    "domContentLoadedMs": 850.0,
    "loadMs": 1210.0
  }
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `inp: null` | No mouse click or keyboard interaction occurred during the measurement window. | Perform an interaction (e.g. [`nova.click_selector`](../browser-automation/nova-click-selector.md)) while measuring. |
| `durationMs: 0 reported unstable LCP` | Immediate collection occurred before hero images finished rendering. | Use `durationMs: 2000` or higher to allow full visual settlement. |

---

## 7. Related Tools & Documentation

* [`nova.detect_overflow`](nova-detect-overflow.md) — Identify visual overflow and layout shifts.
* [`nova.measure_elements`](nova-measure-elements.md) — Measure bounding rectangles across multiple elements.
* [`nova.audit_accessibility`](nova-audit-accessibility.md) — Run WCAG accessibility audits.
