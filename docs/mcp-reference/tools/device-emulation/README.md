# Device Emulation & Responsive Testing

Mobile viewport simulation, touch event emulation, user agent overriding, and dark mode toggles.

* **Capability Bundle(s):** `device_emulation`
* **Core Architecture Guide:** [Core Features: fingerprint-and-identity.md](../../../core-features/fingerprint-and-identity.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (10 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.emulation_clear_device_metrics`](nova-emulation-clear-device-metrics.md)** | Documented | Clear only device viewport emulation (CDP Emulation.clearDeviceMetricsOverride). |
| **[`nova.emulation_clear_locale`](nova-emulation-clear-locale.md)** | Documented | Clear all locale/timezone/geolocation overrides set by nova.emulation_set_locale (reverts to the real values). |
| **[`nova.emulation_clear_media`](nova-emulation-clear-media.md)** | Documented | Clear all emulated CSS media features set by nova.emulation_set_media (reverts color-scheme/reduced-motion/forced-colors/contra... |
| **[`nova.emulation_set_device_metrics`](nova-emulation-set-device-metrics.md)** | Documented | Emulate a device viewport (CDP Emulation.setDeviceMetricsOverride). |
| **[`nova.emulation_set_locale`](nova-emulation-set-locale.md)** | Documented | Emulate locale, timezone, and/or geolocation — the Playwright newContext({locale, timezoneId, geolocation}) equivalent for test... |
| **[`nova.emulation_set_media`](nova-emulation-set-media.md)** | Documented | Emulate CSS media features (CDP Emulation.setEmulatedMedia) — the Playwright page.emulateMedia() equivalent. |
| **[`nova.emulation_set_touch`](nova-emulation-set-touch.md)** | Documented | Enable/disable touch emulation (CDP Emulation.setTouchEmulationEnabled). |
| **[`nova.emulation_set_user_agent`](nova-emulation-set-user-agent.md)** | Documented | Override user agent for this tab (CDP Emulation.setUserAgentOverride). |
| **[`nova.emulation_set_viewport_frame`](nova-emulation-set-viewport-frame.md)** | Documented | Configure the outline Nova draws around an emulated viewport, so the unused area around a device-sized page is recognizable as ... |
| **[`nova.emulation_use_device`](nova-emulation-use-device.md)** | Documented | Apply a named device preset (viewport + deviceScaleFactor + touch + user-agent) in one call — the Playwright `devices['…']` equ... |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
