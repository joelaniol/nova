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

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`scanId`** | `string` | Yes | `null` | Registered scan identifier. Available scans include nova_full_page_text_v1 (visible text + ARIA + inputs + alt text), nova_structured_dom_v1 (DOM skeleton/tag-sequence/roles), and nova_i18n_spellcheck_v1 (visible text only). |
| **`scopeOptions`** | `object` | No | `null` | Optional scope-options applied to the registered scan. Defaults from the registry are used when omitted. |
| **`targetId`** | `string` | No | `null` | Target tab. Default: 'active'. |

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
