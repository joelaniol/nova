# `nova.get_layout_metrics`

> **Retrieves layout viewport dimensions, document scroll boundaries, and device scale factor.**

* **Capability Bundle:** `page_read_debug`
* **Security Tier:** Tier 1 (Read-Only Geometry)
* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.get_layout_metrics` reports layout viewport metrics, scroll offsets, content size, and device pixel ratio (DPR).

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_get_layout_metrics",
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
      "text": "Viewport: 1920x1080, Content height: 4200, Scale: 1.0."
    }
  ],
  "structuredContent": {
    "ok": true,
    "viewportWidth": 1920,
    "viewportHeight": 1080,
    "contentHeight": 4200,
    "deviceScaleFactor": 1
  }
}
```

---

## 4. Operational Best Practices

* **End-of-Page Detection:** Compare viewport height + scrollY with contentHeight to detect scroll exhaustion.

---

## 5. Related Tools

* [`nova.get_element_rect`](nova-get-element-rect.md)
* [`nova.page_info`](nova-page-info.md)
