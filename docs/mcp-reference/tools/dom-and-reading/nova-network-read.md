# `nova.network_read`

> **Reads captured HTTP network requests and responses matching URL filters or status codes.**

* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.network_read` returns network events recorded in the target tab: `fetch` and `xhr` requests with method, status and duration, plus `websocket`, `eventsource`, `beacon` and `performance` entries. Filters such as `urlContains`, `methods`, `kinds`, `statusMin`/`statusMax` and `onlyFailed` run in the page before the list is returned; `summarize` returns grouped counts instead of single entries. Request and response bodies are only recorded after `includeBodies: true`, and headers only for names listed in `includeHeaders`. Continue with `sinceId`.

Recording starts with the first read on a page; `tapInstalledNow: true` means earlier requests were not captured. `waitForMatchMs` waits for a matching entry instead of polling yourself; if none arrives, the call still succeeds and reports `reasonCode: "network_read.wait_timeout"`. The text block carries the same JSON as `structuredContent.result`; the response example below is shortened (`frames`, `serviceWorker`, `outputBudget` and further fields omitted).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `maxEntries` | `integer` | No | `500` | 1–2000 | Maximum number of entries to return. |
| `sinceId` | `integer` | No | `0` | ≥ 0 | If > 0, only entries with id > sinceId are returned. |
| `clear` | `boolean` | No | `false` | — | If true, clears the internal buffer after reading. |
| `includeBodies` | `boolean` | No | — | — | Arm (true) or disarm (false) body capture for future fetch/XHR/WebSocket/eventsource events when text-like. Omit it to leave the current state alone - arming once and then reading is the normal order, and a plain read never disarms it. Off until first armed. |
| `maxBodyChars` | `integer` | No | `1000` | 0–100000 | Maximum characters per captured body preview while body capture is armed. Use 0 to capture metadata only. Omit to keep the current cap. |
| `urlContains` | `string` | No | — | — | Keep only entries whose URL contains this substring (case-insensitive). Applied in the page before serialization. |
| `methods` | `array` of `string` | No | — | — | Keep only entries with one of these HTTP methods, e.g. ['POST']. Entries without a method (performance, websocket) drop out. |
| `kinds` | `array` of `string` | No | — | — | Keep only these entry kinds. An unknown value is rejected instead of silently matching nothing. |
| `excludeWebSocket` | `boolean` | No | `false` | — | Drop websocket entries, the usual noise source on live pages. Shorthand for a kinds filter without 'websocket'. |
| `sinceMs` | `integer` | No | `0` | 0–86400000 | Keep only entries captured within the last N milliseconds. 0 disables the time filter. |
| `onlyFailed` | `boolean` | No | `false` | — | Keep only failures: HTTP status >= 400, a request that threw, or a websocket/eventsource error. Entries that carry no status (performance) drop out. |
| `statusMin` | `integer` | No | `0` | 0–599 | Lowest HTTP status to keep, e.g. 400 for errors. Entries without a status drop out. 0 disables. |
| `statusMax` | `integer` | No | `0` | 0–599 | Highest HTTP status to keep, e.g. 299 together with statusMin=200. Entries without a status drop out. 0 disables. |
| `includeHeaders` | `array` of `string` | No | — | ≤ 12 items | Header names to record on future events, e.g. ['x-request-id','cache-control']. Only the named ones are stored - recording every header would cost buffer and budget on every entry. Like includeBodies this works forward only; omit to keep the current set, pass an empty array to stop capturing. Credential headers (authorization, cookie, x-api-key and similar) come back withheld unless allowSensitiveHeaders=true. |
| `redact` | `array` of `string` | No | — | ≤ 20 items | Names whose values are masked in the returned entries: URL query parameters and same-named headers, e.g. ['accessHash','token']. Credentials travel in URLs at least as often as in headers - a live page carried its account access hash as a query parameter on every presence call. The parameter name and the rest of the URL stay readable, so the entry still shows WHICH call was made. Applied on output, on a copy, so a later read without it still sees the real values. |
| `redactHeaders` | `boolean` | No | `false` | — | Mask credential headers (authorization, cookie, x-api-key and similar) as [redacted] instead of returning their value. Off by default: a header you named in includeHeaders is one you meant to see, and a masked Authorization is what an auth problem cannot be debugged with. Turn it on when the value should not travel into the response and Nova's action log on disk. |
| `summarize` | `boolean` | No | `false` | — | Return aggregated groups INSTEAD of single entries: count, status histogram, failures, min/median/max duration, firstId/lastId per group. On a polling page this turns hundreds of near-identical calls into a few lines. maxEntries then caps the number of groups. |
| `waitForMatchMs` | `integer` | No | `0` | 0–120000 | Wait up to this long for an entry that passes the filters, instead of polling yourself. Use it after a click to see whether the request goes out: the wait starts at the current tap position unless you pass sinceId, so only NEW events count. On timeout the call still succeeds with an empty list plus wait.timedOut=true and reasonCode 'network_read.wait_timeout' - that is not the same as a quiet page. 0 disables waiting. |
| `pollIntervalMs` | `integer` | No | `250` | 50–5000 | How often the filtered read is repeated while waiting. Only used with waitForMatchMs. |
| `groupBy` | `string` | No | `"endpoint"` | `endpoint`, `url`, `status`, `kind` | Grouping key when summarize=true. 'endpoint' (default) groups by method plus path with numeric, uuid and long opaque segments collapsed, so calls that differ only by id land in one group; 'url' keeps the exact URL. |
| `maxChars` | `integer` | No | `50000` | 1000–5000000 | Maximum serialized response characters before truncation. Defaults shrink automatically under context pressure unless explicitly provided. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_network_read",
  "arguments": {
    "targetId": "tab-1",
    "urlContains": "/api/",
    "maxEntries": 25
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "{\"ok\":true,\"requestedMax\":25,\"sinceId\":0,\"clearAfterRead\":false,\"lastId\":31,\"tapInstalledNow\":false,\"entriesConsidered\":31,\"entriesMatched\":1,\"entriesFilteredOut\":30,\"entries\":[{\"id\":12,\"ts\":1791025200789,\"kind\":\"fetch\",\"url\":\"https://example.com/api/products\",\"method\":\"GET\",\"status\":200,\"ok\":true,\"durationMs\":140,\"contentType\":\"application/json\"}]}"
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "ok": true,
    "maxEntries": 25,
    "sinceId": 0,
    "clear": false,
    "entriesCount": 1,
    "entriesTotal": 1,
    "entriesOmitted": 0,
    "truncated": false,
    "result": {
      "ok": true,
      "requestedMax": 25,
      "sinceId": 0,
      "clearAfterRead": false,
      "lastId": 31,
      "tapInstalledNow": false,
      "entriesConsidered": 31,
      "entriesMatched": 1,
      "entriesFilteredOut": 30,
      "entries": [
        {
          "id": 12,
          "ts": 1791025200789,
          "kind": "fetch",
          "url": "https://example.com/api/products",
          "method": "GET",
          "status": 200,
          "ok": true,
          "durationMs": 140,
          "contentType": "application/json"
        }
      ]
    },
    "tap": {
      "filterActive": true,
      "urlContains": "/api/",
      "excludeWebSocket": false,
      "sinceMs": 0,
      "statusMin": 0,
      "statusMax": 0,
      "onlyFailed": false,
      "summarize": false,
      "entriesConsidered": 31,
      "entriesFilteredOut": 30,
      "tapInstalledNow": false
    }
  }
}
```

---

## 4. Operational Best Practices

* **XHR / Fetch Auditing:** Verify background AJAX requests completed successfully after form submissions.

---

## 5. Related Tools

* [`nova.console_read`](nova-console-read.md)
* [`nova.fetch_resource`](nova-fetch-resource.md)
