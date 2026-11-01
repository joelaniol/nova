# `nova.net_devices_update`

Gives a device of the network inventory a name and a note, or forgets it.

> **Upcoming in 1.0.0-alpha.21:** this tool is not in a published setup yet.

---

## 1. Overview

* **Label and note.** `label` is a short name shown instead of the address (for example "Printer 2nd floor"), `note` a free text such as location or owner. An empty string clears either one; a field that is left out stays as it is.
* **Forget.** `forget: true` removes the device and its scan history from the inventory. A later scan that finds it adds it again as a new device.
* **Local only.** Nothing is sent on the network or to the device; only Nova's inventory on this PC changes.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `deviceId` | `string` | Yes | — | ≤ 64 characters | The device's id (dev_...) from nova.net_devices or nova.net_scan. |
| `label` | `string` | No | — | ≤ 120 characters | Short name shown instead of the address; empty clears it. |
| `note` | `string` | No | — | ≤ 2000 characters | Free note, e.g. location or owner; empty clears it. |
| `forget` | `boolean` | No | — | — | true removes the device from the inventory. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.net_devices_update",
  "arguments": {
    "deviceId": "dev_51b0e3",
    "label": "Printer 2nd floor",
    "note": "Office, toner ordered 2026-10"
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "ok": true,
    "device": {
      "deviceId": "dev_51b0e3",
      "label": "Printer 2nd floor",
      "note": "Office, toner ordered 2026-10",
      "class": { "value": "printer_scanner", "confidence": 0.9 },
      "presence": "seen"
    }
  }
}
```

---

## 4. Operational Best Practices

* **Label right after the first scan.** Named devices make every later comparison readable at a glance.
* **Forget only what is really gone.** A forgotten device that comes back is reported as new again.

---

## 5. Related Tools

* [`nova.net_devices`](nova-net-devices.md) — Reads the network inventory
* [`nova.net_scan`](nova-net-scan.md) — Scans a network and fills the inventory
