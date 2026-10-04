# `nova.session_reset_screenshot_budget`

Resets the session screenshot budget counter to allow fresh visual captures.

---

## 1. Overview

`nova.session_reset_screenshot_budget` clears the in-memory cumulative inline-image-bytes counter Nova tracks per MCP session for visual-evidence tools. Nova warns once cumulative inline screenshot bytes for a session cross a soft threshold and refuses further inline images past a hard cap, to bound how much image data one session can push inline; this tool resets both counters back to zero so a long testing session can keep capturing.

* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundles: `page_read_debug`, `visual_evidence`.
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.session_reset_screenshot_budget",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Screenshot session budget reset for current MCP session. Previous inline bytes: 6291456; screenshots: 14."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "reset",
    "reasonCode": "screenshot_budget_reset",
    "scope": "current_mcp_session",
    "sessionKey": "sess-4a21",
    "hadBudget": true,
    "previousCumulativeAagInlineMediaBytes": 6291456,
    "previousScreenshotCount": 14,
    "currentCumulativeAagInlineMediaBytes": 0,
    "currentScreenshotCount": 0
  }
}
```

If the session had not captured any inline screenshots yet, `status` is `"noop"`, `reasonCode` is `"screenshot_budget_not_found"`, and `hadBudget` is `false` (the `previous*` fields are still `0`).

---

## 4. Operational Best Practices

* **Post-Exhaustion Recovery:** Call when a multi-step test intentionally exhausts the cumulative inline-bytes budget (soft-warn around 5 MB, hard cap around 20 MB per session) and requires fresh inline captures for subsequent phases.
* **Session-Scoped:** Only affects the current MCP client session; does not alter global configuration or other sessions.

---

## 5. Related Tools

* [`nova.capture_screenshot`](../visual-evidence/nova-capture-screenshot.md) — Capture visual evidence.
* [`nova.screenshot_diff`](../visual-evidence/nova-screenshot-diff.md) — Pixel diffing.
