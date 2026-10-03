# Site Crawler & URL Discovery Index

Broad-surface website crawling, URL indexing, sitemap verification, and discovery probes.

* **Capability Bundle(s):** `crawler_ops`
* **Core Architecture Guide:** [Core Features: crawler-and-discovery.md](../../../core-features/crawler-and-discovery.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (14 Tools)

| Tool | What it does |
| :--- | :--- |
| **[`nova.crawl_diff`](nova-crawl-diff.md)** | Compares two completed crawls of the same site to detect added, removed, or modified pages. |
| **[`nova.crawl_history`](nova-crawl-history.md)** | Lists past crawl jobs and high-level summaries from the persistent crawler database. |
| **[`nova.crawl_links`](nova-crawl-links.md)** | Instantly extracts and classifies all hyperlinks from an existing active browser tab. |
| **[`nova.crawl_results`](nova-crawl-results.md)** | Retrieves paginated page details, extracted text, metadata, and screenshots from a crawl job. |
| **[`nova.crawl_start`](nova-crawl-start.md)** | Starts a background breadth-first search (BFS) crawl from a root URL using isolated hidden WebViews. |
| **[`nova.crawl_status`](nova-crawl-status.md)** | Checks the live progress, active phase, and error metrics of a background crawl job. |
| **[`nova.crawl_stop`](nova-crawl-stop.md)** | Requests cancellation of an active crawl job, safely draining in-flight workers. |
| **[`nova.crawl_update`](nova-crawl-update.md)** | Dynamically modifies parameters (rate limits, filters, depth, pauses) of an active crawl mid-flight. |
| **[`nova.crawl_verify`](nova-crawl-verify.md)** | Performs targeted, non-traversal verification and DOM extraction against a specific list of URLs. |
| **[`nova.discovery_reset_scope`](nova-discovery-reset-scope.md)** | Destructively clears all persisted crawl history, results, and URL indexes for a site scope. |
| **[`nova.site_discovery_get`](nova-site-discovery-get.md)** | Retrieves cached MCP and AI discovery probe results for a domain without network traffic. |
| **[`nova.site_discovery_probe`](nova-site-discovery-probe.md)** | Probes a website for modern AI and MCP discovery endpoints (llms.txt, /.well-known/mcp.json, A2A). |
| **[`nova.site_urls`](nova-site-urls.md)** | Queries the persistent Site-URL-Index for known endpoints, utility scores, and route candidates. |
| **[`nova.site_urls_report`](nova-site-urls-report.md)** | Reports live navigation observations (new pages, 404s, redirects) to the Site-URL-Index. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
