# `nova.device_diagnostics`

Checks whether every layer of a tab - the page, its embedded frames of other sites and its workers - sees the same device, and the device you asked Nova to emulate.

---

## 1. Overview

A page is rarely one context. Embedded frames of other websites run in their own process, and workers run beside the page. Each of them reads the device for itself: user agent, platform, client hints, touch, screen, cores, memory, time zone. When those answers disagree, a site can tell that something is off - an emulated phone whose embedded frame still reports a desktop is a typical case.

`nova.device_diagnostics` reads the same values in every layer in one call and reports only what disagrees:

* Values Nova set itself (a device preset's platform, touch, screen size, pixel ratio, cores and memory; without emulation, the computer's own) are checked against what Nova expects.
* Everything else (user agent, client hints, time zone, locale, languages ...) is checked against the page.
* Workers are only compared on what workers have - they have no screen, touch or media queries.
* A value a layer could not read (for example high-entropy client hints a site's permissions policy refuses) is listed as unknown with its reason, never as a mismatch.

The tool only reads. It creates no canvas, WebGL or audio contexts.

* **Core Architecture Guide:** [Fingerprint & Identity Systems](../../../core-features/privacy/fingerprint-and-identity/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `detail` | `string` | No | `"issues"` | `issues`, `full` | 'issues' (default): mismatches, unknowns and the layer list. 'full': also every value read per layer and the expected values. |

Capability bundles: `device_emulation`, `page_read_debug`.
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.device_diagnostics",
  "arguments": { "targetId": "tab-1" }
}
```

### JSON-RPC Response (a phone preset, one worker still reporting the computer)
```json
{
  "structuredContent": {
    "targetId": "tab-1",
    "ok": true,
    "diagnostics": {
      "status": "mismatch",
      "expectedSource": "preset:Pixel 9",
      "checked": 41,
      "matched": 39,
      "mismatched": 1,
      "unknown": 1,
      "issues": [
        { "layer": "5F2C...", "type": "worker", "property": "deviceMemory", "expected": 8, "actual": 32, "reason": "differs_from_expected_device" }
      ],
      "unknowns": [
        { "layer": "A91B...", "type": "iframe", "property": "uaModel", "expected": "Pixel 9", "actual": null, "reason": "high_entropy_refused" }
      ],
      "layers": [
        { "layer": "page", "type": "page", "url": "https://example.com/", "read": true },
        { "layer": "A91B...", "type": "iframe", "url": "https://widget.example.net/", "read": true },
        { "layer": "5F2C...", "type": "worker", "url": "https://example.com/worker.js", "read": true }
      ],
      "notCovered": [
        { "type": "shared_worker", "reason": "profile_scoped" },
        { "type": "service_worker", "reason": "ownership_not_exclusive" },
        { "type": "same_process_iframe", "reason": "shares_the_page_values" }
      ]
    }
  }
}
```

`status` is `ok` (everything that could be read agrees), `mismatch` (at least one issue) or `partial` (no issue, but a layer or a value could not be read).

---

## 4. Operational Best Practices

* **Run it after applying a device:** `nova.emulation_use_device`, reload, then `nova.device_diagnostics`. Frames and workers that existed before the preset keep what they read until the page reloads.
* **Known limit:** workers report the computer's `platform` and `deviceMemory`; the browser engine offers no way to change those inside a worker.
* **Look closer at one layer:** `layers[].layer` is the subtarget id - `nova.cdp(subtargetId=...)` runs a call in that layer, `nova.page_info(include=['subtargets'])` lists them.
* **`detail='full'`** returns every value read per layer, useful when you need to see what a site sees.

---

## See Also

* [`nova.emulation_use_device`](nova-emulation-use-device.md) - Apply a device preset.
* [`nova.page_info`](../dom-and-reading/nova-page-info.md) - List a tab's frames and workers.
* [Device Emulation Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
