# Nova MCP Tool Catalog

Every tool exposed by **Nova AI Workspace**, grouped by operational domain. Click a tool name for its own page with the full parameter table (types, defaults, allowed values).

**Reading the Parameters column:** a plain name is required; a name ending in `?` is optional and can be left out (for example `url` must be given, `targetId?` may be omitted). Every tool also accepts the optional `_meta` object, which is not listed here.

**Sections**

<!-- generated:catalog-toc (from the section headings below; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
- [1. Browser Navigation & Tab Strip](#1-browser-navigation--tab-strip) (22)
- [2. DOM Perception & Content Extraction](#2-dom-perception--content-extraction) (20)
- [3. Layout Quality & Measuring QA](#3-layout-quality--measuring-qa) (7)
- [4. Input & Interaction](#4-input--interaction) (18)
- [5. Guarded Actions & Blocker Clearance](#5-guarded-actions--blocker-clearance) (7)
- [6. Visual Evidence & Screenshots](#6-visual-evidence--screenshots) (7)
- [7. Knowledge & Phenomenological Store (PKS)](#7-knowledge--phenomenological-store-pks) (21)
- [8. Credentials & Secure Vault](#8-credentials--secure-vault) (9)
- [9. Terminal Workspaces & Headless CLI](#9-terminal-workspaces--headless-cli) (12)
- [10. Downloads Management & Queue Control](#10-downloads-management--queue-control) (15)
- [11. Desktop Notifications & Alerts](#11-desktop-notifications--alerts) (11)
- [12. Device Emulation & Responsive Testing](#12-device-emulation--responsive-testing) (10)
- [13. External MCP Servers & Secondary Tool Bridging](#13-external-mcp-servers--secondary-tool-bridging) (10)
- [14. Proxy Routing & Network Interception](#14-proxy-routing--network-interception) (16)
- [15. Site Crawler & URL Discovery Index](#15-site-crawler--url-discovery-index) (14)
- [16. Session Tracing & DOM Event Recording](#16-session-tracing--dom-event-recording) (14)
- [17. Scheduled Tasks, Cron & Workspaces](#17-scheduled-tasks-cron--workspaces) (25)
- [18. Connectors, Mail & File Transfer](#18-connectors-mail--file-transfer) (37)
- [19. Media Intelligence & Whisper Speech-to-Text](#19-media-intelligence--whisper-speech-to-text) (24)
- [20. Site Data, Fingerprinting & Sandboxes](#20-site-data-fingerprinting--sandboxes) (23)
- [21. Episodic Task Memory & Guidance](#21-episodic-task-memory--guidance) (34)
- [22. App Shell, Dialogs & DevTools](#22-app-shell-dialogs--devtools) (61)
- [23. Agent-Authored Plugins](#23-agent-authored-plugins) (22)
<!-- /generated:catalog-toc -->

---

## 1. Browser Navigation & Tab Strip

Manage the browser lifecycle, open tabs, switch profiles, and claim exclusive access leases.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.tabs`](tools/browser-automation/nova-tabs.md)** | `activeOnly?`, `kind?`, `domain?`, `claimedBy?`, `mine?`, `agentId?`, `targetIds?`, `outputDetail?` | Lists all open tabs, WebViews, and sandbox surfaces across the workspace with filtering, claim status, and ownership details. |
| **[`nova.tab_new`](tools/browser-automation/nova-tab-new.md)** | `url?`, `activate?`, `waitForLoad?`, `waitForLoadTimeoutMs?`, `waitForSettlement?`, `settlementTimeoutMs?`, `includeScreenshot?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `outputDetail?`, `pksInclude?`, `sandbox?`, `private?`, `isolate?`, `claim?` | Creates a new browser tab with optional immediate navigation, private (incognito) browsing isolation, and automatic lease claiming. |
| **[`nova.tab_close`](tools/browser-automation/nova-tab-close.md)** | `targetId?` | Closes an open browser tab or background WebView, releasing its system resources and associated leases. |
| **[`nova.set_active_tab`](tools/browser-automation/nova-set-active-tab.md)** | `targetId` | Switches the active visual presentation and input focus in the Nova application shell to the specified sandbox surface or browser tab. |
| **[`nova.tab_claim`](tools/browser-automation/nova-tab-claim.md)** | `targetId`, `agentId?`, `agentRole?`, `ttlMs?`, `debugLabel?`, `reclaimReason?` | Claims exclusive write ownership (lease) over a specified browser tab to prevent multi-agent collisions and race conditions. |
| **[`nova.tab_release`](tools/browser-automation/nova-tab-release.md)** | `targetId`, `agentId?`, `finalizationToken?`, `finalizeDecision?`, `finalizeReasonCode?`, `finalizeReasonText?`, `finalizeStats?`, `coverageExhausted?`, `coverageExhaustedReason?`, `finalizeOutboxJobType?`, `finalizeOutboxPayload?` | Releases an active exclusive lease on a browser tab, optionally logging finalization decisions, task outcomes, or coverage status. |
| **[`nova.tab_cleanup_orphans`](tools/browser-automation/nova-tab-cleanup-orphans.md)** | `dryRun?`, `graceMinutes?`, `agentId?` | Scans for and safely closes abandoned MCP-created tabs whose lease has expired, preserving user-opened tabs and preventing memory leaks in autonomous multi-agent environments. |
| **[`nova.navigate`](tools/browser-automation/nova-navigate.md)** | `url`, `targetId?`, `waitForLoad?`, `waitForLoadTimeoutMs?`, `waitForSettlement?`, `settlementTimeoutMs?`, `settlementReadiness?`, `includeScreenshot?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `outputDetail?`, `pksInclude?`, `force?`, `confirmSessionDestruction?`, `forceAuthProbe?` | Navigates an existing browser tab to a specified absolute URL with optional load synchronization, SPA settlement, and screenshot delivery. |
| **[`nova.route`](tools/browser-automation/nova-route.md)** | `targetId?`, `url?`, `selector?`, `waitForRoute?`, `waitForRouteTimeoutMs?`, `includeScreenshot?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `pksInclude?`, `agentId?` | Performs Single Page Application (SPA) client-side routing within the same document, preserving in-memory JavaScript frameworks, Vue/React component states, and ephemeral authentication tokens. |
| **[`nova.back`](tools/browser-automation/nova-back.md)** | `targetId?`, `force?`, `waitForLoad?`, `waitForLoadTimeoutMs?`, `waitForSettlement?`, `settlementTimeoutMs?`, `includeScreenshot?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `outputDetail?` | Navigates backward in browser history, with optional load/settlement waiting and a screenshot sidecar. |
| **[`nova.forward`](tools/browser-automation/nova-forward.md)** | `targetId?`, `force?`, `waitForLoad?`, `waitForLoadTimeoutMs?`, `waitForSettlement?`, `settlementTimeoutMs?`, `includeScreenshot?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `outputDetail?` | Navigates forward in browser history, with optional load/settlement waiting and a screenshot sidecar. |
| **[`nova.reload`](tools/browser-automation/nova-reload.md)** | `targetId?`, `hard?`, `force?`, `confirmSessionDestruction?`, `waitForLoad?`, `waitForLoadTimeoutMs?`, `waitForSettlement?`, `settlementTimeoutMs?`, `includeScreenshot?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `outputDetail?`, `recoverRenderer?`, `agentId?` | Reloads the active tab with configurable cache bypassing, SPA settlement verification, session-destruction protection, and stuck-renderer recovery. |
| **[`nova.wait_for_selector`](tools/browser-automation/nova-wait-for-selector.md)** | `selector`, `targetId?`, `visible?`, `timeoutMs?`, `pollMs?`, `absent?`, `scrollIntoView?`, `autoDismissBlockers?`, `autoDismissMode?`, `includeScreenshot?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `screenshotResponseMode?`, `outputDetail?` | Waits for a DOM element matching a CSS selector to appear, become visible, or disappear, returning its exact bounding rectangle and settlement state. |
| **[`nova.auto_reload_get`](tools/browser-automation/nova-auto-reload-get.md)** | `targetId`, `agentId?` | Reads the native auto-reload configuration and countdown timer for the target tab. |
| **[`nova.auto_reload_set`](tools/browser-automation/nova-auto-reload-set.md)** | `targetId`, `mode`, `expectedRevision`, `clientRequestId`, `intervalSeconds?`, `agentId?` | Configures native periodic reloading for a tab with a specified interval in seconds. |
| **[`nova.history_get`](tools/browser-automation/nova-history-get.md)** | `targetId?` | Retrieves session navigation history entries, active index, and title metadata for a tab. |
| **[`nova.history_go`](tools/browser-automation/nova-history-go.md)** | `targetId?`, `entryId?`, `offset?`, `force?`, `confirmSessionDestruction?`, `waitForLoad?`, `waitForLoadTimeoutMs?`, `waitForSettlement?`, `settlementTimeoutMs?`, `includeScreenshot?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `outputDetail?` | Navigates forward or backward in tab history by a relative delta offset. |
| **[`nova.tab_move`](tools/browser-automation/nova-tab-move.md)** | `targetId`, `targetTabId`, `insertAfter?`, `agentId?` | Moves a tab next to another tab in the same sandbox's tab strip. |
| **[`nova.tab_pin`](tools/browser-automation/nova-tab-pin.md)** | `targetId`, `pinned`, `agentId?` | Pins or unpins a tab in the browser tab bar to prevent accidental closure. |
| **[`nova.tab_snapshot`](tools/browser-automation/nova-tab-snapshot.md)** | `targetIds`, `includeText?`, `maxCharsPerTab?`, `includeOkFacts?` | Reads URL, title, load state and optional text from up to 8 tabs in one call. |
| **[`nova.tab_transfer`](tools/browser-automation/nova-tab-transfer.md)** | `sourceTargetId`, `destTargetId`, `sourceSelector`, `destSelector`, `transform?`, `maxChars?`, `agentId?` | Copies text from an element in one tab into an input field in another tab. |
| **[`nova.wait_for_modal`](tools/browser-automation/nova-wait-for-modal.md)** | `targetId?`, `timeoutMs?`, `pollMs?`, `maxResults?`, `visibleOnly?`, `deep?`, `includeScreenshot?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `screenshotResponseMode?` | Waits until a modal dialog or overlay appears in the document and returns it. |

---

## 2. DOM Perception & Content Extraction

Token-efficient data extraction without requesting raw HTML blobs or full-screen captures.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.read_text_structured`](tools/dom-and-reading/nova-read-text-structured.md)** | `targetId?`, `selector?`, `maxCharsPerRegion?` | Extracts visible page text organized by semantic HTML landmark regions (`header`, `nav`, `main`, `aside`, `footer`, and `modals`), eliminating monolithic text dumps and saving LLM context tokens. |
| **[`nova.read_dom`](tools/dom-and-reading/nova-read-dom.md)** | `targetId?`, `maxChars?` | Reads a sanitized snapshot of the document's outer HTML from a tab, bounded by a configurable character cap and mirrored in structured content. |
| **[`nova.dom_extract`](tools/dom-and-reading/nova-dom-extract.md)** | `selector`, `properties`, `targetId?`, `maxItems?`, `maxChars?` | Extracts a bounded set of fixed, strongly-typed DOM properties and bounding geometry for all elements matching a CSS selector, without executing arbitrary JavaScript. |
| **[`nova.extract_table`](tools/dom-and-reading/nova-extract-table.md)** | `targetId?`, `selector?`, `maxTables?`, `maxRows?`, `maxCols?`, `maxCellChars?` | Extracts HTML `<table>` elements into structured JSON objects containing column headers (`headers[]`) and data rows (`rows[][]`), eliminating manual DOM looping and complex JavaScript evaluation. |
| **[`nova.search_text`](tools/dom-and-reading/nova-search-text.md)** | `text`, `targetId?`, `tag?`, `match?`, `maxResults?`, `caseSensitive?`, `visibleOnly?`, `deep?` | Searches the page for visible text occurrences and returns matching DOM elements with actionable CSS selectors, bounding geometry, and Shadow-DOM traversal chains. |
| **[`nova.perceive`](tools/dom-and-reading/nova-perceive.md)** | `targetId?`, `mode?`, `fields?`, `pksInclude?`, `maxWidth?`, `maxHeight?`, `maxDomChars?`, `maxResults?`, `omitCtas?`, `ctaLimit?`, `visibleOnly?`, `ctaColumnDetail?`, `topK?`, `resolveRefs?`, `sinceRev?`, `deep?`, `includeScreenshot?`, `screenshotFormat?`, `screenshotQuality?`, `knownDomainNotesHash?`, `responseDetail?` | Fusion multi-modal perception engine: captures visual screenshot evidence and extracts structured semantic DOM data in a single coordinated atomic operation. |
| **[`nova.page_info`](tools/dom-and-reading/nova-page-info.md)** | `targetId?`, `maxChars?` | Retrieves essential page metadata (URL, title, DOM ready state, viewport dimensions, scroll offsets, and active focused element) with minimal token overhead. |
| **[`nova.console_read`](tools/dom-and-reading/nova-console-read.md)** | `targetId?`, `maxEntries?`, `sinceId?`, `clear?`, `engineSinceId?`, `maxChars?` | Reads recent JavaScript console log messages (log, info, warn, error) from the page. |
| **[`nova.eval`](tools/dom-and-reading/nova-eval.md)** | `expression`, `targetId?`, `timeoutMs?`, `isolate?`, `functionBody?`, `frameScope?`, `frameId?`, `worldMode?`, `includeShadow?`, `redact?`, `maxChars?`, `outputDetail?` | Evaluates an arbitrary JavaScript expression in the main page world or isolated world. |
| **[`nova.fetch_resource`](tools/dom-and-reading/nova-fetch-resource.md)** | `targetId?`, `url?`, `urls?`, `savePath?`, `saveDir?`, `maxBytes?`, `timeoutMs?` | Downloads one or more URLs with the tab's session cookies and saves them to files. |
| **[`nova.get_active_element_deep`](tools/dom-and-reading/nova-get-active-element-deep.md)** | `targetId?` | Traverses through nested Shadow DOM boundaries to find the truly focused interactive element. |
| **[`nova.get_element_rect`](tools/dom-and-reading/nova-get-element-rect.md)** | `selector`, `targetId?`, `visible?`, `scrollIntoView?`, `screenshot?`, `includeScreenshot?`, `screenshotFormat?`, `screenshotQuality?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotResponseMode?`, `cropPaddingPx?`, `contextPaddingPx?`, `cropPadding?`, `outputDetail?` | Returns the exact bounding client rectangle (x, y, width, height) of an element. |
| **[`nova.get_layout_metrics`](tools/dom-and-reading/nova-get-layout-metrics.md)** | `targetId?` | Retrieves layout viewport dimensions, visual viewport offset/scale, and the full scrollable content size. |
| **[`nova.messages_read`](tools/dom-and-reading/nova-messages-read.md)** | `targetId?`, `maxEntries?`, `sinceId?`, `clear?`, `includePayloads?`, `maxPayloadChars?`, `maxChars?` | Reads captured window postMessage and cross-frame messaging traffic. |
| **[`nova.network_read`](tools/dom-and-reading/nova-network-read.md)** | `targetId?`, `maxEntries?`, `sinceId?`, `clear?`, `includeBodies?`, `maxBodyChars?`, `urlContains?`, `methods?`, `kinds?`, `excludeWebSocket?`, `sinceMs?`, `onlyFailed?`, `statusMin?`, `statusMax?`, `includeHeaders?`, `redact?`, `redactHeaders?`, `summarize?`, `waitForMatchMs?`, `pollIntervalMs?`, `groupBy?`, `maxChars?` | Reads captured HTTP network requests and responses matching URL filters or status codes. |
| **[`nova.page_blobs_list`](tools/dom-and-reading/nova-page-blobs-list.md)** | `targetId?`, `watch?`, `probeMetadata?`, `limit?` | Lists in-memory Blob and Object URLs (blob:http://...) created by the page. |
| **[`nova.perceive_snapshot_query`](tools/dom-and-reading/nova-perceive-snapshot-query.md)** | `snapshotId`, `op?`, `path?`, `node?`, `query?`, `match?`, `caseSensitive?`, `chunkIndex?`, `chunkChars?`, `maxResults?`, `contextChars?` | Queries structured state and elements from a cached perceive snapshot without re-rendering. |
| **[`nova.read_text`](tools/dom-and-reading/nova-read-text.md)** | `targetId?`, `selector?`, `maxChars?`, `offset?`, `continuationToken?` | Extracts clean visible plain text from the document or a specified selector container. |
| **[`nova.stream_url`](tools/dom-and-reading/nova-stream-url.md)** | `kind?`, `targetId?`, `agentId?`, `fps?`, `includeToken?`, `maxWidth?`, `maxHeight?`, `screenshotMaxWidth?`, `screenshotMaxHeight?` | Returns the local address of a live image stream of a tab or of the Nova window. |
| **[`nova.wait_for_eval`](tools/dom-and-reading/nova-wait-for-eval.md)** | `expression`, `targetId?`, `timeoutMs?`, `pollMs?`, `includeScreenshot?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `screenshotResponseMode?` | Polls the target tab until a JavaScript expression evaluates to a truthy value or times out. |

---

## 3. Layout Quality & Measuring QA

Inspect CSS layouts, find clipped elements, and perform accessibility audits without hand-rolling scripts.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.measure_elements`](tools/layout-and-qa/nova-measure-elements.md)** | `selectors`, `targetId?`, `properties?`, `matchMode?`, `maxMatchesPerSelector?` | Measures geometric dimensions, client/scroll metrics, overflow flags, and constraining ancestor boundaries across multiple CSS selectors in a single round-trip. |
| **[`nova.detect_overflow`](tools/layout-and-qa/nova-detect-overflow.md)** | `targetId?`, `selector?`, `maxIssues?` | Scans the page or a scoped subtree for layout defects, clipped text, overflowing containers, and elements bleeding past the viewport edge. |
| **[`nova.get_computed_style`](tools/layout-and-qa/nova-get-computed-style.md)** | `selector`, `targetId?`, `properties?` | Reads the fully resolved CSS computed style and box-model geometry of a specific DOM element, providing authoritative styling data without executing arbitrary JavaScript. |
| **[`nova.audit_accessibility`](tools/layout-and-qa/nova-audit-accessibility.md)** | `targetId?`, `selector?`, `maxIssues?`, `minTargetSize?`, `includeContrast?`, `includeTargetSize?`, `includeLabels?` | Runs an automated Accessibility (a11y) and UX compliance audit over the DOM, checking for WCAG color contrast failures, undersized tap targets, and missing accessible labels. |
| **[`nova.measure_web_vitals`](tools/layout-and-qa/nova-measure-web-vitals.md)** | `targetId?`, `durationMs?`, `reset?` | Measures Core Web Vitals (LCP, a simplified CLS, INP, FCP, plus TTFB and load timings) for the active page, rating LCP/CLS/INP/FCP as `good`, `needs-improvement`, or `poor` for automated performance gating. |
| **[`nova.composer_state`](tools/layout-and-qa/nova-composer-state.md)** | `targetId?`, `selector?`, `frameId?` | Reads what is currently sitting in a chat composer: its text, its attachments, and whether the send control looks ready. |
| **[`nova.force_pseudo_state`](tools/layout-and-qa/nova-force-pseudo-state.md)** | `selector`, `targetId?`, `states?` | Forces CSS pseudo-class states (:hover, :focus, :active, :visited) on an element. |

---

## 4. Input & Interaction

Bot-resilient input execution with natural Bézier physics and Shadow-DOM traversal.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.click_selector`](tools/browser-automation/nova-click-selector.md)** | `targetId?`, `activateIfNeeded?`, `restoreActiveTarget?`, `selector?`, `frameId?`, `button?`, `clickCount?`, `timeoutMs?`, `autoDismissBlockers?`, `autoDismissMode?`, `pksMode?`, `pksAdviceMode?`, `verify?`, `verifyTimeout?`, `waitForNavigation?`, `navigationStrict?`, `strict?`, `waitForNavigationTimeoutMs?`, `includeScreenshot?`, `screenshotPolicy?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `ctaRef?`, `ctaRev?`, `outputDetail?`, `transitionContract?` | Executes a verified click on a DOM element matching a CSS selector or CTA handle, featuring deep Shadow-DOM piercing, backdrop dismissal, and postcondition verification. |
| **[`nova.type_selector`](tools/browser-automation/nova-type-selector.md)** | `selector`, `text`, `targetId?`, `frameId?`, `inputMode?`, `modelUri?`, `clear?`, `pressEnter?`, `timeoutMs?`, `autoDismissBlockers?`, `autoDismissMode?`, `pksMode?`, `pksAdviceMode?`, `verify?`, `verifyMode?`, `verifyNormalizeWhitespace?`, `waitForNavigation?`, `waitForNavigationTimeoutMs?`, `includeScreenshot?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `forceSafety?`, `outputDetail?`, `transitionContract?` | Focuses an input field or contenteditable element, optionally clears existing text, and enters text through CDP-level text insertion or an editor's own model API. |
| **[`nova.scroll_smart`](tools/browser-automation/nova-scroll-smart.md)** | `deltaY`, `targetId?`, `deltaX?`, `containerSelector?`, `useRouteCache?`, `cachePriority?`, `suggestPksHint?` | Detects the real scroll container on the page (not just the window) and scrolls it by the requested delta, with a real mouse-wheel event as an automatic fallback, reporting whether content kept growing (saturation) across repeated calls. |
| **[`nova.input_key`](tools/browser-automation/nova-input-key.md)** | `key`, `targetId?` | Dispatches a physical keyboard keypress (`keydown` followed by `keyup`) to the currently focused DOM element or active viewport. |
| **[`nova.file_upload`](tools/browser-automation/nova-file-upload.md)** | `targetId?`, `filePaths?`, `filePath?`, `selector?`, `frameId?`, `previewPdf?` | Attaches one or more local files directly to an HTML `<input type="file">` element via Chrome DevTools Protocol (CDP), bypassing native OS file picker dialogs. |
| **[`nova.choose_option`](tools/browser-automation/nova-choose-option.md)** | `selector`, `targetId?`, `value?`, `text?`, `values?`, `texts?`, `verify?`, `timeoutMs?`, `autoDismissBlockers?`, `autoDismissMode?`, `includeScreenshot?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?` | Selects an option from a custom UI or standard dropdown by visible text or value. |
| **[`nova.input_click`](tools/browser-automation/nova-input-click.md)** | `x`, `y`, `targetId?`, `activateIfNeeded?`, `restoreActiveTarget?`, `button?`, `clickCount?`, `waitForNavigation?`, `waitForNavigationTimeoutMs?`, `includeScreenshot?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `screenshotResponseMode?` | Dispatches a physical mouse click at exact viewport X/Y coordinates. |
| **[`nova.input_drag`](tools/browser-automation/nova-input-drag.md)** | `targetId?`, `activateIfNeeded?`, `restoreActiveTarget?`, `startX?`, `startY?`, `endX?`, `endY?`, `fromX?`, `fromY?`, `toX?`, `toY?`, `steps?`, `button?` | Executes a physical mouse drag-and-drop gesture from source coordinates to destination. |
| **[`nova.input_drag_humanized`](tools/browser-automation/nova-input-drag-humanized.md)** | `targetId?`, `startX?`, `startY?`, `endX?`, `endY?`, `fromX?`, `fromY?`, `toX?`, `toY?`, `selector?`, `durationMs?`, `jitterPx?` | Performs a drag-and-drop gesture with an eased motion path, overshoot, correction moves, and jitter — aimed at drag-based bot checks that flag perfectly linear mouse vectors. |
| **[`nova.input_move`](tools/browser-automation/nova-input-move.md)** | `x`, `y`, `targetId?`, `activateIfNeeded?`, `restoreActiveTarget?` | Moves the mouse cursor to specified viewport coordinates with a single mouse-move event. |
| **[`nova.input_shortcut`](tools/browser-automation/nova-input-shortcut.md)** | `combo`, `targetId?` | Dispatches a multi-key keyboard shortcut (e.g. Ctrl+A, Control+C, Shift+Enter) to the active element. |
| **[`nova.input_text`](tools/browser-automation/nova-input-text.md)** | `text`, `targetId?` | Sends a raw text string into the currently focused DOM element. |
| **[`nova.input_wheel`](tools/browser-automation/nova-input-wheel.md)** | `x`, `y`, `deltaY`, `targetId?`, `activateIfNeeded?`, `restoreActiveTarget?`, `deltaX?` | Dispatches a physical mouse wheel scroll event at specific coordinates with deltaX and deltaY. |
| **[`nova.run_sequence`](tools/browser-automation/nova-run-sequence.md)** | `steps`, `targetId?`, `agentId?`, `totalTimeoutMs?`, `defaults?`, `options?` | Executes an ordered sequence of tool calls (navigation, click, type, wait, and more) in a single RPC round-trip. |
| **[`nova.scroll_by`](tools/browser-automation/nova-scroll-by.md)** | `deltaY`, `targetId?`, `deltaX?`, `containerSelector?` | Scrolls the page or active container by relative pixel offsets (deltaX, deltaY). |
| **[`nova.scroll_element`](tools/browser-automation/nova-scroll-element.md)** | `selector`, `deltaY`, `targetId?` | Shifts a specific DOM element's internal scroll offset (scrollTop) by a pixel delta. |
| **[`nova.scroll_to`](tools/browser-automation/nova-scroll-to.md)** | `y`, `targetId?`, `x?` | Scrolls the target tab viewport to absolute pixel coordinates (x, y). |
| **[`nova.select_option`](tools/browser-automation/nova-select-option.md)** | `selector`, `targetId?`, `value?`, `values?`, `text?`, `texts?`, `verify?`, `timeoutMs?`, `autoDismissBlockers?`, `autoDismissMode?`, `includeScreenshot?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?` | Selects an option in a standard HTML <select> dropdown by its value attribute or visible text. |

---

## 5. Guarded Actions & Blocker Clearance

High-impact macros that run safety pre-checks to prevent destructive loops or session loss.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.dismiss_blockers`](tools/browser-automation/nova-dismiss-blockers.md)** | `targetId?`, `mode?`, `maxPasses?`, `pressEscape?` | Identifies and removes click-blocking overlays, cookie consent banners, notification prompts, and modal backdrops. |
| **[`nova.guarded_send_message`](tools/guarded-actions/nova-guarded-send-message.md)** | `targetId?`, `activateIfNeeded?`, `restoreActiveTarget?`, `selector?`, `frameId?`, `ctaRef?`, `ctaRev?`, `button?`, `clickCount?`, `timeoutMs?`, `autoDismissBlockers?`, `autoDismissMode?`, `pksMode?`, `pksAdviceMode?`, `verify?`, `verifyTimeout?`, `waitForNavigation?`, `navigationStrict?`, `waitForNavigationTimeoutMs?`, `includeScreenshot?`, `screenshotPolicy?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `outputDetail?`, `transitionContract?`, `text?`, `message?` | High-level guarded macro for chat interfaces (ChatGPT, Claude.ai, Gemini, Slack, Teams): auto-discovers the composer, types text with read-back verification, resolves the send button, clicks it, and verifies delivery in a single atomic operation. |
| **[`nova.guarded_submit_form`](tools/guarded-actions/nova-guarded-submit-form.md)** | `targetId?`, `activateIfNeeded?`, `restoreActiveTarget?`, `selector?`, `frameId?`, `ctaRef?`, `ctaRev?`, `button?`, `clickCount?`, `timeoutMs?`, `autoDismissBlockers?`, `autoDismissMode?`, `pksMode?`, `pksAdviceMode?`, `verify?`, `verifyTimeout?`, `waitForNavigation?`, `navigationStrict?`, `waitForNavigationTimeoutMs?`, `includeScreenshot?`, `screenshotPolicy?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `outputDetail?`, `transitionContract?` | High-level guarded macro for form submissions, wrapping click dispatch in an automated transition contract to verify validation rules, prevent duplicate submissions, and confirm post-submit transitions. |
| **[`nova.guarded_login`](tools/guarded-actions/nova-guarded-login.md)** | `targetId?`, `activateIfNeeded?`, `restoreActiveTarget?`, `selector?`, `frameId?`, `ctaRef?`, `ctaRev?`, `button?`, `clickCount?`, `timeoutMs?`, `autoDismissBlockers?`, `autoDismissMode?`, `pksMode?`, `pksAdviceMode?`, `verify?`, `verifyTimeout?`, `waitForNavigation?`, `navigationStrict?`, `waitForNavigationTimeoutMs?`, `includeScreenshot?`, `screenshotPolicy?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `outputDetail?`, `transitionContract?` | High-level guarded macro for login form submissions, featuring integrated Auth Surface Detection (ASD) that distinguishes between authentication rejections and multi-factor (2FA/MFA) follow-up states. |
| **[`nova.cmp_apply`](tools/guarded-actions/nova-cmp-apply.md)** | `targetId`, `agentId?`, `intent?`, `mode?` | Applies a typed privacy consent policy directly through recognized Consent Management Platform (CMP) vendor JavaScript APIs (OneTrust, Sourcepoint, Cookiebot), verifying consent vector state before and after execution. |
| **[`nova.guarded_switch_model`](tools/guarded-actions/nova-guarded-switch-model.md)** | `targetId?`, `activateIfNeeded?`, `restoreActiveTarget?`, `selector?`, `frameId?`, `ctaRef?`, `ctaRev?`, `button?`, `clickCount?`, `timeoutMs?`, `autoDismissBlockers?`, `autoDismissMode?`, `pksMode?`, `pksAdviceMode?`, `verify?`, `verifyTimeout?`, `waitForNavigation?`, `navigationStrict?`, `waitForNavigationTimeoutMs?`, `includeScreenshot?`, `screenshotPolicy?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `outputDetail?`, `transitionContract?` | Clicks a model entry in a web app's model menu and verifies that the selected model changed. |
| **[`nova.guarded_switch_sandbox`](tools/guarded-actions/nova-guarded-switch-sandbox.md)** | `targetId?`, `activateIfNeeded?`, `restoreActiveTarget?`, `selector?`, `frameId?`, `ctaRef?`, `ctaRev?`, `button?`, `clickCount?`, `timeoutMs?`, `autoDismissBlockers?`, `autoDismissMode?`, `pksMode?`, `pksAdviceMode?`, `verify?`, `verifyTimeout?`, `waitForNavigation?`, `navigationStrict?`, `waitForNavigationTimeoutMs?`, `includeScreenshot?`, `screenshotPolicy?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotFormat?`, `screenshotQuality?`, `outputDetail?`, `transitionContract?` | Clicks a workspace switcher entry in a web app and verifies that the workspace changed. |

---

## 6. Visual Evidence & Screenshots

Lossless visual captures and regression testing with bounded budgets.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.capture_screenshot`](tools/visual-evidence/nova-capture-screenshot.md)** | `targetId?`, `maxWidth?`, `maxHeight?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `format?`, `screenshotFormat?`, `quality?`, `screenshotQuality?`, `region?`, `responseMode?`, `force?`, `highlightSelector?`, `scrollToSelector?`, `selector?`, `cropPaddingPx?`, `contextPaddingPx?`, `cropPadding?`, `includeContextImage?`, `highlightColor?`, `highlightStrokePx?`, `highlightStyle?`, `highlightPlacement?`, `highlightLabel?`, `highlightBackdrop?`, `highlightCenterMarker?`, `outputDetail?`, `fullPage?` | Captures visual screenshot evidence of the active page, a specific DOM element, or a bounded pixel region, with support for cryptographic SHA-256 hashing, visual callout highlights, and token-saving delivery modes. |
| **[`nova.screenshot_diff`](tools/visual-evidence/nova-screenshot-diff.md)** | `beforePath`, `afterPath`, `threshold?`, `minRegionSize?`, `mask?`, `ignoreAntialiasing?`, `maxDiffRatio?` | Performs pixel-by-pixel visual comparison between two screenshot images or resource URIs, returning changed pixel percentages, cluster bounding boxes, and visual diff overlays. |
| **[`nova.screenshot_baseline`](tools/visual-evidence/nova-screenshot-baseline.md)** | `op`, `targetId?`, `name?`, `scope?`, `fullPage?`, `threshold?`, `minRegionSize?`, `mask?`, `ignoreAntialiasing?`, `maxDiffRatio?` | Manages named, persistent visual baselines on disk and automates snapshot comparison, providing the equivalent of Playwright's `toHaveScreenshot()` for autonomous browser testing. |
| **[`nova.save_pdf`](tools/visual-evidence/nova-save-pdf.md)** | `targetId?`, `savePath?`, `timeoutMs?`, `landscape?`, `printBackground?`, `displayHeaderFooter?`, `preferCSSPageSize?`, `generateTaggedPDF?`, `scale?`, `pageRanges?`, `paperWidth?`, `paperHeight?`, `marginTop?`, `marginBottom?`, `marginLeft?`, `marginRight?` | Renders the active web page to a vector PDF document on disk via Chrome DevTools Protocol (`Page.printToPDF`), providing zero-token document archiving and export capabilities. |
| **[`nova.capture_app_screenshot`](tools/visual-evidence/nova-capture-app-screenshot.md)** | `agentId?`, `targetId?`, `maxWidth?`, `maxHeight?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `format?`, `quality?`, `responseMode?` | Captures the Nova app window (tabs, topbar, WebView content) — or, if another agent holds the active tab's claim, a read-only redacted shell view with page content masked out. |
| **[`nova.read_pdf`](tools/visual-evidence/nova-read-pdf.md)** | `path`, `pages?`, `maxChars?`, `includePages?` | Extracts the text of a local PDF file, optionally per page and for selected pages only. |
| **[`nova.responsive_screenshots`](tools/visual-evidence/nova-responsive-screenshots.md)** | `widths`, `targetId?`, `height?`, `deviceScaleFactor?`, `mobile?`, `fullPage?`, `format?`, `quality?` | Sweeps multiple viewport widths one at a time, capturing a screenshot at each and restoring the tab's original viewport afterwards. |

---

## 7. Knowledge & Phenomenological Store (PKS)

Self-learning procedural memory for persistent fast-paths and domain notes.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.pks_get`](tools/pks-and-learning/nova-pks-get.md)** | `scope`, `phenomenonId?`, `outputDetail?`, `context?` | Retrieves domain-scoped Phenomenological Knowledge Store (PKS) entries, playbooks, interaction fingerprints, and contextual environment markers. |
| **[`nova.pks_upsert`](tools/pks-and-learning/nova-pks-upsert.md)** | `scope`, `phenomenon`, `context?`, `trust?` | Stores or updates a verified phenomenon, behavioral playbook, and detection fingerprint in the Phenomenological Knowledge Store (PKS). |
| **[`nova.pks_match`](tools/pks-and-learning/nova-pks-match.md)** | `scope`, `observation`, `topK?`, `context?` | Matches live page observations against registered Phenomenological Knowledge Store (PKS) fingerprints and global platform templates to identify active UI phenomena. |
| **[`nova.telemetry_report`](tools/pks-and-learning/nova-telemetry-report.md)** | `scope`, `phenomenonId`, `outcome`, `targetId?`, `elapsedMs?`, `elapsed_ms?`, `features?` | Reports empirical execution outcomes (`success`, `failure`, or `not_applicable`) for a PKS phenomenon interaction, updating health scores and driving automatic promotion and deprecation gates. |
| **[`nova.explain`](tools/pks-and-learning/nova-explain.md)** | `scope`, `stableId`, `stable_id?`, `observedSignals?`, `observed_signals?` | Explains why a PKS phenomenon resides at its current learning level, returning a detailed per-gate breakdown of promotion requirements, failure reasons, and remediation hints. |
| **[`nova.learn_feedback`](tools/pks-and-learning/nova-learn-feedback.md)** | `scope?`, `since?`, `limit?` | Lists recent learning-level changes (promotions, demotions, deprecations, revivals, generated candidates) in the PKS. |
| **[`nova.learn_generate`](tools/pks-and-learning/nova-learn-generate.md)** | `scope`, `limit?` | Synthesizes a proposed phenomenon interaction playbook from recorded execution trajectories. |
| **[`nova.learn_onboarding_confirm`](tools/pks-and-learning/nova-learn-onboarding-confirm.md)** | `domain`, `paraphrase` | Confirms the learn-mode onboarding for a domain with a paraphrase of its contract, so the onboarding gate stops blocking. |
| **[`nova.learn_onboarding_recall`](tools/pks-and-learning/nova-learn-onboarding-recall.md)** | `domain?` | Re-reads the PKS learn-mode onboarding briefing for a domain without re-triggering the gate. |
| **[`nova.learn_promote`](tools/pks-and-learning/nova-learn-promote.md)** | `scope`, `stableIds?`, `transition?`, `dryRun?` | Evaluates and applies learning-level transitions (promotion, demotion, deprecation, revival) for the PKS entries of one domain. |
| **[`nova.learn_resolve_opportunity`](tools/pks-and-learning/nova-learn-resolve-opportunity.md)** | `opportunityId`, `verdict`, `reason?` | Closes a semantic learning opportunity that Nova raised in a tool result (`pksSemanticLearning`). |
| **[`nova.learn_suggest`](tools/pks-and-learning/nova-learn-suggest.md)** | `scope?`, `limit?` | Ranks the learning opportunities Nova has observed: patterns worth storing in the PKS and stored phenomena that are drifting. |
| **[`nova.phenomenon_apply`](tools/pks-and-learning/nova-phenomenon-apply.md)** | `scope`, `phenomenonId`, `targetId?`, `maxSteps?`, `timeoutMs?`, `observation?` | Executes a stored PKS phenomenon fast-path interaction sequence directly on the page. |
| **[`nova.pks_deprecate`](tools/pks-and-learning/nova-pks-deprecate.md)** | `scope`, `phenomenonId`, `reason?` | Marks an obsolete or broken PKS phenomenon playbook as deprecated. |
| **[`nova.pks_list`](tools/pks-and-learning/nova-pks-list.md)** | `prefix?`, `type?`, `minHealth?`, `trust?`, `serviceCategory?`, `limit?`, `offset?` | Lists the domains that have PKS knowledge, with counts, health and classification, filtered and paginated. |
| **[`nova.pks_patch`](tools/pks-and-learning/nova-pks-patch.md)** | `scope`, `phenomenonId`, `patch` | Applies partial updates or selector refinements to an existing PKS phenomenon playbook. |
| **[`nova.pks_platform_get`](tools/pks-and-learning/nova-pks-platform-get.md)** | `stableId` | Reads one stored platform entry with its pattern templates and aliases. |
| **[`nova.pks_platform_list`](tools/pks-and-learning/nova-pks-platform-list.md)** | *(none)* | Lists supported platform UI frameworks and common component models. |
| **[`nova.pks_platform_seed`](tools/pks-and-learning/nova-pks-platform-seed.md)** | `stableId`, `displayName`, `description?`, `homepageUrl?`, `patterns?`, `aliases?` | Creates or updates a platform entry (for example a cookie-consent vendor) with pattern templates and lookup aliases. |
| **[`nova.pks_upsert_hint`](tools/pks-and-learning/nova-pks-upsert-hint.md)** | `scope`, `domainHint` | Creates or updates a domain hint: CSS selectors that mark ad containers, noise regions or result items on a site. |
| **[`nova.revalidate`](tools/pks-and-learning/nova-revalidate.md)** | `targetId`, `scope?`, `limit?` | Checks stale PKS phenomena of a domain against the live page in a tab and records the outcome. |

---

## 8. Credentials & Secure Vault

Form auto-fill without leaking plaintext secrets to the LLM context.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.vault_list`](tools/vault-and-security/nova-vault-list.md)** | `site?` | Lists stored credential entries (site domain, associated usernames, and creation source) without returning passwords. |
| **[`nova.vault_get`](tools/vault-and-security/nova-vault-get.md)** | `site`, `username?` | Retrieves metadata and account identifiers for a stored vault entry, resolving username ambiguity without exposing password credentials. |
| **[`nova.vault_prepare_fill`](tools/vault-and-security/nova-vault-prepare-fill.md)** | `site`, `targetId?`, `username?` | Prepares stored credentials from the secure Vault for automated form-filling, returning an ephemeral, origin-bound, and single-use `SecretRef` token instead of the raw password string. |
| **[`nova.type_selector_secret`](tools/vault-and-security/nova-type-selector-secret.md)** | `selector`, `secretRef`, `targetId?`, `clear?` | Types a vault password into a target form field using an ephemeral `SecretRef` token, setting the value through the field's native value setter and dispatching input/change events, without exposing plaintext secrets to the agent. |
| **[`nova.secret_set`](tools/vault-and-security/nova-secret-set.md)** | `name`, `value`, `scope`, `workspaceId?`, `taskId?` | Stores an encrypted secret (such as API keys, tokens, or private credentials) into Nova's user-managed secure store with Windows DPAPI encryption. |
| **[`nova.secret_list`](tools/vault-and-security/nova-secret-list.md)** | `scope?`, `workspaceId?`, `taskId?`, `limit?`, `offset?` | Lists registered secret names, scopes, and association identifiers from Nova's user-managed keystore without disclosing secret values. |
| **[`nova.secret_delete`](tools/vault-and-security/nova-secret-delete.md)** | `name`, `scope`, `workspaceId?`, `taskId?` | Deletes an encrypted environment variable or API key secret from the DPAPI store. |
| **[`nova.vault_delete`](tools/vault-and-security/nova-vault-delete.md)** | `id` | Deletes a stored website login credential entry from the encrypted vault. |
| **[`nova.vault_set`](tools/vault-and-security/nova-vault-set.md)** | `site`, `username`, `password`, `createdBy?` | Stores or updates a username and password login credential in the encrypted vault. |

---

## 9. Terminal Workspaces & Headless CLI

Isolated pseudo-terminals (ConPTY), command execution streams, terminal dock control, and session persistence.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.terminal_open`](tools/terminal-ops/nova-terminal-open.md)** | `shell?`, `cwd?`, `cols?`, `rows?` | Opens a new agent-owned PowerShell session in an isolated working directory and returns its unique sessionId. |
| **[`nova.terminal_list`](tools/terminal-ops/nova-terminal-list.md)** | *(none)* | Lists all open agent-owned terminal sessions with status, shell type, and exit codes. |
| **[`nova.terminal_read`](tools/terminal-ops/nova-terminal-read.md)** | `sessionId`, `maxBytes?` | Reads the recent raw output tail of a terminal session scrollback buffer. |
| **[`nova.terminal_write`](tools/terminal-ops/nova-terminal-write.md)** | `sessionId`, `data` | Writes raw characters to the session stdin without appending an implicit newline. |
| **[`nova.terminal_send_key`](tools/terminal-ops/nova-terminal-send-key.md)** | `sessionId`, `key` | Sends a named control key or key combination to the active terminal session. |
| **[`nova.terminal_close`](tools/terminal-ops/nova-terminal-close.md)** | `sessionId` | Terminates an agent-owned terminal session and cleans up its process tree and temporary directory. |
| **[`nova.terminal_run_command`](tools/terminal-ops/nova-terminal-run-command.md)** | `sessionId`, `command`, `timeoutSeconds?` | Executes a single command line in an existing session and waits synchronously for its completion. |
| **[`nova.terminal_get_state`](tools/terminal-ops/nova-terminal-get-state.md)** | `sessionId` | Queries lifecycle status, working directory, and exit code for a specific session. |
| **[`nova.terminal_dock_get_state`](tools/terminal-ops/nova-terminal-dock-get-state.md)** | *(none)* | Reads the presentation state of the visible terminal dock in the Nova application shell. |
| **[`nova.terminal_dock_set_state`](tools/terminal-ops/nova-terminal-dock-set-state.md)** | `state` | Sets the visual presentation of the Nova terminal dock to expanded, collapsed, or hidden. |
| **[`nova.terminal_settings_get`](tools/terminal-ops/nova-terminal-settings-get.md)** | *(none)* | Reads terminal appearance settings and reports why ANSI colour output is enabled or disabled. |
| **[`nova.terminal_settings_set`](tools/terminal-ops/nova-terminal-settings-set.md)** | `theme?`, `fontSize?`, `programColors?` | Updates terminal appearance settings such as color theme, font size, and program color rules. |

---

## 10. Downloads Management & Queue Control

Download tracking, pause/resume, security prompt resolution, and directory management.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.downloads_list`](tools/downloads/nova-downloads-list.md)** | `id?`, `status?`, `limit?`, `offset?` | Lists recent downloads tracked by the browser with status, progress, speed, and error categorization. |
| **[`nova.downloads_wait`](tools/downloads/nova-downloads-wait.md)** | `id?`, `sinceMs?`, `timeoutMs?` | Blocks until downloads reach a terminal state (completed, failed, or cancelled) and returns disk file paths. |
| **[`nova.downloads_cancel`](tools/downloads/nova-downloads-cancel.md)** | `id` | Cancels an active in-progress or queued download by ID. |
| **[`nova.downloads_cancel_all`](tools/downloads/nova-downloads-cancel-all.md)** | *(none)* | Cancels every non-terminal download currently queued, in progress, or paused. |
| **[`nova.downloads_pause`](tools/downloads/nova-downloads-pause.md)** | `id` | Pauses an active WebView2-native download by ID. |
| **[`nova.downloads_pause_all`](tools/downloads/nova-downloads-pause-all.md)** | *(none)* | Pauses all in-progress WebView2-native downloads that support pausing. |
| **[`nova.downloads_resume`](tools/downloads/nova-downloads-resume.md)** | `id` | Resumes a paused live WebView2-native download by ID. |
| **[`nova.downloads_resume_all`](tools/downloads/nova-downloads-resume-all.md)** | *(none)* | Resumes all paused downloads whose underlying WebView2 operation supports resumption. |
| **[`nova.downloads_retry`](tools/downloads/nova-downloads-retry.md)** | `id` | Retries a failed download by re-navigating to its original URL. |
| **[`nova.downloads_open_file`](tools/downloads/nova-downloads-open-file.md)** | `id` | Opens a completed download using the operating system default application. |
| **[`nova.downloads_open_folder`](tools/downloads/nova-downloads-open-folder.md)** | `id` | Reveals the downloaded file in Windows Explorer with the item selected. |
| **[`nova.downloads_preview`](tools/downloads/nova-downloads-preview.md)** | `id` | Opens a completed download inline in a new browser tab using a secure file:// URL. |
| **[`nova.downloads_clear`](tools/downloads/nova-downloads-clear.md)** | `filter?` | Clears terminal download history from the UI and persistent storage. |
| **[`nova.downloads_auto_open_get`](tools/downloads/nova-downloads-auto-open-get.md)** | *(none)* | Retrieves the list of file extensions configured to open automatically upon download completion. |
| **[`nova.downloads_auto_open_set`](tools/downloads/nova-downloads-auto-open-set.md)** | `extensions` | Bulk-replaces the list of file extensions that auto-open with the OS default application. |

---

## 11. Desktop Notifications & Alerts

Native OS notification dispatch, unread inbox management, and per-origin notification permissions.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.notifications_send`](tools/notifications/nova-notifications-send.md)** | `sourceKind`, `title`, `body?`, `tag?`, `targetId?`, `sandboxId?`, `urgent?` | Dispatches a host-authored Windows toast notification and persists it to the Nova notification inbox. |
| **[`nova.notifications_list`](tools/notifications/nova-notifications-list.md)** | `sourceKind?`, `origin?`, `unreadOnly?`, `includeDismissed?`, `limit?`, `offset?` | Queries the Nova notification inbox with filtering by source, website origin, and read status. |
| **[`nova.notifications_get`](tools/notifications/nova-notifications-get.md)** | `notificationId` | Retrieves complete metadata and payload for a single notification by ID. |
| **[`nova.notifications_unread_count`](tools/notifications/nova-notifications-unread-count.md)** | *(none)* | Returns the count of unread, non-dismissed notifications currently in the inbox. |
| **[`nova.notifications_mark_read`](tools/notifications/nova-notifications-mark-read.md)** | `notificationId` | Marks a notification as read without dismissing it from the inbox. |
| **[`nova.notifications_dismiss`](tools/notifications/nova-notifications-dismiss.md)** | `notificationId` | Dismisses a notification, hiding it from the default inbox view. |
| **[`nova.notifications_clear`](tools/notifications/nova-notifications-clear.md)** | `sourceKind?`, `olderThanDays?` | Bulk-dismisses notifications matching source or age criteria. |
| **[`nova.notifications_open`](tools/notifications/nova-notifications-open.md)** | `notificationId` | Navigates to the originating tab, website, or resource referenced by a notification. |
| **[`nova.notifications_permissions_list`](tools/notifications/nova-notifications-permissions-list.md)** | `mode?`, `origin?`, `limit?`, `offset?` | Lists website origin notification permissions and reports the effective global default. |
| **[`nova.notifications_permission_set`](tools/notifications/nova-notifications-permission-set.md)** | `origin`, `mode` | Configures notification permission (Ask, Allow, or Deny) for a specific website origin. |
| **[`nova.notifications_permission_default_set`](tools/notifications/nova-notifications-permission-default-set.md)** | `mode` | Sets the global website notification permission default (Ask, Allow, or Deny). |

---

## 12. Device Emulation & Responsive Testing

Mobile viewport simulation, touch event emulation, user agent overriding, and dark mode toggles.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.emulation_use_device`](tools/device-emulation/nova-emulation-use-device.md)** | `device`, `targetId?` | Applies a named device preset (viewport, DPR, touch capabilities, and user agent) in a single atomic call. |
| **[`nova.emulation_set_device_metrics`](tools/device-emulation/nova-emulation-set-device-metrics.md)** | `width`, `height`, `targetId?`, `deviceScaleFactor?`, `mobile?` | Overrides the viewport dimensions, device scale factor (DPR), and mobile layout behavior for a tab. |
| **[`nova.emulation_clear_device_metrics`](tools/device-emulation/nova-emulation-clear-device-metrics.md)** | `targetId?` | Clears viewport device metrics overrides, restoring normal window-sized rendering. |
| **[`nova.emulation_set_user_agent`](tools/device-emulation/nova-emulation-set-user-agent.md)** | `userAgent`, `targetId?`, `acceptLanguage?`, `platform?` | Overrides the HTTP User-Agent header, navigator.userAgent, and client hints for a tab. |
| **[`nova.emulation_set_touch`](tools/device-emulation/nova-emulation-set-touch.md)** | `enabled`, `targetId?`, `maxTouchPoints?` | Enables or disables touch event simulation and sets the maximum touch points reported by the browser. |
| **[`nova.emulation_set_media`](tools/device-emulation/nova-emulation-set-media.md)** | `targetId?`, `colorScheme?`, `reducedMotion?`, `forcedColors?`, `contrast?`, `media?` | Emulates CSS media features like dark mode, reduced motion, high contrast, and print media. |
| **[`nova.emulation_clear_media`](tools/device-emulation/nova-emulation-clear-media.md)** | `targetId?` | Clears all emulated CSS media features, reverting to host system theme and display settings. |
| **[`nova.emulation_set_locale`](tools/device-emulation/nova-emulation-set-locale.md)** | `targetId?`, `locale?`, `timezone?`, `latitude?`, `longitude?`, `accuracy?` | Emulates browser locale, timezone, and geolocation coordinates for testing localized content. |
| **[`nova.emulation_clear_locale`](tools/device-emulation/nova-emulation-clear-locale.md)** | `targetId?` | Clears all locale, timezone, and geolocation overrides, reverting to host system settings. |
| **[`nova.emulation_set_viewport_frame`](tools/device-emulation/nova-emulation-set-viewport-frame.md)** | `enabled?`, `color?` | Configures the visual outline rendered around an emulated device viewport in the host UI. |

---

## 13. External MCP Servers & Secondary Tool Bridging

Registering, running, and dynamically calling secondary MCP servers through Nova's unified host.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.external_servers`](tools/external-mcp/nova-external-servers.md)** | *(none)* | Lists all configured external MCP servers with runtime status, health, and tool count. |
| **[`nova.external_server_add`](tools/external-mcp/nova-external-server-add.md)** | `displayName`, `transport`, `command?`, `args?`, `cwd?`, `env?`, `endpointUrl?`, `authMode?`, `bearerToken?`, `headers?`, `enabled?`, `autoConnect?`, `autoStart?`, `restartOnCrash?`, `startupTimeoutMs?` | Registers a new external MCP server with stdio, HTTP, or SSE transport. |
| **[`nova.external_server_update`](tools/external-mcp/nova-external-server-update.md)** | `serverKey`, `displayName?`, `command?`, `args?`, `cwd?`, `env?`, `endpointUrl?`, `authMode?`, `bearerToken?`, `headers?`, `enabled?`, `autoConnect?`, `autoStart?`, `restartOnCrash?`, `startupTimeoutMs?` | Updates configuration, environment variables, or transport settings of an existing server. |
| **[`nova.external_server_remove`](tools/external-mcp/nova-external-server-remove.md)** | `serverKey` | Deletes an external MCP server registration, stopping it if running. |
| **[`nova.external_server_start`](tools/external-mcp/nova-external-server-start.md)** | `serverKey` | Launches an external MCP server, runs initialize handshake, and discovers available tools. |
| **[`nova.external_server_stop`](tools/external-mcp/nova-external-server-stop.md)** | `serverKey`, `force?` | Stops a running external MCP server gracefully with force-kill fallback. |
| **[`nova.external_server_logs`](tools/external-mcp/nova-external-server-logs.md)** | `serverKey`, `lines?` | Reads recent stderr log lines captured from an external MCP server process. |
| **[`nova.external_tools`](tools/external-mcp/nova-external-tools.md)** | `serverKey`, `includeSchema?`, `refresh?` | Lists all tools available on an external MCP server, with optional full inputSchema. |
| **[`nova.external_tool_call`](tools/external-mcp/nova-external-tool-call.md)** | `serverKey`, `toolName`, `arguments?`, `timeoutMs?` | Invokes a specific tool on a connected external MCP server and returns the raw response. |
| **[`nova.external_server_import`](tools/external-mcp/nova-external-server-import.md)** | `source`, `filePath?`, `serverName?`, `autoStart?` | Imports MCP server definitions from Claude Desktop, VS Code, Claude Code, or JSON config files. |

---

## 14. Proxy Routing & Network Interception

Proxy profile management, authentication, traffic redirection, and CDP network request/response interception.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.network_intercept_add`](tools/proxy-and-network/nova-network-intercept-add.md)** | `urlPattern`, `targetId?`, `methods?`, `action?`, `errorReason?`, `status?`, `body?`, `contentType?`, `headers?`, `requestHeaders?`, `removeRequestHeaders?`, `rewriteUrl?`, `setMethod?`, `setBody?`, `responseHeaders?`, `removeResponseHeaders?`, `setResponseStatus?`, `setResponseBody?`, `delayMs?`, `ttlMs?`, `maxHits?`, `note?` | Deposits a CDP network interception rule to mock responses, inject delays, modify headers, or fail requests. |
| **[`nova.network_intercept_clear`](tools/proxy-and-network/nova-network-intercept-clear.md)** | `targetId?`, `ruleId?` | Disarms network interception rules: by rule ID, by tab ID, or globally across the entire browser. |
| **[`nova.network_intercept_list`](tools/proxy-and-network/nova-network-intercept-list.md)** | `targetId?` | Lists currently armed network interception rules with remaining hit budgets and expiration timers. |
| **[`nova.network_replay`](tools/proxy-and-network/nova-network-replay.md)** | `agentId?`, `action?`, `replayId?`, `url?`, `method?`, `headers?`, `body?`, `bodyBase64?`, `timeoutMs?`, `maxResponseBytes?`, `compareTo?`, `adoptSessionFrom?` | Targeted HTTP request repeater for replaying, editing, and comparing network payloads out-of-band. |
| **[`nova.proxy_create`](tools/proxy-and-network/nova-proxy-create.md)** | `name`, `host`, `port`, `protocol?`, `bypassList?`, `username?`, `enabled?`, `isGlobalDefault?` | Creates a new proxy profile with host, port, protocol, and optional credentials. |
| **[`nova.proxy_disconnect`](tools/proxy-and-network/nova-proxy-disconnect.md)** | `targetId` | Manually disconnects the proxy for a target scope, blocking all HTTP(S) traffic as an emergency kill switch. |
| **[`nova.proxy_list`](tools/proxy-and-network/nova-proxy-list.md)** | *(none)* | Lists all configured proxy profiles with connection settings, protocols, and sandbox bindings. |
| **[`nova.proxy_log`](tools/proxy-and-network/nova-proxy-log.md)** | `maxLines?` | Reads recent redacted proxy routing and diagnostic log entries from disk. |
| **[`nova.proxy_reconnect`](tools/proxy-and-network/nova-proxy-reconnect.md)** | `targetId` | Reconnects a disconnected proxy and verifies connectivity before unblocking network traffic. |
| **[`nova.proxy_remove`](tools/proxy-and-network/nova-proxy-remove.md)** | `profileId` | Deletes a proxy profile and resets any sandbox bindings back to the global default. |
| **[`nova.proxy_set_password`](tools/proxy-and-network/nova-proxy-set-password.md)** | `profileId`, `password?` | Stores or clears encrypted proxy authentication credentials using Windows DPAPI. |
| **[`nova.proxy_status`](tools/proxy-and-network/nova-proxy-status.md)** | `profileId?`, `targetId?` | Queries real-time connectivity status, latency, and external IP for a proxy profile. |
| **[`nova.proxy_switch`](tools/proxy-and-network/nova-proxy-switch.md)** | `profileId?`, `sandboxId?`, `mode?` | Dynamically switches the active proxy for global tabs or a specific sandbox without restarting Nova. |
| **[`nova.proxy_test`](tools/proxy-and-network/nova-proxy-test.md)** | `profileId`, `probeUrl?` | Executes an active network diagnostic probe through a proxy profile to verify connectivity and external IP. |
| **[`nova.proxy_update`](tools/proxy-and-network/nova-proxy-update.md)** | `profileId`, `name?`, `protocol?`, `host?`, `port?`, `bypassList?`, `username?`, `enabled?`, `isGlobalDefault?` | Updates host, port, protocol, or bypass list of an existing proxy profile. |
| **[`nova.tls_inspect`](tools/proxy-and-network/nova-tls-inspect.md)** | `url?`, `targetId?`, `checks?`, `checkHosts?`, `ctDomain?`, `maxCtEntries?`, `includePem?` | Inspects the TLS certificate and server configuration of one host in depth: full chain, names, purpose, validation level, protocol and cipher support, HSTS and Certificate Transparency subdomains. |

---

## 15. Site Crawler & URL Discovery Index

Broad-surface website crawling, URL indexing, sitemap verification, and discovery probes.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.crawl_start`](tools/crawler-and-discovery/nova-crawl-start.md)** | `startUrl`, `agentId?`, `targetId?`, `url?`, `maxDepth?`, `maxPages?`, `sameDomainOnly?`, `sameScopeOnly?`, `urlPattern?`, `excludePattern?`, `extractContent?`, `contentMode?`, `contentSelector?`, `excludeSelectors?`, `extractMetadata?`, `settleTimeMs?`, `pageDelayMs?`, `validateLinks?`, `maxConsecutiveErrors?`, `backoffStrategy?`, `maxBackoffMs?`, `captureScreenshots?`, `screenshotFormat?`, `screenshotQuality?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotHighlight?`, `respectRobotsTxt?`, `useSitemap?`, `parallel?`, `taskInstanceId?`, `customScript?`, `customScriptTimeoutMs?`, `crawlMode?`, `deltaMode?` | Starts a background breadth-first search (BFS) crawl from a root URL using isolated hidden WebViews. |
| **[`nova.crawl_status`](tools/crawler-and-discovery/nova-crawl-status.md)** | `crawlId`, `agentId?`, `outputDetail?` | Checks the live progress, active phase, and error metrics of a background crawl job. |
| **[`nova.crawl_results`](tools/crawler-and-discovery/nova-crawl-results.md)** | `crawlId`, `agentId?`, `offset?`, `limit?`, `filter?`, `sortBy?`, `sortOrder?`, `sinceSequence?`, `screenshotDetail?`, `outputDetail?`, `maxTextChars?`, `minConfidence?`, `summary?` | Retrieves paginated page details, extracted text, metadata, and screenshots from a crawl job. |
| **[`nova.crawl_stop`](tools/crawler-and-discovery/nova-crawl-stop.md)** | `crawlId`, `agentId?` | Requests cancellation of an active crawl job, safely draining in-flight workers. |
| **[`nova.crawl_update`](tools/crawler-and-discovery/nova-crawl-update.md)** | `crawlId`, `agentId?`, `maxPages?`, `maxDepth?`, `pageDelayMs?`, `settleTimeMs?`, `parallel?`, `burstSize?`, `burstDelayMs?`, `urlPattern?`, `excludePattern?`, `paused?`, `maxConsecutiveErrors?`, `backoffStrategy?`, `maxBackoffMs?` | Dynamically modifies parameters (rate limits, filters, depth, pauses) of an active crawl mid-flight. |
| **[`nova.crawl_verify`](tools/crawler-and-discovery/nova-crawl-verify.md)** | `urls`, `agentId?`, `targetId?`, `extractContent?`, `contentMode?`, `contentSelector?`, `excludeSelectors?`, `extractMetadata?`, `settleTimeMs?`, `pageDelayMs?`, `parallel?`, `burstSize?`, `burstDelayMs?`, `maxConsecutiveErrors?`, `backoffStrategy?`, `maxBackoffMs?`, `captureScreenshots?`, `screenshotFormat?`, `screenshotQuality?`, `screenshotMaxWidth?`, `screenshotMaxHeight?`, `screenshotHighlight?`, `taskInstanceId?`, `customScript?`, `customScriptTimeoutMs?`, `waitFor?`, `assert?`, `renderMode?`, `viewportMode?`, `readOnlyPopover?`, `research?` | Performs targeted, non-traversal verification and DOM extraction against a specific list of URLs. |
| **[`nova.crawl_history`](tools/crawler-and-discovery/nova-crawl-history.md)** | `agentId?`, `ownerAgentId?`, `scopeKey?`, `status?`, `taskInstanceId?`, `limit?` | Lists past crawl jobs and high-level summaries from the persistent crawler database. |
| **[`nova.crawl_diff`](tools/crawler-and-discovery/nova-crawl-diff.md)** | `oldCrawlId`, `newCrawlId`, `agentId?`, `includeUnchanged?`, `limit?` | Compares two completed crawls of the same site to detect added, removed, or modified pages. |
| **[`nova.crawl_links`](tools/crawler-and-discovery/nova-crawl-links.md)** | `targetId?`, `urlPattern?`, `sameDomainOnly?`, `sameScopeOnly?`, `includeText?`, `deep?` | Instantly extracts and classifies all hyperlinks from an existing active browser tab. |
| **[`nova.site_urls`](tools/crawler-and-discovery/nova-site-urls.md)** | `agentId?`, `domain?`, `scopeKey?`, `origin?`, `pathPrefix?`, `includeStale?`, `includeDead?`, `limit?` | Queries the persistent Site-URL-Index for known endpoints, utility scores, and route candidates. |
| **[`nova.site_urls_report`](tools/crawler-and-discovery/nova-site-urls-report.md)** | `reports`, `agentId?` | Reports live navigation observations (new pages, 404s, redirects) to the Site-URL-Index. |
| **[`nova.discovery_reset_scope`](tools/crawler-and-discovery/nova-discovery-reset-scope.md)** | `agentId?`, `domain?`, `scopeKey?`, `origin?` | Destructively clears all persisted crawl history, results, and URL indexes for a site scope. |
| **[`nova.site_discovery_probe`](tools/crawler-and-discovery/nova-site-discovery-probe.md)** | `url`, `forceRefresh?` | Probes a website for modern AI and MCP discovery endpoints (llms.txt, /.well-known/mcp.json, A2A). |
| **[`nova.site_discovery_get`](tools/crawler-and-discovery/nova-site-discovery-get.md)** | `domain` | Retrieves cached MCP and AI discovery probe results for a domain without network traffic. |

---

## 16. Session Tracing & DOM Event Recording

Network HAR capture, user interaction timelines, DOM change snapshots, and replay verification.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.session_record_start`](tools/session-recording/nova-session-record-start.md)** | `tabId`, `ttlMs?`, `permissionClasses?` | Initiates encrypted background recording of CDP network, DOM mutations, console logs, and user interactions on a tab. |
| **[`nova.session_record_stop`](tools/session-recording/nova-session-record-stop.md)** | `recordingId`, `reason?` | Stops an active session recording, flushes buffered events, and finalizes the encrypted artifact with a per-stream SHA-256 integrity manifest. |
| **[`nova.session_record_status`](tools/session-recording/nova-session-record-status.md)** | `recordingId` | Returns the live state, start/expiry timestamps, tab/sandbox binding, and granted permission classes of a recording. |
| **[`nova.session_record_extend`](tools/session-recording/nova-session-record-extend.md)** | `recordingId`, `additionalMs` | Extends an active recording’s time-to-live (TTL) to prevent premature expiration during long workflows. |
| **[`nova.session_record_query`](tools/session-recording/nova-session-record-query.md)** | `recordingId`, `urlMatch?`, `method?`, `mimeType?`, `statusGte?`, `statusLte?`, `sinceMs?`, `untilMs?`, `hasBody?`, `vaultMatched?`, `limit?` | Queries the complete CDP network stream of a finalized recording with rich filters (URL regex, status, headers). |
| **[`nova.session_record_get_entry`](tools/session-recording/nova-session-record-get-entry.md)** | `recordingId`, `requestId`, `includeBody?` | Retrieves the complete event timeline, headers, and decoded payload for a single CDP request ID. |
| **[`nova.session_record_events`](tools/session-recording/nova-session-record-events.md)** | `recordingId`, `stream`, `limit?` | Decrypts and streams generic event logs (console, errors, lifecycle, IndexedDB) from a recording. |
| **[`nova.session_record_interactions`](tools/session-recording/nova-session-record-interactions.md)** | `recordingId`, `source?`, `type?`, `targetSelectorMatch?`, `sinceMs?`, `untilMs?`, `limit?` | Reads the chronological interaction timeline (clicks, typing, form submits) from a recording. |
| **[`nova.session_record_snapshot_dom`](tools/session-recording/nova-session-record-snapshot-dom.md)** | `recordingId?`, `tabId?`, `selector?`, `fullPage?` | Triggers a fresh encrypted DOM snapshot on an active live recording bound to a tab. |
| **[`nova.session_record_dom_snapshot`](tools/session-recording/nova-session-record-dom-snapshot.md)** | `recordingId`, `snapshotId`, `asText?` | Retrieves and decrypts a previously stored DOM snapshot HTML payload by snapshot ID. |
| **[`nova.session_record_export`](tools/session-recording/nova-session-record-export.md)** | `recordingId` | Decodes a finalized encrypted recording to plaintext files on disk for debugging or archival. |
| **[`nova.session_record_purge`](tools/session-recording/nova-session-record-purge.md)** | `olderThanDays` | Destructively deletes finalized session recordings older than a specified day threshold. |
| **[`nova.session_reset_screenshot_budget`](tools/session-recording/nova-session-reset-screenshot-budget.md)** | *(none)* | Resets the session screenshot budget counter to allow fresh visual captures. |
| **[`nova.traces_list`](tools/session-recording/nova-traces-list.md)** | `limit?`, `status?` | Lists recent host operation traces with execution timing, phases, and outcome status for debugging. |

---

## 17. Scheduled Tasks, Cron & Workspaces

Background task automation, cron expressions, file-system watches, task workspaces, and execution logs.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.scheduled_task_create`](tools/scheduled-tasks/nova-scheduled-task-create.md)** | `displayName`, `prompt`, `intervalSeconds?`, `cronExpression?`, `timeZoneId?`, `executorKind?`, `autonomyMode?`, `command?`, `argsTemplate?`, `workingDirectory?`, `timeoutSeconds?`, `maxTurns?`, `maxBudgetUsd?`, `mcpAccess?`, `extraSystemPrompt?`, `oneShot?`, `catchUpMissed?`, `triggerNextTaskId?`, `triggerOnStatus?`, `triggerConditionKey?`, `concurrencyPolicy?`, `totalBudgetCapUsd?`, `watchPath?`, `taskProfileId?`, `workspaceId?`, `workspaceDisplayName?`, `installOnboarding?` | Creates a new scheduled task running on cron expressions, intervals, or filesystem change events. |
| **[`nova.scheduled_task_list`](tools/scheduled-tasks/nova-scheduled-task-list.md)** | *(none)* | Lists all scheduled tasks with enabled state, next run time, last result, and cumulative cost. |
| **[`nova.scheduled_task_get`](tools/scheduled-tasks/nova-scheduled-task-get.md)** | `taskId` | Retrieves full details of a scheduled task including prompt, schedule, chaining, and budget settings. |
| **[`nova.scheduled_task_update`](tools/scheduled-tasks/nova-scheduled-task-update.md)** | `taskId`, `displayName?`, `prompt?`, `intervalSeconds?`, `timeoutSeconds?`, `maxTurns?`, `maxBudgetUsd?`, `mcpAccess?`, `extraSystemPrompt?`, `catchUpMissed?`, `cronExpression?`, `timeZoneId?`, `executorKind?`, `autonomyMode?`, `command?`, `argsTemplate?`, `workingDirectory?`, `oneShot?`, `triggerNextTaskId?`, `triggerOnStatus?`, `triggerConditionKey?`, `concurrencyPolicy?`, `totalBudgetCapUsd?`, `watchPath?`, `taskProfileId?`, `workspaceId?` | Updates fields (prompt, schedule, budget, timeouts, chaining) of an existing scheduled task. |
| **[`nova.scheduled_task_delete`](tools/scheduled-tasks/nova-scheduled-task-delete.md)** | `taskId`, `cleanupWorkspace?` | Permanently deletes a scheduled task, its configuration, and associated run history. |
| **[`nova.scheduled_task_enable`](tools/scheduled-tasks/nova-scheduled-task-enable.md)** | `taskId` | Enables a paused or circuit-broken scheduled task and resets failure counters. |
| **[`nova.scheduled_task_disable`](tools/scheduled-tasks/nova-scheduled-task-disable.md)** | `taskId` | Pauses execution of a scheduled task without modifying its configuration or history. |
| **[`nova.scheduled_task_trigger`](tools/scheduled-tasks/nova-scheduled-task-trigger.md)** | `taskId`, `inputs?` | Manually triggers an immediate run of a scheduled task with optional dynamic inputs. |
| **[`nova.scheduled_task_runs`](tools/scheduled-tasks/nova-scheduled-task-runs.md)** | `taskId`, `limit?` | Retrieves the run execution history (status, duration, exit code, cost) of a scheduled task. |
| **[`nova.scheduled_task_run_output`](tools/scheduled-tasks/nova-scheduled-task-run-output.md)** | `runId`, `stream?`, `maxLines?` | Memory-safe tail reader for stdout and stderr log streams of a specific task run. |
| **[`nova.scheduled_task_run_cancel`](tools/scheduled-tasks/nova-scheduled-task-run-cancel.md)** | `runId` | Requests cancellation of an in-flight background task run asynchronously. |
| **[`nova.scheduled_task_active_runs`](tools/scheduled-tasks/nova-scheduled-task-active-runs.md)** | *(none)* | Lists all currently executing task runs across all background tasks. |
| **[`nova.scheduled_task_templates`](tools/scheduled-tasks/nova-scheduled-task-templates.md)** | *(none)* | Lists pre-built task templates for common automation scenarios (monitoring, reporting, maintenance). |
| **[`nova.scheduled_task_export`](tools/scheduled-tasks/nova-scheduled-task-export.md)** | *(none)* | Exports all scheduled task definitions as a structured array (excluding secrets and history). |
| **[`nova.scheduled_task_import`](tools/scheduled-tasks/nova-scheduled-task-import.md)** | `tasksJson`, `enable?` | Imports scheduled task definitions from a JSON array, creating fresh task IDs and isolated workspaces. |
| **[`nova.scheduled_task_secret_set`](tools/scheduled-tasks/nova-scheduled-task-secret-set.md)** | `taskId`, `key`, `value` | Stores an encrypted secret (API key, auth token) for a task using Windows DPAPI encryption. |
| **[`nova.scheduled_task_secret_list`](tools/scheduled-tasks/nova-scheduled-task-secret-list.md)** | `taskId`, `limit?`, `offset?` | Lists registered secret key names for a task without exposing plaintext secret values. |
| **[`nova.scheduled_task_var_set`](tools/scheduled-tasks/nova-scheduled-task-var-set.md)** | `taskId`, `key`, `value` | Sets a persistent key-value state variable for a task that survives across runs. |
| **[`nova.scheduled_task_var_get`](tools/scheduled-tasks/nova-scheduled-task-var-get.md)** | `taskId`, `key` | Retrieves the current value of a persistent state variable for a task. |
| **[`nova.scheduled_task_var_list`](tools/scheduled-tasks/nova-scheduled-task-var-list.md)** | `taskId`, `limit?`, `offset?`, `includeValues?` | Lists persistent variable keys and value previews configured for a task. |
| **[`nova.scheduled_task_var_delete`](tools/scheduled-tasks/nova-scheduled-task-var-delete.md)** | `taskId`, `key` | Deletes a persistent state variable from a task. |
| **[`nova.scheduled_task_workspace`](tools/scheduled-tasks/nova-scheduled-task-workspace.md)** | `taskId` | Returns the task's workspace paths, a page of its shared files, and the status of its last run. |
| **[`nova.scheduled_task_workspace_list`](tools/scheduled-tasks/nova-scheduled-task-workspace-list.md)** | `taskId`, `relativePath?`, `limit?`, `offset?` | Lists files and subdirectories located within a task’s shared workspace folder. |
| **[`nova.scheduled_task_workspace_read`](tools/scheduled-tasks/nova-scheduled-task-workspace-read.md)** | `taskId`, `relativePath` | Reads a UTF-8 text file from a task’s shared workspace folder. |
| **[`nova.scheduled_task_workspace_write`](tools/scheduled-tasks/nova-scheduled-task-workspace-write.md)** | `taskId`, `relativePath`, `content` | Atomically writes a UTF-8 text file into a task’s shared workspace folder (temp-file + rename). |

---

## 18. Connectors, Mail & File Transfer

IMAP/SMTP email client automation, EML exports, SFTP/FTP server operations, and credential access grants.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.connector_create`](tools/connectors-and-mail/nova-connector-create.md)** | `displayName`, `type`, `username?`, `password?`, `passwordFromVault?`, `authMode?`, `privateKeyPath?`, `keyPassphrase?`, `imapHost?`, `imapPort?`, `imapSecurity?`, `imapAllowInvalidCertificate?`, `signatureText?`, `signatureHtml?`, `smtpHost?`, `smtpPort?`, `smtpSecurity?`, `smtpAllowInvalidCertificate?`, `host?`, `port?`, `security?`, `allowInsecure?` | Creates an E-Mail account (IMAP/SMTP) or remote server connection (SFTP/FTP). |
| **[`nova.connector_list`](tools/connectors-and-mail/nova-connector-list.md)** | `type?` | Lists configured E-Mail accounts and remote file transfer server connections. |
| **[`nova.connector_probe`](tools/connectors-and-mail/nova-connector-probe.md)** | `profileId`, `depth?`, `includeTranscript?`, `allowInsecure?`, `unattended?` | Diagnoses a configured mail account or SFTP/FTP server: reachability, TLS, server identity, features and limits, read-only. |
| **[`nova.connector_update`](tools/connectors-and-mail/nova-connector-update.md)** | `id`, `displayName?`, `username?`, `password?`, `passwordFromVault?`, `authMode?`, `privateKeyPath?`, `keyPassphrase?`, `imapHost?`, `imapPort?`, `imapSecurity?`, `imapAllowInvalidCertificate?`, `signatureText?`, `signatureHtml?`, `smtpHost?`, `smtpPort?`, `smtpSecurity?`, `smtpAllowInvalidCertificate?`, `host?`, `port?`, `security?`, `allowInsecure?` | Updates configuration, endpoints, credentials, or signatures of an existing connection. |
| **[`nova.connector_delete`](tools/connectors-and-mail/nova-connector-delete.md)** | `id` | Deletes a connector profile, associated capability grants, and backing DPAPI secrets. |
| **[`nova.connector_grant_set`](tools/connectors-and-mail/nova-connector-grant-set.md)** | `profileId`, `capability`, `mode`, `scope?`, `allowedMailFolders?`, `allowedMailSenders?` | Sets capability access modes (ask, always, blocked) for a connector. |
| **[`nova.connector_recipient_set`](tools/connectors-and-mail/nova-connector-recipient-set.md)** | `profileId`, `recipients` | Configures recipient allow-lists for autonomous email sending without human prompts. |
| **[`nova.mail_folders`](tools/connectors-and-mail/nova-mail-folders.md)** | `profileId`, `unattended?`, `allowInsecure?` | Lists the personal IMAP folder tree with total and unread message counts. |
| **[`nova.mail_list`](tools/connectors-and-mail/nova-mail-list.md)** | `profileId`, `folder`, `query?`, `limit?`, `sinceCursor?`, `olderCursor?`, `unattended?`, `allowInsecure?` | Lists bounded message metadata (headers, dates, senders) from an exact IMAP folder. |
| **[`nova.mail_read`](tools/connectors-and-mail/nova-mail-read.md)** | `messageId`, `bodyMode?`, `unattended?`, `allowInsecure?` | Reads the sanitized body and attachment inventory of a specific email. |
| **[`nova.mail_search`](tools/connectors-and-mail/nova-mail-search.md)** | `profileId`, `query`, `folder?`, `limit?`, `unattended?`, `allowInsecure?` | Searches mail metadata across the IMAP server and local encrypted search archives. |
| **[`nova.mail_send`](tools/connectors-and-mail/nova-mail-send.md)** | `profileId`, `to`, `subject?`, `bodyText?`, `cc?`, `bcc?`, `bodyHtml?`, `priority?`, `requestReadReceipt?`, `replyTo?`, `includeSignature?`, `attachments?`, `inReplyToMessageId?`, `unattended?`, `allowInsecure?` | Sends an email with optional HTML body, CC/BCC, priority, and attachments via SMTP. |
| **[`nova.mail_draft_create`](tools/connectors-and-mail/nova-mail-draft-create.md)** | `profileId`, `to`, `subject?`, `bodyText?`, `cc?`, `bcc?`, `bodyHtml?`, `priority?`, `requestReadReceipt?`, `replyTo?`, `includeSignature?`, `inReplyToMessageId?`, `replaceDraftId?`, `unattended?`, `allowInsecure?` | Saves an email draft to the server's Drafts folder without sending. |
| **[`nova.mail_mark`](tools/connectors-and-mail/nova-mail-mark.md)** | `messageIds`, `seen?`, `flagged?`, `unattended?`, `allowInsecure?` | Updates seen and/or flagged status flags for up to 200 messages. |
| **[`nova.mail_move`](tools/connectors-and-mail/nova-mail-move.md)** | `messageIds`, `targetFolder`, `unattended?`, `allowInsecure?` | Moves up to 200 messages from one mail account to an exact IMAP destination folder. |
| **[`nova.mail_delete`](tools/connectors-and-mail/nova-mail-delete.md)** | `messageIds`, `unattended?`, `allowInsecure?` | Moves up to 200 messages into the account's Trash folder (non-permanent delete). |
| **[`nova.mail_folder_create`](tools/connectors-and-mail/nova-mail-folder-create.md)** | `profileId`, `name`, `unattended?`, `allowInsecure?` | Creates a top-level personal IMAP message folder. |
| **[`nova.mail_attachment_save`](tools/connectors-and-mail/nova-mail-attachment-save.md)** | `messageId`, `attachmentIndex`, `localPath?`, `unattended?`, `allowInsecure?` | Saves a specific email attachment to Downloads or the workspace directory. |
| **[`nova.mail_export_eml`](tools/connectors-and-mail/nova-mail-export-eml.md)** | `messageId?`, `messageIds?`, `format?`, `localPath?`, `onExists?`, `unattended?`, `allowInsecure?` | Exports raw RFC 822 EML files preserving complete MIME headers and original parts. |
| **[`nova.mail_backup_start`](tools/connectors-and-mail/nova-mail-backup-start.md)** | `profileId`, `mode?`, `folders?`, `since?`, `localPath?`, `unattended?`, `allowInsecure?` | Launches a background job to back up an entire mail account or specific folders. |
| **[`nova.mail_backup_status`](tools/connectors-and-mail/nova-mail-backup-status.md)** | `jobId?`, `profileId?`, `acknowledge?` | Reports progress, downloaded message counts, and active phase of a mail backup job. |
| **[`nova.mail_backup_stop`](tools/connectors-and-mail/nova-mail-backup-stop.md)** | `jobId` | Gracefully stops an in-flight mail backup job, committing all downloaded messages. |
| **[`nova.sftp_list`](tools/connectors-and-mail/nova-sftp-list.md)** | `profileId`, `remotePath?`, `maxEntries?`, `unattended?` | Lists remote directory entries or inspects file metadata through an SFTP connector. |
| **[`nova.sftp_get`](tools/connectors-and-mail/nova-sftp-get.md)** | `profileId`, `localPath`, `remotePath`, `recursive?`, `overwrite?`, `maxFiles?`, `maxBytes?`, `wait?`, `resumeJobId?`, `unattended?` | Downloads a remote file or directory tree of any size over SFTP into Downloads or the workspace, as a resumable background job. |
| **[`nova.sftp_put`](tools/connectors-and-mail/nova-sftp-put.md)** | `profileId`, `localPath`, `remotePath`, `recursive?`, `overwrite?`, `maxFiles?`, `maxBytes?`, `wait?`, `resumeJobId?`, `unattended?` | Uploads a local file or directory tree of any size over SFTP, as a resumable background job. |
| **[`nova.sftp_rename`](tools/connectors-and-mail/nova-sftp-rename.md)** | `profileId`, `remotePath`, `destinationRemotePath`, `overwrite?`, `unattended?` | Renames or moves a remote file or directory over SFTP. |
| **[`nova.ssh_run`](tools/connectors-and-mail/nova-ssh-run.md)** | `profileId`, `command?`, `commands?`, `commandTimeoutSeconds?`, `overallTimeoutSeconds?`, `stopOnError?`, `expectedExitCodes?`, `maxOutputBytes?`, `stdin?`, `unattended?` | Runs shell commands on the server of an SSH/SFTP connection and reports exit status, output and timing honestly. |
| **[`nova.sftp_transfer_status`](tools/connectors-and-mail/nova-sftp-transfer-status.md)** | `jobId?`, `profileId?` | Reports progress and result of background SFTP transfers started by `nova.sftp_get` or `nova.sftp_put`. |
| **[`nova.sftp_transfer_stop`](tools/connectors-and-mail/nova-sftp-transfer-stop.md)** | `jobId` | Stops a running background SFTP transfer softly and keeps everything for a resume. |
| **[`nova.sftp_delete`](tools/connectors-and-mail/nova-sftp-delete.md)** | `profileId`, `remotePath`, `recursive?`, `maxFiles?`, `maxBytes?`, `unattended?` | Deletes a remote file, empty directory, or bounded directory tree over SFTP. |
| **[`nova.ftp_list`](tools/connectors-and-mail/nova-ftp-list.md)** | `profileId`, `remotePath?`, `maxEntries?`, `unattended?`, `allowInsecure?` | Lists remote directory entries or inspects file metadata through an FTP/FTPS connector. |
| **[`nova.ftp_get`](tools/connectors-and-mail/nova-ftp-get.md)** | `profileId`, `localPath`, `remotePath`, `overwrite?`, `maxBytes?`, `wait?`, `resumeJobId?`, `unattended?`, `allowInsecure?` | Downloads a remote regular file over FTP/FTPS into Downloads or the workspace. |
| **[`nova.ftp_put`](tools/connectors-and-mail/nova-ftp-put.md)** | `profileId`, `localPath`, `remotePath`, `overwrite?`, `maxBytes?`, `wait?`, `resumeJobId?`, `unattended?`, `allowInsecure?` | Uploads a local regular file over FTP/FTPS to a remote server. |
| **[`nova.ftp_rename`](tools/connectors-and-mail/nova-ftp-rename.md)** | `profileId`, `remotePath`, `destinationRemotePath`, `overwrite?`, `unattended?`, `allowInsecure?` | Renames or moves a remote file or directory on an FTP/FTPS server. |
| **[`nova.ftp_transfer_status`](tools/connectors-and-mail/nova-ftp-transfer-status.md)** | `jobId?`, `profileId?` | Reports progress and result of background FTP transfers started by `nova.ftp_get` or `nova.ftp_put`. |
| **[`nova.ftp_transfer_stop`](tools/connectors-and-mail/nova-ftp-transfer-stop.md)** | `jobId` | Stops a running background FTP transfer softly and keeps everything for a resume. |
| **[`nova.ftp_delete`](tools/connectors-and-mail/nova-ftp-delete.md)** | `profileId`, `remotePath`, `unattended?`, `allowInsecure?` | Deletes a remote regular file or empty directory on an FTP/FTPS server. |

---

## 19. Media Intelligence & Whisper Speech-to-Text

In-browser audio/video recording, local OpenAI Whisper transcription, model management, and camera/mic permissions.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.hardware_diagnostics_start`](tools/media-and-transcription/nova-hardware-diagnostics-start.md)** | `kind`, `targetId?` | Initiates in-page hardware diagnostic loop for camera, microphone, or audio speaker output. |
| **[`nova.hardware_diagnostics_state`](tools/media-and-transcription/nova-hardware-diagnostics-state.md)** | `targetId?` | Returns current live hardware diagnostic metrics including microphone audio levels and peak decibels. |
| **[`nova.hardware_diagnostics_stop`](tools/media-and-transcription/nova-hardware-diagnostics-stop.md)** | `targetId?`, `kind?`, `reason?` | Stops in-page hardware diagnostics and releases active camera, microphone, or speaker handles. |
| **[`nova.media_activity_status`](tools/media-and-transcription/nova-media-activity-status.md)** | *(none)* | Returns an O(1) instant snapshot of currently active camera, microphone, and screen-sharing streams. |
| **[`nova.media_activity_audit`](tools/media-and-transcription/nova-media-activity-audit.md)** | `kind?`, `limit?` | Retrieves an audit trail of stored media permissions joined with recent decision records per origin. |
| **[`nova.media_activity_delta`](tools/media-and-transcription/nova-media-activity-delta.md)** | `sinceSequence?`, `limit?` | Performs an incremental read of the in-memory media permission activity ring buffer. |
| **[`nova.media_device_preferences_list`](tools/media-and-transcription/nova-media-device-preferences-list.md)** | `origin?` | Lists stored per-site preferred device IDs (camera, microphone, speaker). |
| **[`nova.media_file_info`](tools/media-and-transcription/nova-media-file-info.md)** | `path` | Identifies a local media file's container and duration from its header, without decoding it. |
| **[`nova.media_permission_activity_list`](tools/media-and-transcription/nova-media-permission-activity-list.md)** | `limit?`, `origin?` | Reads recent entries from the in-memory ring buffer of camera, microphone, speaker, screen-share, and geolocation permission decisions. |
| **[`nova.media_permission_get`](tools/media-and-transcription/nova-media-permission-get.md)** | `origin`, `requestingOrigin?` | Reads the effective and stored media permissions for a specific web origin. |
| **[`nova.media_permission_set`](tools/media-and-transcription/nova-media-permission-set.md)** | `origin`, `requestingOrigin?`, `camera?`, `microphone?`, `speaker?`, `screenCapture?`, `geolocation?`, `lifetime?`, `clearAll?` | Sets or clears persistent or session-based camera, mic, speaker, and geolocation permissions. |
| **[`nova.media_permissions_clear_session_grants`](tools/media-and-transcription/nova-media-permissions-clear-session-grants.md)** | *(none)* | Drops all temporary session permissions and halts any live media tracks relying on them. |
| **[`nova.media_permissions_list`](tools/media-and-transcription/nova-media-permissions-list.md)** | `axis?`, `mode?`, `origin?`, `limit?`, `offset?` | Lists all stored per-origin permission overrides along with global default policies. |
| **[`nova.media_status`](tools/media-and-transcription/nova-media-status.md)** | `targetId?` | Inspects the first `<video>` or `<audio>` element on a page: playback state, position, and why it may have stopped. |
| **[`nova.media_stop_all`](tools/media-and-transcription/nova-media-stop-all.md)** | `scope?`, `origin?` | Emergency kill switch terminating all active camera, microphone, and screen-sharing tracks browser-wide. |
| **[`nova.media_capture_start`](tools/media-and-transcription/nova-media-capture-start.md)** | `targetId?`, `saveDir?`, `fileName?`, `maxBytes?`, `reload?`, `source?` | Starts streaming capture of live audio/video playing in a tab (Media Source Extensions streams and WebAudio playback). |
| **[`nova.media_capture_status`](tools/media-and-transcription/nova-media-capture-status.md)** | `targetId?` | Reports progress, elapsed time, and bytes written for an active in-tab media capture. |
| **[`nova.media_capture_stop`](tools/media-and-transcription/nova-media-capture-stop.md)** | `targetId?` | Stops in-tab media capture, flushes pending segments, closes the per-track files, and returns their paths. |
| **[`nova.media_transcribe_models`](tools/media-and-transcription/nova-media-transcribe-models.md)** | *(none)* | Lists known Whisper speech models, installation statuses, and machine CPU/AVX2 capabilities. |
| **[`nova.media_transcribe_model_install`](tools/media-and-transcription/nova-media-transcribe-model-install.md)** | `modelId?`, `path?` | Downloads a Whisper speech model or adopts an existing local GGML model file. |
| **[`nova.media_transcribe_model_remove`](tools/media-and-transcription/nova-media-transcribe-model-remove.md)** | `fileName` | Deletes an installed speech model file to reclaim disk space or prepare for re-download. |
| **[`nova.media_transcribe_start`](tools/media-and-transcription/nova-media-transcribe-start.md)** | `path`, `language?`, `model?`, `waitMs?` | Transcribes local audio or video files into text entirely on-device using local Whisper.cpp. |
| **[`nova.media_transcribe_status`](tools/media-and-transcription/nova-media-transcribe-status.md)** | `jobId`, `includeText?` | Reports progress, elapsed percentage, and recognized text segments of an active transcription. |
| **[`nova.media_transcribe_stop`](tools/media-and-transcription/nova-media-transcribe-stop.md)** | `jobId` | Stops an in-flight transcription job and returns recognized text segments up to the cancellation point. |

---

## 20. Site Data, Fingerprinting & Sandboxes

Cookie jars, localStorage/sessionStorage, cache purging, browser fingerprint spoofing, and sandbox isolation.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.cookie_list`](tools/site-data-and-identity/nova-cookie-list.md)** | `targetId`, `uri?`, `nameFilter?`, `domainFilter?`, `includeValues?`, `maxEntries?`, `cursor?` | Lists cookies for the target tab's profile with metadata (domain, path, flags, expiry). |
| **[`nova.cookie_set`](tools/site-data-and-identity/nova-cookie-set.md)** | `targetId`, `name`, `value`, `domain`, `path?`, `expires?`, `httpOnly?`, `secure?`, `sameSite?`, `dryRun?` | Sets or updates a cookie in the target sandbox profile's cookie jar. |
| **[`nova.cookie_delete`](tools/site-data-and-identity/nova-cookie-delete.md)** | `targetId`, `cookieId?`, `name?`, `domain?`, `path?`, `dryRun?` | Deletes a specific cookie by cookieId or by name, domain, and path tuple. |
| **[`nova.cookie_clear`](tools/site-data-and-identity/nova-cookie-clear.md)** | `targetId`, `domain?` | Clears cookies across the target profile, with optional domain filtering. |
| **[`nova.storage_inspect`](tools/site-data-and-identity/nova-storage-inspect.md)** | `targetId`, `storageType`, `keyFilter?`, `includeValues?`, `valueMaxChars?`, `maxEntries?` | Reads localStorage or sessionStorage key-value pairs for the target page. |
| **[`nova.storage_set`](tools/site-data-and-identity/nova-storage-set.md)** | `targetId`, `storageType`, `key`, `value` | Sets a key-value pair in localStorage or sessionStorage for the target page. |
| **[`nova.storage_delete`](tools/site-data-and-identity/nova-storage-delete.md)** | `targetId`, `storageType`, `key` | Deletes a key from localStorage or sessionStorage for the target page. |
| **[`nova.cache_clear`](tools/site-data-and-identity/nova-cache-clear.md)** | `targetId`, `dataTypes` | Clears selected browsing data (cache, cookies, storage, service workers, or history) for the target profile. |
| **[`nova.fingerprint_get`](tools/site-data-and-identity/nova-fingerprint-get.md)** | `sandboxId?`, `tabId?` | Reads the active browser fingerprint protection level (global, sandbox, or tab override). |
| **[`nova.fingerprint_set_global`](tools/site-data-and-identity/nova-fingerprint-set-global.md)** | `level` | Sets the global browser fingerprint protection level across all sandboxes. |
| **[`nova.fingerprint_set_sandbox`](tools/site-data-and-identity/nova-fingerprint-set-sandbox.md)** | `sandboxId`, `level` | Sets or clears the per-sandbox fingerprint protection override. |
| **[`nova.fingerprint_set_tab`](tools/site-data-and-identity/nova-fingerprint-set-tab.md)** | `tabId`, `level` | Sets an ephemeral per-tab fingerprint protection override that expires on tab close. |
| **[`nova.identity_get`](tools/site-data-and-identity/nova-identity-get.md)** | *(none)* | Reads the active browser identity profile, spoofed User-Agent, and client hints. |
| **[`nova.identity_presets`](tools/site-data-and-identity/nova-identity-presets.md)** | *(none)* | Lists available browser identity presets and selectable browser engine versions. |
| **[`nova.identity_set`](tools/site-data-and-identity/nova-identity-set.md)** | `preset?`, `version?`, `customUserAgent?` | Configures and persists a new browser identity profile (preset + version/custom UA). |
| **[`nova.resolve_sandbox`](tools/site-data-and-identity/nova-resolve-sandbox.md)** | `intentKey`, `serviceHint?`, `accountHint?` | Resolves the best matching sandbox container for a given workflow intent. |
| **[`nova.sandbox_context`](tools/site-data-and-identity/nova-sandbox-context.md)** | `targetId` | Returns detailed identity, cookie jar bounds, and context metadata for a specific sandbox. |
| **[`nova.sandbox_create`](tools/site-data-and-identity/nova-sandbox-create.md)** | `name?`, `color?`, `startUrl?`, `purpose?`, `accountLabel?`, `aliases?`, `preferredFor?` | Creates a new isolated sandbox profile with dedicated storage, cookies, and cache. |
| **[`nova.sandbox_update`](tools/site-data-and-identity/nova-sandbox-update.md)** | `sandboxId`, `name?`, `color?`, `startUrl?`, `purpose?`, `accountLabel?`, `aliases?`, `preferredFor?`, `isPaused?` | Updates configuration, display name, color tag, or purpose of an existing sandbox. |
| **[`nova.sandbox_delete`](tools/site-data-and-identity/nova-sandbox-delete.md)** | `sandboxId`, `confirm` | Permanently removes a sandbox profile and deletes its storage, cookies, and cache. |
| **[`nova.site_mcp_inspect`](tools/site-data-and-identity/nova-site-mcp-inspect.md)** | `domain` | Inspects a discovered MCP server from cached discovery metadata (identity, transport, auth status). |
| **[`nova.site_mcp_connect_request`](tools/site-data-and-identity/nova-site-mcp-connect-request.md)** | `domain` | Requests an authenticated OAuth 2.1 connection to a website's discovered MCP server. |
| **[`nova.site_permissions_reset_origin`](tools/site-data-and-identity/nova-site-permissions-reset-origin.md)** | `origin` | One-click reset of all stored permissions (media, notifications, geolocation) for an origin. |

---

## 21. Episodic Task Memory & Guidance

Task instance tracking, guidance logs, coverage scans, surface exploration, and operator domain notes.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.board_contribute`](tools/task-memory/nova-board-contribute.md)** | `kind`, `text`, `anchor`, `idempotencyKey`, `topicId?`, `openNew?`, `hypothesis?`, `evidenceRefs?` | Opens a new Agent Knowledge Board topic or appends an evidence-bound research contribution. |
| **[`nova.board_get`](tools/task-memory/nova-board-get.md)** | `topicId?`, `anchor?`, `blind?`, `limit?`, `deliveryId?`, `irrelevant?` | Reads an Agent Knowledge Board laboratory topic by ID or exact structured anchor. |
| **[`nova.coverage_scan`](tools/task-memory/nova-coverage-scan.md)** | `scanId`, `targetId?`, `scopeOptions?` | Runs a server-registered scan script on a tab and returns trust-checked coverage evidence for a Task URL Coverage unit. |
| **[`nova.domain_note`](tools/task-memory/nova-domain-note.md)** | `domain`, `key`, `value`, `enforcement?`, `repeatMinutes?`, `repeatToolCalls?`, `sandboxId?`, `sandboxRef?` | Stores or updates a domain-scoped operational note automatically surfaced during navigation. |
| **[`nova.domain_note_ack`](tools/task-memory/nova-domain-note-ack.md)** | `domain`, `key`, `targetId?` | Explicitly acknowledges a MUST-read domain note block to unblock subsequent tool calls. |
| **[`nova.domain_note_delete`](tools/task-memory/nova-domain-note-delete.md)** | `domain`, `key`, `scope?`, `sandboxId?`, `sandboxRef?` | Deletes a domain note by domain name and key. |
| **[`nova.domain_notes_list`](tools/task-memory/nova-domain-notes-list.md)** | `domain`, `scope?`, `sandboxId?`, `sandboxRef?` | Lists all stored procedural notes and operator instructions for a specific domain. |
| **[`nova.explore_surface`](tools/task-memory/nova-explore-surface.md)** | `mode`, `targetId`, `executionSurface`, `guardProfile`, `agentId?`, `expectedUrl?`, `routeId?`, `stability?`, `discover?`, `activate?`, `close?`, `hover?` | Discovers interactive UI triggers (buttons, tabs, accordions) and activates them to reveal hidden DOM. |
| **[`nova.goal_register`](tools/task-memory/nova-goal-register.md)** | `op`, `targetId?`, `goalId?`, `summary?`, `mode?`, `preconditions?`, `preconditionsJson?`, `ownerAgentId?`, `ownerAgent?`, `sidecarSessionId?`, `ownerSession?`, `leaseMs?`, `leaseTimeoutMs?`, `steps?`, `includeSteps?`, `includeEvents?`, `eventsLimit?`, `state?`, `content?`, `source?` | Manages closed-loop task goals, verifying step advancement and milestone criteria. |
| **[`nova.memory_add_candidate`](tools/task-memory/nova-memory-add-candidate.md)** | `targetId`, `component`, `claim`, `agentId?`, `status?`, `confidence?` | Proposes a lightweight candidate memory claim for the currently claimed task and tab. |
| **[`nova.memory_forget`](tools/task-memory/nova-memory-forget.md)** | `domain?`, `memoryId?`, `memoryType?`, `all?` | Deletes browsing memories matching domain, memoryType, or text query filters. |
| **[`nova.memory_note`](tools/task-memory/nova-memory-note.md)** | `content`, `memoryType?`, `domain?`, `urlPattern?` | Saves a persistent browsing memory (user preference, workflow hint, domain context). |
| **[`nova.memory_recall`](tools/task-memory/nova-memory-recall.md)** | `domain?`, `query?`, `memoryType?`, `limit?`, `includeExpired?` | Recalls browsing memories and stored preferences for a domain or across all sites. |
| **[`nova.memory_stats`](tools/task-memory/nova-memory-stats.md)** | `windowHours?`, `topComponents?`, `maxSkipReasons?`, `topRoutes?`, `topHosts?`, `topSelectors?`, `componentFilter?` | Reports memory engine metrics, commit rates, verification health, and outbox queues. |
| **[`nova.operator_notes_delete`](tools/task-memory/nova-operator-notes-delete.md)** | `id` | Deletes an operator note by unique ID. |
| **[`nova.operator_notes_list`](tools/task-memory/nova-operator-notes-list.md)** | `offset?`, `limit?`, `scope?`, `sandboxId?`, `sandboxRef?` | Lists all persistent operator notes with tags and sandbox scopes. |
| **[`nova.operator_notes_query`](tools/task-memory/nova-operator-notes-query.md)** | `keywords`, `minScore?`, `limit?`, `scope?`, `sandboxId?`, `sandboxRef?` | Queries operator notes by keywords with tag-intersection and TF-IDF relevance scoring. |
| **[`nova.operator_notes_store`](tools/task-memory/nova-operator-notes-store.md)** | `content`, `tags`, `category?`, `source?`, `id?`, `sandboxId?`, `sandboxRef?` | Stores or updates a persistent operator note with search tags and category. |
| **[`nova.task_guidance_log_add`](tools/task-memory/nova-task-guidance-log-add.md)** | `guidanceKind`, `sourceKind`, `profileId?`, `instanceId?`, `payload?`, `sourceRef?` | Logs a guidance observation or proposal without directly mutating task profiles. |
| **[`nova.task_guidance_logs`](tools/task-memory/nova-task-guidance-logs.md)** | `profileId?`, `instanceId?`, `guidanceKind?`, `status?`, `limit?` | Lists guidance log entries filtered by profile, domain, or guidance kind. |
| **[`nova.task_instance_abort`](tools/task-memory/nova-task-instance-abort.md)** | `instanceId`, `expectedInstanceRev`, `clientEventId`, `reason`, `outcome?` | Ends a task instance without meeting completion conditions (site offline, unsolvable error). |
| **[`nova.task_instance_complete`](tools/task-memory/nova-task-instance-complete.md)** | `instanceId`, `expectedInstanceRev`, `clientEventId`, `note?`, `completionNote?`, `evidenceReport?` | Requests server evaluation and completion for an episodic task instance. |
| **[`nova.task_instance_create`](tools/task-memory/nova-task-instance-create.md)** | `profileId?`, `adHocContext?`, `targetUrl?`, `currentScope?`, `overrides?`, `agentId?`, `declaredTaskKind?`, `unitSource?` | Creates a new episodic task instance from a profile or ad-hoc context with snapshot state. |
| **[`nova.task_instance_get`](tools/task-memory/nova-task-instance-get.md)** | `instanceId`, `includePendingUnits?`, `pendingUnitsLimit?`, `includeDiscoveredUnitsPreview?`, `discoveredUnitsPreviewLimit?`, `includeRecentEvents?`, `recentEventLimit?` | Loads a task instance snapshot for session-crossing resume and progress inspection. |
| **[`nova.task_instance_progress`](tools/task-memory/nova-task-instance-progress.md)** | `instanceId`, `expectedInstanceRev`, `clientEventId`, `discoveredUnits?`, `unitUpdates?`, `findings?`, `mandatoryCheckUpdates?`, `resumeStateDelta?`, `setDiscoveryState?`, `note?` | Commits progress deltas, completed work units, and observations to a task instance. |
| **[`nova.task_instance_reconcile_coverage`](tools/task-memory/nova-task-instance-reconcile-coverage.md)** | `instanceId`, `dryRun?`, `observationCutoff?` | Replays an instance’s observation log against the unit table to propose discovered-to-checked upgrades. |
| **[`nova.task_instance_verify`](tools/task-memory/nova-task-instance-verify.md)** | `instanceId` | Retrieves the completion-gate state and, if the task profile defines one, the verification contract steps required for task completion. |
| **[`nova.task_match`](tools/task-memory/nova-task-match.md)** | `taskDescription`, `taskType?`, `domain?`, `platform?`, `targetUrl?`, `currentScope?` | Finds the best matching task profiles for a task description with score breakdowns. |
| **[`nova.task_profile_get`](tools/task-memory/nova-task-profile-get.md)** | `profileId` | Retrieves full details of a task profile: guidance, mandatory checks, and completion conditions. |
| **[`nova.task_profile_upsert`](tools/task-memory/nova-task-profile-upsert.md)** | `taskType`, `displayName`, `goal`, `profileId?`, `expectedContentRev?`, `domain?`, `platform?`, `stableGuidance?`, `mandatoryChecks?`, `completionCondition?`, `knownExceptions?`, `confidence?`, `sourceInstanceId?` | Creates or updates a task profile with semantic content revision tracking. |
| **[`nova.task_profiles`](tools/task-memory/nova-task-profiles.md)** | `taskType?`, `domain?`, `platform?`, `includeArchived?`, `limit?` | Lists known task profiles, optionally filtered by taskType, domain, or platform. |
| **[`nova.task_promote_guidance`](tools/task-memory/nova-task-promote-guidance.md)** | `guidanceLogId`, `profileId` | Explicitly promotes a guidance log entry into a profile’s stable guidance. |
| **[`nova.task_promotion_candidates`](tools/task-memory/nova-task-promotion-candidates.md)** | `profileId`, `threshold?` | Lists guidance log entries and override patterns that are candidates for profile promotion. |
| **[`nova.task_search`](tools/task-memory/nova-task-search.md)** | `query`, `domain?`, `platform?`, `taskType?`, `limit?` | Searches for matching task profiles by free-text query with keyword ranking. |

---

## 22. App Shell, Dialogs & DevTools

WinUI window controls, native OS dialog handling, DevTools panels, setup wizard, and onboarding injection.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.agent_activity_summary`](tools/app-shell-and-ui/nova-agent-activity-summary.md)** | `agentId?`, `sinceMinutes?` | Returns a per-agent summary of this session's MCP tool calls: call counts, tab targets, and failure reason codes. |
| **[`nova.app_info`](tools/app-shell-and-ui/nova-app-info.md)** | *(none)* | Returns runtime environment metadata: app version, WebView2/OS runtime info, MCP endpoint, and storage paths. |
| **[`nova.app_quit`](tools/app-shell-and-ui/nova-app-quit.md)** | `force?`, `reason?` | Gracefully terminates the Nova host application process and all child WebView2 runtimes. |
| **[`nova.bookmarks_folder_create`](tools/app-shell-and-ui/nova-bookmarks-folder-create.md)** | `name`, `parentId?` | Creates a hierarchical folder in the browser bookmark collection. |
| **[`nova.bookmarks_folder_delete`](tools/app-shell-and-ui/nova-bookmarks-folder-delete.md)** | `id`, `mode?` | Deletes a bookmark folder and either moves its contents to the root or deletes them with it. |
| **[`nova.bookmarks_folder_rename`](tools/app-shell-and-ui/nova-bookmarks-folder-rename.md)** | `id`, `name` | Renames an existing bookmark folder. |
| **[`nova.bookmarks_folders_list`](tools/app-shell-and-ui/nova-bookmarks-folders-list.md)** | *(none)* | Lists all bookmark folders with hierarchical parent-child relationships and depths. |
| **[`nova.cdp`](tools/app-shell-and-ui/nova-cdp.md)** | `method`, `targetId?`, `params?`, `maxChars?` | Executes a raw Chrome DevTools Protocol (CDP) method directly on the target WebView2 instance. |
| **[`nova.clipboard_read`](tools/app-shell-and-ui/nova-clipboard-read.md)** | *(none)* | Reads the current plain text contents from the Windows OS system clipboard. |
| **[`nova.clipboard_write`](tools/app-shell-and-ui/nova-clipboard-write.md)** | `text` | Writes plain text to the Windows OS system clipboard. |
| **[`nova.create_dump`](tools/app-shell-and-ui/nova-create-dump.md)** | `targetId?`, `mode?` | Writes a diagnostic dump of a browser tab (screenshot, DOM, page info, and in full mode MHTML and resources) to a folder on disk. |
| **[`nova.devtools_open`](tools/app-shell-and-ui/nova-devtools-open.md)** | `targetId?`, `mode?` | Opens the Chromium DevTools inspection window for a specified browser tab. |
| **[`nova.devtools_select_panel`](tools/app-shell-and-ui/nova-devtools-select-panel.md)** | `panel`, `targetId?` | Dispatches the keyboard shortcut for a DevTools panel (Console, Elements, Network, Sources, ...) in an already-open DevTools window. |
| **[`nova.favorites_add`](tools/app-shell-and-ui/nova-favorites-add.md)** | `url`, `title?`, `folderId?` | Adds a URL to the browser favorites collection with optional title and target folder. |
| **[`nova.favorites_list`](tools/app-shell-and-ui/nova-favorites-list.md)** | `query?`, `folderId?`, `maxResults?` | Lists all saved browser favorites. |
| **[`nova.favorites_move`](tools/app-shell-and-ui/nova-favorites-move.md)** | `id?`, `url?`, `folderId?` | Moves a bookmark favorite into a different folder or to the root collection. |
| **[`nova.favorites_open`](tools/app-shell-and-ui/nova-favorites-open.md)** | `url`, `openInNewTab?` | Opens a saved favorite in the current or a new browser tab. |
| **[`nova.favorites_remove`](tools/app-shell-and-ui/nova-favorites-remove.md)** | `id?`, `url?` | Removes a saved favorite by its id or URL. |
| **[`nova.get_instructions`](tools/app-shell-and-ui/nova-get-instructions.md)** | `mode?`, `scope?`, `targetId?`, `agentId?`, `domain?`, `scopeDomain?`, `domainScope?`, `taskKeywords?`, `detail?` | Retrieves the complete Nova AI operational contract, conventions, and agent guidelines. |
| **[`nova.get_onboarding`](tools/app-shell-and-ui/nova-get-onboarding.md)** | *(none)* | Returns a manual edit plan — reference file contents and marker-block edits — for onboarding an agent to Nova's MCP tools, as an alternative to the one-call `nova.install_onboarding`. |
| **[`nova.grep_resources`](tools/app-shell-and-ui/nova-grep-resources.md)** | `pattern`, `targetId?`, `source?`, `types?`, `caseSensitive?`, `regex?`, `maxItems?`, `maxResourceChars?`, `maxMatches?`, `contextChars?`, `maxChars?` | Searches the text of a tab's loaded resources (scripts, stylesheets, documents) for literal text or a regex. |
| **[`nova.install_onboarding`](tools/app-shell-and-ui/nova-install-onboarding.md)** | `projectRoot`, `confirmNewLocation?` | Writes Nova's reference files and a Nova block in the project's agent instruction file into a project directory. |
| **[`nova.list_resources`](tools/app-shell-and-ui/nova-list-resources.md)** | `targetId?`, `source?`, `types?`, `maxItems?` | Lists all network resources (scripts, stylesheets, frames, images) loaded by the target tab. |
| **[`nova.mcp_transport_log`](tools/app-shell-and-ui/nova-mcp-transport-log.md)** | `run?`, `startLine?`, `maxLines?`, `contains?`, `caseSensitive?` | Reads recent redacted entries from Nova's internal MCP JSON-RPC transport log. |
| **[`nova.ok_observe`](tools/app-shell-and-ui/nova-ok-observe.md)** | `claims`, `targetId?`, `perceptionId?` | Records structured Operational Knowledge (OK) claims about the service open in a tab, such as login state or active model. |
| **[`nova.ok_signal_schema`](tools/app-shell-and-ui/nova-ok-signal-schema.md)** | `namespace?`, `includeDeprecated?`, `maxEntries?` | Lists the canonical Operational Knowledge signal keys accepted by nova.ok_observe. |
| **[`nova.permission_center_get`](tools/app-shell-and-ui/nova-permission-center-get.md)** | *(none)* | Retrieves the global default permission modes for camera, microphone, speaker, and geolocation, plus the detected hardware devices. |
| **[`nova.permission_center_set`](tools/app-shell-and-ui/nova-permission-center-set.md)** | `cameraPermissionMode?`, `microphonePermissionMode?`, `speakerPermissionMode?`, `geolocationPermissionMode?`, `preferredCameraDeviceId?`, `preferredMicrophoneDeviceId?`, `preferredSpeakerDeviceId?`, `clearPreferredDevices?`, `validateDeviceIds?` | Sets the global Permission Center defaults for camera, microphone, speaker and location, and the preferred media devices. |
| **[`nova.permission_prompt`](tools/app-shell-and-ui/nova-permission-prompt.md)** | `tool_name`, `description`, `schemaVersion?`, `risk_level?` | Asks the Nova operator to approve or deny an action that an agent wants to run. |
| **[`nova.read_resource`](tools/app-shell-and-ui/nova-read-resource.md)** | `url`, `targetId?`, `frameId?`, `maxChars?`, `maxBytes?`, `charOffset?` | Fetches the raw text content of a loaded web resource by its URL. |
| **[`nova.read_screenshot_resource`](tools/app-shell-and-ui/nova-read-screenshot-resource.md)** | `uri`, `maxBytes?` | Reads a screenshot resource URI (`nova://screenshot/...`) returned by a capture tool and returns its image bytes as base64. |
| **[`nova.reference_doc_read`](tools/app-shell-and-ui/nova-reference-doc-read.md)** | `docId`, `cursor?`, `maxChars?` | Reads the complete text content of an allowlisted internal Nova reference document. |
| **[`nova.reference_docs_list`](tools/app-shell-and-ui/nova-reference-docs-list.md)** | *(none)* | Lists all internal Nova reference documents available for in-session reading. |
| **[`nova.setup_status`](tools/app-shell-and-ui/nova-setup-status.md)** | *(none)* | Reports the connection and configuration health of AI agent runtimes on the host machine. |
| **[`nova.setup_wizard_open`](tools/app-shell-and-ui/nova-setup-wizard-open.md)** | *(none)* | Opens Nova's guided connection setup wizard dialog in the graphical user interface. |
| **[`nova.tools_bundle`](tools/app-shell-and-ui/nova-tools-bundle.md)** | `bundle?`, `toolName?`, `query?`, `maxResults?`, `includeDescriptions?`, `includeInputSchema?`, `includeUnavailable?`, `includeCatalog?` | Discovers, searches, and activates curated MCP tool capability bundles or queries tools by natural language. |
| **[`nova.ui_auth_prompt_resolve`](tools/app-shell-and-ui/nova-ui-auth-prompt-resolve.md)** | `decision`, `username?` | Answers Nova's HTTP sign-in dialog with a stored vault entry, or cancels it. |
| **[`nova.ui_certificate_prompt_resolve`](tools/app-shell-and-ui/nova-ui-certificate-prompt-resolve.md)** | `decision` | Answers Nova's dialog for a server certificate it could not verify: refuse the connection or proceed for this session. |
| **[`nova.ui_client_certificate_prompt_resolve`](tools/app-shell-and-ui/nova-ui-client-certificate-prompt-resolve.md)** | `decision`, `subject?` | Answers Nova's client-certificate dialog: send a named certificate or continue without one. |
| **[`nova.ui_close_downloads`](tools/app-shell-and-ui/nova-ui-close-downloads.md)** | *(none)* | Closes the download manager drawer panel in the Nova host user interface. |
| **[`nova.ui_close_favorites`](tools/app-shell-and-ui/nova-ui-close-favorites.md)** | *(none)* | Closes the favorites panel if one is open. |
| **[`nova.ui_close_settings`](tools/app-shell-and-ui/nova-ui-close-settings.md)** | *(none)* | Closes the settings drawer overlay in the Nova host user interface. |
| **[`nova.ui_confirm_native_dialog`](tools/app-shell-and-ui/nova-ui-confirm-native-dialog.md)** | `button?` | Presses a button in the open dialog: by name in any dialog, including Nova's own, or the affirmative button of a Windows dialog. |
| **[`nova.ui_dismiss_native_dialog`](tools/app-shell-and-ui/nova-ui-dismiss-native-dialog.md)** | *(none)* | Dismisses or cancels the currently active host-owned Win32 native dialog. |
| **[`nova.ui_download_security_prompt_resolve`](tools/app-shell-and-ui/nova-ui-download-security-prompt-resolve.md)** | `decision` | Answers Nova's "Keep this file?" question for a download that Windows can run (for example .exe, .msi, .bat, .ps1). |
| **[`nova.ui_get_state`](tools/app-shell-and-ui/nova-ui-get-state.md)** | *(none)* | Inspects host application UI state: active tab, overlay visibility, responsiveness, and open dialogs. |
| **[`nova.ui_inspect_native_dialog`](tools/app-shell-and-ui/nova-ui-inspect-native-dialog.md)** | *(none)* | Inspects the open dialog — a Windows dialog Nova owns or one of Nova's own dialogs — with its texts and buttons. |
| **[`nova.ui_open_downloads`](tools/app-shell-and-ui/nova-ui-open-downloads.md)** | *(none)* | Opens the download manager drawer panel in the Nova host user interface. |
| **[`nova.ui_open_favorites`](tools/app-shell-and-ui/nova-ui-open-favorites.md)** | `query?`, `folderId?` | Opens the favorites panel in the Nova user interface, optionally with a search already typed. |
| **[`nova.ui_open_settings`](tools/app-shell-and-ui/nova-ui-open-settings.md)** | `section?` | Opens the settings drawer overlay in the Nova host user interface. |
| **[`nova.ui_permission_prompt_resolve`](tools/app-shell-and-ui/nova-ui-permission-prompt-resolve.md)** | `decision?` | Defers or answers the permission dialog that Nova is showing for a site (for example location, notifications, clipboard read or advanced device access). |
| **[`nova.ui_restore_tabs_prompt_resolve`](tools/app-shell-and-ui/nova-ui-restore-tabs-prompt-resolve.md)** | `decision` | Resolves the startup tab restoration prompt modal after an abnormal browser termination. |
| **[`nova.ui_restore_tabs_prompt_state`](tools/app-shell-and-ui/nova-ui-restore-tabs-prompt-state.md)** | *(none)* | Inspects whether a startup tab restoration prompt is active and previews saved session tabs. |
| **[`nova.ui_set_native_dialog_file_name`](tools/app-shell-and-ui/nova-ui-set-native-dialog-file-name.md)** | `text` | Fills the file path or name field of an active Win32 native file picker dialog. |
| **[`nova.webview_get_zoom`](tools/app-shell-and-ui/nova-webview-get-zoom.md)** | `targetId?` | Retrieves the current zoom factor of the target tab's WebView2 control. |
| **[`nova.webview_reset_zoom`](tools/app-shell-and-ui/nova-webview-reset-zoom.md)** | `targetId?` | Resets the target tab's WebView2 zoom factor back to the default 1.0 (100%). |
| **[`nova.webview_set_zoom`](tools/app-shell-and-ui/nova-webview-set-zoom.md)** | `zoomFactor`, `targetId?`, `persistForSite?` | Sets the zoom factor for a target tab's WebView2 instance. |
| **[`nova.window_get_bounds`](tools/app-shell-and-ui/nova-window-get-bounds.md)** | *(none)* | Returns host application window boundaries (position, size) and monitor inventory metadata. |
| **[`nova.window_move`](tools/app-shell-and-ui/nova-window-move.md)** | `monitorIndex`, `position?` | Moves the Nova application window to a monitor, by index. |
| **[`nova.window_set_size`](tools/app-shell-and-ui/nova-window-set-size.md)** | `width`, `height` | Resizes the Nova application window to specified pixel width and height. |
| **[`nova.window_set_state`](tools/app-shell-and-ui/nova-window-set-state.md)** | `state` | Sets host application window state: minimize, maximize, restore, or bring to foreground. |

---

## 23. Agent-Authored Plugins

Write, test, and ship agent-authored browser plugins that change how pages behave.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.plugin_create`](tools/plugins/nova-plugin-create.md)** | `manifest`, `code?`, `files?`, `deferActivation?`, `agentId?` | Create and install a new agent-authored plugin from a manifest JSON string. |
| **[`nova.plugin_css_reset`](tools/plugins/nova-plugin-css-reset.md)** | `pluginId` | Remove the plugin's host-owned injected stylesheet from active page sessions. |
| **[`nova.plugin_disable`](tools/plugins/nova-plugin-disable.md)** | `pluginId`, `reason?` | Disable a plugin. |
| **[`nova.plugin_enable`](tools/plugins/nova-plugin-enable.md)** | `pluginId` | Activate a plugin that is either disabled or waiting in Testing state. |
| **[`nova.plugin_export`](tools/plugins/nova-plugin-export.md)** | `pluginId`, `includeKvData?` | Export a plugin as a base64-encoded .novaplugin ZIP bundle containing manifest, source code, and optionally persistent KV storage data (including typed storage.local / storage.sync snapshots). |
| **[`nova.plugin_get_code`](tools/plugins/nova-plugin-get-code.md)** | `pluginId` | Read the declared JavaScript source files of an installed plugin. |
| **[`nova.plugin_get_version_code`](tools/plugins/nova-plugin-get-version-code.md)** | `pluginId`, `historyId` | Read a specific historical snapshot of a plugin's code + manifest from plugin_version_history. |
| **[`nova.plugin_grant_active_tab`](tools/plugins/nova-plugin-grant-active-tab.md)** | `pluginId`, `targetId?`, `permissions?` | Start an installed plugin on the current browser tab with temporary activeTab-style access. |
| **[`nova.plugin_icons_list`](tools/plugins/nova-plugin-icons-list.md)** | *(none)* | List all plugin icon names known to the host (used in manifest.ui.icon). |
| **[`nova.plugin_import`](tools/plugins/nova-plugin-import.md)** | `bundleBase64`, `overwrite?` | Import a plugin from a base64-encoded .novaplugin ZIP bundle. |
| **[`nova.plugin_inject_reset`](tools/plugins/nova-plugin-inject-reset.md)** | `pluginId` | Unmount all overlay elements injected by a plugin. |
| **[`nova.plugin_inspect`](tools/plugins/nova-plugin-inspect.md)** | `pluginId` | Detailed inspection of a plugin: full state snapshot, manifest details, granted permissions, contentScriptInventory for static/dynamic scripts vs active/known live frames, plugin storage key counts (persistent KV plus host-managed keys), active mutation count, and recent mutations. |
| **[`nova.plugin_list`](tools/plugins/nova-plugin-list.md)** | `includeUninstalled?` | List all installed agent-authored plugins with their install state, runtime state, permissions, and error/crash counts. |
| **[`nova.plugin_logs`](tools/plugins/nova-plugin-logs.md)** | `pluginId`, `limit?` | Retrieve recent error log entries for a specific plugin. |
| **[`nova.plugin_managed_storage_get`](tools/plugins/nova-plugin-managed-storage-get.md)** | `pluginId`, `key?` | Read host-controlled managed storage for an installed plugin. |
| **[`nova.plugin_managed_storage_update`](tools/plugins/nova-plugin-managed-storage-update.md)** | `pluginId`, `values?`, `deleteKeys?`, `clearExisting?` | Create, update, or delete host-controlled managed storage values for an installed plugin. |
| **[`nova.plugin_request_permission`](tools/plugins/nova-plugin-request-permission.md)** | `pluginId`, `permissions?`, `mcpTools?`, `grantHostPermissions?`, `grantNetworkAccess?` | Grant review-gated permissions or scopes for an installed plugin. |
| **[`nova.plugin_rollback`](tools/plugins/nova-plugin-rollback.md)** | `pluginId`, `historyId`, `changeNote?`, `deferActivation?` | Restore an installed plugin to a specific snapshot from plugin_version_history. |
| **[`nova.plugin_security_log`](tools/plugins/nova-plugin-security-log.md)** | `pluginId`, `limit?` | Read recent security policy violations recorded by the bridge enforcement layer (permission_denied, quota_exceeded, url_blocked, script_blocked, redirect_blocked, oversize_attempt). |
| **[`nova.plugin_test`](tools/plugins/nova-plugin-test.md)** | `pluginId`, `script?`, `mode?`, `applyWrites?`, `activateAfterPass?` | Execute or smoke-test a JS script in a plugin's Jint runtime. |
| **[`nova.plugin_uninstall`](tools/plugins/nova-plugin-uninstall.md)** | `pluginId`, `deleteData?` | Uninstall a plugin. |
| **[`nova.plugin_update`](tools/plugins/nova-plugin-update.md)** | `pluginId`, `code?`, `files?`, `manifest?`, `changeNote?`, `deferActivation?` | Update an installed plugin's source code and/or manifest. |

---

## Next Steps

* Review protocol communication in **[Protocol & Transport](protocol-and-transport.md)**.
* Return to the **[MCP Reference Index](README.md)**.
