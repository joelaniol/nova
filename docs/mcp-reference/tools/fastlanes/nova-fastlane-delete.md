# `nova.fastlane_delete`

> **Deletes a fastlane; it stops reacting at once.**

* **Area:** [Fastlanes](README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

Removes the fastlane with its revisions, its approval and any waiting timers. Status `deleted`, or `not_found` when there was none, so a deletion that did nothing is never reported as done. To stop it only for a while, pause it with [`nova.fastlane_set_state`](nova-fastlane-set-state.md).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `fastlaneId` | `string` | Yes | — | ≤ 32 characters | Fastlane id from nova.fastlane_create or nova.fastlane_list (e.g. 'fl_3f9a1c2b7d4e'). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `fastlanes` (load it with `nova.tools_bundle(bundle='fastlanes')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.fastlane_delete",
  "arguments": { "fastlaneId": "fl_3f9a1c2b7d4e" }
}
```

---

## 4. Related Tools

* [`nova.fastlane_list`](nova-fastlane-list.md) - find the id.
