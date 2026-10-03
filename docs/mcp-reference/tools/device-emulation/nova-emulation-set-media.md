# `nova.emulation_set_media`

Emulates CSS media features like dark mode, reduced motion, high contrast, and print media.

---

## 1. Overview

`nova.emulation_set_media` overrides CSS media queries via CDP `Emulation.setEmulatedMedia`. It allows testing dark themes (`colorScheme: "dark"`), accessibility features, and print stylesheets.

* **Security Tier:** Tier 2 (CSS Emulation)
* **Core Architecture Guide:** [Fingerprint & Identity Systems](../../../core-features/fingerprint-and-identity.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `colorScheme` | `string` | No | — | `light`, `dark`, `no-preference` | Emulate prefers-color-scheme — use 'dark' to test dark mode. |
| `reducedMotion` | `string` | No | — | `reduce`, `no-preference` | Emulate prefers-reduced-motion — use 'reduce' to test motion-reduced layouts/animations. |
| `forcedColors` | `string` | No | — | `active`, `none` | Emulate forced-colors — use 'active' to test Windows High Contrast / forced-colors mode. |
| `contrast` | `string` | No | — | `more`, `less`, `custom`, `no-preference` | Emulate prefers-contrast. |
| `media` | `string` | No | — | `screen`, `print` | Emulate the CSS media type — use 'print' to preview print stylesheets. |

Capability bundle: `device_emulation` (load it with `nova.tools_bundle(bundle='device_emulation')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.emulation_set_media",
  "arguments": {
    "colorScheme": "dark",
    "reducedMotion": "reduce"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Emulated media features applied: color-scheme=dark, reduced-motion=reduce."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "colorScheme": "dark",
    "reducedMotion": "reduce",
    "forcedColors": null,
    "contrast": null,
    "media": null
  }
}
```

---

## 4. Operational Best Practices

* **Dark Mode QA:** Set `colorScheme: "dark"` before taking screenshots to audit high contrast legibility and dark theme styling.
* **Print Stylesheets:** Set `media: "print"` before calling `nova.save_pdf` to ensure clean print layout rendering.

---

## See Also

* [`nova.emulation_clear_media`](nova-emulation-clear-media.md) - Clear emulated media features.
* [`nova.save_pdf`](../visual-evidence/nova-save-pdf.md) - Render PDF page.
* [Device Emulation Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
