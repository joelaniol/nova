# `nova.fastlane_get`

> **Shows one fastlane: whether it runs, its revisions in plain words and what it did lately.**

* **Area:** [Fastlanes](README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

`running`, the approved and the waiting revision (each with contract, hash and confirmation text), and `activity` over about the last two days: events delivered at once, coalesced into an open window, limited by the hourly cap, timers waiting and actions pending. Zero activity is reported as zeros. `sourceGap` appears when events expired before Nova could read them. It only reads.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `fastlaneId` | `string` | Yes | — | ≤ 32 characters | Fastlane id from nova.fastlane_create or nova.fastlane_list (e.g. 'fl_3f9a1c2b7d4e'). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `fastlanes` (load it with `nova.tools_bundle(bundle='fastlanes')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.fastlane_get",
  "arguments": { "fastlaneId": "fl_3f9a1c2b7d4e" }
}
```

---

## 4. Related Tools

* [`nova.fastlane_list`](nova-fastlane-list.md) - all fastlanes.
* [`nova.fastlane_set_state`](nova-fastlane-set-state.md) - pause or resume.
