# `nova.history_search`

> **Searches the browsing history.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.history_search` returns visits from the browsing history, newest first: the same visits the user sees on Nova's history page, across all browser tabs and sandboxes. Each visit carries its `url`, `title`, `visitedAt` (ISO 8601), `source` (`user` or `agent`, so an agent can tell its own runs from the user's browsing) and `transition` (how the page was reached: link, typed, bookmark, reload, redirect, other).

Without arguments it lists the newest visits. `query` keeps only visits whose URL or title contain every word from its start, ignoring case. `totalMatches` counts all matching visits. When `hasMore` is `true`, pass `nextCursor` as `cursor` to get the next page; pages never overlap.

Private tabs record no history, so they never appear. Pages an agent opened appear only while the setting that records agent browsing in the history is on (it is on by default). The tool needs no tab and takes no claim.

This is not the back/forward list of a single tab: for that use [`nova.history_get`](../browser-automation/nova-history-get.md).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `query` | `string` | No | — | ≤ 200 characters | Optional search words, e.g. 'linkedin' or 'github pull'. Every word must match the start of a word in URL or title. Omit to list the newest visits. |
| `maxResults` | `integer` | No | `50` | 1–200 | Visits per page. |
| `cursor` | `string` | No | — | ≤ 64 characters | nextCursor from the previous result, to continue after its last visit. Omit for the first page. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_history_search",
  "arguments": { "query": "example docs", "maxResults": 2 }
}
```

### JSON-RPC Response
```json
{
  "structuredContent": {
    "ok": true,
    "query": "example docs",
    "visits": [
      {
        "url": "https://docs.example.com/api",
        "title": "Example API",
        "visitedAt": "2026-10-05T09:14:02.0000000+00:00",
        "source": "user",
        "transition": "typed"
      },
      {
        "url": "https://docs.example.com/guide",
        "title": "Example Guide",
        "visitedAt": "2026-10-04T17:40:11.0000000+00:00",
        "source": "agent",
        "transition": "link"
      }
    ],
    "returned": 2,
    "totalMatches": 7,
    "hasMore": true,
    "nextCursor": "1759599611000.4182",
    "message": "Returned the 2 newest of 7 visits matching 'example docs'; pass nextCursor for the next page."
  }
}
```

---

## 4. Operational Best Practices

* **Find a page you only half remember:** search one or two distinctive words from the site name or page title instead of a full URL.
* **Open a result:** pass its `url` to `nova.navigate` or `nova.tab_new`.
* **Unavailable right after start:** `ok=false` with `reasonCode` `history.unavailable` means the history was not open yet; retry shortly.

---

## 5. Related Tools

* [`nova.favorites_list`](nova-favorites-list.md)
* [`nova.history_get`](../browser-automation/nova-history-get.md)
