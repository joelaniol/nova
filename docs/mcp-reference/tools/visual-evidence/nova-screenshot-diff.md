# `nova.screenshot_diff`

Performs pixel-by-pixel visual comparison between two screenshot images or resource URIs, returning changed pixel percentages, cluster bounding boxes, and visual diff overlays.

---

## 1. Overview

`nova.screenshot_diff` provides deterministic visual regression analysis. When verifying frontend changes, CSS refactors, or theme switches, manual inspection is slow and prone to oversight. This tool calculates Euclidean RGB distances across all pixels, groups mutations into connected clusters using 8-connectivity component labeling, and generates a visual diff overlay image.

* **Capability Bundle:** `visual_evidence`, `quality_inspection`
* **Resource URI & Disk Support:** Accepts local file paths or `nova://screenshot/...` URIs returned by [`nova.capture_screenshot`](nova-capture-screenshot.md).
* **Anti-Flake Controls:** Built-in anti-aliasing edge suppression (`ignoreAntialiasing`) and exclusion masks (`mask`) for dynamic content like timestamps or avatars.
* **Diff Overlay Artifact:** Generates an annotated PNG highlighting changed pixels in bright magenta.

---

## 2. Anti-Flake Regression Controls

Visual regression tests often suffer from false alarms caused by sub-pixel font rendering, dynamic clocks, or animated carousels. Nova includes three robust stabilization mechanisms:

### A. Anti-Aliasing Filter (`ignoreAntialiasing: true`)
Uses pixelmatch heuristics to detect edge pixels whose color change is merely sub-pixel font smoothing or border anti-aliasing, filtering out false positives across different GPU configurations.

### B. Exclusion Masks (`mask`)
Exclude dynamic UI zones (such as live clocks, user profile pictures, or rotating advertising banners) by supplying an array of exclusion bounding boxes:
```json
{
  "mask": [
    { "x": 1200, "y": 10, "width": 240, "height": 40 },
    { "x": 0, "y": 850, "width": 300, "height": 50 }
  ]
}
```

### C. Tolerance Thresholds (`maxDiffRatio`, `threshold`)
* `threshold`: Sensitivity of color detection (default `30`, lower values are stricter).
* `maxDiffRatio`: Tolerance percentage (e.g. `0.05` allows up to 0.05% pixel change before marking the check as failed).
* `minRegionSize`: Ignores isolated single-pixel speckles by requiring clusters to have at least `N` connected pixels (default `100`).

---

## 3. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`beforePath`** | `string` | **Yes** | — | Path to baseline PNG or `nova://screenshot/...` URI. |
| **`afterPath`** | `string` | **Yes** | — | Path to comparison PNG or `nova://screenshot/...` URI. |
| **`threshold`** | `integer` | No | `30` | Per-pixel Euclidean RGB distance threshold (0–255). |
| **`ignoreAntialiasing`**| `boolean` | No | `false`| Skip sub-pixel font and border anti-aliasing edges. |
| **`mask`** | `array<object>`| No | `null` | Array of `{ x, y, width, height }` boxes to ignore. Max 256. |
| **`maxDiffRatio`** | `number` | No | `0.0` | Acceptable percentage of changed pixels (0–100%). |
| **`minRegionSize`** | `integer` | No | `100` | Minimum connected pixel cluster size to count as a region. |

---

## 4. Example Calls

### Strict Regression Diff Between Two Captures
```json
{
  "beforePath": "nova://screenshot/baseline-home.png",
  "afterPath": "nova://screenshot/current-home.png",
  "ignoreAntialiasing": true,
  "maxDiffRatio": 0.01
}
```

### Masking Dynamic Timestamp Header
```json
{
  "beforePath": "C:/NovaArtifacts/screens/v1.png",
  "afterPath": "C:/NovaArtifacts/screens/v2.png",
  "mask": [
    { "x": 1100, "y": 20, "width": 180, "height": 30 }
  ],
  "threshold": 25
}
```

---

## 5. Return Value Structure

```json
{
  "status": "compared",
  "changed": true,
  "withinTolerance": false,
  "dimensions": { "width": 1440, "height": 900 },
  "totalPixels": 1296000,
  "totalChangedPixels": 14820,
  "pixelDiffPercent": 1.14,
  "changedRegions": [
    {
      "index": 0,
      "pixelCount": 12400,
      "rect": { "x": 120, "y": 340, "width": 420, "height": 80 },
      "description": "Primary banner layout shift"
    }
  ],
  "diffOverlayPath": "nova://screenshot/diff-overlay-9912.png"
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `status: "dimension_mismatch"` | The two screenshots have differing width or height resolutions. | Ensure both captures were taken at identical viewport dimensions using `nova.window_set_size`. |
| `File not found: ...` | Specified image path does not exist or expired from session cache. | Re-capture images or check file paths. |

---

## 7. Related Tools & Documentation

* [`nova.capture_screenshot`](nova-capture-screenshot.md) — Capture initial and subsequent screenshots.
* [`nova.screenshot_baseline`](nova-screenshot-baseline.md) — Automated visual regression with stored baselines.
* [`nova.measure_elements`](../layout-and-qa/nova-measure-elements.md) — Inspect structural layout dimensions.
