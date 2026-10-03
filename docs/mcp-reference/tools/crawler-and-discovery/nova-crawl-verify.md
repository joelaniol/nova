# `nova.crawl_verify`

Performs targeted, non-traversal verification and DOM extraction against a specific list of URLs.

---

## 1. Overview

`nova.crawl_verify` visits an explicit list of URLs in isolated hidden WebViews without following outbound hyperlinks. It is designed for regression testing, link health validation, selector assertions, and deterministic data scraping across up to 50 URLs in a single call.

* **Capability Bundle:** `crawler_ops`
* **Security Tier:** Tier 2 (Targeted Verification)
* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`urls`** | `array of strings` | Yes | `none` | Array of up to 50 absolute HTTP/HTTPS URLs to verify. |
| **`assert`** | `object` | No | `null` | Optional selector assertion (e.g. `{ selector: ".checkout-btn", present: true }`). |
| **`extractMetadata`** | `boolean` | No | `true` | Extract page titles, meta tags, and HTTP statuses. |
| **`extractContent`** | `boolean` | No | `false` | Extract page text or markdown content. |
| **`contentSelector`** | `string` | No | `null` | CSS selector scoping content extraction. |
| **`captureScreenshots`** | `boolean` | No | `false` | Capture visual screenshots for verified pages. |
| **`customScript`** | `string` | No | `null` | Custom JavaScript snippet executed after JS settlement returning structured JSON. |
| **`pageDelayMs`** | `integer` | No | `500` | Minimum delay between visits on the same origin. |
| **`parallel`** | `integer` | No | `1` | Concurrent worker count (1-3). |
| **`targetId`** | `string` | No | `null` | Target tab ID to share cookies, session tokens, and local storage. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
      "present": true
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
      "text": "Verified 2 URLs: 2 successful, 0 failed, 0 assertion errors."
    }
  ],
  "structuredContent": {
    "ok": true,
    "verifiedCount": 2,
    "results": [
      {
        "url": "https://docs.example.com/api/auth",
        "httpStatus": 200,
        "title": "Authentication — Example Docs",
        "assertionPassed": true,
        "settleTimeMs": 410
      },
      {
        "url": "https://docs.example.com/api/pricing",
        "httpStatus": 200,
        "title": "API Pricing & Tiers — Example Docs",
        "assertionPassed": true,
        "settleTimeMs": 380
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Automated Regression Checks:** Use `assert` to verify critical DOM elements exist after deployment across multiple key endpoints.
* **Custom Scrape Probes:** Supply `customScript` to evaluate complex page state and return typed JSON without manual step navigation.
* **Bounded Batch Size:** Maximum 50 URLs per call ensures deterministic execution and prevents hanging workers.

---

## 5. Related Tools

* [`nova.crawl_start`](nova-crawl-start.md) — Full BFS crawler.
* [`nova.crawl_links`](nova-crawl-links.md) — Quick tab link extraction.
