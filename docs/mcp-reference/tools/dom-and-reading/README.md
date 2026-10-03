# DOM Perception & Semantic Extraction

Token-efficient text extraction, structured landmark reading, typed DOM attributes, and multi-modal fusion perception.

* **Capability Bundle(s):** `page_read_debug`
* **Core Architecture Guide:** [Core Features: tob.md](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (20 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.console_read`](nova-console-read.md)** | Documented | Read recent console messages from the page. |
| **[`nova.dom_extract`](nova-dom-extract.md)** | Documented | Extract a bounded set of fixed, read-only DOM properties for every element matching a CSS selector. |
| **[`nova.eval`](nova-eval.md)** | Documented | Execute a JavaScript expression in the page context (returns JSON). |
| **[`nova.extract_table`](nova-extract-table.md)** | Documented | Extract HTML tables from the page as structured { headers[], rows[][] } JSON — the dedicated tabular-read tool, instead of hand... |
| **[`nova.fetch_resource`](nova-fetch-resource.md)** | Documented | Fetch one or more URLs using the tab's authenticated session and write the bytes to disk — the bridge from 'this tab is logged ... |
| **[`nova.get_active_element_deep`](nova-get-active-element-deep.md)** | Documented | Get the active/focused element with deep traversal across open shadow roots and same-origin iframes.. |
| **[`nova.get_element_rect`](nova-get-element-rect.md)** | Documented | Get an element's bounding rect (querySelector + getBoundingClientRect). |
| **[`nova.get_layout_metrics`](nova-get-layout-metrics.md)** | Documented | Get viewport and scroll metrics (CDP Page.getLayoutMetrics). |
| **[`nova.messages_read`](nova-messages-read.md)** | Documented | Read recent postMessage, MessagePort, and CustomEvent traffic captured by an opt-in page tap. |
| **[`nova.network_read`](nova-network-read.md)** | Documented | Read recent in-page network activity captured by an opt-in tap for fetch, XHR, WebSocket, server-sent events, sendBeacon, and e... |
| **[`nova.page_blobs_list`](nova-page-blobs-list.md)** | Documented | List the blob: URLs that are live in this page, so they can be saved with nova.fetch_resource. |
| **[`nova.page_info`](nova-page-info.md)** | Documented | Read basic page info (href/title/readyState/scroll/viewport + active element).. |
| **[`nova.perceive`](nova-perceive.md)** | Documented | Fusion perception tool: by default captures a screenshot AND extracts structured page data in one call. |
| **[`nova.perceive_snapshot_query`](nova-perceive-snapshot-query.md)** | Documented | Query a saved oversized perceive(mode='full') snapshot without rerunning live DOM extraction. |
| **[`nova.read_dom`](nova-read-dom.md)** | Documented | Read document outerHTML from a tab (best-effort; may be truncated). |
| **[`nova.read_text`](nova-read-text.md)** | Documented | Read visible text content (best-effort; innerText). |
| **[`nova.read_text_structured`](nova-read-text-structured.md)** | Documented | Extract visible text grouped by page landmark regions (header, nav, main, aside, footer, modals). |
| **[`nova.search_text`](nova-search-text.md)** | Documented | Search for visible text on the page and return matching elements with CSS selectors. |
| **[`nova.stream_url`](nova-stream-url.md)** | Documented | Build a local /stream URL (multipart PNG stream). |
| **[`nova.wait_for_eval`](nova-wait-for-eval.md)** | Documented | Wait until a JavaScript expression returns a truthy value (polling). |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
