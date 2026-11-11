# `nova.fastlane_list`

> **Lists the fastlanes of this Nova profile with their state.**

* **Area:** [Fastlanes](README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

Each fastlane with its state (`pending_user_approval`, `active`, `paused`, `rejected`), the approved and the waiting revision, whether the user paused it and whether the calling session proposed it. `waitingForUser` counts the proposals the user has not answered yet. It only reads.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `fastlanes` (load it with `nova.tools_bundle(bundle='fastlanes')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.fastlane_list",
  "arguments": {}
}
```

---

## 4. Related Tools

* [`nova.fastlane_get`](nova-fastlane-get.md) - one fastlane in detail.
