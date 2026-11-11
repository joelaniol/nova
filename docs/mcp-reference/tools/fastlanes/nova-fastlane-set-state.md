# `nova.fastlane_set_state`

> **Pauses or resumes an approved fastlane.**

* **Area:** [Fastlanes](README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

Pausing is always allowed and needs no approval; events while paused are not caught up later. Resuming works only for a fastlane an agent paused: one the user paused answers `paused_by_user` and stays paused until the user resumes it. A fastlane without an approved revision answers `not_approved`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `fastlaneId` | `string` | Yes | — | ≤ 32 characters | Fastlane id from nova.fastlane_create or nova.fastlane_list (e.g. 'fl_3f9a1c2b7d4e'). |
| `state` | `string` | Yes | — | `paused`, `active` | 'paused' (stop reacting; events that began and ended while paused are not caught up) or 'active' (react again; a disturbance still open counts once). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `fastlanes` (load it with `nova.tools_bundle(bundle='fastlanes')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.fastlane_set_state",
  "arguments": { "fastlaneId": "fl_3f9a1c2b7d4e", "state": "paused" }
}
```

---

## 4. Related Tools

* [`nova.fastlane_delete`](nova-fastlane-delete.md) - remove it for good.
