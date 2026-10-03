# `nova.messages_read`

> **Reads captured window postMessage and cross-frame messaging traffic.**

* **Capability Bundle:** `page_read_debug`
* **Security Tier:** Tier 1 (Read-Only Telemetry)
* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.messages_read` inspects postMessage traffic exchanged between frames, iframes, and worker threads on the page.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `clear` | `boolean` | No | If true, clears the internal buffer after reading. |
| `includePayloads` | `boolean` | No | If true, include bounded payload previews. If false, return payload summaries only. |
| `maxChars` | `integer` | No | Maximum serialized response characters before truncation. Defaults shrink automatically under context pressure unless explicitly provided. |
| `maxEntries` | `integer` | No | Maximum number of entries to return. |
| `maxPayloadChars` | `integer` | No | Maximum characters per payload preview when includePayloads=true. Use 0 to keep summaries only. |
| `sinceId` | `integer` | No | If > 0, only entries with id > sinceId are returned. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_messages_read",
  "arguments": {
    "targetId": "tab-1",
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
      "text": "Found 4 postMessage events."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "messages": [
      {
        "origin": "https://auth.example.com",
        "data": {
          "type": "AUTH_SUCCESS"
        }
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **OAuth / SSO Interception:** Inspect postMessage payloads during embedded SSO or payment provider modal flows.

---

## 5. Related Tools

* [`nova.console_read`](nova-console-read.md)
* [`nova.network_read`](nova-network-read.md)
