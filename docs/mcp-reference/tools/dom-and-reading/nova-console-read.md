# `nova.console_read`

> **Reads recent JavaScript console log messages (log, info, warn, error) from the page.**

* **Capability Bundle:** `page_read_debug`
* **Security Tier:** Tier 1 (Read-Only Diagnostics)
* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.console_read` extracts recent browser console entries captured from the target tab, including message text, log levels, timestamps, and stack traces.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `clear` | `boolean` | No | If true, clears the internal buffer after reading. |
| `engineSinceId` | `integer` | No | Cursor for engineEntries only; independent of sinceId. Continue from nextEngineSinceId. |
| `maxChars` | `integer` | No | Maximum serialized response characters before truncation. Defaults shrink automatically under context pressure unless explicitly provided. |
| `maxEntries` | `integer` | No | Maximum number of entries to return. |
| `sinceId` | `integer` | No | If > 0, only entries with id > sinceId are returned. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_console_read",
  "arguments": {
    "targetId": "tab-1",
    "level": "error",
    "limit": 20
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 2 console error entries."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "messages": [
      {
        "level": "error",
        "text": "Uncaught TypeError: Cannot read properties of undefined",
        "line": 42
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Bug Triaging:** Check console logs immediately when pages fail to respond to click events.
* **Level Filtering:** Filter by `error` or `warn` to avoid noise from noisy analytics logs.

---

## 5. Related Tools

* [`nova.network_read`](nova-network-read.md)
* [`nova.messages_read`](nova-messages-read.md)
