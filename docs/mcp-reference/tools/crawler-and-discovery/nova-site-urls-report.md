# `nova.site_urls_report`

Reports live navigation observations (new pages, 404s, redirects) to the Site-URL-Index.

---

## 1. Overview

`nova.site_urls_report` allows agents to contribute live findings back to the shared Site-URL-Index. When an agent discovers a 404 dead link, a new page title, or a URL redirection during everyday navigation, reporting it keeps the persistent index fresh for future runs.

* **Capability Bundle:** `crawler_ops`
* **Security Tier:** Tier 2 (Index Mutation)
* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`reports`** | `array of objects` | Yes | `none` | Array of observation objects containing `url`, `status`, and optional `title` or `redirectUrl`. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
        "status": 404,
        "note": "Endpoint removed in v2 migration"
      },
      {
        "url": "https://docs.example.com/api/v2/auth",
        "status": 200,
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
      "text": "Processed 2 URL observations into Site-URL-Index (1 updated, 1 marked dead)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "processedCount": 2,
    "updated": 1,
    "markedDead": 1
  }
}
```

---

## 4. Operational Best Practices

* **Self-Healing Navigation:** Whenever [`nova.navigate`](../browser-automation/nova-navigate.md) encounters a 404 or redirect, report it immediately to update the route index.
* **Batch Reporting:** Collate multiple findings and submit them in a single call to save protocol roundtrips.
* **Community Value:** Keeping the Site-URL-Index accurate speeds up route finding for all subsequent subagents and workflows.

---

## 5. Related Tools

* [`nova.site_urls`](nova-site-urls.md) — Read the indexed URL catalog.
* [`nova.discovery_reset_scope`](nova-discovery-reset-scope.md) — Clear index for a domain.
