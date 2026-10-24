# `nova.browser_api_evidence`

> **Shows, per category of fingerprint-relevant browser APIs, where a page's loaded scripts mention them and which calls a recording actually observed — kept apart.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.browser_api_evidence` answers "which browser APIs does this page use for fingerprinting?" without mixing two very different kinds of proof.

* **Static evidence** — names such as `toDataURL`, `getParameter` or `hardwareConcurrency` in the tab's already-loaded scripts and documents. The tab is read passively: no new request, no page code. A name in a script only proves that the text exists, not that it ran.
* **Observed evidence** — calls recorded by a finished session recording that was started with `permissionClasses: ["api_calls"]`. That recording wraps the APIs inside the page, so it is active and a page can detect it. Start it only when that is acceptable.

Categories: `webrtc`, `canvas`, `webgl`, `audio`, `hardware`, `screen`, `language`, `timezone`, `fonts`. Neither kind of evidence proves a fingerprinting purpose. Workers and aliased or obfuscated access are not covered, and nothing is recorded after the fact.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. The static scan reads this tab's loaded resources. |
| `recordingId` | `string` | No | — | — | Optional finished session recording that granted 'api_calls'. Omit to report static evidence only. |
| `categories` | `array` of `string` | No | — | — | Categories to report. Omit for all nine. |
| `maxItems` | `integer` | No | `200` | 1–2000 | Maximum resources to enumerate for the static scan. |
| `maxResourceChars` | `integer` | No | `100000` | 1000–5000000 | Maximum characters read per resource; resources cut at this limit are listed in staticScan.truncatedResources - raise it for large bundles. |
| `maxReferencesPerCategory` | `integer` | No | `10` | 1–200 | Maximum static references returned per category; referenceCount still counts all. |
| `maxCallsPerCategory` | `integer` | No | `5` | 1–200 | Maximum observed calls returned per category; recordedCalls and apiTotals still count all. |
| `contextChars` | `integer` | No | `60` | 0–500 | Characters of source context around each static reference. |
| `redact` | `boolean` | No | `false` | — | true omits call stacks and strips URL parameters from observed calls. false returns recorded values as stored (capture-time redaction cannot be undone). |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### Static evidence only
```json
{
  "name": "nova_browser_api_evidence",
  "arguments": {
    "targetId": "tab-1",
    "categories": ["canvas", "webgl"]
  }
}
```

### With observed calls
Record first (`nova.session_record_start` with `permissionClasses: ["api_calls"]`), use the page, stop the recording, then:

```json
{
  "name": "nova_browser_api_evidence",
  "arguments": {
    "targetId": "tab-1",
    "recordingId": "20261024_101500_..."
  }
}
```

### JSON-RPC Response
Abridged:

```json
{
  "structuredContent": {
    "ok": true,
    "byCategory": [
      {
        "category": "canvas",
        "staticEvidence": {
          "kind": "static_reference",
          "referenceCount": 3,
          "references": [
            { "url": "https://example.test/app.js", "token": "toDataURL", "line": 1, "column": 4120, "scriptHasObservedCallInCategory": true }
          ]
        },
        "observedEvidence": {
          "status": "observed",
          "recordedCalls": 2,
          "apiTotals": { "HTMLCanvasElement.toDataURL": 2 }
        }
      }
    ],
    "evidenceRules": "Static reference = the text exists in a loaded script, not that it ran. ..."
  }
}
```

`observedEvidence.status` is `not_requested` without `recordingId`, `not_recorded` when the recording did not capture `api_calls`, `not_observed_in_recording` when it did but saw no call of that category, and `observed` otherwise.
