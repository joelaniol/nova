# `nova.emulation_set_media`

Emulates CSS media features like dark mode, reduced motion, high contrast, and print media.

---

## 1. Overview

`nova.emulation_set_media` overrides CSS media queries via CDP `Emulation.setEmulatedMedia`. It allows testing dark themes (`colorScheme: "dark"`), accessibility features, and print stylesheets.

* **Capability Bundle:** `device_emulation`
* **Security Tier:** Tier 2 (CSS Emulation)
* **Core Architecture Guide:** [Fingerprint & Identity Systems](../../../core-features/fingerprint-and-identity.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`colorScheme`** | `string` | No | `null` | `prefers-color-scheme`: `"light"`, `"dark"`, or `"no-preference"`. |
| **`reducedMotion`** | `string` | No | `null` | `prefers-reduced-motion`: `"reduce"` or `"no-preference"`. |
| **`forcedColors`** | `string` | No | `null` | `forced-colors`: `"active"` or `"none"` for high contrast testing. |
| **`contrast`** | `string` | No | `null` | `prefers-contrast`: `"more"`, `"less"`, `"custom"`, or `"no-preference"`. |
| **`media`** | `string` | No | `null` | CSS media type: `"screen"` or `"print"`. |
| **`targetId`** | `string` | No | `"active"` | Target tab ID. |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
