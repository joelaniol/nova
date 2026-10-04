# `nova.history_get`

> **Retrieves session navigation history entries, active index, and title metadata for a tab.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.history_get` returns the WebView2 navigation history stack of the target tab: each entry's index, ID, URL, title, and transition type, plus the current index and whether the tab can still go back or forward.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_history_get",
  "arguments": {
    "targetId": "tab-1"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Session history: 4 entries, current index: 3."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "stage": "history_get",
    "retryable": false,
    "targetId": "tab-1",
    "currentIndex": 3,
    "canGoBack": true,
    "canGoForward": false,
    "totalEntries": 4,
    "truncated": false,
    "entries": [
      {
        "index": 0,
        "id": 1001,
        "url": "https://example.com",
        "title": "Example Domain",
        "transitionType": "typed",
        "isCurrent": false
      },
      {
        "index": 3,
        "id": 1004,
        "url": "https://example.com/login",
        "title": "Login",
        "transitionType": "link",
        "isCurrent": true
      }
    ]
  }
}
```

The full entry list can be large; large stacks are clipped to a maximum entry count, with `truncated`/`droppedBefore`/`droppedAfter` reporting what was cut.

---

## 4. Operational Best Practices

* **Stack Awareness:** Check history depth before issuing multiple `nova.back` calls to avoid navigating out of the session.

---

## 5. Related Tools

* [`nova.history_go`](nova-history-go.md)
* [`nova.back`](nova-back.md)
* [`nova.forward`](nova-forward.md)
