# `nova.emulation_set_viewport_frame`

Configures the visual outline rendered around an emulated device viewport in the host UI.

---

## 1. Overview

`nova.emulation_set_viewport_frame` styles the visible border outline around a device-emulated page within the Nova window, making empty surrounding area clearly recognizable during human or visual agent reviews.


---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `enabled` | `boolean` | No | — | — | Whether the outline is drawn at all. Omit to keep the current setting. |
| `color` | `string` | No | — | — | Outline color as '#RRGGBB' or '#AARRGGBB' (6-digit values are treated as fully opaque), or 'default' to restore Nova's accent color. Omit to keep the current color. |

Capability bundle: `device_emulation` (load it with `nova.tools_bundle(bundle='device_emulation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.emulation_set_viewport_frame",
  "arguments": {
    "enabled": true,
    "color": "#FF35CCE6"
  }
}
```

### JSON-RPC Response

```json
{
  "content": [
    {
      "type": "text",
      "text": "Viewport frame enabled with color #FF35CCE6. The frame is drawn only while a device viewport override is active on the visible tab (nova.emulation_set_device_metrics / nova.emulation_use_device)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "updated",
    "changed": true,
    "enabled": true,
    "enabledChanged": true,
    "color": "#FF35CCE6",
    "effectiveColor": "#FF35CCE6",
    "usesDefaultColor": false,
    "colorChanged": true,
    "message": "Viewport frame enabled with color #FF35CCE6.",
    "note": "The frame is drawn only while a device viewport override is active on the visible tab (nova.emulation_set_device_metrics / nova.emulation_use_device)."
  }
}
```

A no-op call (nothing actually changed, e.g. re-sending the same `enabled`/`color` the frame already
has) returns `status: "noop"`, `changed: false`, and `message: "No change: the viewport frame already
had these settings."` instead of an error — it is not treated as a failure.

---

## 4. Operational Best Practices

* **Host-Only Rendering:** This outline is rendered in Nova's native XAML composition layer and does not touch or affect the page DOM or WebViews.

---

## See Also

* [`nova.emulation_set_device_metrics`](nova-emulation-set-device-metrics.md) - Set viewport dimensions.
* [Device Emulation Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
