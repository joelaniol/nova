# `nova.history_get`

> **Retrieves session navigation history entries, active index, and title metadata for a tab.**

* **Security Tier:** Tier 1 (Read-Only History)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.history_get` returns the forward/backward navigation stack of the target tab, including visited URLs, timestamps, page titles, and the current index.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
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
    "targetId": "tab-1",
    "currentIndex": 3,
    "entries": [
      {
        "url": "https://example.com",
        "title": "Example Domain"
      },
      {
        "url": "https://example.com/login",
        "title": "Login"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Stack Awareness:** Check history depth before issuing multiple `nova.back` calls to avoid navigating out of the session.

---

## 5. Related Tools

* [`nova.history_go`](nova-history-go.md)
* [`nova.back`](nova-back.md)
* [`nova.forward`](nova-forward.md)
