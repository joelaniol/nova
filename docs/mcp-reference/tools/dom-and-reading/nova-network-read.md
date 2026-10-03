# `nova.network_read`

> **Reads captured HTTP network requests and responses matching URL filters or status codes.**

* **Capability Bundle:** `page_read_debug`
* **Security Tier:** Tier 1 (Read-Only Network)
* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.network_read` returns recent network log records from the target tab, including request URLs, response status codes, latency timings, and headers.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `clear` | `boolean` | No | If true, clears the internal buffer after reading. |
| `excludeWebSocket` | `boolean` | No | Drop websocket entries, the usual noise source on live pages. Shorthand for a kinds filter without 'websocket'. |
| `groupBy` | `string` | No | Grouping key when summarize=true. 'endpoint' (default) groups by method plus path with numeric, uuid and long opaque segments collapsed, so calls that differ only by id land in one group; 'url' keeps the exact URL. |
| `includeBodies` | `boolean` | No | Arm (true) or disarm (false) body capture for future fetch/XHR/WebSocket/eventsource events when text-like. Omit it to leave the current state alone - arming once and then reading is the normal order, and a plain read never disarms it. Off until first armed. |
| `includeHeaders` | `array` | No | Header names to record on future events, e.g. ['x-request-id','cache-control']. Only the named ones are stored - recording every header would cost buffer and budget on every entry. Like includeBodies this works forward only; omit to keep the current set, pass an empty array to stop capturing. Credential headers (authorization, cookie, x-api-key and similar) come back withheld unless allowSensitiveHeaders=true. |
| `kinds` | `array` | No | Keep only these entry kinds. An unknown value is rejected instead of silently matching nothing. |
| `maxBodyChars` | `integer` | No | Maximum characters per captured body preview while body capture is armed. Use 0 to capture metadata only. Omit to keep the current cap. |
| `maxChars` | `integer` | No | Maximum serialized response characters before truncation. Defaults shrink automatically under context pressure unless explicitly provided. |
| `maxEntries` | `integer` | No | Maximum number of entries to return. |
| `methods` | `array` | No | Keep only entries with one of these HTTP methods, e.g. ['POST']. Entries without a method (performance, websocket) drop out. |
| `onlyFailed` | `boolean` | No | Keep only failures: HTTP status >= 400, a request that threw, or a websocket/eventsource error. Entries that carry no status (performance) drop out. |
| `pollIntervalMs` | `integer` | No | How often the filtered read is repeated while waiting. Only used with waitForMatchMs. |
| `redact` | `array` | No | Names whose values are masked in the returned entries: URL query parameters and same-named headers, e.g. ['accessHash','token']. Credentials travel in URLs at least as often as in headers - a live page carried its account access hash as a query parameter on every presence call. The parameter name and the rest of the URL stay readable, so the entry still shows WHICH call was made. Applied on output, on a copy, so a later read without it still sees the real values. |
| `redactHeaders` | `boolean` | No | Mask credential headers (authorization, cookie, x-api-key and similar) as [redacted] instead of returning their value. Off by default: a header you named in includeHeaders is one you meant to see, and a masked Authorization is what an auth problem cannot be debugged with. Turn it on when the value should not travel into the response and Nova's action log on disk. |
| `sinceId` | `integer` | No | If > 0, only entries with id > sinceId are returned. |
| `sinceMs` | `integer` | No | Keep only entries captured within the last N milliseconds. 0 disables the time filter. |
| `statusMax` | `integer` | No | Highest HTTP status to keep, e.g. 299 together with statusMin=200. Entries without a status drop out. 0 disables. |
| `statusMin` | `integer` | No | Lowest HTTP status to keep, e.g. 400 for errors. Entries without a status drop out. 0 disables. |
| `summarize` | `boolean` | No | Return aggregated groups INSTEAD of single entries: count, status histogram, failures, min/median/max duration, firstId/lastId per group. On a polling page this turns hundreds of near-identical calls into a few lines. maxEntries then caps the number of groups. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `urlContains` | `string` | No | Keep only entries whose URL contains this substring (case-insensitive). Applied in the page before serialization. |
| `waitForMatchMs` | `integer` | No | Wait up to this long for an entry that passes the filters, instead of polling yourself. Use it after a click to see whether the request goes out: the wait starts at the current tap position unless you pass sinceId, so only NEW events count. On timeout the call still succeeds with an empty list plus wait.timedOut=true and reasonCode 'network_read.wait_timeout' - that is not the same as a quiet page. 0 disables waiting. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_network_read",
  "arguments": {
    "targetId": "tab-1",
    "urlFilter": "/api/",
    "limit": 25
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Captured 8 matching network requests."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "requests": [
      {
        "url": "https://example.com/api/products",
        "status": 200,
        "durationMs": 140
      }
    ]
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
