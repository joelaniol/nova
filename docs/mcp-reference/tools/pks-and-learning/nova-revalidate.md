# `nova.revalidate`

> **Re-verifies validity of a learned phenomenon against current live website markup.**

* **Capability Bundle:** `pks_learning`
* **Security Tier:** Tier 2 (Verification Gate)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.revalidate` executes pre-verification checks on a target tab to confirm that selectors, polarity assertions, and invariants still hold.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | No | — | — | Domain scope to revalidate (e.g. 'example.com'). If omitted, revalidation is scoped to the current target host. |
| `limit` | `integer` | No | — | 1–5 | Max phenomena to check (default 3, max 5). |
| `targetId` | `string` | Yes | — | — | Tab/sandbox to run DOM checks in. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_revalidate",
  "arguments": {
    "targetId": "tab-1",
    "phenomenonId": "phenom-dismiss-newsletter"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Revalidation successful: phenomenon remains valid on live markup."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "phenomenonId": "phenom-dismiss-newsletter",
    "isValid": true,
    "matchedElementsCount": 1
  }
}
```

---

## 4. Operational Best Practices

* **Pre-flight Revalidation:** Always call before executing critical playbooks in production.

---

## 5. Related Tools

* [`nova.phenomenon_apply`](nova-phenomenon-apply.md)
* [`nova.pks_get`](nova-pks-get.md)
