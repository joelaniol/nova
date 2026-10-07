# `nova.crawl_links`

Instantly extracts and classifies all hyperlinks from an existing active browser tab.

---

## 1. Overview

`nova.crawl_links` performs fast, synchronous hyperlink extraction from an open tab without launching a background crawl job. It categorizes links by relation, external vs internal domain status, and navigation intent, while optionally penetrating Shadow DOM roots and iframes.

* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `urlPattern` | `string` | No | — | — | Optional JavaScript-RegExp-compatible filter for extracted links by URL. Browser-incompatible patterns are rejected fail-fast instead of degrading to an empty result. |
| `sameDomainOnly` | `boolean` | No | `false` | — | Legacy filter name. If true, only return links on the current page's exact origin (same scheme, host, and port). |
| `sameScopeOnly` | `boolean` | No | `false` | — | Preferred alias for sameDomainOnly. For crawl_links this means exact-origin only, not alias-aware same-site merging. Must match sameDomainOnly if both are provided. |
| `includeText` | `boolean` | No | `true` | — | If true, include the visible text of each link. |
| `deep` | `boolean` | No | `false` | — | If true, also search iframes and shadow DOM for links. |

Capability bundle: `crawler_ops` (load it with `nova.tools_bundle(bundle='crawler_ops')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.crawl_links",
  "arguments": {
    "sameDomainOnly": true,
    "includeText": true,
    "urlPattern": ".*\\/docs\\/.*"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 12 links on https://example.com/welcome"
    }
  ],
  "structuredContent": {
    "links": [
      {
        "url": "https://example.com/docs/getting-started",
        "text": "Getting Started Guide",
        "rel": null,
        "isExternal": false,
        "isNavigation": true
      },
      {
        "url": "https://example.com/docs/api-reference",
        "text": "Full API Reference",
        "rel": null,
        "isExternal": false,
        "isNavigation": true
      }
    ],
    "count": 12,
    "truncated": false,
    "linkLimit": 500,
    "pageUrl": "https://example.com/welcome",
    "sameDomainOnly": true,
    "sameScopeOnly": true,
    "frameworkHint": null,
    "pageSignals": {
      "title": "Welcome — Example",
      "lang": "en",
      "canonical": null,
      "robots": null
    },
    "agentSignals": null
  }
}
```

There is no top-level `ok` field. `linkLimit` reflects Nova's internal cap on extracted links per call (truncation is reported via `truncated`); `pageSignals`/`agentSignals` carry page metadata and any cached AI/MCP discovery signal for the page's origin. `pageSignals` also carries `contentLanguage`, an `hreflang` array, and an `auth` object (login-wall/logged-in signals from the page's auth probe) that are left out of this shortened example.

---

## 4. Operational Best Practices

* **Zero-Cost Exploration:** Use `nova.crawl_links` when you only need to explore the immediate next steps on the current page without background worker overhead.
* **Shadow DOM Extraction:** Pass `deep: true` if the target application uses Web Components or custom elements for navigation menus.
* **Prefilter with RegEx:** Use `urlPattern` to discard anchor fragments (`#section`), media links, or unwanted paths before receiving the payload.

---

## 5. Related Tools

* [`nova.crawl_start`](nova-crawl-start.md) — Comprehensive multi-page background crawler.
* [`nova.dom_extract`](../dom-and-reading/nova-dom-extract.md) — Custom selector attribute extraction.
