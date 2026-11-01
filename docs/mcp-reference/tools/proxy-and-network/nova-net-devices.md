# `nova.net_devices`

Reads Nova's network inventory: every device `nova.net_scan` has found, with what it is, its addresses and open ports, and whether it was seen lately. Also compares two stored scans.

> **Upcoming in 1.0.0-alpha.21:** this tool is not in a published setup yet.

---

## 1. Overview

`nova.net_devices` answers **"which devices do I have, and what changed?"** without sending anything on the network.

* **One entry per device.** Class, vendor and model, operating-system family, addresses, MAC addresses, names, open ports, roles, first and last seen, and the `label` and `note` a person or agent gave it.
* **Presence.** `seen` (in its last scan), `not_seen` (missing from 1–2 comparable scans), `likely_gone` (missing from 3 or more). A device is never marked as removed on its own; [`nova.net_devices_update`](nova-net-devices-update.md) with `forget: true` removes it.
* **Filters.** By `class`, open `port`, `presence`, `subnet` (CIDR), `newSince` (date/time of first sight) or free text in `query` (label, note, vendor, model, names, addresses, MACs). `limit` caps the list; `total` says how many matched.
* **Difference between two scans.** With `fromScanId` and `toScanId`: devices added, devices missing from the later scan, devices with other addresses, and ports opened or closed. Compare scans of the same targets; [`nova.net_scan_status`](nova-net-scan-status.md) lists the stored scan ids.
* **Kept locally.** The inventory lives on this PC in Nova's profile folder. Scans are kept for 90 days; devices stay until they are forgotten.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `deviceId` | `string` | No | — | ≤ 64 characters | One device by its id (dev_...). |
| `class` | `string` | No | — | ≤ 40 characters | Only devices of this class, one of router_gateway, access_point, printer_scanner, nas_storage, camera, tv_media, iot, windows_client, server, database, mail, unknown. |
| `port` | `integer` | No | — | 1–65535 | Only devices with this TCP port open in their last scan. |
| `presence` | `string` | No | — | `seen`, `not_seen`, `likely_gone` | seen (in its last scan), not_seen (missing from 1-2 comparable scans), likely_gone (missing from 3 or more). |
| `subnet` | `string` | No | — | ≤ 43 characters | Only devices with an address in this IPv4 network, CIDR like '192.168.1.0/24'. |
| `newSince` | `string` | No | — | ≤ 40 characters | Only devices first seen at or after this ISO date/time, e.g. '2026-11-01T00:00:00Z'. |
| `query` | `string` | No | — | ≤ 120 characters | Free text matched against label, note, vendor, model, names, addresses and MACs. |
| `limit` | `integer` | No | `100` | 1–1000 | Most devices returned; total says how many matched. |
| `fromScanId` | `string` | No | — | ≤ 64 characters | Earlier scan of a difference; needs toScanId. Compare scans of the same targets. |
| `toScanId` | `string` | No | — | ≤ 64 characters | Later scan of a difference; needs fromScanId. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### All printers
```json
{
  "name": "nova.net_devices",
  "arguments": { "class": "printer_scanner" }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "ok": true,
    "total": 1,
    "devices": [
      {
        "deviceId": "dev_51b0e3",
        "label": "Printer 2nd floor",
        "class": { "value": "printer_scanner", "confidence": 0.9 },
        "vendor": "Brother",
        "model": "MFC-L2750DW",
        "addresses": ["192.168.178.31"],
        "macs": ["00:80:77:00:00:31"],
        "openPorts": [80, 443, 515, 631, 9100],
        "presence": "seen",
        "firstSeenUtc": "2026-11-01T09:12:44Z",
        "lastSeenUtc": "2026-11-01T14:03:10Z"
      }
    ]
  }
}
```

### What changed between two scans
```json
{
  "name": "nova.net_devices",
  "arguments": { "fromScanId": "scan_3f9a1c07be52", "toScanId": "scan_8c21d4e09a17" }
}
```

```json
{
  "structuredContent": {
    "ok": true,
    "added": ["dev_a90c12"],
    "missing": [],
    "addressChanged": [{ "deviceId": "dev_51b0e3", "from": ["192.168.178.31"], "to": ["192.168.178.44"] }],
    "portsChanged": [{ "deviceId": "dev_9e0d11", "opened": [23], "closed": [] }]
  }
}
```

---

## 4. Operational Best Practices

* **New devices since a date:** `newSince` answers "what joined my network this week?" without a new scan.
* **Before relying on `not_seen`, scan again.** A device that sleeps or roams is often only away for a moment; `likely_gone` needs three comparable scans in a row.
* **Use labels.** A labelled device is easier to recognise in every later answer and in the text summary.

---

## 5. Related Tools

* [`nova.net_scan`](nova-net-scan.md) — Scans a network and fills the inventory
* [`nova.net_devices_update`](nova-net-devices-update.md) — Gives a device a label and note, or forgets it
* [`nova.net_scan_status`](nova-net-scan-status.md) — Lists the stored scans
