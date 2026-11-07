# `nova.plugin_logs`

> **Retrieve recent error log entries for a specific plugin.**

* **Core Feature Guide:** [Agent-Authored Plugins](../../../core-features/plugins/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Retrieve recent error log entries for a specific plugin. Returns level, message, stack trace, and timestamp per entry.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `pluginId` | `string` | Yes | — | — | The plugin ID to query error logs for. |
| `limit` | `integer` | No | `20` | 1–100 | Maximum number of log entries to return (newest first). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `plugin_management` (load it with `nova.tools_bundle(bundle='plugin_management')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request

```json
{
  "_meta": { "intent": "Inspect recent error logs for debugging" },
  "pluginId": "com.example.price-scanner",
  "limit": 20
}
```

### JSON-RPC Response

```json
{
  "ok": true,
  "pluginId": "com.example.price-scanner",
  "entries": [
    {
      "timestamp": "2026-11-07T08:00:00Z",
      "level": "error",
      "message": "TypeError: Cannot read property 'querySelector' of null",
      "stack": "at scanPrices (content.js:42:15)"
    }
  ]
}
```

---

## 4. Operational Best Practices

* **Targeted Debugging:** Query `nova.plugin_logs` immediately following a crash or unexpected plugin behavior to inspect the exact JavaScript stack trace within the Jint runtime.
* **Ring-Buffer Sizing:** Specify a `limit` between 1 and 100 entries. Entries are delivered newest-first, allowing quick detection of repetitive exceptions or infinite loop triggers.
* **Complementary to Security Logs:** General runtime errors (syntax, null references, execution timeouts) appear in `nova.plugin_logs`, whereas host policy and sandbox permission violations are recorded in `nova.plugin_security_log`.

---

## 5. Related Tools

* [All plugin tools](README.md)
* [Agent-Authored Plugins](../../../core-features/plugins/README.md)
