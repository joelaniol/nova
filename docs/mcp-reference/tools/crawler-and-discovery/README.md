# Site Crawler & URL Discovery Index

Broad-surface website crawling, URL indexing, sitemap verification, and discovery probes.

* **Capability Bundle(s):** `crawler_ops`
* **Core Architecture Guide:** [Core Features: crawler-and-discovery.md](../../../core-features/crawler-and-discovery.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (14 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.crawl_diff`](nova-crawl-diff.md)** | Documented | Compare two completed crawls of the same site to find what changed (Delta Mode). |
| **[`nova.crawl_history`](nova-crawl-history.md)** | Documented | List historical crawl jobs from the persistent crawl database. |
| **[`nova.crawl_links`](nova-crawl-links.md)** | Documented | Quick link extraction from an existing tab — no background crawl job. |
| **[`nova.crawl_results`](nova-crawl-results.md)** | Documented | Retrieve paginated results from a crawl job. |
| **[`nova.crawl_start`](nova-crawl-start.md)** | Documented | Start a background BFS crawl from a URL. |
| **[`nova.crawl_status`](nova-crawl-status.md)** | Documented | Check the progress of a crawl job. |
| **[`nova.crawl_stop`](nova-crawl-stop.md)** | Documented | Request cancellation of a running crawl job. |
| **[`nova.crawl_update`](nova-crawl-update.md)** | Documented | Modify parameters of a running or paused crawl job mid-flight. |
| **[`nova.crawl_verify`](nova-crawl-verify.md)** | Documented | Targeted re-check of specific URLs without BFS link following. |
| **[`nova.discovery_reset_scope`](nova-discovery-reset-scope.md)** | Documented | Destructively reset all persisted crawler/discovery data for one logical site scope. |
| **[`nova.site_discovery_get`](nova-site-discovery-get.md)** | Documented | Retrieve cached MCP site discovery result for a domain. |
| **[`nova.site_discovery_probe`](nova-site-discovery-probe.md)** | Documented | Probe a website for MCP/AI discovery signals: server card, direct MCP endpoint, A2A agent card, llms.txt, etc. |
| **[`nova.site_urls`](nova-site-urls.md)** | Documented | Query the persistent Site-URL-Index — a cross-crawl accumulation of discovered URLs per domain. |
| **[`nova.site_urls_report`](nova-site-urls-report.md)** | Documented | Report URL observations back to the Site-URL-Index. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
