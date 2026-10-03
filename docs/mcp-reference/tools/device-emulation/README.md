# Device Emulation & Responsive Testing

Mobile viewport simulation, touch event emulation, user agent overriding, and dark mode toggles.

* **Capability Bundle(s):** `device_emulation`
* **Core Architecture Guide:** [Core Features: fingerprint-and-identity.md](../../../core-features/fingerprint-and-identity.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (10 Tools)

| Tool | What it does |
| :--- | :--- |
| **[`nova.emulation_clear_device_metrics`](nova-emulation-clear-device-metrics.md)** | Clears viewport device metrics overrides, restoring normal window-sized rendering. |
| **[`nova.emulation_clear_locale`](nova-emulation-clear-locale.md)** | Clears all locale, timezone, and geolocation overrides, reverting to host system settings. |
| **[`nova.emulation_clear_media`](nova-emulation-clear-media.md)** | Clears all emulated CSS media features, reverting to host system theme and display settings. |
| **[`nova.emulation_set_device_metrics`](nova-emulation-set-device-metrics.md)** | Overrides the viewport dimensions, device scale factor (DPR), and mobile layout behavior for a tab. |
| **[`nova.emulation_set_locale`](nova-emulation-set-locale.md)** | Emulates browser locale, timezone, and geolocation coordinates for testing localized content. |
| **[`nova.emulation_set_media`](nova-emulation-set-media.md)** | Emulates CSS media features like dark mode, reduced motion, high contrast, and print media. |
| **[`nova.emulation_set_touch`](nova-emulation-set-touch.md)** | Enables or disables touch event simulation and sets the maximum touch points reported by the browser. |
| **[`nova.emulation_set_user_agent`](nova-emulation-set-user-agent.md)** | Overrides the HTTP User-Agent header, navigator.userAgent, and client hints for a tab. |
| **[`nova.emulation_set_viewport_frame`](nova-emulation-set-viewport-frame.md)** | Configures the visual outline rendered around an emulated device viewport in the host UI. |
| **[`nova.emulation_use_device`](nova-emulation-use-device.md)** | Applies a named device preset (viewport, DPR, touch capabilities, and user agent) in a single atomic call. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
