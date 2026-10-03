# `nova.coverage_scan`

Runs a server-registered Coverage Scan script to discover and audit all interactive surfaces.

---

## 1. Overview

`nova.coverage_scan` runs an isolated, server-trusted audit script on the active tab. It discovers links, inputs, and interactive widgets to populate the Task URL Coverage (TUC) unit table.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 2 (Coverage Audit)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

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
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.coverage_scan",
  "arguments": {
    "scanId": "default-surface-scan",
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
      "text": "Coverage scan completed: 42 units discovered, 12 checked."
    }
  ],
  "structuredContent": {
    "ok": true,
    "scanId": "default-surface-scan",
    "discoveredUnits": 42,
    "checkedUnits": 12,
    "coveragePercent": 28.5
  }
}
```

---

## 4. Operational Best Practices

* **Automated Unit Table Generation:** Use coverage scans to establish the denominator of units required for task completion.

---

## 5. Related Tools

* [`nova.explore_surface`](nova-explore-surface.md)
* [`nova.task_instance_reconcile_coverage`](nova-task-instance-reconcile-coverage.md)
