# `nova.coverage_scan`

Runs a server-registered scan script on a tab and returns trust-checked coverage evidence for a Task URL Coverage unit.

---

## 1. Overview

`nova.coverage_scan` runs one of a fixed set of server-registered scan scripts on the active tab and returns a structured evidence payload. The server checks the script's claimed text extraction against measured values and the page's current URL; when both checks pass, the result counts as trusted evidence that the matching Task URL Coverage (TUC) unit was covered. It does not discover new units itself — URL units come from `unitSource` on `nova.task_instance_create`.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/episodic-task-memory-etm/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scanId` | `string` | Yes | — | — | Registered scan identifier. Available scans include nova_full_page_text_v1 (visible text + ARIA + inputs + alt text), nova_structured_dom_v1 (DOM skeleton/tag-sequence/roles), and nova_i18n_spellcheck_v1 (visible text only). |
| `targetId` | `string` | No | — | — | Target tab. Default: 'active'. |
| `scopeOptions` | `object` | No | — | — | Optional scope-options applied to the registered scan. Defaults from the registry are used when omitted. |
| `scopeOptions.includeShadowDom` | `boolean` | No | — | — | Walk Shadow DOM nodes when collecting visible text. Default: registry-defined, usually true. |
| `scopeOptions.includeIframes` | `boolean` | No | — | — | Recurse into same-origin iframes. Default: false. Required for full coverage on iframe-heavy pages. |
| `scopeOptions.waitForHydration` | `boolean` | No | — | — | Wait for the document to reach a stable readyState before scanning. Default: true. |
| `scopeOptions.hydrationTimeoutMs` | `integer` | No | — | 0–30000 | Max milliseconds to wait for hydration. Default: 5000. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.coverage_scan",
  "arguments": {
    "scanId": "nova_full_page_text_v1",
    "targetId": "tab-1"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Coverage scan complete: 4820 text chars across 212 nodes."
    }
  ],
  "structuredContent": {
    "coverageEvidence": {
      "version": 1,
      "producer": "nova_registered_scan",
      "registeredScanId": "nova_full_page_text_v1",
      "scanHash": "sha256:...",
      "document": {
        "effectiveUrl": "https://shop.example.com/checkout",
        "visibleTextCharsMeasured": 4820,
        "nodeCountMeasured": 212,
        "iframeCount": 0,
        "shadowRootCount": 0
      },
      "extraction": {
        "textChars": 4820,
        "textCoverageRatio": 1.0,
        "includedVisibleText": true,
        "includedAriaLabels": true,
        "includedInputs": true,
        "includedAltText": true,
        "includedShadowDom": true,
        "includedIframes": false,
        "domSkeleton": null
      },
      "trust": { "trusted": true, "reason": "server_registered_scan" }
    },
    "targetId": "tab-1",
    "rawUrlBefore": "https://shop.example.com/checkout",
    "rawUrlAfter": "https://shop.example.com/checkout"
  },
  "isError": false
}
```

`scanHash` is a placeholder; the real value is a SHA-256 hex digest. A `raw` field with the scan script's full parsed output is omitted here for brevity. When the effective URL does not match the tab's current URL, or the claimed text exceeds what was measured, `trust.trusted` is `false` and `trust.reason` becomes `effective_url_mismatch` or `claimed_text_exceeds_measured`.

---

## 4. Operational Best Practices

* **Trusted Evidence for Open Units:** Run a coverage scan on each URL unit's page to mark it covered by server-trusted evidence rather than by the agent's own claim.

---

## 5. Related Tools

* [`nova.explore_surface`](nova-explore-surface.md)
* [`nova.task_instance_reconcile_coverage`](nova-task-instance-reconcile-coverage.md)
