# `nova.audit_accessibility`

Runs an automated Accessibility (a11y) and UX compliance audit over the DOM, checking for WCAG color contrast failures, undersized tap targets, and missing accessible labels.

---

## 1. Overview

`nova.audit_accessibility` provides built-in accessibility analysis without requiring third-party libraries (such as axe-core). It inspects the live rendered DOM for the most frequent usability violations: unreadable text contrast, tap targets too small for mobile fingertips, unlabelled form inputs, and icon-only buttons missing ARIA names.

* **Three Core Check Families:** WCAG Text Contrast, Tap Target Size, and Accessible Labels/Alt-Text.
* **Component-Level Scoping (`selector`):** Audit an individual design component, modal, or form subtree.
* **Dark Mode Compatible:** Runs against whatever is currently rendered, so pair it with [`nova.emulation_set_media`](../device-emulation/nova-emulation-set-media.md) to audit dark/light themes or `prefers-reduced-motion`.

---

## 2. Check Families & Rules

### A. WCAG Color Contrast (`includeContrast: true`)
Calculates the relative luminance ratio between computed text color and the nearest opaque ancestor background:
* **Normal Text:** Flags contrast ratios `< 4.5:1` (WCAG 2.2 Level AA).
* **Large Text** (≥18pt or ≥14pt bold): Flags contrast ratios `< 3.0:1`.

### B. Interactive Target Size (`includeTargetSize: true`)
Checks the physical rendered dimensions (`width` and `height`) of interactive nodes: `<a href>`, `<button>`, `<select>`, `<textarea>`, non-hidden `<input>` elements, and anything with `role="button"`, `"link"`, `"checkbox"`, `"radio"`, `"switch"`, `"tab"`, or `"menuitem"`:
* **Default Threshold (`minTargetSize: 24`):** Enforces WCAG 2.2 SC 2.5.8 (Target Size Minimum, Level AA).
* **Mobile / AAA Guidance (`minTargetSize: 44`):** Can be raised to 44px to audit touch-screen and mobile viewport compliance.

### C. Accessible Names & Labels (`includeLabels: true`)
Identifies elements missing programmatic names for screen readers:
* `<img>` tags missing the `alt` attribute.
* Form controls (`<input>`, `<select>`, `<textarea>`) lacking an associated `<label>`, `aria-label`, or `aria-labelledby`.
* Empty buttons or icon-only links containing SVG/icons without accessible text.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | No | `"body"` | — | CSS selector for the root element to audit. Defaults to 'body' (whole page). Scope to a component to audit just that subtree. |
| `maxIssues` | `integer` | No | `200` | 1–2000 | Maximum number of issues to return; the scan stops early and sets truncated=true when reached. |
| `minTargetSize` | `integer` | No | `24` | 1–200 | Minimum acceptable tap-target size in CSS pixels (smallest of width/height). Default 24 = WCAG 2.2 SC 2.5.8 Level AA; raise to 44 for the AAA / common mobile guidance. |
| `includeContrast` | `boolean` | No | `true` | — | Include WCAG text-contrast checks. |
| `includeTargetSize` | `boolean` | No | `true` | — | Include tap-target-size checks for interactive elements. |
| `includeLabels` | `boolean` | No | `true` | — | Include missing alt-text / form-label / accessible-name checks. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Full Page Accessibility Audit
```json
{
  "minTargetSize": 24
}
```

### Mobile Target Size Audit on Checkout Form
```json
{
  "selector": "form#payment-form",
  "minTargetSize": 44,
  "includeContrast": true,
  "includeLabels": true
}
```

### Contrast-Only Check on Navigation Bar
```json
{
  "selector": "header.site-header",
  "includeContrast": true,
  "includeTargetSize": false,
  "includeLabels": false
}
```

---

## 5. Return Value Structure

`structuredContent` wraps the in-page probe's own result under `result`; `issueCount`, `truncated`, and `selector` are lifted to the top level for convenience. Each issue's `type` is one of `contrast`, `target-size`, `missing-alt`, `missing-label`, or `empty-control`, and `details` varies by type:

```json
{
  "targetId": "tab-101",
  "ok": true,
  "selector": "form#payment-form",
  "minTargetSize": 24,
  "issueCount": 2,
  "truncated": false,
  "result": {
    "ok": true,
    "selectorMatched": true,
    "url": "https://example.com/checkout",
    "scanned": 184,
    "summary": { "contrast": 1, "targetSize": 1, "labels": 0, "total": 2 },
    "issues": [
      {
        "type": "contrast",
        "selector": "p.terms-disclaimer",
        "tag": "p",
        "text": "By continuing you agree to the terms.",
        "details": {
          "ratio": 2.8,
          "threshold": 4.5,
          "fontSizePx": 13,
          "largeText": false,
          "color": "rgb(170, 170, 170)",
          "background": "rgb(255, 255, 255)"
        }
      },
      {
        "type": "target-size",
        "selector": "button.close-icon-btn",
        "tag": "button",
        "text": "",
        "details": { "width": 18, "height": 18, "min": 24 }
      }
    ],
    "truncated": false
  }
}
```

Each scan examines at most 8000 elements (`scanned` reports how many were actually visible and checked); a larger subtree sets `truncated: true` without a separate warning field.

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `-32004: No element matched selector '...'` | Provided root `selector` does not exist in the DOM. | Check selector spelling or verify the component has rendered. |
| `-32602: at least one of includeContrast, includeTargetSize, includeLabels must be enabled` | All three check families were disabled at once. | Enable at least one family. |
| `-32002: Accessibility audit probe failed: ...` | The in-page probe threw (e.g. a selector querySelector cannot parse). | Check the selector syntax and retry. |
| Contrast is advisory only | Alpha-blended text/backgrounds and background images are not modelled; the probe assumes white when no opaque ancestor background is found. | Treat contrast findings as a lead, not a verdict; verify visually when alpha-blending is involved. |

---

## 7. Related Tools & Documentation

* [`nova.detect_overflow`](nova-detect-overflow.md) — Identify visual clipping and container spillages.
* [`nova.get_computed_style`](nova-get-computed-style.md) — Read exact color and font size values.
* [`nova.measure_elements`](nova-measure-elements.md) — Measure bounding boxes and layout constraints.
