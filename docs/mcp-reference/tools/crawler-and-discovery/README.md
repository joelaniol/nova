# Site Crawler & URL Discovery Index

Broad-surface website crawling, URL indexing, sitemap verification, and exploration of UI states no URL reaches.

* **Core Architecture Hub:** [Crawler & Discovery Architecture Hub](../../../core-features/crawler-and-discovery/README.md)
* **Domain Guides:**
  * [Autonomous Breadth-First Crawler](../../../core-features/crawler-and-discovery/crawler/README.md)
  * [Surface Explorer & In-Page State Analysis](../../../core-features/crawler-and-discovery/surface-explorer/README.md)
  * [Persistent Site URL Index & Routing Memory](../../../core-features/crawler-and-discovery/site-url-index/README.md)
  * [AI Discovery, llms.txt & Website MCP Probing](../../../core-features/crawler-and-discovery/site-discovery-and-mcp/README.md)
  * [Crawl History, Diffs & Verification](../../../core-features/crawler-and-discovery/diff-and-verification/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (13 Tools)

Capability bundles of these tools: `crawler_ops`, `surface_explorer`.

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
| **[`nova.explore_surface`](nova-explore-surface.md)** | Discovers interactive UI triggers (buttons, tabs, accordions) and activates them to reveal hidden DOM. |
| **[`nova.site_urls`](nova-site-urls.md)** | Queries the persistent Site-URL-Index for known endpoints, utility scores, and route candidates. |
| **[`nova.site_urls_report`](nova-site-urls-report.md)** | Reports live navigation observations (new pages, 404s, redirects) to the Site-URL-Index. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
