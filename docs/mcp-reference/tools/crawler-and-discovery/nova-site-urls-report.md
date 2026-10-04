# `nova.site_urls_report`

Reports live navigation observations (new pages, 404s, redirects) to the Site-URL-Index.

---

## 1. Overview

`nova.site_urls_report` allows agents to contribute live findings back to the shared Site-URL-Index. Each report's `status` is one of the lifecycle values `active`/`dead`/`stale` (not an HTTP status code); the HTTP status code itself goes in the separate `httpStatus` field. When an agent discovers a dead link, a new page title, or a redirect during everyday navigation, reporting it keeps the persistent index fresh for future runs.

* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity. Defaults to 'default'. |
| `reports` | `array` of `object` | Yes | — | — | Array of URL observations to report. |

Capability bundle: `crawler_ops` (load it with `nova.tools_bundle(bundle='crawler_ops')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.site_urls_report",
  "arguments": {
    "reports": [
      {
        "url": "https://docs.example.com/api/v1/deprecated",
        "status": "dead",
        "httpStatus": 404
      },
      {
        "url": "https://docs.example.com/api/v2/auth",
        "status": "active",
        "httpStatus": 200,
        "title": "Updated Auth V2 Guide"
      }
    ]
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Accepted 2 reports, rejected 0."
    }
  ],
  "structuredContent": {
    "accepted": 2,
    "rejected": 0,
    "warnings": []
  }
}
```

There is no top-level `ok`, `processedCount`, `updated`, or `markedDead` field — the real fields are `accepted`/`rejected`/`warnings`. Each report object only accepts `url`, `status` (`active`/`dead`/`stale`), `title`, `httpStatus`, `finalUrl`, `sourceUrl`, `isNavigation`, and `entryMode`; an unrecognized property (such as a free-text `note`) causes that report entry to be rejected (listed in `warnings`), not silently accepted.

---

## 4. Operational Best Practices

* **Self-Healing Navigation:** Whenever [`nova.navigate`](../browser-automation/nova-navigate.md) encounters a dead link or redirect, report it immediately with `status: "dead"`/`"stale"` (plus the observed `httpStatus`) to update the route index.
* **Batch Reporting:** Collate multiple findings and submit them in a single call to save protocol roundtrips.
* **Community Value:** Keeping the Site-URL-Index accurate speeds up route finding for all subsequent subagents and workflows.

---

## 5. Related Tools

* [`nova.site_urls`](nova-site-urls.md) — Read the indexed URL catalog.
* [`nova.discovery_reset_scope`](nova-discovery-reset-scope.md) — Clear index for a domain.
