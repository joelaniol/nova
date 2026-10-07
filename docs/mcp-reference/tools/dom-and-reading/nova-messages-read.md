# `nova.messages_read`

> **Reads captured window postMessage and cross-frame messaging traffic.**

* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tool-observation-bus-tob/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.messages_read` returns messaging events recorded in the page: `window.postMessage` calls (`direction: "out"`), incoming `message` events with their `origin` (`direction: "in"`), `MessagePort.postMessage` calls (`kind: "messagePort"`) and dispatched `CustomEvent`s (`kind: "customEvent"`). Each entry carries a payload summary and, with `includePayloads`, a preview cut at `maxPayloadChars`. Continue with `sinceId`.

Recording starts with the first read on a page, so events from before that moment are missing. The response example below is an excerpt; the budget fields (`outputBudget`, `chars`) are omitted.

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
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_messages_read",
  "arguments": {
    "targetId": "tab-1",
    "maxEntries": 20
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "{\"ok\":true,\"requestedMax\":20,\"sinceId\":0,\"clearAfterRead\":false,\"includePayloads\":true,\"maxPayloadChars\":1000,\"lastId\":4,\"entries\":[{\"id\":4,\"ts\":1791025200456,\"kind\":\"postMessage\",\"direction\":\"in\",\"origin\":\"https://auth.example.com\",\"lastEventId\":\"\",\"payload\":{\"summary\":{\"type\":\"object\",\"keys\":[\"type\"]},\"preview\":\"{\\\"type\\\":\\\"AUTH_SUCCESS\\\"}\",\"truncated\":false,\"chars\":23}}]}"
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "ok": true,
    "maxEntries": 20,
    "sinceId": 0,
    "clear": false,
    "entriesCount": 1,
    "entriesTotal": 1,
    "entriesOmitted": 0,
    "truncated": false,
    "result": {
      "ok": true,
      "requestedMax": 20,
      "sinceId": 0,
      "clearAfterRead": false,
      "includePayloads": true,
      "maxPayloadChars": 1000,
      "lastId": 4,
      "entries": [
        {
          "id": 4,
          "ts": 1791025200456,
          "kind": "postMessage",
          "direction": "in",
          "origin": "https://auth.example.com",
          "lastEventId": "",
          "payload": {
            "summary": {
              "type": "object",
              "keys": [
                "type"
              ]
            },
            "preview": "{\"type\":\"AUTH_SUCCESS\"}",
            "truncated": false,
            "chars": 23
          }
        }
      ]
    },
    "tap": {
      "includePayloads": true,
      "maxPayloadChars": 1000
    }
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
