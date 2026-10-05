# `nova.screenshot_baseline`

Manages named, persistent visual baselines on disk and automates snapshot comparison, providing the equivalent of Playwright's `toHaveScreenshot()` for autonomous browser testing.

---

## 1. Overview

Manually saving, organizing, and referencing "before" and "after" image paths makes visual regression testing tedious. `nova.screenshot_baseline` provides a persistent, named baseline repository. Agents can create baselines (`save`), update approved changes (`update`), list existing baselines (`list`), and verify live pages against baselines (`compare`) in a single command.

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

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. Used by save/update/compare. |
| `op` | `string` | Yes | — | `save`, `update`, `compare`, `list`, `delete` | save: create new baseline (errors if exists). update: create-or-overwrite. compare: capture + diff vs baseline. list: all baselines. delete: remove one. |
| `name` | `string` | No | — | — | Baseline name (1-128 chars: letters, digits, '.', '_', '-', starting with a letter or digit). Required for save/update/compare/delete in scope='global'; optional in scope='target' where it defaults to 'default'. |
| `scope` | `string` | No | `"global"` | `global`, `target` | Baseline namespace. global: legacy durable flat store under ScreenshotBaselines/<name>.png. target: durable per-target store under ScreenshotBaselines/targets/<target>/ and omitted name defaults to 'default'. |
| `fullPage` | `boolean` | No | `false` | — | Capture the full scrollable page instead of the viewport (save/update/compare). Use the same value for save and compare. |
| `threshold` | `integer` | No | `30` | 0–255 | compare: per-pixel Euclidean RGB distance threshold. |
| `minRegionSize` | `integer` | No | `100` | 1–1000000 | compare: minimum connected pixel count per reported region. |
| `mask` | `array` of `object` | No | — | — | compare: rectangles (image pixels) to exclude from the diff — for dynamic regions (timestamps, ads, avatars). Max 256. |
| `ignoreAntialiasing` | `boolean` | No | `false` | — | compare: skip anti-aliasing-edge pixels (pixelmatch heuristic). |
| `maxDiffRatio` | `number` | No | `0` | 0–100 | compare: tolerance as percent of total pixels; <= this reports withinTolerance=true, changed=false. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundles: `system_tools`, `visual_evidence`.
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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

`structuredContent` is flat (no extra nesting). A match within tolerance:

```json
{
  "targetId": "tab-101",
  "ok": true,
  "op": "compare",
  "name": "login_modal_dark_theme",
  "scope": "global",
  "scopeTargetId": null,
  "status": "compared",
  "changed": false,
  "withinTolerance": true,
  "pixelDiffPercent": 0.004,
  "totalChangedPixels": 58,
  "changedRegions": [],
  "dimensions": { "width": 1440, "height": 900 },
  "diffOverlayPath": null,
  "diffOverlayStatus": "not_needed",
  "threshold": 30,
  "minRegionSize": 100,
  "maxDiffRatio": 0,
  "ignoreAntialiasing": false,
  "maskedRectCount": 0,
  "baselinePath": "C:\\Users\\me\\AppData\\Local\\nova-cognitive\\Nova\\ScreenshotBaselines\\login_modal_dark_theme.png"
}
```

If a regression is detected outside tolerance, `changedRegions` carries flat `{x, y, width, height, pixelCount}` entries and `diffOverlayPath` points at a **local file path** Nova wrote next to the baseline (not a `nova://` resource URI):
```json
{
  "status": "compared",
  "changed": true,
  "withinTolerance": false,
  "pixelDiffPercent": 2.45,
  "totalChangedPixels": 31752,
  "changedRegions": [
    { "x": 120, "y": 340, "width": 420, "height": 80, "pixelCount": 29800 }
  ],
  "diffOverlayPath": "C:\\Users\\me\\AppData\\Local\\nova-cognitive\\Nova\\ScreenshotBaselines\\diff-overlays\\login_modal_dark_theme.diff-20261002_194512_123.png",
  "diffOverlayStatus": "created"
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `status: "no_baseline"` (response is still `ok: true`) | Attempted to `compare` against a baseline name that has not been saved yet in this scope. | Run `op: "save"` to register the baseline first. |
| `status: "dimension_mismatch"` (`ok: true`, `changed: null`) | Viewport size changed between baseline creation and comparison; `baselineDimensions`/`currentDimensions` show the difference. | Use the same viewport size and `fullPage` setting as the original baseline, or run `op: "update"` to approve the new size. |
| `-32602: Baseline '<name>' already exists in scope '<scope>'` | `op: "save"` was called on an existing baseline. | Use `op: "update"` if you intend to approve changes. |

---

## 7. Related Tools & Documentation

* [`nova.capture_screenshot`](nova-capture-screenshot.md) — One-off screenshot captures and cropped evidence.
* [`nova.screenshot_diff`](nova-screenshot-diff.md) — Ad-hoc visual diffing between arbitrary image files.
