# `nova.console_read`

> **Reads recent JavaScript console log messages (log, info, warn, error) from the page.**

* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tool-observation-bus-tob/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.console_read` returns two lists from the target tab:

* `entries` (inside `result`): what the page logged through `console.log`, `info`, `warn`, `error` and `debug`, each with `id`, timestamp `ts`, `level` and the stringified `args`. Continue with `sinceId`.
* `engineEntries`: what the browser engine reported without going through `console.*`, such as CORS and CSP errors, failed subresource loads and uncaught exceptions, with `source`, `level`, `text`, `url` and `lineNumber`. Continue with `engineSinceId` from `nextEngineSinceId`.

Both recorders start on the first read. If `tapInstalledNow` or `engineTapInstalledNow` is true, nothing from before that moment was captured; an empty list then is not evidence that the page logged nothing (`coverageNote` / `engineCoverageNote` say so). There is no level filter; filter the returned entries yourself. The response example below is an excerpt; `outputBudget` and the other budget fields are omitted.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `maxEntries` | `integer` | No | `500` | 1–2000 | Maximum number of entries to return. |
| `sinceId` | `integer` | No | `0` | ≥ 0 | If > 0, only entries with id > sinceId are returned. |
| `clear` | `boolean` | No | `false` | — | If true, clears the internal buffer after reading. |
| `engineSinceId` | `integer` | No | `0` | ≥ 0 | Cursor for engineEntries only; independent of sinceId. Continue from nextEngineSinceId. |
| `maxChars` | `integer` | No | `50000` | 1000–5000000 | Maximum serialized response characters before truncation. Defaults shrink automatically under context pressure unless explicitly provided. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_console_read",
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
      "text": "{\"ok\":true,\"requestedMax\":20,\"sinceId\":0,\"clearAfterRead\":false,\"lastId\":7,\"tapInstalledNow\":false,\"entries\":[{\"id\":7,\"ts\":1791025200123,\"level\":\"error\",\"args\":[\"Failed to save draft\",\"HTTP 500\"]}]}"
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
    "tapInstalledNow": false,
    "engineEntries": [
      {
        "id": 3,
        "source": "uncaught-exception",
        "level": "error",
        "text": "Uncaught TypeError: Cannot read properties of undefined (reading 'id')",
        "url": "https://app.example.com/assets/app.js",
        "lineNumber": 42,
        "atUtc": "2026-10-03T09:00:00.1230000+00:00"
      }
    ],
    "engineEntriesCount": 1,
    "engineSinceId": 0,
    "nextEngineSinceId": 3,
    "engineTapInstalledNow": false,
    "engineEntriesDropped": 0,
    "truncated": false,
    "result": {
      "ok": true,
      "requestedMax": 20,
      "sinceId": 0,
      "clearAfterRead": false,
      "lastId": 7,
      "tapInstalledNow": false,
      "entries": [
        {
          "id": 7,
          "ts": 1791025200123,
          "level": "error",
          "args": [
            "Failed to save draft",
            "HTTP 500"
          ]
        }
      ]
    }
  }
}
```

---

## 4. Operational Best Practices

* **Bug Triaging:** Check console logs immediately when pages fail to respond to click events.
* **Read Twice:** If the first read installed the recorder, re-trigger the action (or reload) and read again.
* **Level Filtering:** Look at `level` (`error`, `warn`) in the returned entries to skip noise from analytics logs.

---

## 5. Related Tools

* [`nova.network_read`](nova-network-read.md)
* [`nova.messages_read`](nova-messages-read.md)
