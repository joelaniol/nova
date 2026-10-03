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

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity. Defaults to 'default'. |
| `domain` | `string` | No | — | — | Legacy primary scope query. Accepts a domain, host:port, or origin (for example 'www.example.com', 'www.example.com:8443', or 'https://www.example.com'). Paths, queries, and fragments are invalid. |
| `scopeKey` | `string` | No | — | — | Preferred alias when reusing a persisted crawler scope from crawl_history. Accepts the same host/host:port/origin syntax as domain and must match domain/origin if multiple aliases are provided. |
| `origin` | `string` | No | — | — | Explicit origin-style alias for the reset scope (for example 'https://www.example.com:8443'). Must match domain/scopeKey if multiple aliases are provided. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.
<!-- /generated:parameters -->

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
