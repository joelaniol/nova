# `nova.audit_accessibility`

Runs an automated Accessibility (a11y) and UX compliance audit over the DOM, checking for WCAG color contrast failures, undersized tap targets, and missing accessible labels.

---

## 1. Overview

`nova.audit_accessibility` provides built-in accessibility analysis without requiring third-party libraries (such as axe-core). It inspects the live rendered DOM for the most frequent usability violations: unreadable text contrast, tap targets too small for mobile fingertips, unlabelled form inputs, and icon-only buttons missing ARIA names.

* **Capability Bundle:** `layout_and_qa`, `quality_inspection`
* **Three Core Check Families:** WCAG Text Contrast, Tap Target Size, and Accessible Labels/Alt-Text.
* **Component-Level Scoping (`selector`):** Audit an individual design component, modal, or form subtree.
* **Dark Mode Compatible:** Works seamlessly with [`nova.emulation_set_media`](../browser-automation/nova-navigate.md) to audit both light and dark themes.

---

## 2. Check Families & Rules

### A. WCAG Color Contrast (`includeContrast: true`)
Calculates the relative luminance ratio between computed text color and the nearest opaque ancestor background:
* **Normal Text:** Flags contrast ratios `< 4.5:1` (WCAG 2.2 Level AA).
* **Large Text** (≥18pt or ≥14pt bold): Flags contrast ratios `< 3.0:1`.

### B. Interactive Target Size (`includeTargetSize: true`)
Checks the physical rendered dimensions (`width` and `height`) of all interactive nodes (`<button>`, `<a>`, `<input>`, `<select>`, and elements with `role="button"`):
* **Default Threshold (`minTargetSize: 24`):** Enforces WCAG 2.2 SC 2.5.8 (Target Size Minimum, Level AA).
* **Mobile / AAA Guidance (`minTargetSize: 44`):** Can be raised to 44px to audit touch-screen and mobile viewport compliance.

### C. Accessible Names & Labels (`includeLabels: true`)
Identifies elements missing programmatic names for screen readers:
* `<img>` tags missing the `alt` attribute.
* Form controls (`<input>`, `<select>`, `<textarea>`) lacking an associated `<label>`, `aria-label`, or `aria-labelledby`.
* Empty buttons or icon-only links containing SVG/icons without accessible text.

---

## 3. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`selector`** | `string` | No | `"body"` | Root element to audit. Defaults to `"body"`. Scope to a component to audit just that subtree. |
| **`minTargetSize`** | `integer` | No | `24` | Minimum acceptable tap-target size in CSS pixels (1–200). Default `24` (AA); use `44` for AAA/mobile. |
| **`includeContrast`** | `boolean` | No | `true` | Include WCAG text-contrast checks. |
| **`includeTargetSize`**| `boolean` | No | `true` | Include tap-target-size checks. |
| **`includeLabels`** | `boolean` | No | `true` | Include missing alt-text and accessible name checks. |
| **`maxIssues`** | `integer` | No | `200` | Maximum issues to return (1–2,000). Excess sets `truncated: true`. |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs`, or `"active"`. |
| **`agentId`** | `string` | No | `"default"` | Agent identity for claim lease verification. |

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

```json
{
  "targetId": "tab-101",
  "scannedRoot": "form#payment-form",
  "totalIssues": 3,
  "truncated": false,
  "issues": [
    {
      "category": "contrast",
      "severity": "serious",
      "selector": "p.terms-disclaimer",
      "ratio": 2.8,
      "requiredRatio": 4.5,
      "textColor": "rgb(170, 170, 170)",
      "backgroundColor": "rgb(255, 255, 255)",
      "message": "Text contrast ratio of 2.8:1 fails WCAG AA standard of 4.5:1."
    },
    {
      "category": "target_size",
      "severity": "moderate",
      "selector": "button.close-icon-btn",
      "size": { "width": 18, "height": 18 },
      "minRequired": 24,
      "message": "Target dimensions (18x18px) are below minimum 24px requirement."
    },
    {
      "category": "labels",
      "severity": "critical",
      "selector": "input#promo-code",
      "message": "Input element lacks an accessible label or aria-label."
    }
  ]
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `Selector matched nothing: ...` | Provided root `selector` does not exist in the DOM. | Check selector spelling. |
| `Contrast advisory note` | Alpha-blended or background image elements cannot be statically evaluated for contrast. | Inspect manually or use [`nova.perceive`](../dom-and-reading/nova-perceive.md) with visual screenshots. |

---

## 7. Related Tools & Documentation

* [`nova.detect_overflow`](nova-detect-overflow.md) — Identify visual clipping and container spillages.
* [`nova.get_computed_style`](nova-get-computed-style.md) — Read exact color and font size values.
* [`nova.measure_elements`](nova-measure-elements.md) — Measure bounding boxes and layout constraints.
