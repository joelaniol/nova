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
<!-- /generated:parameters -->

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
