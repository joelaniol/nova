# Browser Navigation & Physical Automation

Page navigation, tab strip lifecycle management, physical clicks, humanized typing, scroll mechanics, and file uploads.

* **Capability Bundle(s):** `browser_automation`
* **Core Architecture Guide:** [Core Features: humanized-input-engine.md](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (41 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.auto_reload_get`](nova-auto-reload-get.md)** | Documented | Read the session-only native Auto-Reload state for one explicit target. |
| **[`nova.auto_reload_set`](nova-auto-reload-set.md)** | Documented | Create, update, pause, resume, or stop native session-only Auto-Reload for one explicitly claimed target. |
| **[`nova.back`](nova-back.md)** | Documented | Navigate back in history (best-effort). |
| **[`nova.choose_option`](nova-choose-option.md)** | Documented | Universal option chooser that auto-detects the control type (native <select>, ARIA combobox, standalone listbox, radio group) a... |
| **[`nova.click_selector`](nova-click-selector.md)** | Documented | Click an element by CSS selector or CTA v3 handle reference (ctaRef). |
| **[`nova.file_upload`](nova-file-upload.md)** | Documented | Upload a file to a <input type="file"> element by setting it via CDP (bypasses the native file dialog). |
| **[`nova.forward`](nova-forward.md)** | Documented | Navigate forward in history (best-effort). |
| **[`nova.history_get`](nova-history-get.md)** | Documented | Read-only snapshot of the tab's session navigation history (same source the browser's long-press Back/Forward menu uses). |
| **[`nova.history_go`](nova-history-go.md)** | Documented | Jump to a specific entry in the tab's session navigation history. |
| **[`nova.input_click`](nova-input-click.md)** | Documented | Click at x/y coordinates (CDP Input.dispatchMouseEvent). |
| **[`nova.input_drag`](nova-input-drag.md)** | Documented | Drag from (startX,startY) to (endX,endY) (best-effort; CDP Input.dispatchMouseEvent). |
| **[`nova.input_drag_humanized`](nova-input-drag-humanized.md)** | Documented | Perform a human-like drag using JS setTimeout cascade with realistic timing, jitter, and overshoot/correction from (startX,star... |
| **[`nova.input_key`](nova-input-key.md)** | Documented | Press a special key (Enter/Tab/Escape/Backspace/Arrows).. |
| **[`nova.input_move`](nova-input-move.md)** | Documented | Move the mouse pointer (hover) to x/y coordinates. |
| **[`nova.input_shortcut`](nova-input-shortcut.md)** | Documented | Send a keyboard shortcut with modifiers plus exactly one key, e.g. |
| **[`nova.input_text`](nova-input-text.md)** | Documented | Type text into the currently focused element (CDP Input.insertText). |
| **[`nova.input_wheel`](nova-input-wheel.md)** | Documented | Scroll at specific x/y coordinates via mouse wheel (CDP). |
| **[`nova.navigate`](nova-navigate.md)** | Documented | Navigate a tab to a URL. |
| **[`nova.reload`](nova-reload.md)** | Documented | Reload the tab. |
| **[`nova.route`](nova-route.md)** | Documented | SPA-safe same-document navigation. |
| **[`nova.run_sequence`](nova-run-sequence.md)** | Documented | Execute a sequence of tool calls atomically in a single MCP request. |
| **[`nova.scroll_by`](nova-scroll-by.md)** | Documented | Scroll the page by deltaX/deltaY (window.scrollBy). |
| **[`nova.scroll_element`](nova-scroll-element.md)** | Documented | Scroll a specific container element by deltaY (querySelector + scrollTop). |
| **[`nova.scroll_smart`](nova-scroll-smart.md)** | Documented | Scroll using a smart strategy that prefers the most relevant visible scroll container (main/dialog/content), with automatic fal... |
| **[`nova.scroll_to`](nova-scroll-to.md)** | Documented | Scroll the page to x/y (window.scrollTo). |
| **[`nova.select_option`](nova-select-option.md)** | Documented | Select an option on a native HTML <select> element by option value or visible label. |
| **[`nova.set_active_tab`](nova-set-active-tab.md)** | Documented | Switch the active target in the app UI (sandbox ID or browser tab ID).. |
| **[`nova.tab_claim`](nova-tab-claim.md)** | Documented | Claim a tab for exclusive control by an agent. |
| **[`nova.tab_cleanup_orphans`](nova-tab-cleanup-orphans.md)** | Documented | Close orphaned MCP-created tabs: tabs opened via nova.tab_new whose claim expired/was released, with no tool activity within th... |
| **[`nova.tab_close`](nova-tab-close.md)** | Documented | Close a browser tab by ID (or close current active target when targetId='active').. |
| **[`nova.tab_move`](nova-tab-move.md)** | Documented | Reorder a browser tab within its sandbox by naming the tab it should sit next to. |
| **[`nova.tab_new`](nova-tab-new.md)** | Documented | Create a new browser tab. |
| **[`nova.tab_pin`](nova-tab-pin.md)** | Documented | Pin or unpin a browser tab. |
| **[`nova.tab_release`](nova-tab-release.md)** | Documented | Release a previously claimed tab. |
| **[`nova.tab_snapshot`](nova-tab-snapshot.md)** | Documented | Read page info and optional text content from multiple tabs in a single call. |
| **[`nova.tab_transfer`](nova-tab-transfer.md)** | Documented | Transfer data between tabs: reads text content from a source tab element and writes it into a destination tab element. |
| **[`nova.tabs`](nova-tabs.md)** | Documented | List MCP targets (sandboxes + browser tabs) with URL/title and active target. |
| **[`nova.type_selector`](nova-type-selector.md)** | Documented | Focus an element by CSS selector and type text into it. |
| **[`nova.type_selector_secret`](../vault-and-security/nova-type-selector-secret.md)** | Documented | Type a vault password into a form field using a SecretRef token. |
| **[`nova.wait_for_modal`](nova-wait-for-modal.md)** | Documented | Wait until an open modal/dialog/overlay is detected (with optional deep traversal into same-origin iframes + open shadow roots).. |
| **[`nova.wait_for_selector`](nova-wait-for-selector.md)** | Documented | Wait for an element to exist (and optionally be visible) and return its bounding rect. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
