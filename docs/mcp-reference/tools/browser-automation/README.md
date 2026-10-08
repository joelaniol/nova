# Browser Navigation & Physical Automation

Page navigation, tab strip lifecycle management, physical clicks, humanized typing, scroll mechanics, and file uploads.

* **Core Architecture Guide:** [Browser Interaction](../../../core-features/browser-interaction/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (41 Tools)

Capability bundles of these tools: `browser_automation`, `form_submission`, `page_read_debug`, `visual_evidence`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.auto_reload_get`](nova-auto-reload-get.md)** | Reads the native auto-reload configuration and countdown timer for the target tab. |
| **[`nova.auto_reload_set`](nova-auto-reload-set.md)** | Configures native periodic reloading for a tab with a specified interval in seconds. |
| **[`nova.back`](nova-back.md)** | Navigates backward in browser history, with optional load/settlement waiting and a screenshot sidecar. |
| **[`nova.choose_option`](nova-choose-option.md)** | Selects an option from a custom UI or standard dropdown by visible text or value. |
| **[`nova.click_selector`](nova-click-selector.md)** | Executes a verified click on a DOM element matching a CSS selector or CTA handle, featuring deep Shadow-DOM piercing, backdrop dismissal, and postcondition verification. |
| **[`nova.dismiss_blockers`](nova-dismiss-blockers.md)** | Identifies and removes click-blocking overlays, cookie consent banners, notification prompts, and modal backdrops. |
| **[`nova.file_upload`](nova-file-upload.md)** | Attaches one or more local files directly to an HTML `<input type="file">` element via Chrome DevTools Protocol (CDP), bypassing native OS file picker dialogs. |
| **[`nova.forward`](nova-forward.md)** | Navigates forward in browser history, with optional load/settlement waiting and a screenshot sidecar. |
| **[`nova.history_get`](nova-history-get.md)** | Retrieves session navigation history entries, active index, and title metadata for a tab. |
| **[`nova.history_go`](nova-history-go.md)** | Navigates forward or backward in tab history by a relative delta offset. |
| **[`nova.input_click`](nova-input-click.md)** | Dispatches a physical mouse click at exact viewport X/Y coordinates. |
| **[`nova.input_drag`](nova-input-drag.md)** | Executes a physical mouse drag-and-drop gesture from source coordinates to destination. |
| **[`nova.input_drag_humanized`](nova-input-drag-humanized.md)** | Performs a drag-and-drop gesture with an eased motion path, overshoot, correction moves, and jitter — aimed at drag-based bot checks that flag perfectly linear mouse vectors. |
| **[`nova.input_key`](nova-input-key.md)** | Dispatches a physical keyboard keypress (`keydown` followed by `keyup`) to the currently focused DOM element or active viewport. |
| **[`nova.input_move`](nova-input-move.md)** | Moves the mouse cursor to specified viewport coordinates with a single mouse-move event. |
| **[`nova.input_shortcut`](nova-input-shortcut.md)** | Dispatches a multi-key keyboard shortcut (e.g. Ctrl+A, Control+C, Shift+Enter) to the active element. |
| **[`nova.input_text`](nova-input-text.md)** | Sends a raw text string into the currently focused DOM element. |
| **[`nova.input_wheel`](nova-input-wheel.md)** | Dispatches a physical mouse wheel scroll event at specific coordinates with deltaX and deltaY. |
| **[`nova.navigate`](nova-navigate.md)** | Navigates an existing browser tab to a specified absolute URL with optional load synchronization, SPA settlement, and screenshot delivery. |
| **[`nova.reload`](nova-reload.md)** | Reloads the active tab with configurable cache bypassing, SPA settlement verification, session-destruction protection, and stuck-renderer recovery. |
| **[`nova.route`](nova-route.md)** | Performs Single Page Application (SPA) client-side routing within the same document, preserving in-memory JavaScript frameworks, Vue/React component states, and ephemeral authentication tokens. |
| **[`nova.run_sequence`](nova-run-sequence.md)** | Executes an ordered sequence of tool calls (navigation, click, type, wait, and more) in a single RPC round-trip. |
| **[`nova.scroll_by`](nova-scroll-by.md)** | Scrolls the page or active container by relative pixel offsets (deltaX, deltaY). |
| **[`nova.scroll_element`](nova-scroll-element.md)** | Shifts a specific DOM element's internal scroll offset (scrollTop) by a pixel delta. |
| **[`nova.scroll_smart`](nova-scroll-smart.md)** | Detects the real scroll container on the page (not just the window) and scrolls it by the requested delta, with a real mouse-wheel event as an automatic fallback, reporting whether content kept growing (saturation) across repeated calls. |
| **[`nova.scroll_to`](nova-scroll-to.md)** | Scrolls the target tab viewport to absolute pixel coordinates (x, y). |
| **[`nova.select_option`](nova-select-option.md)** | Selects an option in a standard HTML <select> dropdown by its value attribute or visible text. |
| **[`nova.set_active_tab`](nova-set-active-tab.md)** | Switches the active visual presentation and input focus in the Nova application shell to the specified sandbox surface or browser tab. |
| **[`nova.tab_claim`](nova-tab-claim.md)** | Claims exclusive write ownership (lease) over a specified browser tab to prevent multi-agent collisions and race conditions. |
| **[`nova.tab_cleanup_orphans`](nova-tab-cleanup-orphans.md)** | Scans for and safely closes abandoned MCP-created tabs whose lease has expired, preserving user-opened tabs and preventing memory leaks in autonomous multi-agent environments. |
| **[`nova.tab_close`](nova-tab-close.md)** | Closes an open browser tab or background WebView, releasing its system resources and associated leases. |
| **[`nova.tab_move`](nova-tab-move.md)** | Moves a tab next to another tab in the same sandbox's tab strip. |
| **[`nova.tab_new`](nova-tab-new.md)** | Creates a new browser tab with optional immediate navigation, private (incognito) browsing isolation, and automatic lease claiming. |
| **[`nova.tab_pin`](nova-tab-pin.md)** | Pins or unpins a tab in the browser tab bar to prevent accidental closure. |
| **[`nova.tab_release`](nova-tab-release.md)** | Releases an active exclusive lease on a browser tab, optionally logging finalization decisions, task outcomes, or coverage status. |
| **[`nova.tab_snapshot`](nova-tab-snapshot.md)** | Reads URL, title, load state and optional text from up to 8 tabs in one call. |
| **[`nova.tab_transfer`](nova-tab-transfer.md)** | Copies text from an element in one tab into an input field in another tab. |
| **[`nova.tabs`](nova-tabs.md)** | Lists all open tabs, WebViews, and sandbox surfaces across the workspace with filtering, claim status, and ownership details. |
| **[`nova.type_selector`](nova-type-selector.md)** | Focuses an input field or contenteditable element, optionally clears existing text, and enters text through CDP-level text insertion or an editor's own model API. |
| **[`nova.wait_for_modal`](nova-wait-for-modal.md)** | Waits until a modal dialog or overlay appears in the document and returns it. |
| **[`nova.wait_for_selector`](nova-wait-for-selector.md)** | Waits for a DOM element matching a CSS selector to appear, become visible, or disappear, returning its exact bounding rectangle and settlement state. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
