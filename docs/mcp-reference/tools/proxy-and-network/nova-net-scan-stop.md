# `nova.net_scan_stop`

Stops a running `nova.net_scan` and returns what it found so far.

> **Upcoming in 1.0.0-alpha.21:** this tool is not in a published setup yet.

---

## 1. Overview

* **Stops at once.** Checks in flight are cancelled; Nova waits a few seconds for the scan to wrap up.
* **Nothing is lost.** The answer is the result so far with `complete: false` and `incompleteReason: "stopped"`, and it is stored in the inventory like any scan.
* **Already finished?** The result is returned unchanged.
* **Unknown id.** A `scanId` that is not in this Nova session fails with `scan_not_found`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scanId` | `string` | Yes | — | ≤ 64 characters | The scanId from nova.net_scan or nova.net_scan_status. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.net_scan_stop",
  "arguments": { "scanId": "scan_3f9a1c07be52" }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "ok": true,
    "scanId": "scan_3f9a1c07be52",
    "status": "done",
    "complete": false,
    "incompleteReason": "stopped",
    "summary": { "seen": 21, "new": 0, "notSeen": 0, "likelyGone": 0 }
  }
}
```

---

## 4. Operational Best Practices

* **A stopped scan counts no device as missing.** Devices are only counted as not seen by complete scans, so stopping never marks a device as gone.
* **Too slow?** Instead of stopping, start again with fewer ports or a smaller range.

---

## 5. Related Tools

* [`nova.net_scan`](nova-net-scan.md) — Starts a scan
* [`nova.net_scan_status`](nova-net-scan-status.md) — Progress or result of a scan
