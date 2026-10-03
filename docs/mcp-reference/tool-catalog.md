# Nova MCP Tool Catalog

This catalog provides a functional reference for the primary tools exposed by **Nova AI Workspace**, categorized by operational domain. Click on any tool name to view its dedicated reference documentation, parameter table, JSON examples, and error handling notes.

---

## 1. Browser Navigation & Tab Strip

Manage the browser lifecycle, open tabs, switch profiles, and claim exclusive access leases.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.tabs`](tools/browser-automation/nova-tabs.md)** | `outputDetail?` ("minimal" | "full") | Lists all open tabs across all sandboxes with IDs, titles, URLs, active state, and claim status. |
| **[`nova.tab_new`](tools/browser-automation/nova-tab-new.md)** | `url`, `private?`, `isolate?` | Opens a new tab. `private: true` opens an ephemeral incognito context with a pristine cookie jar. |
| **[`nova.tab_close`](tools/browser-automation/nova-tab-close.md)** | `targetId?` | Closes the specified tab. |
| **[`nova.set_active_tab`](tools/browser-automation/nova-set-active-tab.md)** | `targetId` | Switches focus and visual presentation to the specified tab. |
| **[`nova.tab_claim`](tools/browser-automation/nova-tab-claim.md)** | `targetId`, `purpose`, `leaseDurationMs?` | Leases exclusive write access to a tab, preventing other agents from clobbering input or navigating away. |
| **[`nova.tab_release`](tools/browser-automation/nova-tab-release.md)** | `targetId` | Voluntarily releases an active tab lease before expiration. |
| **[`nova.tab_cleanup_orphans`](tools/browser-automation/nova-tab-cleanup-orphans.md)** | *(none)* | Scans for and closes background WebViews with no parent UI and no active leases. |
| **[`nova.navigate`](tools/browser-automation/nova-navigate.md)** | `url`, `targetId?`, `waitForSettlement?` | Navigates the target tab to a URL. Returns domain notes and operator hints if present. |
| **[`nova.route`](tools/browser-automation/nova-route.md)** | `routePath`, `targetId?` | Route-safe client-side SPA navigation without triggering a full page reload. |
| **[`nova.back`](tools/browser-automation/nova-back.md)** / **[`nova.forward`](tools/browser-automation/nova-forward.md)** | `targetId?` | History traversal. |
| **[`nova.reload`](tools/browser-automation/nova-reload.md)** | `targetId?`, `ignoreCache?` | Reloads the page. |
| **[`nova.wait_for_selector`](tools/browser-automation/nova-wait-for-selector.md)** | `selector`, `absent?`, `visible?`, `timeoutMs?` | Waits for an element to appear, become visible, or disappear, returning bounding rects. |
| **[`nova.auto_reload_get`](tools/browser-automation/nova-auto-reload-get.md)** | `_meta?`, `agentId?`, `targetId` | Read the session-only native Auto-Reload state for one explicit target. This is the same state shown in Nova's reload... |
| **[`nova.auto_reload_set`](tools/browser-automation/nova-auto-reload-set.md)** | `_meta?`, `agentId?`, `clientRequestId`, `expectedRevision`, `intervalSeconds?`, `mode`, `targetId` | Create, update, pause, resume, or stop native session-only Auto-Reload for one explicitly claimed target. The user se... |
| **[`nova.history_get`](tools/browser-automation/nova-history-get.md)** | `_meta?`, `agentId?`, `targetId?` | Read-only snapshot of the tab's session navigation history (same source the browser's long-press Back/Forward menu us... |
| **[`nova.history_go`](tools/browser-automation/nova-history-go.md)** | `_meta?`, `agentId?`, `confirmSessionDestruction?`, `entryId?`, `force?`, `includeScreenshot?`, `offset?`, `outputDetail?`, `screenshotFormat?`, `screenshotMaxHeight?`, `screenshotMaxWidth?`, `screenshotQuality?`, `settlementTimeoutMs?`, `targetId?`, `waitForLoad?`, `waitForLoadTimeoutMs?`, `waitForSettlement?` | Jump to a specific entry in the tab's session navigation history. Provide either entryId (preferred — copy from nova.... |
| **[`nova.tab_move`](tools/browser-automation/nova-tab-move.md)** | `_meta?`, `agentId?`, `insertAfter?`, `targetId`, `targetTabId` | Reorder a browser tab within its sandbox by naming the tab it should sit next to. Positions are expressed as neighbou... |
| **[`nova.tab_pin`](tools/browser-automation/nova-tab-pin.md)** | `_meta?`, `agentId?`, `pinned`, `targetId` | Pin or unpin a browser tab. Pinned tabs always sort before unpinned ones in the strip, so pinning also moves the tab;... |
| **[`nova.tab_snapshot`](tools/browser-automation/nova-tab-snapshot.md)** | `_meta?`, `agentId?`, `includeOkFacts?`, `includeText?`, `maxCharsPerTab?`, `targetIds` | Read page info and optional text content from multiple tabs in a single call. Returns an array of tab contexts — usef... |
| **[`nova.tab_transfer`](tools/browser-automation/nova-tab-transfer.md)** | `_meta?`, `agentId?`, `destSelector`, `destTargetId`, `maxChars?`, `sourceSelector`, `sourceTargetId`, `transform?` | Transfer data between tabs: reads text content from a source tab element and writes it into a destination tab element... |
| **[`nova.wait_for_modal`](tools/browser-automation/nova-wait-for-modal.md)** | `_meta?`, `agentId?`, `deep?`, `includeScreenshot?`, `maxResults?`, `pollMs?`, `screenshotFormat?`, `screenshotMaxHeight?`, `screenshotMaxWidth?`, `screenshotQuality?`, `screenshotResponseMode?`, `targetId?`, `timeoutMs?`, `visibleOnly?` | Wait until an open modal/dialog/overlay is detected (with optional deep traversal into same-origin iframes + open sha... |

---

## 2. DOM Perception & Content Extraction

Token-efficient data extraction without requesting raw HTML blobs or full-screen captures.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.read_text_structured`](tools/dom-and-reading/nova-read-text-structured.md)** | `targetId?`, `selector?`, `maxCharsPerRegion?` | Extracts clean, structured text elements grouped by semantic landmark regions (`header`, `nav`, `main`, `footer`). |
| **[`nova.read_dom`](tools/dom-and-reading/nova-read-dom.md)** | `targetId?`, `maxChars?` | Returns a pruned, serialized outerHTML DOM snapshot for the requested container. |
| **[`nova.dom_extract`](tools/dom-and-reading/nova-dom-extract.md)** | `selector`, `properties`, `maxItems?` | High-speed, typed extraction of text, classes, and HTML attributes across Shadow DOM roots. |
| **[`nova.extract_table`](tools/dom-and-reading/nova-extract-table.md)** | `targetId?`, `selector?`, `maxRows?` | Parses HTML tables into structured JSON `{ headers: [...], rows: [[...]] }`. |
| **[`nova.search_text`](tools/dom-and-reading/nova-search-text.md)** | `text`, `match?`, `tag?`, `deep?` | Searches the page for visible text occurrences and returns actionable CSS selectors and bounding rects. |
| **[`nova.perceive`](tools/dom-and-reading/nova-perceive.md)** | `targetId?`, `mode?`, `deep?` | Multi-modal fusion perception: visual screenshot and structured page state in a single call. |
| **[`nova.page_info`](tools/dom-and-reading/nova-page-info.md)** | `targetId?` | Ultra-low token check for URL, title, document readyState, viewport dimensions, and focused element. |
| **[`nova.console_read`](tools/dom-and-reading/nova-console-read.md)** | `_meta?`, `agentId?`, `clear?`, `engineSinceId?`, `maxChars?`, `maxEntries?`, `sinceId?`, `targetId?` | Read recent console messages from the page. Installs a lightweight console tap on first use for that page context - s... |
| **[`nova.eval`](tools/dom-and-reading/nova-eval.md)** | `_meta?`, `agentId?`, `expression`, `frameId?`, `frameScope?`, `functionBody?`, `includeShadow?`, `isolate?`, `maxChars?`, `outputDetail?`, `redact?`, `targetId?`, `timeoutMs?`, `worldMode?` | Execute a JavaScript expression in the page context (returns JSON). Default worldMode='isolated' runs in a CDP isolat... |
| **[`nova.fetch_resource`](tools/dom-and-reading/nova-fetch-resource.md)** | `_meta?`, `agentId?`, `maxBytes?`, `saveDir?`, `savePath?`, `targetId?`, `timeoutMs?`, `url?`, `urls?` | Fetch one or more URLs using the tab's authenticated session and write the bytes to disk — the bridge from 'this tab ... |
| **[`nova.get_active_element_deep`](tools/dom-and-reading/nova-get-active-element-deep.md)** | `_meta?`, `agentId?`, `targetId?` | Get the active/focused element with deep traversal across open shadow roots and same-origin iframes. |
| **[`nova.get_element_rect`](tools/dom-and-reading/nova-get-element-rect.md)** | `_meta?`, `agentId?`, `contextPaddingPx?`, `cropPadding?`, `cropPaddingPx?`, `includeScreenshot?`, `outputDetail?`, `screenshot?`, `screenshotFormat?`, `screenshotMaxHeight?`, `screenshotMaxWidth?`, `screenshotQuality?`, `screenshotResponseMode?`, `scrollIntoView?`, `selector`, `targetId?`, `visible?` | Get an element's bounding rect (querySelector + getBoundingClientRect). With includeScreenshot=true it also returns a... |
| **[`nova.get_layout_metrics`](tools/dom-and-reading/nova-get-layout-metrics.md)** | `_meta?`, `agentId?`, `targetId?` | Get viewport and scroll metrics (CDP Page.getLayoutMetrics). Useful for coordinate mapping and as the canonical oracl... |
| **[`nova.messages_read`](tools/dom-and-reading/nova-messages-read.md)** | `_meta?`, `agentId?`, `clear?`, `includePayloads?`, `maxChars?`, `maxEntries?`, `maxPayloadChars?`, `sinceId?`, `targetId?` | Read recent postMessage, MessagePort, and CustomEvent traffic captured by an opt-in page tap. Installs the tap on fir... |
| **[`nova.network_read`](tools/dom-and-reading/nova-network-read.md)** | `_meta?`, `agentId?`, `clear?`, `excludeWebSocket?`, `groupBy?`, `includeBodies?`, `includeHeaders?`, `kinds?`, `maxBodyChars?`, `maxChars?`, `maxEntries?`, `methods?`, `onlyFailed?`, `pollIntervalMs?`, `redact?`, `redactHeaders?`, `sinceId?`, `sinceMs?`, `statusMax?`, `statusMin?`, `summarize?`, `targetId?`, `urlContains?`, `waitForMatchMs?` | Read recent in-page network activity captured by an opt-in tap for fetch, XHR, WebSocket, server-sent events, sendBea... |
| **[`nova.page_blobs_list`](tools/dom-and-reading/nova-page-blobs-list.md)** | `_meta?`, `agentId?`, `limit?`, `probeMetadata?`, `targetId?`, `watch?` | List the blob: URLs that are live in this page, so they can be saved with nova.fetch_resource. A blob: handle is a ru... |
| **[`nova.perceive_snapshot_query`](tools/dom-and-reading/nova-perceive-snapshot-query.md)** | `_meta?`, `caseSensitive?`, `chunkChars?`, `chunkIndex?`, `contextChars?`, `match?`, `maxResults?`, `node?`, `op?`, `path?`, `query?`, `snapshotId` | Query a saved oversized perceive(mode='full') snapshot without rerunning live DOM extraction. Use this when structure... |
| **[`nova.read_text`](tools/dom-and-reading/nova-read-text.md)** | `_meta?`, `agentId?`, `continuationToken?`, `maxChars?`, `offset?`, `selector?`, `targetId?` | Read visible text content (best-effort; innerText). Useful for lightweight assertions. When the text does not fit, th... |
| **[`nova.stream_url`](tools/dom-and-reading/nova-stream-url.md)** | `_meta?`, `agentId?`, `fps?`, `includeToken?`, `kind?`, `maxHeight?`, `maxWidth?`, `screenshotMaxHeight?`, `screenshotMaxWidth?`, `targetId?` | Build a local /stream URL (multipart PNG stream). Useful for screenshot streaming loops. |
| **[`nova.wait_for_eval`](tools/dom-and-reading/nova-wait-for-eval.md)** | `_meta?`, `agentId?`, `expression`, `includeScreenshot?`, `pollMs?`, `screenshotFormat?`, `screenshotMaxHeight?`, `screenshotMaxWidth?`, `screenshotQuality?`, `screenshotResponseMode?`, `targetId?`, `timeoutMs?` | Wait until a JavaScript expression returns a truthy value (polling). Useful for waiting on dynamic state changes (e.g... |

---

## 3. Layout Quality & Measuring QA

Inspect CSS layouts, find clipped elements, and perform accessibility audits without hand-rolling scripts.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.measure_elements`](tools/layout-and-qa/nova-measure-elements.md)** | `selectors` (up to 25), `properties?` | Measures element geometry: window width, container offered width, rendered size, and `usedWidthRatio`. |
| **[`nova.detect_overflow`](tools/layout-and-qa/nova-detect-overflow.md)** | `targetId?`, `selector?` | Finds clipped text, overflowing containers, and elements bleeding past the viewport edge. |
| **[`nova.get_computed_style`](tools/layout-and-qa/nova-get-computed-style.md)** | `selector`, `properties?`, `targetId?` | Returns exact computed CSS values (color, font, margin, z-index) for an element. |
| **[`nova.audit_accessibility`](tools/layout-and-qa/nova-audit-accessibility.md)** | `targetId?`, `selector?`, `minTargetSize?` | Runs WCAG contrast checks, missing ARIA labels, and touch-target size validations. |
| **[`nova.measure_web_vitals`](tools/layout-and-qa/nova-measure-web-vitals.md)** | `targetId?`, `durationMs?`, `reset?` | Measures live Core Web Vitals: LCP (Largest Contentful Paint), CLS (Layout Shift), and INP. |
| **[`nova.composer_state`](tools/layout-and-qa/nova-composer-state.md)** | `_meta?`, `agentId?`, `frameId?`, `selector?`, `targetId?` | Read what is currently sitting in a chat composer: its text, its attachments, and whether the send control is ready. ... |
| **[`nova.force_pseudo_state`](tools/layout-and-qa/nova-force-pseudo-state.md)** | `_meta?`, `agentId?`, `selector`, `states?`, `targetId?` | Hold a CSS state on one element so it can be screenshotted or inspected: :hover, :active, :focus, :focus-visible, :fo... |

---

## 4. Humanized Input & Interaction

Bot-resilient input execution with natural Bézier physics and Shadow-DOM traversal.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.click_selector`](tools/browser-automation/nova-click-selector.md)** | `selector`, `targetId?`, `verify?` | Clicks an element. Uses ` >>> ` for deep Shadow-DOM piercing. Verifies clickability before clicking. |
| **[`nova.type_selector`](tools/browser-automation/nova-type-selector.md)** | `selector`, `text`, `pressEnter?` | Focuses an input field and types text with realistic inter-keystroke intervals. |
| **[`nova.scroll_smart`](tools/browser-automation/nova-scroll-smart.md)** | `deltaY`, `targetId?` | Natural mouse-wheel scroll on CDP level. Reports `saturation` so agents know when lazy feeds end. |
| **[`nova.input_key`](tools/browser-automation/nova-input-key.md)** | `key`, `targetId?` | Dispatches physical keyboard keydown/keyup events (e.g. `Enter`, `Escape`, `Tab`). |
| **[`nova.file_upload`](tools/browser-automation/nova-file-upload.md)** | `selector?`, `filePaths`, `frameId?` | Attaches one or more local files to an HTML `<input type="file">` element cleanly. |
| **[`nova.choose_option`](tools/browser-automation/nova-choose-option.md)** | `_meta?`, `agentId?`, `autoDismissBlockers?`, `autoDismissMode?`, `includeScreenshot?`, `screenshotFormat?`, `screenshotMaxHeight?`, `screenshotMaxWidth?`, `screenshotQuality?`, `selector`, `targetId?`, `text?`, `texts?`, `timeoutMs?`, `value?`, `values?`, `verify?` | Universal option chooser that auto-detects the control type (native <select>, ARIA combobox, standalone listbox, radi... |
| **[`nova.input_click`](tools/browser-automation/nova-input-click.md)** | `_meta?`, `activateIfNeeded?`, `agentId?`, `button?`, `clickCount?`, `includeScreenshot?`, `restoreActiveTarget?`, `screenshotFormat?`, `screenshotMaxHeight?`, `screenshotMaxWidth?`, `screenshotQuality?`, `screenshotResponseMode?`, `targetId?`, `waitForNavigation?`, `waitForNavigationTimeoutMs?`, `x`, `y` | Click at x/y coordinates (CDP Input.dispatchMouseEvent). Use when no CSS selector is available; prefer nova.click_selector... |
| **[`nova.input_drag`](tools/browser-automation/nova-input-drag.md)** | `_meta?`, `activateIfNeeded?`, `agentId?`, `button?`, `endX?`, `endY?`, `fromX?`, `fromY?`, `restoreActiveTarget?`, `startX?`, `startY?`, `steps?`, `targetId?`, `toX?`, `toY?` | Drag from (startX,startY) to (endX,endY) (best-effort; CDP Input.dispatchMouseEvent). Also drives HTML5 drag-and-drop... |
| **[`nova.input_drag_humanized`](tools/browser-automation/nova-input-drag-humanized.md)** | `_meta?`, `agentId?`, `durationMs?`, `endX?`, `endY?`, `fromX?`, `fromY?`, `jitterPx?`, `selector?`, `startX?`, `startY?`, `targetId?`, `toX?`, `toY?` | Perform a human-like drag using JS setTimeout cascade with realistic timing, jitter, and overshoot/correction from (s... |
| **[`nova.input_move`](tools/browser-automation/nova-input-move.md)** | `_meta?`, `activateIfNeeded?`, `agentId?`, `restoreActiveTarget?`, `targetId?`, `x`, `y` | Move the mouse pointer (hover) to x/y coordinates. Useful for triggering hover states before clicking. |
| **[`nova.input_shortcut`](tools/browser-automation/nova-input-shortcut.md)** | `_meta?`, `agentId?`, `combo`, `targetId?` | Send a keyboard shortcut with modifiers plus exactly one key, e.g. Ctrl+L / Ctrl+K / Alt+Left / Ctrl++ (best-effort). |
| **[`nova.input_text`](tools/browser-automation/nova-input-text.md)** | `_meta?`, `agentId?`, `targetId?`, `text` | Type text into the currently focused element (CDP Input.insertText). Text is sent as one insertText dispatch and is l... |
| **[`nova.input_wheel`](tools/browser-automation/nova-input-wheel.md)** | `_meta?`, `activateIfNeeded?`, `agentId?`, `deltaX?`, `deltaY`, `restoreActiveTarget?`, `targetId?`, `x`, `y` | Scroll at specific x/y coordinates via mouse wheel (CDP). Use when you need to scroll at a particular position; prefe... |
| **[`nova.run_sequence`](tools/browser-automation/nova-run-sequence.md)** | `_meta?`, `agentId?`, `defaults?`, `options?`, `steps`, `targetId?`, `totalTimeoutMs?` | Execute a sequence of tool calls atomically in a single MCP request. Supports retry, conditional execution, and error... |
| **[`nova.scroll_by`](tools/browser-automation/nova-scroll-by.md)** | `_meta?`, `agentId?`, `containerSelector?`, `deltaX?`, `deltaY`, `targetId?` | Scroll the page by deltaX/deltaY (window.scrollBy). Preferred for simple page scrolling. If the window cannot scroll,... |
| **[`nova.scroll_element`](tools/browser-automation/nova-scroll-element.md)** | `_meta?`, `agentId?`, `deltaY`, `selector`, `targetId?` | Scroll a specific container element by deltaY (querySelector + scrollTop). Use for scrollable inner containers; use n... |
| **[`nova.scroll_to`](tools/browser-automation/nova-scroll-to.md)** | `_meta?`, `agentId?`, `targetId?`, `x?`, `y` | Scroll the page to x/y (window.scrollTo). window.scrollTo only moves the document — on pages with an inner scroll con... |
| **[`nova.select_option`](tools/browser-automation/nova-select-option.md)** | `_meta?`, `agentId?`, `autoDismissBlockers?`, `autoDismissMode?`, `includeScreenshot?`, `screenshotFormat?`, `screenshotMaxHeight?`, `screenshotMaxWidth?`, `screenshotQuality?`, `selector`, `targetId?`, `text?`, `texts?`, `timeoutMs?`, `value?`, `values?`, `verify?` | Select an option on a native HTML <select> element by option value or visible label. Use this instead of nova.eval fo... |

---

## 5. Guarded Actions & Blocker Clearance

High-impact macros that run safety pre-checks to prevent destructive loops or session loss.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.dismiss_blockers`](tools/browser-automation/nova-dismiss-blockers.md)** | `targetId?`, `mode?` | Identifies and clicks modal close buttons, backdrop dismissals, and cookie consent overlays. |
| **[`nova.guarded_send_message`](tools/guarded-actions/nova-guarded-send-message.md)** | `text`, `targetId?` | Automatically locates chat composer and send button, enters text, and verifies transmission. |
| **[`nova.guarded_submit_form`](tools/guarded-actions/nova-guarded-submit-form.md)** | `formSelector`, `targetId?` | Verifies form validation rules before triggering submission. |
| **[`nova.guarded_login`](tools/guarded-actions/nova-guarded-login.md)** | `usernameSelector`, `passwordSelector` | Submits credentials under ASD (Auth Surface Detection) watch to verify login success vs rejection. |
| **[`nova.cmp_apply`](tools/guarded-actions/nova-cmp-apply.md)** | `targetId`, `mode?`, `intent?` | Applies typed privacy consent directly via CMP JavaScript APIs (OneTrust, Sourcepoint, Cookiebot). |
| **[`nova.guarded_switch_model`](tools/guarded-actions/nova-guarded-switch-model.md)** | `_meta?`, `activateIfNeeded?`, `agentId?`, `autoDismissBlockers?`, `autoDismissMode?`, `button?`, `clickCount?`, `ctaRef?`, `ctaRev?`, `frameId?`, `includeScreenshot?`, `navigationStrict?`, `outputDetail?`, `pksAdviceMode?`, `pksMode?`, `restoreActiveTarget?`, `screenshotFormat?`, `screenshotMaxHeight?`, `screenshotMaxWidth?`, `screenshotPolicy?`, `screenshotQuality?`, `selector?`, `targetId?`, `timeoutMs?`, `transitionContract?`, `verify?`, `verifyTimeout?`, `waitForNavigation?`, `waitForNavigationTimeoutMs?` | High-level guarded macro for model switching actions. Wraps nova.click_selector and auto-injects a select-option tran... |
| **[`nova.guarded_switch_sandbox`](tools/guarded-actions/nova-guarded-switch-sandbox.md)** | `_meta?`, `activateIfNeeded?`, `agentId?`, `autoDismissBlockers?`, `autoDismissMode?`, `button?`, `clickCount?`, `ctaRef?`, `ctaRev?`, `frameId?`, `includeScreenshot?`, `navigationStrict?`, `outputDetail?`, `pksAdviceMode?`, `pksMode?`, `restoreActiveTarget?`, `screenshotFormat?`, `screenshotMaxHeight?`, `screenshotMaxWidth?`, `screenshotPolicy?`, `screenshotQuality?`, `selector?`, `targetId?`, `timeoutMs?`, `transitionContract?`, `verify?`, `verifyTimeout?`, `waitForNavigation?`, `waitForNavigationTimeoutMs?` | High-level guarded macro for sandbox/workspace switch actions. Wraps nova.click_selector and auto-injects a select-option... |

---

## 6. Visual Evidence & Screenshots

Lossless visual captures and regression testing with bounded budgets.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.capture_screenshot`](tools/visual-evidence/nova-capture-screenshot.md)** | `targetId?`, `selector?`, `region?`, `responseMode?` | Captures lossless PNG crops or full pages with cryptographic SHA-256 evidence. |
| **[`nova.screenshot_diff`](tools/visual-evidence/nova-screenshot-diff.md)** | `beforePath`, `afterPath`, `mask?`, `threshold?` | Compares two screenshots pixel-by-pixel and generates visual diff overlays. |
| **[`nova.screenshot_baseline`](tools/visual-evidence/nova-screenshot-baseline.md)** | `op`, `name?`, `scope?`, `mask?` | Manages named, persistent visual baselines for automated UI regression testing. |
| **[`nova.save_pdf`](tools/visual-evidence/nova-save-pdf.md)** | `savePath?`, `pageRanges?`, `landscape?` | Renders the current document to a clean vector PDF file on disk. |
| **[`nova.capture_app_screenshot`](tools/visual-evidence/nova-capture-app-screenshot.md)** | `_meta?`, `agentId?`, `format?`, `maxHeight?`, `maxWidth?`, `quality?`, `responseMode?`, `screenshotMaxHeight?`, `screenshotMaxWidth?`, `targetId?` | Capture app-UI evidence. An unclaimed or caller-owned target returns the full app UI (tabs/topbar + WebView content).... |
| **[`nova.read_pdf`](tools/visual-evidence/nova-read-pdf.md)** | `_meta?`, `agentId?`, `includePages?`, `maxChars?`, `pages?`, `path` | Read the text of a PDF on disk - the other half of nova.save_pdf. Use it to verify what a document actually says: tha... |
| **[`nova.responsive_screenshots`](tools/visual-evidence/nova-responsive-screenshots.md)** | `_meta?`, `agentId?`, `deviceScaleFactor?`, `format?`, `fullPage?`, `height?`, `mobile?`, `quality?`, `targetId?`, `widths` | Responsive-breakpoint sweep: capture one screenshot per viewport width in a single call (the 'screenshot @ [375, 768,... |

---

## 7. Knowledge & Phenomenological Store (PKS)

Self-learning procedural memory for persistent fast-paths and domain notes.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.pks_get`](tools/pks-and-learning/nova-pks-get.md)** | `scope`, `outputDetail?`, `phenomenonId?` | Retrieves stored UI phenomenon playbooks by domain scope and ID. |
| **[`nova.pks_upsert`](tools/pks-and-learning/nova-pks-upsert.md)** | `scope`, `phenomenon` | Learns or updates a site UI pattern with mandatory pre-verification and polarity checks. |
| **[`nova.pks_match`](tools/pks-and-learning/nova-pks-match.md)** | `scope`, `observation`, `topK?` | Matches live page elements against learned phenomena fingerprints. |
| **[`nova.telemetry_report`](tools/pks-and-learning/nova-telemetry-report.md)** | `scope`, `phenomenonId`, `outcome` | Reports whether a learned fast-path succeeded or failed, adjusting confidence weights. |
| **[`nova.explain`](tools/pks-and-learning/nova-explain.md)** | `scope`, `stableId` | Explains why a PKS phenomenon resides at its current learning level with gate breakdowns. |
| **[`nova.learn_feedback`](tools/pks-and-learning/nova-learn-feedback.md)** | `_meta?`, `limit?`, `scope?`, `since?` | Return recent promotion/demotion/deprecation events as a learning feedback log. Shows what changed, when, and why. |
| **[`nova.learn_generate`](tools/pks-and-learning/nova-learn-generate.md)** | `_meta?`, `limit?`, `scope` | Generate candidate phenomena/hints from accumulated observations. Runs heuristic rules over observation clusters to p... |
| **[`nova.learn_onboarding_confirm`](tools/pks-and-learning/nova-learn-onboarding-confirm.md)** | `_meta?`, `domain`, `paraphrase` | Confirm the learn-mode onboarding for a domain. The AAG gate that fired with structuredContent.learnOnboarding wants ... |
| **[`nova.learn_onboarding_recall`](tools/pks-and-learning/nova-learn-onboarding-recall.md)** | `_meta?`, `domain?` | Read-only: fetch the current learn-mode onboarding payload for a domain (or, when domain is omitted, for the session'... |
| **[`nova.learn_promote`](tools/pks-and-learning/nova-learn-promote.md)** | `_meta?`, `dryRun?`, `scope`, `stableIds?`, `transition?` | Evaluate and execute staged promotions for PKS entries. Checks gate conditions for level transitions (L0->L1, L1->L2)... |
| **[`nova.learn_resolve_opportunity`](tools/pks-and-learning/nova-learn-resolve-opportunity.md)** | `_meta?`, `opportunityId`, `reason?`, `verdict` | Resolve a semantic learning opportunity. Pass the opportunityId from structuredContent.pksSemanticLearning plus a ver... |
| **[`nova.learn_suggest`](tools/pks-and-learning/nova-learn-suggest.md)** | `_meta?`, `limit?`, `scope?` | Return top learning opportunities from accumulated observations. Shows patterns that may warrant creating new phenome... |
| **[`nova.phenomenon_apply`](tools/pks-and-learning/nova-phenomenon-apply.md)** | `_meta?`, `agentId?`, `maxSteps?`, `observation?`, `phenomenonId`, `scope`, `targetId?`, `timeoutMs?` | Execute a PKS phenomenon playbook server-side. Loads the playbook for the given phenomenon and executes its steps seq... |
| **[`nova.pks_deprecate`](tools/pks-and-learning/nova-pks-deprecate.md)** | `_meta?`, `phenomenonId`, `reason?`, `scope` | Mark a phenomenon as deprecated (soft-delete). Deprecated phenomena are skipped during matching. Like the other PKS w... |
| **[`nova.pks_list`](tools/pks-and-learning/nova-pks-list.md)** | `_meta?`, `limit?`, `minHealth?`, `offset?`, `prefix?`, `serviceCategory?`, `trust?`, `type?` | List all known PKS domains with summary stats (active phenomenon counts plus per-domain health metrics). Filterable b... |
| **[`nova.pks_patch`](tools/pks-and-learning/nova-pks-patch.md)** | `_meta?`, `patch`, `phenomenonId`, `scope` | Partially update a phenomenon (merge fields without replacing the whole entry). Only provided top-level fields (type,... |
| **[`nova.pks_platform_get`](tools/pks-and-learning/nova-pks-platform-get.md)** | `_meta?`, `stableId` | Get a platform's details including platform metadata, active-vs-total pattern counts, status/freshness hints, and all... |
| **[`nova.pks_platform_list`](tools/pks-and-learning/nova-pks-platform-list.md)** | `_meta?` | List all platforms with summary metadata including active-vs-total pattern counts plus status and freshness fields th... |
| **[`nova.pks_platform_seed`](tools/pks-and-learning/nova-pks-platform-seed.md)** | `_meta?`, `aliases?`, `description?`, `displayName`, `homepageUrl?`, `patterns?`, `stableId` | Seed or update a platform with patterns and aliases. stableId is canonicalized to lowercase, the legacy test-only pat... |
| **[`nova.pks_upsert_hint`](tools/pks-and-learning/nova-pks-upsert-hint.md)** | `_meta?`, `agentId?`, `domainHint`, `scope` | Create or update a declarative domain hint for CTA detection scoring. Domain hints are NOT interactive playbooks - th... |
| **[`nova.revalidate`](tools/pks-and-learning/nova-revalidate.md)** | `_meta?`, `agentId?`, `limit?`, `scope?`, `targetId` | Silent DOM-only revalidation of PKS phenomena. Checks if fingerprint selectors still exist without executing playbook... |

---

## 8. Credentials & Secure Vault

Form auto-fill without leaking plaintext secrets to the LLM context.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.vault_list`](tools/vault-and-security/nova-vault-list.md)** | `site?` | Lists available credentials for a domain (account IDs, usernames; passwords redacted). |
| **[`nova.vault_get`](tools/vault-and-security/nova-vault-get.md)** | `site`, `username?` | Inspects account metadata and resolves username ambiguity. |
| **[`nova.vault_prepare_fill`](tools/vault-and-security/nova-vault-prepare-fill.md)** | `site`, `targetId?`, `username?` | Generates a single-use, origin-bound, short-lived `SecretRef` token. |
| **[`nova.type_selector_secret`](tools/vault-and-security/nova-type-selector-secret.md)** | `selector`, `secretRef`, `clear?` | Injects the DPAPI-decrypted password directly into the DOM input field without exposing it. |
| **[`nova.secret_set`](tools/vault-and-security/nova-secret-set.md)** | `name`, `value`, `scope` | Stores an encrypted environment variable or API key using Windows DPAPI. |
| **[`nova.secret_list`](tools/vault-and-security/nova-secret-list.md)** | `scope?`, `workspaceId?`, `taskId?` | Lists registered secret names and scopes without disclosing secret values. |
| **[`nova.secret_delete`](tools/vault-and-security/nova-secret-delete.md)** | `_meta?`, `name`, `scope`, `taskId?`, `workspaceId?` | Delete a secret from the user-managed store. Result reports found=false when no matching secret existed (never a sile... |
| **[`nova.vault_delete`](tools/vault-and-security/nova-vault-delete.md)** | `_meta?`, `id` | Delete a vault entry by ID. |
| **[`nova.vault_set`](tools/vault-and-security/nova-vault-set.md)** | `_meta?`, `createdBy?`, `password`, `site`, `username` | Store or update credentials. Upserts by site+username and returns entryId for cleanup or later metadata reads. Agent-... |

---

## 9. Terminal Workspaces & Headless CLI

Isolated pseudo-terminals (ConPTY), command execution streams, terminal dock control, and session persistence.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.terminal_open`](tools/terminal-ops/nova-terminal-open.md)** | `cwd?`, `cols?`, `rows?`, `shell?`, `agentId?` | Opens a new agent-owned PowerShell session in an isolated working directory and returns its `sessionId`. |
| **[`nova.terminal_list`](tools/terminal-ops/nova-terminal-list.md)** | `agentId?` | Lists all open agent-owned terminal sessions with status, shell type, and exit codes. |
| **[`nova.terminal_read`](tools/terminal-ops/nova-terminal-read.md)** | `sessionId`, `maxBytes?`, `agentId?` | Reads the recent raw output tail of a terminal session scrollback buffer. |
| **[`nova.terminal_write`](tools/terminal-ops/nova-terminal-write.md)** | `sessionId`, `data`, `agentId?` | Writes raw characters to session stdin without appending an implicit newline. |
| **[`nova.terminal_send_key`](tools/terminal-ops/nova-terminal-send-key.md)** | `sessionId`, `key`, `agentId?` | Sends a named control key (`Enter`, `Tab`, `Escape`, `Ctrl+C`, etc.) to the session. |
| **[`nova.terminal_close`](tools/terminal-ops/nova-terminal-close.md)** | `sessionId`, `agentId?` | Terminates an agent-owned session and kills its ConPTY process tree. |
| **[`nova.terminal_run_command`](tools/terminal-ops/nova-terminal-run-command.md)** | `sessionId`, `command`, `timeoutSeconds?` | Runs a single command line and waits synchronously for its completion sentinel. |
| **[`nova.terminal_get_state`](tools/terminal-ops/nova-terminal-get-state.md)** | `sessionId`, `agentId?` | Queries lifecycle status, working directory, and exit code for a session. |
| **[`nova.terminal_dock_get_state`](tools/terminal-ops/nova-terminal-dock-get-state.md)** | *(none)* | Reads presentation state of visible terminal dock (expanded, collapsed, hidden). |
| **[`nova.terminal_dock_set_state`](tools/terminal-ops/nova-terminal-dock-set-state.md)** | `state` | Sets visible terminal dock state (`"expanded"`, `"collapsed"`, `"hidden"`). |
| **[`nova.terminal_settings_get`](tools/terminal-ops/nova-terminal-settings-get.md)** | *(none)* | Reads terminal appearance settings and reports color availability reason code. |
| **[`nova.terminal_settings_set`](tools/terminal-ops/nova-terminal-settings-set.md)** | `theme?`, `fontSize?`, `programColors?` | Updates terminal appearance settings (theme, font size, NO_COLOR preference). |

---

## 10. Downloads Management & Queue Control

Download tracking, pause/resume, security prompt resolution, and directory management.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.downloads_list`](tools/downloads/nova-downloads-list.md)** | `id?`, `status?`, `limit?`, `offset?` | Lists recent downloads tracked by the browser with progress, speeds, and error categories. |
| **[`nova.downloads_wait`](tools/downloads/nova-downloads-wait.md)** | `id?`, `sinceMs?`, `timeoutMs?` | Blocks until downloads reach a terminal state and returns exact disk file paths. |
| **[`nova.downloads_cancel`](tools/downloads/nova-downloads-cancel.md)** | `id` | Cancels an active in-progress or queued download by ID. |
| **[`nova.downloads_cancel_all`](tools/downloads/nova-downloads-cancel-all.md)** | *(none)* | Cancels every non-terminal download currently queued, in progress, or paused. |
| **[`nova.downloads_pause`](tools/downloads/nova-downloads-pause.md)** | `id` | Pauses an active WebView2-native download by ID. |
| **[`nova.downloads_pause_all`](tools/downloads/nova-downloads-pause-all.md)** | *(none)* | Pauses all in-progress WebView2-native downloads that support pausing. |
| **[`nova.downloads_resume`](tools/downloads/nova-downloads-resume.md)** | `id` | Resumes a paused live WebView2-native download by ID. |
| **[`nova.downloads_resume_all`](tools/downloads/nova-downloads-resume-all.md)** | *(none)* | Resumes all paused downloads whose underlying operation supports resumption. |
| **[`nova.downloads_retry`](tools/downloads/nova-downloads-retry.md)** | `id` | Retries a failed download by re-navigating to its original URL. |
| **[`nova.downloads_open_file`](tools/downloads/nova-downloads-open-file.md)** | `id` | Opens a completed download using the operating system default application. |
| **[`nova.downloads_open_folder`](tools/downloads/nova-downloads-open-folder.md)** | `id` | Reveals the downloaded file in Windows Explorer with the item selected. |
| **[`nova.downloads_preview`](tools/downloads/nova-downloads-preview.md)** | `id` | Opens a completed download inline in a new browser tab using a secure `file://` URL. |
| **[`nova.downloads_clear`](tools/downloads/nova-downloads-clear.md)** | `filter?` | Clears terminal download history from the UI and persistent storage. |
| **[`nova.downloads_auto_open_get`](tools/downloads/nova-downloads-auto-open-get.md)** | *(none)* | Retrieves configured auto-open file extensions and executable blocklist. |
| **[`nova.downloads_auto_open_set`](tools/downloads/nova-downloads-auto-open-set.md)** | `extensions` | Bulk-replaces the list of file extensions that auto-open with the OS default app. |

---

## 11. Desktop Notifications & Alerts

Native OS notification dispatch, unread inbox management, and per-origin notification permissions.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.notifications_send`](tools/notifications/nova-notifications-send.md)** | `sourceKind`, `title`, `body?`, `urgent?`, `tag?`, `targetId?` | Dispatches a host-authored Windows toast notification and persists it to the inbox. |
| **[`nova.notifications_list`](tools/notifications/nova-notifications-list.md)** | `sourceKind?`, `origin?`, `unreadOnly?`, `limit?`, `offset?` | Queries the notification inbox with filtering by source, website origin, and read status. |
| **[`nova.notifications_get`](tools/notifications/nova-notifications-get.md)** | `notificationId` | Retrieves complete metadata and payload for a single notification by ID. |
| **[`nova.notifications_unread_count`](tools/notifications/nova-notifications-unread-count.md)** | *(none)* | Returns the count of unread, non-dismissed notifications currently in the inbox. |
| **[`nova.notifications_mark_read`](tools/notifications/nova-notifications-mark-read.md)** | `notificationId` | Marks a notification as read without dismissing it from the inbox. |
| **[`nova.notifications_dismiss`](tools/notifications/nova-notifications-dismiss.md)** | `notificationId` | Dismisses a notification, hiding it from the default inbox view. |
| **[`nova.notifications_clear`](tools/notifications/nova-notifications-clear.md)** | `sourceKind?`, `olderThanDays?` | Bulk-dismisses notifications matching source or age criteria. |
| **[`nova.notifications_open`](tools/notifications/nova-notifications-open.md)** | `notificationId`, `agentId?` | Navigates to the originating tab, website, or resource referenced by a notification. |
| **[`nova.notifications_permissions_list`](tools/notifications/nova-notifications-permissions-list.md)** | `origin?`, `mode?`, `limit?`, `offset?` | Lists website origin notification permissions and reports the effective global default. |
| **[`nova.notifications_permission_set`](tools/notifications/nova-notifications-permission-set.md)** | `origin`, `mode` | Configures notification permission (Ask, Allow, or Deny) for a specific website origin. |
| **[`nova.notifications_permission_default_set`](tools/notifications/nova-notifications-permission-default-set.md)** | `mode` | Sets the global website notification permission default (Ask, Allow, or Deny). |

---

## 12. Device Emulation & Responsive Testing

Mobile viewport simulation, touch event emulation, user agent overriding, and dark mode toggles.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.emulation_use_device`](tools/device-emulation/nova-emulation-use-device.md)** | `device`, `targetId?` | Applies a named device preset (viewport, DPR, touch, and user agent) in one call. |
| **[`nova.emulation_set_device_metrics`](tools/device-emulation/nova-emulation-set-device-metrics.md)** | `width`, `height`, `deviceScaleFactor?`, `mobile?` | Overrides the viewport dimensions, device scale factor, and mobile layout behavior. |
| **[`nova.emulation_clear_device_metrics`](tools/device-emulation/nova-emulation-clear-device-metrics.md)** | `targetId?` | Clears viewport device metrics overrides, restoring normal window-sized rendering. |
| **[`nova.emulation_set_user_agent`](tools/device-emulation/nova-emulation-set-user-agent.md)** | `userAgent`, `platform?`, `acceptLanguage?` | Overrides User-Agent header, navigator.userAgent, and client hints for a tab. |
| **[`nova.emulation_set_touch`](tools/device-emulation/nova-emulation-set-touch.md)** | `enabled`, `maxTouchPoints?` | Enables or disables touch event simulation and sets maximum touch points. |
| **[`nova.emulation_set_media`](tools/device-emulation/nova-emulation-set-media.md)** | `colorScheme?`, `reducedMotion?`, `forcedColors?` | Emulates CSS media features like dark mode, reduced motion, and print media. |
| **[`nova.emulation_clear_media`](tools/device-emulation/nova-emulation-clear-media.md)** | `targetId?` | Clears all emulated CSS media features, reverting to host system theme. |
| **[`nova.emulation_set_locale`](tools/device-emulation/nova-emulation-set-locale.md)** | `locale?`, `timezone?`, `latitude?`, `longitude?` | Emulates browser locale, timezone, and geolocation coordinates. |
| **[`nova.emulation_clear_locale`](tools/device-emulation/nova-emulation-clear-locale.md)** | `targetId?` | Clears all locale, timezone, and geolocation overrides, reverting to host settings. |
| **[`nova.emulation_set_viewport_frame`](tools/device-emulation/nova-emulation-set-viewport-frame.md)** | `enabled?`, `color?` | Configures visual outline rendered around emulated device viewports in host UI. |

---

## 13. External MCP Servers & Secondary Tool Bridging

Registering, running, and dynamically calling secondary MCP servers through Nova's unified host.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.external_servers`](tools/external-mcp/nova-external-servers.md)** | *(none)* | Lists all configured external MCP servers with runtime status, health, and tool count. |
| **[`nova.external_server_add`](tools/external-mcp/nova-external-server-add.md)** | `displayName`, `transport`, `command?`, `endpointUrl?` | Registers a new external MCP server with stdio, HTTP, or SSE transport. |
| **[`nova.external_server_update`](tools/external-mcp/nova-external-server-update.md)** | `serverKey`, `displayName?`, `command?`, `env?` | Updates configuration, environment variables, or transport settings of an existing server. |
| **[`nova.external_server_remove`](tools/external-mcp/nova-external-server-remove.md)** | `serverKey` | Deletes an external MCP server registration, stopping it if running. |
| **[`nova.external_server_start`](tools/external-mcp/nova-external-server-start.md)** | `serverKey` | Launches an external MCP server, runs initialize handshake, and discovers tools. |
| **[`nova.external_server_stop`](tools/external-mcp/nova-external-server-stop.md)** | `serverKey`, `force?` | Stops a running external MCP server gracefully with force-kill fallback. |
| **[`nova.external_server_logs`](tools/external-mcp/nova-external-server-logs.md)** | `serverKey`, `lines?` | Reads recent stderr log lines captured from an external MCP server process. |
| **[`nova.external_tools`](tools/external-mcp/nova-external-tools.md)** | `serverKey`, `includeSchema?`, `refresh?` | Lists all tools available on an external MCP server, with optional full inputSchema. |
| **[`nova.external_tool_call`](tools/external-mcp/nova-external-tool-call.md)** | `serverKey`, `toolName`, `arguments?`, `timeoutMs?` | Invokes a specific tool on a connected external MCP server and returns the raw response. |
| **[`nova.external_server_import`](tools/external-mcp/nova-external-server-import.md)** | `source`, `filePath?`, `serverName?`, `autoStart?` | Imports MCP server definitions from Claude Desktop, VS Code, Claude Code, or JSON files. |

---

## 14. Proxy Routing & Network Interception

Proxy profile management, authentication, traffic redirection, and CDP network request/response interception.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.network_intercept_add`](tools/proxy-and-network/nova-network-intercept-add.md)** | `urlPattern`, `action?`, `status?`, `body?`, `delayMs?`, `maxHits?`, `ttlMs?`, `targetId?` | Deposits a CDP network interception rule to mock responses, inject delays, modify headers, or fail requests. |
| **[`nova.network_intercept_clear`](tools/proxy-and-network/nova-network-intercept-clear.md)** | `ruleId?`, `targetId?` | Clears armed network interception rules for a rule ID, a target tab, or browser-wide. |
| **[`nova.network_intercept_list`](tools/proxy-and-network/nova-network-intercept-list.md)** | `targetId?` | Lists all active network interception rules with hit counts and remaining TTL. |
| **[`nova.network_replay`](tools/proxy-and-network/nova-network-replay.md)** | `action?`, `url?`, `method?`, `headers?`, `body?`, `adoptSessionFrom?`, `timeoutMs?` | Targeted HTTP repeater for testing modified requests, validating headers, and replaying sessions. |
| **[`nova.proxy_create`](tools/proxy-and-network/nova-proxy-create.md)** | `name`, `host`, `port`, `protocol?`, `username?`, `bypassList?`, `enabled?` | Registers a new HTTP, HTTPS, SOCKS4, or SOCKS5 proxy profile. |
| **[`nova.proxy_disconnect`](tools/proxy-and-network/nova-proxy-disconnect.md)** | `targetId` | Manually disconnects the proxy for a target scope, falling back to direct network connectivity. |
| **[`nova.proxy_list`](tools/proxy-and-network/nova-proxy-list.md)** | *(none)* | Lists all configured proxy profiles with active assignments, routing mode, and status. |
| **[`nova.proxy_log`](tools/proxy-and-network/nova-proxy-log.md)** | `maxLines?` | Reads recent diagnostic log entries from the proxy routing engine (credentials redacted). |
| **[`nova.proxy_reconnect`](tools/proxy-and-network/nova-proxy-reconnect.md)** | `targetId` | Reconnects a previously disconnected proxy for a target scope. |
| **[`nova.proxy_remove`](tools/proxy-and-network/nova-proxy-remove.md)** | `profileId` | Deletes a proxy profile and its stored credentials. |
| **[`nova.proxy_set_password`](tools/proxy-and-network/nova-proxy-set-password.md)** | `profileId`, `password?` | Stores or clears the password for a proxy profile in DPAPI-protected storage. |
| **[`nova.proxy_status`](tools/proxy-and-network/nova-proxy-status.md)** | `profileId?`, `targetId?` | Retrieves live connection health, latency, and throughput statistics for a proxy profile. |
| **[`nova.proxy_switch`](tools/proxy-and-network/nova-proxy-switch.md)** | `mode?`, `profileId?`, `sandboxId?` | Switches the active proxy profile globally or for a specific sandbox container. |
| **[`nova.proxy_test`](tools/proxy-and-network/nova-proxy-test.md)** | `profileId`, `probeUrl?` | Runs an end-to-end health probe against a proxy profile and measures latency. |
| **[`nova.proxy_update`](tools/proxy-and-network/nova-proxy-update.md)** | `profileId`, `name?`, `host?`, `port?`, `protocol?`, `username?`, `enabled?` | Updates endpoint configuration, credentials, or bypass lists for an existing proxy profile. |

---

## 15. Site Crawler & URL Discovery Index

Broad-surface website crawling, URL indexing, sitemap verification, and discovery probes.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.crawl_start`](tools/crawler-and-discovery/nova-crawl-start.md)** | `startUrl`, `maxPages?`, `maxDepth?`, `crawlMode?`, `urlPattern?`, `excludePattern?`, `extractMetadata?`, `extractContent?`, `pageDelayMs?` | Launches a background BFS crawl from a root URL using isolated hidden WebViews. |
| **[`nova.crawl_status`](tools/crawler-and-discovery/nova-crawl-status.md)** | `crawlId`, `outputDetail?` | Checks live progress, active phase, visited page counts, and error metrics for a crawl job. |
| **[`nova.crawl_results`](tools/crawler-and-discovery/nova-crawl-results.md)** | `crawlId`, `limit?`, `offset?`, `sinceSequence?`, `filter?`, `sortBy?`, `summary?` | Retrieves paginated page details, extracted text, metadata, and screenshots from a crawl job. |
| **[`nova.crawl_stop`](tools/crawler-and-discovery/nova-crawl-stop.md)** | `crawlId` | Requests graceful cancellation of an active crawl job, draining in-flight workers. |
| **[`nova.crawl_update`](tools/crawler-and-discovery/nova-crawl-update.md)** | `crawlId`, `paused?`, `pageDelayMs?`, `maxPages?`, `maxDepth?`, `urlPattern?` | Dynamically modifies parameters (rate limits, filters, depth, pauses) of an active crawl mid-flight. |
| **[`nova.crawl_verify`](tools/crawler-and-discovery/nova-crawl-verify.md)** | `urls`, `assert?`, `extractMetadata?`, `extractContent?`, `customScript?`, `pageDelayMs?` | Performs targeted, non-traversal verification and DOM extraction against a specific list of URLs. |
| **[`nova.crawl_history`](tools/crawler-and-discovery/nova-crawl-history.md)** | `scopeKey?`, `status?`, `limit?`, `taskInstanceId?` | Lists past crawl jobs and high-level summaries from the persistent crawler database. |
| **[`nova.crawl_diff`](tools/crawler-and-discovery/nova-crawl-diff.md)** | `oldCrawlId`, `newCrawlId`, `includeUnchanged?`, `limit?` | Compares two completed crawls of the same site to detect added, removed, or modified pages. |
| **[`nova.crawl_links`](tools/crawler-and-discovery/nova-crawl-links.md)** | `targetId?`, `sameDomainOnly?`, `sameScopeOnly?`, `includeText?`, `deep?`, `urlPattern?` | Instantly extracts and classifies all hyperlinks from an existing active browser tab. |
| **[`nova.site_urls`](tools/crawler-and-discovery/nova-site-urls.md)** | `scopeKey?`, `domain?`, `pathPrefix?`, `limit?`, `includeDead?`, `includeStale?` | Queries the persistent Site-URL-Index for known endpoints, utility scores, and route candidates. |
| **[`nova.site_urls_report`](tools/crawler-and-discovery/nova-site-urls-report.md)** | `reports` | Reports live navigation observations (new pages, 404s, redirects) to the Site-URL-Index. |
| **[`nova.discovery_reset_scope`](tools/crawler-and-discovery/nova-discovery-reset-scope.md)** | `scopeKey?`, `domain?`, `origin?` | Destructively clears all persisted crawl history, results, and URL indexes for a site scope. |
| **[`nova.site_discovery_probe`](tools/crawler-and-discovery/nova-site-discovery-probe.md)** | `url`, `forceRefresh?` | Probes a website for modern AI and MCP discovery endpoints (llms.txt, /.well-known/mcp.json, A2A). |
| **[`nova.site_discovery_get`](tools/crawler-and-discovery/nova-site-discovery-get.md)** | `domain` | Retrieves cached MCP and AI discovery probe results for a domain without network traffic. |

---

## 16. Session Tracing & DOM Event Recording

Network HAR capture, user interaction timelines, DOM change snapshots, and replay verification.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.session_record_start`](tools/session-recording/nova-session-record-start.md)** | `tabId`, `ttlMs?`, `permissionClasses?` | Starts an encrypted background recording of CDP network, DOM mutations, console logs, and interactions. |
| **[`nova.session_record_stop`](tools/session-recording/nova-session-record-stop.md)** | `recordingId`, `reason?` | Stops an active session recording, flushes memory channels, and generates cryptographic integrity manifests. |
| **[`nova.session_record_status`](tools/session-recording/nova-session-record-status.md)** | `recordingId` | Returns the live state, expiry timestamp, active permission classes, and byte counts of a recording. |
| **[`nova.session_record_extend`](tools/session-recording/nova-session-record-extend.md)** | `recordingId`, `additionalMs` | Extends an active recording's time-to-live (TTL), clamped to a 60-minute hard cap. |
| **[`nova.session_record_query`](tools/session-recording/nova-session-record-query.md)** | `recordingId`, `urlMatch?`, `method?`, `statusGte?`, `statusLte?`, `mimeType?`, `hasBody?`, `limit?` | Queries the complete CDP network stream of a finalized recording with rich filters. |
| **[`nova.session_record_get_entry`](tools/session-recording/nova-session-record-get-entry.md)** | `recordingId`, `requestId`, `includeBody?` | Retrieves the complete event timeline, headers, and decoded payload for a single CDP request ID. |
| **[`nova.session_record_events`](tools/session-recording/nova-session-record-events.md)** | `recordingId`, `stream`, `limit?` | Decrypts and streams generic event logs (console, errors, lifecycle, IndexedDB) from a recording. |
| **[`nova.session_record_interactions`](tools/session-recording/nova-session-record-interactions.md)** | `recordingId`, `source?`, `type?`, `targetSelectorMatch?`, `limit?` | Reads the chronological interaction timeline (clicks, typing, form submits) from a recording. |
| **[`nova.session_record_snapshot_dom`](tools/session-recording/nova-session-record-snapshot-dom.md)** | `tabId?`, `recordingId?`, `fullPage?`, `selector?` | Triggers a fresh encrypted DOM snapshot on an active live recording bound to a tab. |
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
| **[`nova.scheduled_task_create`](tools/scheduled-tasks/nova-scheduled-task-create.md)** | `displayName`, `prompt`, `executorKind?`, `cronExpression?`, `intervalSeconds?`, `timeZoneId?`, `mcpAccess?` | Creates a new scheduled task running on cron expressions, intervals, or filesystem change events. |
| **[`nova.scheduled_task_list`](tools/scheduled-tasks/nova-scheduled-task-list.md)** | *(none)* | Lists all scheduled tasks with execution status, next run times, last results, and cumulative costs. |
| **[`nova.scheduled_task_get`](tools/scheduled-tasks/nova-scheduled-task-get.md)** | `taskId` | Retrieves full details of a scheduled task including prompt, schedule, chaining, and budget settings. |
| **[`nova.scheduled_task_update`](tools/scheduled-tasks/nova-scheduled-task-update.md)** | `taskId`, `displayName?`, `prompt?`, `cronExpression?`, `intervalSeconds?`, `timeoutSeconds?` | Updates fields (prompt, schedule, budget, timeouts, chaining) of an existing scheduled task. |
| **[`nova.scheduled_task_delete`](tools/scheduled-tasks/nova-scheduled-task-delete.md)** | `taskId` | Permanently deletes a scheduled task, its configuration, and associated run history. |
| **[`nova.scheduled_task_enable`](tools/scheduled-tasks/nova-scheduled-task-enable.md)** | `taskId` | Enables a paused or circuit-broken scheduled task and resets failure counters. |
| **[`nova.scheduled_task_disable`](tools/scheduled-tasks/nova-scheduled-task-disable.md)** | `taskId` | Pauses execution of a scheduled task without modifying its configuration or history. |
| **[`nova.scheduled_task_trigger`](tools/scheduled-tasks/nova-scheduled-task-trigger.md)** | `taskId`, `inputs?` | Manually triggers an immediate run of a scheduled task with optional dynamic inputs. |
| **[`nova.scheduled_task_runs`](tools/scheduled-tasks/nova-scheduled-task-runs.md)** | `taskId`, `limit?` | Retrieves the run execution history (status, duration, exit code, cost) of a scheduled task. |
| **[`nova.scheduled_task_run_output`](tools/scheduled-tasks/nova-scheduled-task-run-output.md)** | `runId`, `stream?`, `maxLines?` | Memory-safe tail reader for stdout and stderr log streams of a specific task run. |
| **[`nova.scheduled_task_run_cancel`](tools/scheduled-tasks/nova-scheduled-task-run-cancel.md)** | `runId` | Cancels an in-flight background task run asynchronously. |
| **[`nova.scheduled_task_active_runs`](tools/scheduled-tasks/nova-scheduled-task-active-runs.md)** | *(none)* | Lists all currently executing task runs across all background tasks. |
| **[`nova.scheduled_task_templates`](tools/scheduled-tasks/nova-scheduled-task-templates.md)** | *(none)* | Lists pre-built task templates for common automation scenarios (monitoring, scraping, backups). |
| **[`nova.scheduled_task_export`](tools/scheduled-tasks/nova-scheduled-task-export.md)** | *(none)* | Exports all scheduled task definitions as a portable JSON array (excluding secrets and history). |
| **[`nova.scheduled_task_import`](tools/scheduled-tasks/nova-scheduled-task-import.md)** | `tasksJson` | Imports scheduled task definitions from a JSON array, creating fresh task IDs and isolated workspaces. |
| **[`nova.scheduled_task_secret_set`](tools/scheduled-tasks/nova-scheduled-task-secret-set.md)** | `taskId`, `key`, `value` | Stores an encrypted secret (API key, auth token) for a task using Windows DPAPI encryption. |
| **[`nova.scheduled_task_secret_list`](tools/scheduled-tasks/nova-scheduled-task-secret-list.md)** | `taskId`, `limit?`, `offset?` | Lists registered secret key names for a task without exposing plaintext secret values. |
| **[`nova.scheduled_task_var_set`](tools/scheduled-tasks/nova-scheduled-task-var-set.md)** | `taskId`, `key`, `value` | Sets a persistent key-value state variable for a task that survives across runs. |
| **[`nova.scheduled_task_var_get`](tools/scheduled-tasks/nova-scheduled-task-var-get.md)** | `taskId`, `key` | Retrieves the current value of a persistent state variable for a task. |
| **[`nova.scheduled_task_var_list`](tools/scheduled-tasks/nova-scheduled-task-var-list.md)** | `taskId`, `includeValues?`, `limit?`, `offset?` | Lists persistent variable keys and value previews configured for a task. |
| **[`nova.scheduled_task_var_delete`](tools/scheduled-tasks/nova-scheduled-task-var-delete.md)** | `taskId`, `key` | Deletes a persistent state variable from a task. |
| **[`nova.scheduled_task_workspace`](tools/scheduled-tasks/nova-scheduled-task-workspace.md)** | `taskId` | Returns directory metadata, file count, and last run status for a task's isolated workspace. |
| **[`nova.scheduled_task_workspace_list`](tools/scheduled-tasks/nova-scheduled-task-workspace-list.md)** | `taskId`, `relativePath?`, `limit?`, `offset?` | Lists files and subdirectories located within a task's shared workspace folder. |
| **[`nova.scheduled_task_workspace_read`](tools/scheduled-tasks/nova-scheduled-task-workspace-read.md)** | `taskId`, `relativePath` | Reads a UTF-8 text file from a task's shared workspace folder. |
| **[`nova.scheduled_task_workspace_write`](tools/scheduled-tasks/nova-scheduled-task-workspace-write.md)** | `taskId`, `relativePath`, `content` | Atomically writes a UTF-8 text file into a task's shared workspace folder (temp-file + rename). |

---

## 18. Connectors, Mail & File Transfer

IMAP/SMTP email client automation, EML exports, SFTP/FTP server operations, and credential access grants.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.connector_create`](tools/connectors-and-mail/nova-connector-create.md)** | `displayName`, `type`, `host?`, `port?`, `username?`, `password?`, `security?` | Creates an E-Mail account (IMAP/SMTP) or remote server connection (SFTP/FTP). |
| **[`nova.connector_list`](tools/connectors-and-mail/nova-connector-list.md)** | `type?` | Lists configured E-Mail accounts and remote file transfer server connections. |
| **[`nova.connector_update`](tools/connectors-and-mail/nova-connector-update.md)** | `id`, `displayName?`, `host?`, `port?`, `username?`, `password?` | Updates configuration, endpoints, credentials, or signatures of an existing connection. |
| **[`nova.connector_delete`](tools/connectors-and-mail/nova-connector-delete.md)** | `id` | Deletes a connector profile, associated capability grants, and backing DPAPI secrets. |
| **[`nova.connector_grant_set`](tools/connectors-and-mail/nova-connector-grant-set.md)** | `profileId`, `capability`, `mode`, `scope?`, `allowedMailFolders?` | Sets capability access modes (ask, allow, blocked) for a connector. |
| **[`nova.connector_recipient_set`](tools/connectors-and-mail/nova-connector-recipient-set.md)** | `profileId`, `recipients` | Configures recipient allow-lists for autonomous email sending without human prompts. |
| **[`nova.mail_folders`](tools/connectors-and-mail/nova-mail-folders.md)** | `profileId` | Lists the personal IMAP folder tree with total and unread message counts. |
| **[`nova.mail_list`](tools/connectors-and-mail/nova-mail-list.md)** | `profileId`, `folder`, `limit?`, `olderCursor?`, `sinceCursor?` | Lists bounded message metadata (headers, dates, senders) from an exact IMAP folder. |
| **[`nova.mail_read`](tools/connectors-and-mail/nova-mail-read.md)** | `messageId`, `bodyMode?` | Reads the parsed body (text, HTML, markdown) and attachment inventory of a specific email. |
| **[`nova.mail_search`](tools/connectors-and-mail/nova-mail-search.md)** | `profileId`, `query`, `folder?`, `limit?` | Searches mail metadata across the IMAP server and local encrypted search archives. |
| **[`nova.mail_send`](tools/connectors-and-mail/nova-mail-send.md)** | `profileId`, `to`, `subject?`, `bodyText?`, `bodyHtml?`, `attachments?`, `priority?` | Sends an email with optional HTML body, CC/BCC, priority, and attachments via SMTP. |
| **[`nova.mail_draft_create`](tools/connectors-and-mail/nova-mail-draft-create.md)** | `profileId`, `to`, `subject?`, `bodyText?`, `bodyHtml?`, `replaceDraftId?` | Saves an email draft to the server's Drafts folder without sending. |
| **[`nova.mail_mark`](tools/connectors-and-mail/nova-mail-mark.md)** | `messageIds`, `seen?`, `flagged?` | Updates seen and/or flagged status flags for up to 200 messages. |
| **[`nova.mail_move`](tools/connectors-and-mail/nova-mail-move.md)** | `messageIds`, `targetFolder` | Moves up to 200 messages from one mail account to an exact IMAP destination folder. |
| **[`nova.mail_delete`](tools/connectors-and-mail/nova-mail-delete.md)** | `messageIds` | Moves up to 200 messages into the account's Trash folder (non-permanent delete). |
| **[`nova.mail_folder_create`](tools/connectors-and-mail/nova-mail-folder-create.md)** | `profileId`, `name` | Creates a top-level personal IMAP message folder. |
| **[`nova.mail_attachment_save`](tools/connectors-and-mail/nova-mail-attachment-save.md)** | `messageId`, `attachmentIndex`, `localPath?` | Saves a specific email attachment to Downloads or the workspace directory. |
| **[`nova.mail_export_eml`](tools/connectors-and-mail/nova-mail-export-eml.md)** | `messageId?`, `messageIds?`, `localPath?`, `format?` | Exports raw RFC 822 EML files preserving complete MIME headers and original parts. |
| **[`nova.mail_backup_start`](tools/connectors-and-mail/nova-mail-backup-start.md)** | `profileId`, `folders?`, `mode?`, `since?` | Launches a background job to back up an entire mail account or specific folders. |
| **[`nova.mail_backup_status`](tools/connectors-and-mail/nova-mail-backup-status.md)** | `jobId?`, `profileId?` | Reports progress, downloaded message counts, and active phase of a mail backup job. |
| **[`nova.mail_backup_stop`](tools/connectors-and-mail/nova-mail-backup-stop.md)** | `jobId` | Gracefully stops an in-flight mail backup job, committing all downloaded messages. |
| **[`nova.sftp_list`](tools/connectors-and-mail/nova-sftp-list.md)** | `profileId`, `remotePath?`, `maxEntries?` | Lists remote directory entries or inspects file metadata through an SFTP connector. |
| **[`nova.sftp_get`](tools/connectors-and-mail/nova-sftp-get.md)** | `profileId`, `localPath`, `remotePath`, `recursive?`, `maxBytes?`, `overwrite?` | Downloads a remote file or directory tree over SFTP into Downloads or the workspace. |
| **[`nova.sftp_put`](tools/connectors-and-mail/nova-sftp-put.md)** | `profileId`, `localPath`, `remotePath`, `recursive?`, `overwrite?` | Uploads a local file or directory tree over SFTP to a remote destination. |
| **[`nova.sftp_rename`](tools/connectors-and-mail/nova-sftp-rename.md)** | `profileId`, `remotePath`, `destinationRemotePath`, `overwrite?` | Renames or moves a remote file or directory over SFTP. |
| **[`nova.sftp_delete`](tools/connectors-and-mail/nova-sftp-delete.md)** | `profileId`, `remotePath`, `recursive?` | Deletes a remote file, empty directory, or bounded directory tree over SFTP. |
| **[`nova.ftp_list`](tools/connectors-and-mail/nova-ftp-list.md)** | `profileId`, `remotePath?`, `maxEntries?` | Lists remote directory entries or inspects file metadata through an FTP/FTPS connector. |
| **[`nova.ftp_get`](tools/connectors-and-mail/nova-ftp-get.md)** | `profileId`, `localPath`, `remotePath`, `maxBytes?`, `overwrite?` | Downloads a remote regular file over FTP/FTPS into Downloads or the workspace. |
| **[`nova.ftp_put`](tools/connectors-and-mail/nova-ftp-put.md)** | `profileId`, `localPath`, `remotePath`, `maxBytes?`, `overwrite?` | Uploads a local regular file over FTP/FTPS to a remote server. |
| **[`nova.ftp_rename`](tools/connectors-and-mail/nova-ftp-rename.md)** | `profileId`, `remotePath`, `destinationRemotePath`, `overwrite?` | Renames or moves a remote file or directory on an FTP/FTPS server. |
| **[`nova.ftp_delete`](tools/connectors-and-mail/nova-ftp-delete.md)** | `profileId`, `remotePath` | Deletes a remote regular file or empty directory on an FTP/FTPS server. |

---

## 19. Media Intelligence & Whisper Speech-to-Text

In-browser audio/video recording, local OpenAI Whisper transcription, model management, and camera/mic permissions.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.hardware_diagnostics_start`](tools/media-and-transcription/nova-hardware-diagnostics-start.md)** | `kind`, `targetId?` | Initiates in-page hardware diagnostic loop for camera, microphone, or audio speaker output. |
| **[`nova.hardware_diagnostics_state`](tools/media-and-transcription/nova-hardware-diagnostics-state.md)** | `targetId?` | Returns current live hardware diagnostic metrics including microphone audio levels and peak decibels. |
| **[`nova.hardware_diagnostics_stop`](tools/media-and-transcription/nova-hardware-diagnostics-stop.md)** | `kind?`, `reason?`, `targetId?` | Stops in-page hardware diagnostics and releases active camera, microphone, or speaker handles. |
| **[`nova.media_activity_status`](tools/media-and-transcription/nova-media-activity-status.md)** | *(none)* | Returns an O(1) instant snapshot of currently active camera, microphone, and screen-sharing streams. |
| **[`nova.media_activity_audit`](tools/media-and-transcription/nova-media-activity-audit.md)** | `kind?`, `limit?` | Retrieves an audit trail of stored media permissions joined with recent decision records per origin. |
| **[`nova.media_activity_delta`](tools/media-and-transcription/nova-media-activity-delta.md)** | `sinceSequence?`, `limit?` | Performs an incremental read of the in-memory media permission activity ring buffer. |
| **[`nova.media_device_preferences_list`](tools/media-and-transcription/nova-media-device-preferences-list.md)** | `origin?` | Lists stored per-site preferred device IDs (camera, microphone, speaker). |
| **[`nova.media_file_info`](tools/media-and-transcription/nova-media-file-info.md)** | `path` | Inspects media container metadata, duration, channels, and codecs from a local file without ffmpeg. |
| **[`nova.media_permission_activity_list`](tools/media-and-transcription/nova-media-permission-activity-list.md)** | `origin?`, `limit?` | Reads the complete in-memory ring buffer audit log of camera, mic, and screen permission decisions. |
| **[`nova.media_permission_get`](tools/media-and-transcription/nova-media-permission-get.md)** | `origin`, `requestingOrigin?` | Reads the effective and stored media permissions for a specific web origin. |
| **[`nova.media_permission_set`](tools/media-and-transcription/nova-media-permission-set.md)** | `origin`, `camera?`, `microphone?`, `speaker?`, `lifetime?`, `clearAll?` | Sets or clears persistent or session-based camera, mic, speaker, and geolocation permissions. |
| **[`nova.media_permissions_clear_session_grants`](tools/media-and-transcription/nova-media-permissions-clear-session-grants.md)** | *(none)* | Drops all temporary session permissions and halts any live media tracks relying on them. |
| **[`nova.media_permissions_list`](tools/media-and-transcription/nova-media-permissions-list.md)** | `axis?`, `origin?`, `mode?`, `limit?`, `offset?` | Lists all stored per-origin permission overrides along with global default policies. |
| **[`nova.media_status`](tools/media-and-transcription/nova-media-status.md)** | `targetId?` | Inspects playback status, current timestamp, duration, and volume of in-page audio/video elements. |
| **[`nova.media_stop_all`](tools/media-and-transcription/nova-media-stop-all.md)** | `scope?`, `origin?` | Emergency kill switch terminating all active camera, microphone, and screen-sharing tracks browser-wide. |
| **[`nova.media_capture_start`](tools/media-and-transcription/nova-media-capture-start.md)** | `targetId?`, `source?`, `fileName?`, `saveDir?`, `maxBytes?` | Starts streaming capture of live audio/video playing in a tab (WebAudio, MSE, dynamic blobs). |
| **[`nova.media_capture_status`](tools/media-and-transcription/nova-media-capture-status.md)** | `targetId?` | Reports progress, elapsed time, and bytes written for an active in-tab media capture. |
| **[`nova.media_capture_stop`](tools/media-and-transcription/nova-media-capture-stop.md)** | `targetId?` | Stops in-tab media capture, flushes pending segments, closes files, and returns completed paths. |
| **[`nova.media_transcribe_models`](tools/media-and-transcription/nova-media-transcribe-models.md)** | *(none)* | Lists known Whisper speech models, installation statuses, and machine CPU/AVX2 capabilities. |
| **[`nova.media_transcribe_model_install`](tools/media-and-transcription/nova-media-transcribe-model-install.md)** | `modelId?`, `path?` | Downloads a Whisper speech model or adopts an existing local GGML model file. |
| **[`nova.media_transcribe_model_remove`](tools/media-and-transcription/nova-media-transcribe-model-remove.md)** | `fileName` | Deletes an installed speech model file to reclaim disk space or prepare for re-download. |
| **[`nova.media_transcribe_start`](tools/media-and-transcription/nova-media-transcribe-start.md)** | `path`, `model?`, `language?`, `waitMs?` | Transcribes local audio or video files into text entirely on-device using local Whisper.cpp. |
| **[`nova.media_transcribe_status`](tools/media-and-transcription/nova-media-transcribe-status.md)** | `jobId`, `includeText?` | Reports progress, elapsed percentage, and recognized text segments of an active transcription. |
| **[`nova.media_transcribe_stop`](tools/media-and-transcription/nova-media-transcribe-stop.md)** | `jobId` | Stops an in-flight transcription job and returns recognized text segments up to the cancellation point. |

---

## 20. Site Data, Fingerprinting & Sandboxes

Cookie jars, localStorage/sessionStorage, cache purging, browser fingerprint spoofing, and sandbox isolation.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.cookie_list`](tools/site-data-and-identity/nova-cookie-list.md)** | `targetId`, `domainFilter?`, `nameFilter?`, `includeValues?` | Lists cookies for the target tab's profile with metadata (domain, path, flags, expiry). |
| **[`nova.cookie_set`](tools/site-data-and-identity/nova-cookie-set.md)** | `targetId`, `name`, `value`, `domain`, `path?`, `secure?`, `sameSite?` | Sets or updates a cookie in the target sandbox profile's cookie jar. |
| **[`nova.cookie_delete`](tools/site-data-and-identity/nova-cookie-delete.md)** | `targetId`, `cookieId?`, `name?`, `domain?`, `path?` | Deletes a specific cookie by cookieId or by name, domain, and path tuple. |
| **[`nova.cookie_clear`](tools/site-data-and-identity/nova-cookie-clear.md)** | `targetId`, `domain?` | Clears cookies across the target profile, with optional domain filtering. |
| **[`nova.storage_inspect`](tools/site-data-and-identity/nova-storage-inspect.md)** | `targetId`, `storageType`, `includeValues?`, `keyFilter?` | Reads localStorage or sessionStorage key-value pairs for the target page. |
| **[`nova.storage_set`](tools/site-data-and-identity/nova-storage-set.md)** | `targetId`, `storageType`, `key`, `value` | Sets a key-value pair in localStorage or sessionStorage for the target page. |
| **[`nova.storage_delete`](tools/site-data-and-identity/nova-storage-delete.md)** | `targetId`, `storageType`, `key` | Deletes a key from localStorage or sessionStorage for the target page. |
| **[`nova.cache_clear`](tools/site-data-and-identity/nova-cache-clear.md)** | `targetId`, `dataTypes` | Clears HTTP cache, cookies, DOM storage, and indexedDB for the target profile. |
| **[`nova.fingerprint_get`](tools/site-data-and-identity/nova-fingerprint-get.md)** | `tabId?`, `sandboxId?` | Reads the active browser fingerprint protection level (global, sandbox, or tab override). |
| **[`nova.fingerprint_set_global`](tools/site-data-and-identity/nova-fingerprint-set-global.md)** | `level` | Sets the global browser fingerprint protection level across all sandboxes. |
| **[`nova.fingerprint_set_sandbox`](tools/site-data-and-identity/nova-fingerprint-set-sandbox.md)** | `sandboxId`, `level` | Sets or clears the per-sandbox fingerprint protection override. |
| **[`nova.fingerprint_set_tab`](tools/site-data-and-identity/nova-fingerprint-set-tab.md)** | `tabId`, `level` | Sets an ephemeral per-tab fingerprint protection override that expires on tab close. |
| **[`nova.identity_get`](tools/site-data-and-identity/nova-identity-get.md)** | *(none)* | Reads the active browser identity profile, spoofed User-Agent, and client hints. |
| **[`nova.identity_presets`](tools/site-data-and-identity/nova-identity-presets.md)** | *(none)* | Lists available browser identity presets and selectable browser engine versions. |
| **[`nova.identity_set`](tools/site-data-and-identity/nova-identity-set.md)** | `preset?`, `version?`, `customUserAgent?` | Configures and persists a new browser identity profile (preset + version/custom UA). |
| **[`nova.resolve_sandbox`](tools/site-data-and-identity/nova-resolve-sandbox.md)** | `intentKey`, `serviceHint?`, `accountHint?` | Resolves the best matching sandbox container for a given workflow intent. |
| **[`nova.sandbox_context`](tools/site-data-and-identity/nova-sandbox-context.md)** | `targetId` | Returns detailed identity, cookie jar bounds, and context metadata for a specific sandbox. |
| **[`nova.sandbox_create`](tools/site-data-and-identity/nova-sandbox-create.md)** | `name?`, `purpose?`, `color?`, `startUrl?` | Creates a new isolated sandbox profile with dedicated storage, cookies, and cache. |
| **[`nova.sandbox_update`](tools/site-data-and-identity/nova-sandbox-update.md)** | `sandboxId`, `name?`, `color?`, `purpose?`, `isPaused?` | Updates configuration, display name, color tag, or purpose of an existing sandbox. |
| **[`nova.sandbox_delete`](tools/site-data-and-identity/nova-sandbox-delete.md)** | `sandboxId`, `confirm` | Permanently removes a sandbox profile and deletes its storage, cookies, and cache. |
| **[`nova.site_mcp_inspect`](tools/site-data-and-identity/nova-site-mcp-inspect.md)** | `domain` | Inspects a discovered MCP server from cached discovery metadata (identity, transport, auth). |
| **[`nova.site_mcp_connect_request`](tools/site-data-and-identity/nova-site-mcp-connect-request.md)** | `domain` | Requests an authenticated OAuth 2.1 connection to a website's discovered MCP server. |
| **[`nova.site_permissions_reset_origin`](tools/site-data-and-identity/nova-site-permissions-reset-origin.md)** | `origin` | One-click reset of all stored permissions (media, notifications, geolocation) for an origin. |

---

## 21. Episodic Task Memory & Guidance

Task instance tracking, guidance logs, coverage scans, surface exploration, and operator domain notes.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.board_contribute`](tools/task-memory/nova-board-contribute.md)** | `_meta?`, `anchor`, `evidenceRefs?`, `hypothesis?`, `idempotencyKey`, `kind`, `openNew?`, `text`, `topicId?` | Open a new Agent Knowledge Board laboratory topic or append an evidence-bound contribution. Provide exactly one of to... |
| **[`nova.board_get`](tools/task-memory/nova-board-get.md)** | `_meta?`, `anchor?`, `blind?`, `deliveryId?`, `irrelevant?`, `limit?`, `topicId?` | Read one Agent Knowledge Board laboratory topic by topicId or exact structured anchor. Returns the compact symptom pr... |
| **[`nova.coverage_scan`](tools/task-memory/nova-coverage-scan.md)** | `_meta?`, `agentId?`, `scanId`, `scopeOptions?`, `targetId?` | Run a server-registered Coverage Scan script on the resolved tab. Server-trusted by construction — only scripts in th... |
| **[`nova.domain_note`](tools/task-memory/nova-domain-note.md)** | `_meta?`, `domain`, `enforcement?`, `key`, `repeatMinutes?`, `repeatToolCalls?`, `sandboxId?`, `sandboxRef?`, `value` | Store or update a domain-scoped note. Notes are key-value pairs bound to a domain and automatically surfaced in perce... |
| **[`nova.domain_note_ack`](tools/task-memory/nova-domain-note-ack.md)** | `_meta?`, `domain`, `key`, `targetId?` | Explicitly acknowledge a MUST-read site-note block. Equivalent to retrying the blocked tool call: marks the note as a... |
| **[`nova.domain_note_delete`](tools/task-memory/nova-domain-note-delete.md)** | `_meta?`, `domain`, `key`, `sandboxId?`, `sandboxRef?`, `scope?` | Delete a single domain note by domain and key. When both a global and a sandbox-scoped note exist on the same (domain... |
| **[`nova.domain_notes_list`](tools/task-memory/nova-domain-notes-list.md)** | `_meta?`, `domain`, `sandboxId?`, `sandboxRef?`, `scope?` | List all notes for a specific domain. Response includes `sandboxId`, `sandboxName`, `sandboxRef`, and `sandboxStatus`... |
| **[`nova.explore_surface`](tools/task-memory/nova-explore-surface.md)** | `_meta?`, `activate?`, `agentId?`, `close?`, `discover?`, `executionSurface`, `expectedUrl?`, `guardProfile`, `hover?`, `mode`, `routeId?`, `stability?`, `targetId` | Discover interactive UI triggers (buttons, tabs, modals, accordions) on the current page surface, activate them to re... |
| **[`nova.goal_register`](tools/task-memory/nova-goal-register.md)** | `_meta?`, `agentId?`, `content?`, `eventsLimit?`, `goalId?`, `includeEvents?`, `includeSteps?`, `leaseMs?`, `leaseTimeoutMs?`, `mode?`, `op`, `ownerAgent?`, `ownerAgentId?`, `ownerSession?`, `preconditions?`, `preconditionsJson?`, `sidecarSessionId?`, `source?`, `state?`, `steps?`, `summary?`, `targetId?` | Create/query/close/annotate closed-loop goals. Runtime owns step advancement. |
| **[`nova.memory_add_candidate`](tools/task-memory/nova-memory-add-candidate.md)** | `_meta?`, `agentId?`, `claim`, `component`, `confidence?`, `status?`, `targetId` | Add or update a lightweight LCJ candidate for the currently claimed task/tab. Designed for actor-side one-line learni... |
| **[`nova.memory_forget`](tools/task-memory/nova-memory-forget.md)** | `_meta?`, `all?`, `domain?`, `memoryId?`, `memoryType?` | Delete browsing memories. At least one filter parameter is required; domain and memoryType are intersected when both ... |
| **[`nova.memory_note`](tools/task-memory/nova-memory-note.md)** | `_meta?`, `content`, `domain?`, `memoryType?`, `urlPattern?` | Save a browsing memory — a note, preference, or session context for a domain. Memories persist across sessions and ar... |
| **[`nova.memory_recall`](tools/task-memory/nova-memory-recall.md)** | `_meta?`, `domain?`, `includeExpired?`, `limit?`, `memoryType?`, `query?` | Recall browsing memories for a domain or across all domains. Returns user preferences, notes, and session context sav... |
| **[`nova.memory_stats`](tools/task-memory/nova-memory-stats.md)** | `_meta?`, `componentFilter?`, `maxSkipReasons?`, `topComponents?`, `topHosts?`, `topRoutes?`, `topSelectors?`, `windowHours?` | Read LCJ/finalize/outbox memory metrics with derived rates (commit/verification/curation/outbox health). |
| **[`nova.operator_notes_delete`](tools/task-memory/nova-operator-notes-delete.md)** | `_meta?`, `id` | Delete an operator note by ID. |
| **[`nova.operator_notes_list`](tools/task-memory/nova-operator-notes-list.md)** | `_meta?`, `limit?`, `offset?`, `sandboxId?`, `sandboxRef?`, `scope?` | List all operator notes (paginated). Default scope is 'current_sandbox' (active sandbox + global); fails closed to gl... |
| **[`nova.operator_notes_query`](tools/task-memory/nova-operator-notes-query.md)** | `_meta?`, `keywords`, `limit?`, `minScore?`, `sandboxId?`, `sandboxRef?`, `scope?` | Query operator notes by keywords. Uses tag-intersection + TF-IDF content scoring with temporal decay. Returns notes w... |
| **[`nova.operator_notes_store`](tools/task-memory/nova-operator-notes-store.md)** | `_meta?`, `category?`, `content`, `id?`, `sandboxId?`, `sandboxRef?`, `source?`, `tags` | Store or update an operator note. Notes persist across sessions and are surfaced to agents when keywords match tags. ... |
| **[`nova.task_guidance_log_add`](tools/task-memory/nova-task-guidance-log-add.md)** | `_meta?`, `guidanceKind`, `instanceId?`, `payload?`, `profileId?`, `sourceKind`, `sourceRef?` | Log a guidance observation or proposal. Does NOT directly mutate profiles — logs are collected for later explicit pro... |
| **[`nova.task_guidance_logs`](tools/task-memory/nova-task-guidance-logs.md)** | `_meta?`, `guidanceKind?`, `instanceId?`, `limit?`, `profileId?`, `status?` | List guidance log entries with optional filters. Shows learning traces, match telemetry, override patterns, and profi... |
| **[`nova.task_instance_abort`](tools/task-memory/nova-task-instance-abort.md)** | `_meta?`, `clientEventId`, `expectedInstanceRev`, `instanceId`, `outcome?`, `reason` | End a task instance WITHOUT meeting its completion condition — use when the task cannot be finished (site offline, un... |
| **[`nova.task_instance_complete`](tools/task-memory/nova-task-instance-complete.md)** | `_meta?`, `clientEventId`, `completionNote?`, `evidenceReport?`, `expectedInstanceRev`, `instanceId`, `note?` | Request task completion. Evaluates completion policy and returns completed:false with reason if policy is not satisfi... |
| **[`nova.task_instance_create`](tools/task-memory/nova-task-instance-create.md)** | `_meta?`, `adHocContext?`, `agentId?`, `currentScope?`, `declaredTaskKind?`, `overrides?`, `profileId?`, `targetUrl?`, `unitSource?` | Create a new task instance from a profile or ad-hoc context. Snapshots and returns effectiveContextJson, effectiveCon... |
| **[`nova.task_instance_get`](tools/task-memory/nova-task-instance-get.md)** | `_meta?`, `discoveredUnitsPreviewLimit?`, `includeDiscoveredUnitsPreview?`, `includePendingUnits?`, `includeRecentEvents?`, `instanceId`, `pendingUnitsLimit?`, `recentEventLimit?` | Load a task instance snapshot for session-crossing resume. Returns full state including effectiveContextJson/effectiv... |
| **[`nova.task_instance_progress`](tools/task-memory/nova-task-instance-progress.md)** | `_meta?`, `clientEventId`, `discoveredUnits?`, `expectedInstanceRev`, `findings?`, `instanceId`, `mandatoryCheckUpdates?`, `note?`, `resumeStateDelta?`, `setDiscoveryState?`, `unitUpdates?` | Commit delta/append progress to a task instance. Uses compare-and-set (expectedInstanceRev) and idempotency (clientEv... |
| **[`nova.task_instance_reconcile_coverage`](tools/task-memory/nova-task-instance-reconcile-coverage.md)** | `_meta?`, `dryRun?`, `instanceId`, `observationCutoff?` | Replay an instance's observation log against the current unit table and propose discovered -> checked upgrades. dryRu... |
| **[`nova.task_instance_verify`](tools/task-memory/nova-task-instance-verify.md)** | `_meta?`, `instanceId` | Retrieve verification contract steps for a task instance. Returns the tools and assertions the agent should execute b... |
| **[`nova.task_match`](tools/task-memory/nova-task-match.md)** | `_meta?`, `currentScope?`, `domain?`, `platform?`, `targetUrl?`, `taskDescription`, `taskType?` | Find the best matching task profiles for a task description. Returns top-3 with score breakdown and normalized weight... |
| **[`nova.task_profile_get`](tools/task-memory/nova-task-profile-get.md)** | `_meta?`, `profileId` | Get a single task profile with full guidance, mandatory checks, completion condition, and known exceptions. |
| **[`nova.task_profile_upsert`](tools/task-memory/nova-task-profile-upsert.md)** | `_meta?`, `completionCondition?`, `confidence?`, `displayName`, `domain?`, `expectedContentRev?`, `goal`, `knownExceptions?`, `mandatoryChecks?`, `platform?`, `profileId?`, `sourceInstanceId?`, `stableGuidance?`, `taskType` | Create or update a task profile. On update, contentRev is bumped only on semantic change. Optionally seed from an exi... |
| **[`nova.task_profiles`](tools/task-memory/nova-task-profiles.md)** | `_meta?`, `domain?`, `includeArchived?`, `limit?`, `platform?`, `taskType?` | List known task profiles, optionally filtered by taskType, domain, or platform. |
| **[`nova.task_promote_guidance`](tools/task-memory/nova-task-promote-guidance.md)** | `_meta?`, `guidanceLogId`, `profileId` | Explicitly promote a guidance log entry into a profile's stableGuidance. This is a reviewed, intentional action — not... |
| **[`nova.task_promotion_candidates`](tools/task-memory/nova-task-promotion-candidates.md)** | `_meta?`, `profileId`, `threshold?` | List guidance log entries and override patterns that are candidates for promotion into a profile. Returns entries wit... |
| **[`nova.task_search`](tools/task-memory/nova-task-search.md)** | `_meta?`, `domain?`, `limit?`, `platform?`, `query`, `taskType?` | Search for matching task profiles by free-text query. Returns ranked candidates with goal, hasGuidance, usageCount, a... |

---

## 22. App Shell, Dialogs & DevTools

WinUI window controls, native OS dialog handling, DevTools panels, setup wizard, and onboarding injection.

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| **[`nova.agent_activity_summary`](tools/app-shell-and-ui/nova-agent-activity-summary.md)** | `_meta?`, `agentId?`, `sinceMinutes?` | Aggregate this session's MCP tool calls per agent: which agentId ran how many calls on which tabs (targets), top tool... |
| **[`nova.app_info`](tools/app-shell-and-ui/nova-app-info.md)** | `_meta?` | Read app/version/build/runtime/storage metadata (Info / Version / Sysinfo). |
| **[`nova.app_quit`](tools/app-shell-and-ui/nova-app-quit.md)** | `_meta?`, `force?`, `reason?` | Gracefully shut down the entire Nova app. Closes every browser tab and sandbox page and exits the process. The normal... |
| **[`nova.bookmarks_folder_create`](tools/app-shell-and-ui/nova-bookmarks-folder-create.md)** | `_meta?`, `name`, `parentId?` | Create a bookmark folder. Optional parentId nests the folder; omit or pass null for root. Name must be 1..64 printabl... |
| **[`nova.bookmarks_folder_delete`](tools/app-shell-and-ui/nova-bookmarks-folder-delete.md)** | `_meta?`, `id`, `mode?` | Delete a bookmark folder. Mode 'moveToRoot' (default) moves immediate children to root; 'deleteContents' deletes the ... |
| **[`nova.bookmarks_folder_rename`](tools/app-shell-and-ui/nova-bookmarks-folder-rename.md)** | `_meta?`, `id`, `name` | Rename a bookmark folder. |
| **[`nova.bookmarks_folders_list`](tools/app-shell-and-ui/nova-bookmarks-folders-list.md)** | `_meta?` | List bookmark folders (id, name, parentId, sortOrder, depth, createdUtc). Depth -1 means the folder was orphaned and ... |
| **[`nova.cdp`](tools/app-shell-and-ui/nova-cdp.md)** | `_meta?`, `agentId?`, `maxChars?`, `method`, `params?`, `targetId?` | Raw CDP passthrough: call an arbitrary DevTools protocol method (dangerous). Untruncated JSON responses are mirrored ... |
| **[`nova.clipboard_read`](tools/app-shell-and-ui/nova-clipboard-read.md)** | `_meta?` | Read the current text content from the Windows clipboard. |
| **[`nova.clipboard_write`](tools/app-shell-and-ui/nova-clipboard-write.md)** | `_meta?`, `text` | Write text to the Windows clipboard. This is a high-impact overwrite of the current clipboard text and normally requi... |
| **[`nova.create_dump`](tools/app-shell-and-ui/nova-create-dump.md)** | `_meta?`, `agentId?`, `mode?`, `targetId?` | Create a debug dump (screenshot, DOM, resources) for a tab. Writes into NovaBrowser Dumps and returns the dump folder... |
| **[`nova.devtools_open`](tools/app-shell-and-ui/nova-devtools-open.md)** | `_meta?`, `agentId?`, `mode?`, `targetId?` | Open DevTools for a target. Mode can be docked into Nova's browser surface or popout. When omitted, Nova uses the Dev... |
| **[`nova.devtools_select_panel`](tools/app-shell-and-ui/nova-devtools-select-panel.md)** | `_meta?`, `agentId?`, `panel`, `targetId?` | Dispatch the DevTools panel shortcut for a target (for example: elements, console, network). Result distinguishes sho... |
| **[`nova.favorites_add`](tools/app-shell-and-ui/nova-favorites-add.md)** | `_meta?`, `folderId?`, `title?`, `url` | Add or update a favorite/bookmark by URL. When folderId is provided, the favorite is placed into that bookmark folder... |
| **[`nova.favorites_list`](tools/app-shell-and-ui/nova-favorites-list.md)** | `_meta?` | List saved favorites/bookmarks. |
| **[`nova.favorites_move`](tools/app-shell-and-ui/nova-favorites-move.md)** | `_meta?`, `folderId?`, `id?`, `url?` | Move a favorite into a bookmark folder (or to root when folderId is null). Prefer 'id' (from nova.favorites_list) to ... |
| **[`nova.favorites_open`](tools/app-shell-and-ui/nova-favorites-open.md)** | `_meta?`, `agentId?`, `openInNewTab?`, `url` | Open a saved favorite URL in the current active browser tab, or in a new browser tab when requested. If the tabs surf... |
| **[`nova.favorites_remove`](tools/app-shell-and-ui/nova-favorites-remove.md)** | `_meta?`, `id?`, `url?` | Remove a favorite/bookmark. Prefer 'id' (from nova.favorites_list) to delete one specific entry — favorites are not U... |
| **[`nova.get_instructions`](tools/app-shell-and-ui/nova-get-instructions.md)** | `_meta?`, `agentId?`, `detail?`, `domain?`, `domainScope?`, `mode?`, `scope?`, `scopeDomain?`, `targetId?`, `taskKeywords?` | Get the Nova agent contract and operational instructions. Returns the contract text in content text and mirrors it in... |
| **[`nova.get_onboarding`](tools/app-shell-and-ui/nova-get-onboarding.md)** | `_meta?` | Manual onboarding fallback — write the files yourself. Most agents should call nova.install_onboarding instead (one c... |
| **[`nova.grep_resources`](tools/app-shell-and-ui/nova-grep-resources.md)** | `_meta?`, `agentId?`, `caseSensitive?`, `contextChars?`, `maxChars?`, `maxItems?`, `maxMatches?`, `maxResourceChars?`, `pattern`, `regex?`, `source?`, `targetId?`, `types?` | Search loaded text resources (scripts, stylesheets, documents) for a literal string or regex and return compact match... |
| **[`nova.install_onboarding`](tools/app-shell-and-ui/nova-install-onboarding.md)** | `_meta?`, `confirmNewLocation?`, `projectRoot` | Primary onboarding entrypoint — call this when asked to onboard, set up, or install Nova into a project. Writes .nova... |
| **[`nova.list_resources`](tools/app-shell-and-ui/nova-list-resources.md)** | `_meta?`, `agentId?`, `maxItems?`, `source?`, `targetId?`, `types?` | List loaded resources for a tab (scripts/stylesheets/documents). Source is best-effort (CDP resource tree, Performanc... |
| **[`nova.mcp_transport_log`](tools/app-shell-and-ui/nova-mcp-transport-log.md)** | `_meta?`, `caseSensitive?`, `contains?`, `maxLines?`, `run?`, `startLine?` | Read a bounded, redacted view of Nova's own MCP transport/server log from Logs/mcp/mcp-*.log. This is not the browser... |
| **[`nova.ok_observe`](tools/app-shell-and-ui/nova-ok-observe.md)** | `_meta?`, `agentId?`, `claims`, `perceptionId?`, `targetId?` | Push structured observations about current page state. Use canonical signal keys (core.*) from the signal vocabulary.... |
| **[`nova.ok_signal_schema`](tools/app-shell-and-ui/nova-ok-signal-schema.md)** | `_meta?`, `includeDeprecated?`, `maxEntries?`, `namespace?` | List canonical Operational Knowledge signal keys accepted by nova.ok_observe. Use this after unknown core.* key valid... |
| **[`nova.permission_center_get`](tools/app-shell-and-ui/nova-permission-center-get.md)** | `_meta?` | Get global Permission Center defaults (camera/microphone/speaker/geolocation) and currently available media devices, ... |
| **[`nova.permission_center_set`](tools/app-shell-and-ui/nova-permission-center-set.md)** | `_meta?`, `cameraPermissionMode?`, `clearPreferredDevices?`, `geolocationPermissionMode?`, `microphonePermissionMode?`, `preferredCameraDeviceId?`, `preferredMicrophoneDeviceId?`, `preferredSpeakerDeviceId?`, `speakerPermissionMode?`, `validateDeviceIds?` | Update global Permission Center defaults plus preferred camera/microphone/speaker device IDs. geolocationPermissionMo... |
| **[`nova.permission_prompt`](tools/app-shell-and-ui/nova-permission-prompt.md)** | `_meta?`, `description`, `risk_level?`, `schemaVersion?`, `tool_name` | Request permission from the Nova operator to perform an action. Called by the Claude Code sidecar when it needs appro... |
| **[`nova.read_resource`](tools/app-shell-and-ui/nova-read-resource.md)** | `_meta?`, `agentId?`, `charOffset?`, `frameId?`, `maxBytes?`, `maxChars?`, `targetId?`, `url` | Read resource content (best-effort). Prefers CDP Page.getResourceContent and falls back to fetch() for http(s). Use t... |
| **[`nova.read_screenshot_resource`](tools/app-shell-and-ui/nova-read-screenshot-resource.md)** | `_meta?`, `agentId?`, `maxBytes?`, `uri` | Read a Nova screenshot resource URI returned by capture tools (nova://screenshot/...). Convenience wrapper for agents... |
| **[`nova.reference_doc_read`](tools/app-shell-and-ui/nova-reference-doc-read.md)** | `_meta?`, `cursor?`, `docId`, `maxChars?` | Read one allowlisted Nova reference document by docId. Use cursor + maxChars to page large docs; maxChars is clamped ... |
| **[`nova.reference_docs_list`](tools/app-shell-and-ui/nova-reference-docs-list.md)** | `_meta?` | List Nova's bundled reference documents that agents can fetch through MCP when the Nova source repository is not avai... |
| **[`nova.setup_status`](tools/app-shell-and-ui/nova-setup-status.md)** | `_meta?` | Report whether AI programs on this machine are connected to this Nova. Returns per-program state ('connected', 'not_i... |
| **[`nova.setup_wizard_open`](tools/app-shell-and-ui/nova-setup-wizard-open.md)** | `_meta?` | Open Nova's guided connection setup dialog, which walks the user through connecting AI programs (Claude Code, Codex, ... |
| **[`nova.tools_bundle`](tools/app-shell-and-ui/nova-tools-bundle.md)** | `_meta?`, `bundle?`, `includeCatalog?`, `includeDescriptions?`, `includeInputSchema?`, `includeUnavailable?`, `maxResults?`, `query?`, `toolName?` | Two ways in, and the second is the one to reach for when you are unsure: (1) bundle='<id>' returns a curated toolset;... |
| **[`nova.ui_auth_prompt_resolve`](tools/app-shell-and-ui/nova-ui-auth-prompt-resolve.md)** | `_meta?`, `decision`, `username?` | Answer Nova's HTTP sign-in dialog (the one raised by a server's 401 challenge). 'use_vault' signs in with a stored va... |
| **[`nova.ui_certificate_prompt_resolve`](tools/app-shell-and-ui/nova-ui-certificate-prompt-resolve.md)** | `_meta?`, `decision` | Answer Nova's certificate dialog (raised when a server presents a certificate Nova cannot verify). 'refuse' declines ... |
| **[`nova.ui_client_certificate_prompt_resolve`](tools/app-shell-and-ui/nova-ui-client-certificate-prompt-resolve.md)** | `_meta?`, `decision`, `subject?` | Answer Nova's client-certificate dialog (raised when a server asks the browser to identify itself with a certificate)... |
| **[`nova.ui_close_downloads`](tools/app-shell-and-ui/nova-ui-close-downloads.md)** | `_meta?` | Close the download manager panel in the app UI. |
| **[`nova.ui_close_settings`](tools/app-shell-and-ui/nova-ui-close-settings.md)** | `_meta?` | Close the settings overlay in the app UI. |
| **[`nova.ui_confirm_native_dialog`](tools/app-shell-and-ui/nova-ui-confirm-native-dialog.md)** | `_meta?` | Best-effort trigger the primary affirmative action on the currently open host-owned native dialog. For standard dialo... |
| **[`nova.ui_dismiss_native_dialog`](tools/app-shell-and-ui/nova-ui-dismiss-native-dialog.md)** | `_meta?` | Best-effort cancel the currently open host-owned native dialog (for example a file picker or print dialog) by focusin... |
| **[`nova.ui_download_security_prompt_resolve`](tools/app-shell-and-ui/nova-ui-download-security-prompt-resolve.md)** | `_meta?`, `decision` | Answer Nova's question about a download Windows could execute (.exe, .msi, .ps1, .bat and the like). 'discard' does n... |
| **[`nova.ui_get_state`](tools/app-shell-and-ui/nova-ui-get-state.md)** | `_meta?` | Get app UI state (active tab, overlay visibility, UI responsiveness, and whether a host-owned native dialog is curren... |
| **[`nova.ui_inspect_native_dialog`](tools/app-shell-and-ui/nova-ui-inspect-native-dialog.md)** | `_meta?` | Inspect the currently open host-owned native dialog. Returns best-effort button hints and whether Nova detected a sta... |
| **[`nova.ui_open_downloads`](tools/app-shell-and-ui/nova-ui-open-downloads.md)** | `_meta?` | Open the download manager panel in the app UI. |
| **[`nova.ui_open_settings`](tools/app-shell-and-ui/nova-ui-open-settings.md)** | `_meta?`, `section?` | Open the settings overlay (gear icon) in the app UI. Pass 'section' to jump straight to a top-level settings section ... |
| **[`nova.ui_permission_prompt_resolve`](tools/app-shell-and-ui/nova-ui-permission-prompt-resolve.md)** | `_meta?`, `decision?` | End a Nova permission dialog that is blocking tool calls (e.g. a site asking to send notifications). decision='defer'... |
| **[`nova.ui_restore_tabs_prompt_resolve`](tools/app-shell-and-ui/nova-ui-restore-tabs-prompt-resolve.md)** | `_meta?`, `decision` | Resolve the startup restore-tabs prompt with a decision (restore, discard, or not_now). |
| **[`nova.ui_restore_tabs_prompt_state`](tools/app-shell-and-ui/nova-ui-restore-tabs-prompt-state.md)** | `_meta?` | Get startup restore-tabs prompt state and preview of the pending tab snapshot. |
| **[`nova.ui_set_native_dialog_file_name`](tools/app-shell-and-ui/nova-ui-set-native-dialog-file-name.md)** | `_meta?`, `text` | Best-effort fill the standard file-name field of the currently open host-owned file picker dialog. This is intended f... |
| **[`nova.webview_get_zoom`](tools/app-shell-and-ui/nova-webview-get-zoom.md)** | `_meta?`, `agentId?`, `targetId?` | Get the WebView zoom factor (CSS zoom, best-effort). |
| **[`nova.webview_reset_zoom`](tools/app-shell-and-ui/nova-webview-reset-zoom.md)** | `_meta?`, `agentId?`, `targetId?` | Reset the WebView zoom factor to the default 1.0 / 100% (CSS zoom, best-effort). Blocked on PDF tabs with reasonCode=... |
| **[`nova.webview_set_zoom`](tools/app-shell-and-ui/nova-webview-set-zoom.md)** | `_meta?`, `agentId?`, `persistForSite?`, `targetId?`, `zoomFactor` | Set the WebView zoom factor (CSS zoom, best-effort). By default the zoom lasts for this session only; pass persistFor... |
| **[`nova.window_get_bounds`](tools/app-shell-and-ui/nova-window-get-bounds.md)** | `_meta?` | Get the app window bounds (position + size) plus current-monitor and monitor-inventory metadata. |
| **[`nova.window_move`](tools/app-shell-and-ui/nova-window-move.md)** | `_meta?`, `monitorIndex`, `position?` | Move the app window to a selected monitor work area using a monitor index from nova.window_get_bounds.availableMonito... |
| **[`nova.window_set_size`](tools/app-shell-and-ui/nova-window-set-size.md)** | `_meta?`, `height`, `width` | Resize the app window (best-effort). |
| **[`nova.window_set_state`](tools/app-shell-and-ui/nova-window-set-state.md)** | `_meta?`, `state` | Set the app window state: minimize, maximize, restore, or bring to foreground. |

---

## Next Steps

* Review protocol communication in **[Protocol & Transport](protocol-and-transport.md)**.
* Return to the **[MCP Reference Index](README.md)**.
