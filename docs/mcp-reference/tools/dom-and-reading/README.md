# DOM Perception & Semantic Extraction

Token-efficient text extraction, structured landmark reading, typed DOM attributes, and multi-modal fusion perception.

* **Capability Bundle(s):** `page_read_debug`
* **Core Architecture Guide:** [Core Features: tob.md](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (20 Tools)

| Tool | What it does |
| :--- | :--- |
| **[`nova.console_read`](nova-console-read.md)** | Reads recent JavaScript console log messages (log, info, warn, error) from the page. |
| **[`nova.dom_extract`](nova-dom-extract.md)** | Extracts a bounded set of fixed, strongly-typed DOM properties and bounding geometry for all elements matching a CSS selector, without executing arbitrary JavaScript. |
| **[`nova.eval`](nova-eval.md)** | Evaluates an arbitrary JavaScript expression in the main page world or isolated world. |
| **[`nova.extract_table`](nova-extract-table.md)** | Extracts HTML `<table>` elements into structured JSON objects containing column headers (`headers[]`) and data rows (`rows[][]`), eliminating manual DOM looping and complex JavaScript evaluation. |
| **[`nova.fetch_resource`](nova-fetch-resource.md)** | Fetches content from a URL inside the browser tab context, inheriting session cookies and origin credentials. |
| **[`nova.get_active_element_deep`](nova-get-active-element-deep.md)** | Traverses through nested Shadow DOM boundaries to find the truly focused interactive element. |
| **[`nova.get_element_rect`](nova-get-element-rect.md)** | Returns the exact bounding client rectangle (x, y, width, height) of an element. |
| **[`nova.get_layout_metrics`](nova-get-layout-metrics.md)** | Retrieves layout viewport dimensions, document scroll boundaries, and device scale factor. |
| **[`nova.messages_read`](nova-messages-read.md)** | Reads captured window postMessage and cross-frame messaging traffic. |
| **[`nova.network_read`](nova-network-read.md)** | Reads captured HTTP network requests and responses matching URL filters or status codes. |
| **[`nova.page_blobs_list`](nova-page-blobs-list.md)** | Lists in-memory Blob and Object URLs (blob:http://...) created by the page. |
| **[`nova.page_info`](nova-page-info.md)** | Retrieves essential page metadata (URL, title, DOM ready state, viewport dimensions, scroll offsets, and active focused element) with minimal token overhead. |
| **[`nova.perceive`](nova-perceive.md)** | Fusion multi-modal perception engine: captures visual screenshot evidence and extracts structured semantic DOM data in a single coordinated atomic operation. |
| **[`nova.perceive_snapshot_query`](nova-perceive-snapshot-query.md)** | Queries structured state and elements from a cached perceive snapshot without re-rendering. |
| **[`nova.read_dom`](nova-read-dom.md)** | Reads a sanitized snapshot of the document's outer HTML from a tab, bounded by a configurable character cap and mirrored in structured content. |
| **[`nova.read_text`](nova-read-text.md)** | Extracts clean visible plain text from the document or a specified selector container. |
| **[`nova.read_text_structured`](nova-read-text-structured.md)** | Extracts visible page text organized by semantic HTML landmark regions (`header`, `nav`, `main`, `aside`, `footer`, and `modals`), eliminating monolithic text dumps and saving LLM context tokens. |
| **[`nova.search_text`](nova-search-text.md)** | Searches the page for visible text occurrences and returns matching DOM elements with actionable CSS selectors, bounding geometry, and Shadow-DOM traversal chains. |
| **[`nova.stream_url`](nova-stream-url.md)** | Subscribes to Server-Sent Events (SSE) or WebSocket streaming traffic on the page. |
| **[`nova.wait_for_eval`](nova-wait-for-eval.md)** | Polls the target tab until a JavaScript expression evaluates to a truthy value or times out. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
