# `nova.crawl_verify`

Performs targeted, non-traversal verification and DOM extraction against a specific list of URLs.

---

## 1. Overview

`nova.crawl_verify` queues a background job (depth 0, no link following) that visits an explicit list of up to 50 URLs in isolated hidden WebViews. Like `nova.crawl_start`, it runs asynchronously: the call itself only returns a `crawlId` and `status: "running"` once the URLs are queued — per-URL results (HTTP status, assertions, extracted content) must be fetched afterward with [`nova.crawl_results`](nova-crawl-results.md) or watched with [`nova.crawl_status`](nova-crawl-status.md), not read from this call's own response.

* **Core Architecture Guide:** [Autonomous Crawler & URL Discovery](../../../core-features/crawler-and-discovery/crawler/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity for crawl ownership. Defaults to 'default'. |
| `targetId` | `string` | No | — | — | Optional claimed target whose shared WebView2 user-data root, ProfileName, cookies, and persistent origin storage are reused. Nova checks profile/cookie/auth parity per URL and attempts canonical no-requested-navigation WebView recovery if the still-known target lost its Core. Required when viewportMode='target'. Without targetId, uses the isolated crawler profile. |
| `urls` | `array` of `string` | Yes | — | 1–50 items | Array of absolute http/https URLs to verify. The raw array is capped at 50 entries before any duplicate collapsing, and each URL is visited once at depth 0 (no link following). |
| `extractContent` | `boolean` | No | `false` | — | Extract page content for each URL. |
| `contentMode` | `string` | No | `"text_blob"` | `text_blob`, `structured` | Content extraction mode. |
| `contentSelector` | `string` | No | — | — | CSS selector to scope content extraction. |
| `excludeSelectors` | `array` of `string` | No | — | — | CSS selectors to exclude from content extraction. |
| `extractMetadata` | `boolean` | No | `true` | — | Extract title, meta description, headings. |
| `settleTimeMs` | `integer` | No | `3000` | 500–15000 | JS settlement wait time per page. |
| `pageDelayMs` | `integer` | No | `500` | 200–5000 | Global minimum spacing in milliseconds between page starts, enforced per origin. Every verify worker shares this per-origin gate, so parallel workers cannot multiply the configured host rate. |
| `parallel` | `integer` | No | `1` | 1–3 | Maximum simultaneously active hidden verify workers. 1 preserves serial behavior; 2-3 process independent URLs concurrently while sharing per-origin rate and burst gates. Extra target-bound workers reuse the hidden profile context and do not navigate the visible target tab. |
| `burstSize` | `integer` | No | `1` | 1–50 | Maximum number of page starts per origin in one burst. The default 1 is conservative; burstDelayMs=0 means pageDelayMs alone spaces starts. |
| `burstDelayMs` | `integer` | No | `0` | 0–60000 | Minimum pause in milliseconds between bursts on the same origin. 0 disables an extra burst pause while pageDelayMs remains enforced. |
| `maxConsecutiveErrors` | `integer` | No | `5` | 1–50 | Per-origin circuit-breaker threshold for consecutive 403, 429, transport, or other classified failures. |
| `backoffStrategy` | `string` | No | `"exponential"` | `none`, `linear`, `exponential` | Per-origin adaptive start-delay strategy after classified errors. Retry-After and the dedicated 429 floor remain authoritative even when 'none' is selected. |
| `maxBackoffMs` | `integer` | No | `10000` | 1000–60000 | Maximum adaptive per-origin backoff delay in milliseconds, except the existing dedicated 429 safety floor. |
| `captureScreenshots` | `boolean` | No | `false` | — | Capture a screenshot artifact for each verified URL after JS settlement. Later crawl_results calls expose screenshot metadata by default and only expand to inline image/base64 payloads when `screenshotDetail='full'` is requested. |
| `screenshotFormat` | `string` | No | `"jpeg"` | `png`, `jpeg` | Screenshot format. |
| `screenshotQuality` | `integer` | No | `75` | 1–100 | JPEG quality. |
| `screenshotMaxWidth` | `integer` | No | `800` | 100–3840 | Maximum screenshot width. |
| `screenshotMaxHeight` | `integer` | No | `600` | 100–2160 | Maximum screenshot height. |
| `screenshotHighlight` | `array` of `string` | No | — | ≤ 20 items | CSS selectors to highlight with a red dashed outline in screenshots. |
| `taskInstanceId` | `string` | No | — | — | Optional ETM task instance ID to bind this verify run to. On completion, the verify crawl is recorded as an artifact event on the task instance. The instance must exist (validated at start). |
| `customScript` | `string` | No | — | — | JavaScript body to execute after JS settlement on each verified page. Return a JSON-serializable value (for example `return { postCount: document.querySelectorAll('[data-section-id=Post]').length };`). Promise returns and async/await are awaited through Runtime.evaluate; pages[].customScriptStatus distinguishes ok, timeout, execution_failed, skipped_incomplete, and skipped_navigation_error, so a legitimate empty object is not ambiguous. Cannot be combined with readOnlyPopover because arbitrary code cannot carry its read-only guarantee. |
| `customScriptTimeoutMs` | `integer` | No | `5000` | 500–30000 | Timeout for awaited custom script execution per verified page in ms. |
| `waitFor` | `object` | No | — | — | Optional declarative readiness gate evaluated after navigation and before extraction. The selector must reach minMatches continuously for stableForMs before timeoutMs; otherwise the page is incomplete with an explicit reasonCode. |
| `waitFor.selector` | `string` | Yes | — | 1–2048 characters | CSS selector that represents page readiness. Use a profile-ready selector when an empty content list is a valid outcome. |
| `waitFor.minMatches` | `integer` | No | `1` | 1–10000 | Minimum number of matching elements required for readiness. |
| `waitFor.timeoutMs` | `integer` | No | `15000` | 500–30000 | Maximum readiness wait in milliseconds. |
| `waitFor.stableForMs` | `integer` | No | `750` | 0–5000 | Continuous time in milliseconds that the match count must remain at or above minMatches. |
| `assert` | `object` | No | — | — | Optional post-extraction selector assertion. Failure marks the page incomplete even when navigation returned HTTP 200; point it at a profile-ready selector when zero domain items is a valid result. |
| `assert.selector` | `string` | Yes | — | 1–2048 characters | CSS selector whose final match count is asserted. |
| `assert.minMatches` | `integer` | No | `1` | 1–10000 | Minimum final match count required for a complete page result. |
| `renderMode` | `string` | No | `"auto"` | `auto`, `hidden`, `active` | Hidden-WebView rendering mode. 'auto' requests Page activation plus active lifecycle/focus emulation for target-bound verifies and plain hidden mode otherwise. 'active' requests that behavior explicitly without navigating or covering the visible user tab. 'hidden' disables it. pages[].runtimeContext reports the applied mode and actual document.visibilityState/document.hidden. |
| `viewportMode` | `string` | No | `"compact"` | `compact`, `target` | Hidden-WebView viewport source. 'compact' keeps the explicit 1280x720, DPR 1 performance viewport. 'target' requires targetId, snapshots that target's effective window.innerWidth/window.innerHeight/devicePixelRatio at verify start, applies the snapshot before navigation, and fails with a reasonCode instead of falling back when the target is unavailable. pages[].runtimeContext reports viewportSource plus the actual effective dimensions and deviceScaleFactor. |
| `readOnlyPopover` | `object` | No | — | — | Optional passive DOM-only popover/menu extraction after page settlement. Nova resolves an already-present panel and reads it without click, hover, focus, event dispatch, submit, send, purchase, navigation, or DOM mutation. Panels mounted only after interaction return panel_not_found. Mutually exclusive with customScript. |
| `readOnlyPopover.openerSelector` | `string` | Yes | — | 1–2048 characters | CSS selector for the opener. Nova reads its relationship attributes but never activates it. |
| `readOnlyPopover.panelSelector` | `string` | No | — | 1–2048 characters | Optional explicit CSS selector for the already-present panel. When omitted, Nova resolves aria-controls, aria-owns, popovertarget, data-target, data-bs-target, or a hash href on the opener. |
| `readOnlyPopover.itemSelector` | `string` | No | `"button,[role=\u0022menuitem\u0022],[role=\u0022option\u0022],li,a"` | 1–2048 characters | CSS selector evaluated inside the resolved panel for bounded item extraction. |
| `readOnlyPopover.labelSelector` | `string` | No | — | 1–2048 characters | Optional CSS selector evaluated inside each item before reading its label. |
| `readOnlyPopover.labelAttribute` | `string` | No | — | 1–128 characters | Optional attribute to read as the item label instead of textContent. |
| `readOnlyPopover.valueSelector` | `string` | No | — | 1–2048 characters | Optional CSS selector evaluated inside each item before reading its value. |
| `readOnlyPopover.valueAttribute` | `string` | No | — | 1–128 characters | Optional attribute to read as the item value instead of textContent. |
| `readOnlyPopover.maxItems` | `integer` | No | `50` | 1–50 | Maximum number of panel items returned per URL. matchedItemCount and truncated remain truthful when more items exist. |
| `readOnlyPopover.maxTextChars` | `integer` | No | `4000` | 100–20000 | Maximum characters returned for the panel text per URL. |
| `research` | `object` | No | — | — | Optional deterministic research mode. An inline recipe registers its exact customScript/schema/provenance/replay definition immutably by owner agent ID + recipe ID/version; source=stored lets the same owner reuse that Nova-owned definition without resending it. The script must return exactly `{ state, records }`; Nova validates records, commits page/checkpoint/records transactionally, skips completed inputs on explicit resume, and atomically materializes the selected Nova-owned export sink. No LLM roundtrip occurs per page. |
| `research.runId` | `string` | No | — | 1–48 characters | Stable research-run identifier. Omit for a new generated ID; supply the returned ID together with resume=true after interruption, rate limiting, or login handoff. |
| `research.resume` | `boolean` | No | `false` | — | Resume an existing runId. The URL list/order and recipe hash must match exactly; inputs already checkpointed as completed are not revisited. |
| `research.recipe` | `object` | Yes | — | — | Versioned immutable recipe identity. Inline definitions are registered on first successful run start; source=stored loads the exact script, schema, provenance, sink format, and replay fixtures from crawl.db. |
| `research.recordSchema` | `object` | No | — | — | Strict typed schema applied to every record before any dataset commit. The configured key field provides exactly-once record identity across resume attempts. |
| `research.sink` | `object` | No | — | — | Atomically replaced export snapshot under Nova's own Exports/Research directory. crawl.db remains the authoritative checkpoint across crashes. |
| `research.replayCases` | `array` of `object` | No | — | ≤ 20 items | Optional deterministic replay assertions. scriptResult revalidates a legacy stored result envelope; pageState.html loads a CSP-isolated offline Chromium DOM and executes the exact recipe customScript before any live URL navigation. |

Capability bundle: `crawler_ops` (load it with `nova.tools_bundle(bundle='crawler_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.crawl_verify",
  "arguments": {
    "urls": [
      "https://docs.example.com/api/auth",
      "https://docs.example.com/api/pricing"
    ],
    "extractMetadata": true,
    "assert": {
      "selector": "h1",
      "minMatches": 1
    }
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Verify started: 2 of 2 URLs queued as crawl crawl-7c3e19aa. Use crawl_status/crawl_results to track progress."
    }
  ],
  "structuredContent": {
    "crawlId": "crawl-7c3e19aa",
    "status": "running",
    "crawlKind": "verify",
    "crawlMode": "hidden",
    "ownerAgentId": "default",
    "urlCount": 2,
    "queuedUrlCount": 2,
    "urls": [
      "https://docs.example.com/api/auth",
      "https://docs.example.com/api/pricing"
    ],
    "pollAfterMs": 500,
    "retentionMode": "best_effort",
    "terminalRetentionMinutes": 30,
    "maxRetainedTerminalCrawls": 12,
    "taskInstanceId": null,
    "advisoryNote": "Use crawl_results(crawlId) to retrieve per-URL verification results. The verify job follows no links (depth=0) and visits only the provided URLs."
  }
}
```

There is no top-level `ok` field, and no immediate `verifiedCount`/`results[]`/`assertionPassed` in this response — that per-URL detail (HTTP status, title, `assert`/`waitFor` outcome, timings) is what [`nova.crawl_results`](nova-crawl-results.md) returns once the queued URLs have been visited. Also note `assert`'s field is `minMatches` (a match-count threshold), not a boolean `present`.

---

## 4. Operational Best Practices

* **Automated Regression Checks:** Use `assert` to verify critical DOM elements exist after deployment across multiple key endpoints, then read the outcome via `nova.crawl_results`.
* **Custom Scrape Probes:** Supply `customScript` to evaluate complex page state and return typed JSON without manual step navigation.
* **Bounded Batch Size:** Maximum 50 URLs per call ensures deterministic execution and prevents hanging workers.
* **Poll for Completion:** Since the call itself only queues the job, poll [`nova.crawl_status`](nova-crawl-status.md) (or call `nova.crawl_results` once `resultsComplete`/`status` indicates it finished) before reading results.

---

## 5. Related Tools

* [`nova.crawl_start`](nova-crawl-start.md) — Full BFS crawler.
* [`nova.crawl_links`](nova-crawl-links.md) — Quick tab link extraction.
