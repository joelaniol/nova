# `nova.discovery_reset_scope`

Destructively clears all persisted crawl history, results, and URL indexes for a site scope.

---

## 1. Overview

`nova.discovery_reset_scope` purges all stored crawler artifacts for a domain or canonical origin from `crawl.db`. This includes crawl job histories, extracted page text, screenshot artifacts, and Site-URL-Index rows. It is used when a website undergoes a complete redesign or during clean testing.

* **Capability Bundle:** `crawler_ops`
* **Security Tier:** Tier 3 (Destructive Purge)
* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`scopeKey`** | `string` | No | `null` | Preferred alias: canonical origin scope (e.g. `"https://docs.example.com"`). |
| **`domain`** | `string` | No | `null` | Domain or host name to purge (e.g. `"docs.example.com"`). |
| **`origin`** | `string` | No | `null` | Explicit origin-style alias. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.discovery_reset_scope",
  "arguments": {
    "domain": "docs.example.com"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Scope 'https://docs.example.com' reset: deleted 4 crawls, 85 visited page records, and 120 URL index entries."
    }
  ],
  "structuredContent": {
    "ok": true,
    "scopeKey": "https://docs.example.com",
    "deletedCrawls": 4,
    "deletedPageRecords": 85,
    "deletedIndexEntries": 120
  }
}
```

---

## 4. Operational Best Practices

* **Use with Caution:** This operation is irreversible; historical diff baselines for this scope will be lost.
* **Pre-Redesign Clean Slates:** Recommended after major web application releases or site architecture overhauls to avoid stale route pollution.
* **Domain Scoping:** Only purges data matching the exact scopeKey or domain; other sites in `crawl.db` remain untouched.

---

## 5. Related Tools

* [`nova.crawl_history`](nova-crawl-history.md) — Inspect history before resetting.
* [`nova.site_urls`](nova-site-urls.md) — Query index state.
