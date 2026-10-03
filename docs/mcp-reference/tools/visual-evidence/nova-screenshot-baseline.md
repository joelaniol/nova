# `nova.screenshot_baseline`

Manages named, persistent visual baselines on disk and automates snapshot comparison, providing the equivalent of Playwright's `toHaveScreenshot()` for autonomous browser testing.

---

## 1. Overview

Manually saving, organizing, and referencing "before" and "after" image paths makes visual regression testing tedious. `nova.screenshot_baseline` provides a persistent, named baseline repository. Agents can create baselines (`save`), update approved changes (`update`), list existing baselines (`list`), and verify live pages against baselines (`compare`) in a single command.

* **Capability Bundle:** `visual_evidence`, `quality_inspection`
* **Persistent Storage:** Baselines survive across agent restarts and browser reboots on disk.
* **Playwright Parity:** Seamless replacement for Playwright's `expect(page).toHaveScreenshot()`.
* **Scoped Namespaces (`scope`):** Store baselines globally (`scope: "global"`) or per target sandbox (`scope: "target"`).
* **Anti-Flake Controls:** Inherits exclusion masks (`mask`), anti-aliasing edge suppression, and difference tolerances from [`nova.screenshot_diff`](nova-screenshot-diff.md).

---

## 2. Supported Operations (`op`)

| Operation | Purpose | Behavior if Baseline Exists |
| :--- | :--- | :--- |
| **`save`** | Capture current tab and register as a new baseline. | Fails with an error to prevent accidental overwrites. |
| **`update`** | Approve intentional visual changes. | Captures current tab and overwrites existing baseline. |
| **`compare`** | Capture tab and diff against registered baseline. | Returns regression status, changed percentage, and diff overlay. |
| **`list`** | Retrieve all registered baseline names. | Lists baselines in the active scope. |
| **`delete`** | Remove baseline and associated diff artifacts. | Removes baseline file from disk. |

---

## 3. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`op`** | `string` | **Yes** | — | Operation: `"save"`, `"update"`, `"compare"`, `"list"`, or `"delete"`. |
| **`name`** | `string` | **Conditional** | `"default"` | Baseline name (1–128 chars). Required for `global` scope. |
| **`scope`** | `string` | No | `"global"` | Baseline namespace: `"global"` (flat store) or `"target"` (per sandbox). |
| **`fullPage`** | `boolean` | No | `false` | Capture the full scrollable page instead of just the viewport. |
| **`ignoreAntialiasing`**| `boolean` | No | `false` | `compare`: Skip font smoothing and border anti-aliasing pixels. |
| **`mask`** | `array<object>`| No | `null` | `compare`: Array of `{ x, y, width, height }` boxes to ignore. |
| **`maxDiffRatio`** | `number` | No | `0.0` | `compare`: Acceptable change percentage (0–100%). |
| **`threshold`** | `integer` | No | `30` | `compare`: Euclidean RGB color difference sensitivity. |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs`, or `"active"`. |
| **`agentId`** | `string` | No | `"default"` | Agent identity for claim lease verification. |

---

## 4. Example Workflows

### 1. Registering an Initial Baseline
```json
{
  "op": "save",
  "name": "login_modal_dark_theme",
  "fullPage": false
}
```

### 2. Verifying a Build Against the Baseline
```json
{
  "op": "compare",
  "name": "login_modal_dark_theme",
  "ignoreAntialiasing": true,
  "maxDiffRatio": 0.02
}
```

### 3. Approving Intentional UI Updates
```json
{
  "op": "update",
  "name": "login_modal_dark_theme"
}
```

---

## 5. Return Value Structure (Compare Operation)

```json
{
  "op": "compare",
  "name": "login_modal_dark_theme",
  "status": "compared",
  "changed": false,
  "withinTolerance": true,
  "pixelDiffPercent": 0.004,
  "dimensions": { "width": 1440, "height": 900 }
}
```

If visual regressions are detected outside tolerance:
```json
{
  "op": "compare",
  "name": "login_modal_dark_theme",
  "status": "compared",
  "changed": true,
  "withinTolerance": false,
  "pixelDiffPercent": 2.45,
  "totalChangedPixels": 31752,
  "diffOverlayPath": "nova://screenshot/diff-login_modal_dark_theme.png"
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `status: "no_baseline"` | Attempted to `compare` against a baseline name that has not been saved. | Run `op: "save"` to register the baseline first. |
| `status: "dimension_mismatch"` | Viewport size changed between baseline creation and comparison. | Set standard window dimensions before capturing. |
| `Baseline already exists` | `op: "save"` was called on an existing baseline. | Use `op: "update"` if you intend to approve changes. |

---

## 7. Related Tools & Documentation

* [`nova.capture_screenshot`](nova-capture-screenshot.md) — One-off screenshot captures and cropped evidence.
* [`nova.screenshot_diff`](nova-screenshot-diff.md) — Ad-hoc visual diffing between arbitrary image files.
