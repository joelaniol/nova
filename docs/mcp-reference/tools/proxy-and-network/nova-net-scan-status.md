# `nova.net_scan_status`

Shows the progress or the result of a `nova.net_scan` job, or lists the scans of this Nova session and the latest stored scans.

> **Upcoming in 1.0.0-alpha.21:** this tool is not in a published setup yet.

---

## 1. Overview

A scan of a large range can take longer than the call that started it. [`nova.net_scan`](nova-net-scan.md) then answers with `scanId` and `status: "running"`, and `nova.net_scan_status` follows it up.

* **With `scanId`, while it runs:** the phase (`discovery`, `ports`, `names`, `evaluating`) and counters: addresses, hosts found, port checks done of the total.
* **With `scanId`, once done:** the full result, the same as `nova.net_scan` returns (devices, summary, findings, devices not seen).
* **A scan of an earlier Nova session** answers `status: "stored"`; its devices are in the inventory, read them with [`nova.net_devices`](nova-net-devices.md).
* **Without `scanId`:** the scans of this Nova session (running, done or failed) plus the 10 latest scans stored in the inventory, with their ids for a comparison.

The call only reads; it sends nothing on the network.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scanId` | `string` | No | — | ≤ 64 characters | The scanId from nova.net_scan. Leave out to list scans. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.net_scan_status",
  "arguments": { "scanId": "scan_3f9a1c07be52" }
}
```

### Response while the scan runs (shortened)
```json
{
  "structuredContent": {
    "ok": true,
    "scanId": "scan_3f9a1c07be52",
    "status": "running",
    "phase": "ports",
    "progress": { "addressesTotal": 1024, "hostsDiscovered": 37, "portChecksDone": 410, "portChecksTotal": 740 },
    "timeBudgetSeconds": 300,
    "nextAction": "nova.net_scan_status"
  }
}
```

---

## 4. Operational Best Practices

* **Poll calmly.** Every few seconds is enough; the scan does not run faster when it is asked more often.
* **Keep the `scanId`.** It is the key for a later comparison with `nova.net_devices(fromScanId, toScanId)`.

---

## 5. Related Tools

* [`nova.net_scan`](nova-net-scan.md) — Starts a scan
* [`nova.net_scan_stop`](nova-net-scan-stop.md) — Ends a running scan and keeps what was found
* [`nova.net_devices`](nova-net-devices.md) — Reads the network inventory
