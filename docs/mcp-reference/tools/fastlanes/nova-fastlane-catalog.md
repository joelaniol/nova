# `nova.fastlane_catalog`

> **Lists what a fastlane can react to and do: event sources with their conditions, the instances that exist, actions, defaults and limits.**

* **Area:** [Fastlanes](README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

The starting point for an agent that wants Nova to react to an event instead of polling. The answer lists the sources (events of Nova's long-term network monitors), their typed conditions (`on_event`, `event_persists`, `on_recovery`), the monitor ids that exist right now, the actions (`notify`), the coalesce and limit defaults, what is not available yet, and a contract that passes [`nova.fastlane_preview`](nova-fastlane-preview.md) as it is. It only reads.

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
  "name": "nova.fastlane_catalog",
  "arguments": {}
}
```

---

## 4. Related Tools

* [`nova.fastlane_preview`](nova-fastlane-preview.md) - checks a contract built from the catalog.
* [`nova.fastlane_create`](nova-fastlane-create.md) - proposes it to the user.
