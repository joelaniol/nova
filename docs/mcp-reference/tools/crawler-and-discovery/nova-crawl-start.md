# `nova.crawl_start`

Starts a background breadth-first search (BFS) crawl from a root URL using isolated hidden WebViews.

---

## 1. Overview

`nova.crawl_start` launches an autonomous, background crawler task that navigates a website according to breadth-first traversal rules. It runs entirely inside dedicated hidden WebView2 instances without interfering with the user's active browser tabs or visual viewport.

The crawler automatically detects DOM settlement (waiting for MutationObserver quiescence and network idle), extracts structured page metadata, follows in-scope hyperlinks, respects rate limits, and persists results into the local SQLite `crawl.db` index.

* **Capability Bundle:** `crawler_ops`
* **Security Tier:** Tier 2 (Autonomous Navigation)
* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity that becomes the owner of the crawl job. Subsequent crawl_status, crawl_results, and crawl_stop calls for this crawlId must use the same agentId. Defaults to 'default'. |
| `targetId` | `string` | No | — | — | Optional visible target whose browser profile should be reused for the hidden crawl WebView. Use this to crawl inside the same cookie/localStorage context as an existing tab or sandbox. When provided, the call must also satisfy that target's claim owner/session gate, and Nova will reject the start if the visible target currently depends on fragile live-tab SPA/auth state that a hidden crawler cannot safely preserve. |
| `startUrl` | `string` | Yes | — | — | Absolute http/https URL to start crawling from. |
| `url` | `string` | No | — | — | Compatibility alias for startUrl. Must match startUrl when both are provided. |
| `maxDepth` | `integer` | No | `2` | 0–10 | BFS depth limit. 0 = only the start page (no link following). |
| `maxPages` | `integer` | No | `30` | 1–500 | Maximum number of pages to visit before stopping. |
| `sameDomainOnly` | `boolean` | No | `true` | — | If true, only follow links on the same effective crawl domain. After the first successfully loaded page, the scope rebinds to that page's final host so canonical redirects like example.com -> www.example.com do not collapse the crawl to a single page. |
| `sameScopeOnly` | `boolean` | No | `true` | — | Preferred clarity alias for sameDomainOnly. In hidden mode this means the effective crawl host after canonical rebind; in live_tab mode the runtime tightens further to same-origin and same port. Must match sameDomainOnly if both are provided. |
| `urlPattern` | `string` | No | — | — | Optional regex filter — only follow URLs matching this pattern. |
| `excludePattern` | `string` | No | — | — | Optional regex filter — skip URLs matching this pattern. |
| `extractContent` | `boolean` | No | `false` | — | If true, extract page content. This legacy flag is also enabled implicitly when contentMode, contentSelector, or excludeSelectors is provided. |
| `contentMode` | `string` | No | `"text_blob"` | `text_blob`, `structured` | Content output mode. 'text_blob' keeps the legacy flat textContent field only. 'structured' keeps textContent and also returns lightweight semantic contentBlocks per page. |
| `contentSelector` | `string` | No | — | — | Optional CSS selector that scopes content extraction to one subtree. If the selector matches nothing, the crawler falls back to the page body/root for that page. |
| `excludeSelectors` | `array` of `string` | No | — | — | Optional list of CSS selectors to remove from a detached clone before content extraction. Useful for excluding repeated chrome like header, footer, nav, cookie banners, or sidebars. |
| `extractMetadata` | `boolean` | No | `true` | — | If true, extract title, meta description, and headings per page. |
| `settleTimeMs` | `integer` | No | `3000` | 500–15000 | Maximum time in ms to wait for JS settlement (MutationObserver quiet + network idle) per page. |
| `pageDelayMs` | `integer` | No | `500` | 200–5000 | Global minimum spacing in ms between page starts on the same origin. Parallel workers share this origin gate, so they cannot multiply the configured host rate. |
| `validateLinks` | `boolean` | No | `false` | — | If true, detect hydration drift on SPA pages by comparing <a href> with the actual same-document router target observed after a trusted click. The probe installs pass-through observers for pushState/replaceState plus same-document hash/popstate changes, snapshots original hrefs before mutating clicks, polls briefly after each trusted click so delayed same-document router commits stay observable, skips obvious logout/delete/download-style same-origin links from the sample, dispatches trusted CDP-backed clicks so isTrusted/pointer-gated routers stay observable, and samples links from the top document, open shadow roots, and same-origin iframes. Only links with an observable route target count as validated samples, and the loop stops once the live SPA leaves the initial route. Only runs on pages where a JS framework with client-side routing is detected. crawl_results surfaces page-level drift fields (hydrationDriftDetected, hydrationDriftRatio, hydrationDriftSampleSize) so callers can treat extracted SPA hrefs as heuristic; domain-level PKS auto-learning only escalates once at least 5 validated links were observed for the domain. This flag is invalid together with targetId because trusted probe clicks must not run inside a claimed live-profile crawl. |
| `maxConsecutiveErrors` | `integer` | No | `5` | 1–50 | Circuit breaker threshold: after this many consecutive failures on the same domain, the crawler skips remaining URLs on that domain until a 60s cooldown expires. |
| `backoffStrategy` | `string` | No | `"exponential"` | `none`, `linear`, `exponential` | Adaptive delay strategy for ordinary error streaks. 'none': fixed pageDelayMs unless a 429/circuit-breaker protection path is active. 'linear': +500ms per consecutive error. 'exponential': multiply by 1.5x per consecutive error (recommended). HTTP 429 still applies a dedicated rate-limit cooldown floor. |
| `maxBackoffMs` | `integer` | No | `10000` | 1000–60000 | Maximum adaptive delay cap in ms. Backoff delay never exceeds this value. |
| `captureScreenshots` | `boolean` | No | `false` | — | Capture a screenshot artifact for each page after JS settlement. crawl_results returns lightweight screenshot metadata by default (`screenshotDetail='meta'`) and only loads inline image/base64 payloads when you explicitly request `screenshotDetail='full'`. Hidden crawls support this fully; `crawlMode='live_tab'` rejects screenshot capture and screenshot tuning args with Invalid params. |
| `screenshotFormat` | `string` | No | `"jpeg"` | `png`, `jpeg` | Screenshot format. JPEG is recommended for crawls (smaller, quality-adjustable). Only valid for hidden crawls; live_tab rejects screenshot tuning args. |
| `screenshotQuality` | `integer` | No | `75` | 1–100 | JPEG quality (1-100). Ignored for PNG. Lower = smaller files. Only valid for hidden crawls; live_tab rejects screenshot tuning args. |
| `screenshotMaxWidth` | `integer` | No | `800` | 100–3840 | Maximum screenshot width in pixels. Page is scaled down if wider. Only valid for hidden crawls; live_tab rejects screenshot tuning args. |
| `screenshotMaxHeight` | `integer` | No | `600` | 100–2160 | Maximum screenshot height in pixels. Only valid for hidden crawls; live_tab rejects screenshot tuning args. |
| `screenshotHighlight` | `array` of `string` | No | — | ≤ 20 items | CSS selectors to highlight with a red dashed outline in screenshots. The outline is injected before and removed after each screenshot. Use to visually mark elements for QM reports (e.g., untranslated nav items, missing alt text). Only valid for hidden crawls; live_tab rejects screenshot tuning args. |
| `respectRobotsTxt` | `boolean` | No | `false` | — | When true, fetch and respect robots.txt on the effective canonical crawl origin: skip matched Disallow paths and apply Crawl-Delay. The parser now uses explicit User-agent groups plus wildcard/end-anchor matching. When false (default), robots.txt is still fetched only for BFS crawls and exposed diagnostically in crawl_status, but not enforced. `crawlMode='live_tab'` rejects this flag because robots/site discovery is hidden-crawler-only. |
| `useSitemap` | `boolean` | No | `false` | — | When true, fetch sitemap discovery on the effective canonical crawl origin and seed the BFS queue with discovered URLs at depth 0. Robots.txt Sitemap directives, multiple sitemap files, sitemap indexes, relative Sitemap paths, and common fallback paths are resolved with truncation metadata visible in crawl_status. When false, sitemap discovery is skipped entirely. `crawlMode='live_tab'` rejects this flag because sitemap discovery is hidden-crawler-only. |
| `parallel` | `integer` | No | `1` | 1–3 | Number of parallel hidden WebViews for page processing. 1=sequential (default), 2-3=parallel. Each extra WebView uses ~150MB RAM. Pages are processed from the shared BFS queue without duplicate visits, while pageDelayMs remains a shared per-origin start limit. |
| `taskInstanceId` | `string` | No | — | — | Optional ETM task instance ID to bind this crawl to. On completion, the crawl is recorded as an artifact event on the task instance. The instance must exist (validated at start). |
| `customScript` | `string` | No | — | — | JavaScript body to execute after JS settlement on each page. Return a JSON-serializable value (use `return {...}`). Promise returns and async/await are awaited through Runtime.evaluate; pages[].customScriptStatus distinguishes ok, timeout, and execution_failed. Use for custom data extraction and keep scripts side-effect-free — do not click, navigate, or modify the DOM. |
| `customScriptTimeoutMs` | `integer` | No | `5000` | 500–30000 | Timeout for awaited custom script execution per page in ms. |
| `crawlMode` | `string` | No | `"hidden"` | `hidden`, `live_tab` | hidden: dedicated background WebView (default, fast, no auth). live_tab: crawl inside the visible target tab via SPA-route clicks (slow, sequential, preserves session/auth). live_tab requires targetId, forces sameDomainOnly=true and parallel=1, rejects screenshot capture plus robots/sitemap discovery flags, and keeps history scope on the effective origin instead of collapsing to host-only. |
| `deltaMode` | `boolean` | No | `false` | — | If true, enable advisory Site-URL-Index delta seeding for hidden path-routed crawls only. Active path routes with a stored content hash are pre-skipped as already known; this does not pre-detect content changes, and hash-routed/hashbang SPA routes are excluded from delta seeding. Requires a prior crawl with extractContent=true to have populated hash-bearing Site-URL-Index entries. `crawlMode='live_tab'` rejects this flag with Invalid params. The response mirrors deltaMode only when eligible hidden-mode index hashes were actually found; otherwise the request proceeds normally without a deltaMode block. |
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.crawl_start",
  "arguments": {
    "startUrl": "https://docs.example.com/api",
    "maxPages": 25,
    "maxDepth": 2,
    "extractMetadata": true,
    "extractContent": true,
    "contentSelector": "main",
    "pageDelayMs": 750
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Background crawl job started with ID 'crawl-4a92c81e' on https://docs.example.com/api (max 25 pages, depth 2)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "crawlId": "crawl-4a92c81e",
    "status": "running",
    "startUrl": "https://docs.example.com/api",
    "scopeKey": "https://docs.example.com",
    "maxPages": 25,
    "maxDepth": 2,
    "queuedPages": 1
  }
}
```

---

## 4. Operational Best Practices

* **Polling Progress:** Use [`nova.crawl_status`](nova-crawl-status.md) to inspect crawl progression rather than making blocking wait calls.
* **Targeted Content Extraction:** Always specify `contentSelector: "main"` or `contentSelector: "article"` when enabling `extractContent: true` to avoid ingesting repetitive navigation and footer boilerplate.
* **Session Continuity:** Pass `targetId` if the target website requires an active authenticated session from an existing browser tab.

---

## 5. Related Tools

* [`nova.crawl_status`](nova-crawl-status.md) — Monitor crawl progress and page counters.
* [`nova.crawl_results`](nova-crawl-results.md) — Retrieve discovered URLs and extracted content.
* [`nova.crawl_stop`](nova-crawl-stop.md) — Cancel a running crawl job.
