# `nova.messages_read`

> **Reads captured window postMessage and cross-frame messaging traffic.**

* **Security Tier:** Tier 1 (Read-Only Telemetry)
* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.messages_read` inspects postMessage traffic exchanged between frames, iframes, and worker threads on the page.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `maxEntries` | `integer` | No | `500` | 1–2000 | Maximum number of entries to return. |
| `sinceId` | `integer` | No | `0` | ≥ 0 | If > 0, only entries with id > sinceId are returned. |
| `clear` | `boolean` | No | `false` | — | If true, clears the internal buffer after reading. |
| `includePayloads` | `boolean` | No | `true` | — | If true, include bounded payload previews. If false, return payload summaries only. |
| `maxPayloadChars` | `integer` | No | `1000` | 0–100000 | Maximum characters per payload preview when includePayloads=true. Use 0 to keep summaries only. |
| `maxChars` | `integer` | No | `50000` | 1000–5000000 | Maximum serialized response characters before truncation. Defaults shrink automatically under context pressure unless explicitly provided. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
<!-- /generated:parameters -->

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
