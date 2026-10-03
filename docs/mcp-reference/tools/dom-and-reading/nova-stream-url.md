# `nova.stream_url`

> **Subscribes to Server-Sent Events (SSE) or WebSocket streaming traffic on the page.**

* **Capability Bundle:** `page_read_debug`
* **Security Tier:** Tier 2 (Streaming Network)
* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.stream_url` reads incoming event streams from real-time data feeds, capturing live updates up to a message count or timeout.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `kind` | `string` | No | `"tab"` | `tab`, `app` | Stream source. 'tab': web content only (page viewport). 'app': entire application window including browser chrome (title bar, tabs, URL bar). |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity for claim authorization. Defaults to 'default'. |
| `fps` | `integer` | No | `2` | 1–10 | Frames per second for the stream. |
| `includeToken` | `boolean` | No | `false` | — | If true, embed the bearer auth token in the URL for direct browser access. |
| `maxWidth` | `integer` | No | — | 1–10000 | Legacy alias for screenshotMaxWidth. Max frame width in pixels. |
| `maxHeight` | `integer` | No | — | 1–10000 | Legacy alias for screenshotMaxHeight. Max frame height in pixels. |
| `screenshotMaxWidth` | `integer` | No | — | 1–10000 | Preferred frame width limit in pixels. Must match maxWidth if both are provided. |
| `screenshotMaxHeight` | `integer` | No | — | 1–10000 | Preferred frame height limit in pixels. Must match maxHeight if both are provided. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_stream_url",
  "arguments": {
    "targetId": "tab-1",
    "url": "https://example.com/live/feed",
    "maxMessages": 10,
    "timeoutMs": 5000
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Streamed 10 SSE messages."
    }
  ],
  "structuredContent": {
    "ok": true,
    "messagesReceived": 10,
    "events": [
      {
        "event": "price_update",
        "data": "{\"symbol\": \"NVDA\", \"price\": 140.2}"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Real-time AI Feeds:** Monitor streaming token outputs from web chat interfaces.

---

## 5. Related Tools

* [`nova.fetch_resource`](nova-fetch-resource.md)
* [`nova.network_read`](nova-network-read.md)
