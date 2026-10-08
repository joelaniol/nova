# Crawler & Discovery

Website exploration has two complementary parts: discovering routes across a site and revealing interactive states within a page. Choose the guide that matches the surface you need to inspect.

| Area | What it discovers | Where it works |
| :--- | :--- | :--- |
| [Autonomous Crawler & URL Discovery](crawler/README.md) | Linked pages, known URLs, crawl results and AI/MCP discovery files. | Hidden crawl workers or supported routes in a live tab; persistent site URL index. |
| [Surface Explorer](surface-explorer/README.md) | Menus, dialogs, tab panels, accordions, hover content and eligible navigation triggers. | The current visible tab, with classified triggers and guarded interactions. |

## How They Work Together

A crawler can map a documentation site and provide relevant routes from its URL index. Surface Explorer can then inspect content that a particular page reveals through its menus or panels. A completed URL traversal does not establish that every interactive state was inspected; a completed surface run does not establish that every URL was visited.

The URL index stores known routes and prior observations. Surface exploration can persist its own runs, states and evidence. Define the required work units separately when a task needs exhaustive coverage.

## Related Documentation

* [Task Memory (ETM)](../learning/episodic-task-memory-etm/README.md) — Defined work units and evidence of coverage.
* [Auth Surface Detection](../auth-surface-detection-asd/README.md) — Login barriers and session-state assessment.
* [Crawler Tool Reference](../../mcp-reference/tools/crawler-and-discovery/README.md) — Crawl and site-discovery contracts.
* [Surface Explorer Tool Reference](../../mcp-reference/tools/task-memory/nova-explore-surface.md) — Modes, parameters, results and protocol examples.

[All core features](../README.md)
