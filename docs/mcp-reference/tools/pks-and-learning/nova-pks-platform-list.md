# `nova.pks_platform_list`

> **Lists supported platform UI frameworks and common component models.**

* **Capability Bundle:** `pks_learning`
* **Security Tier:** Tier 1 (Read-Only Platform Models)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.pks_platform_list` lists all available platform knowledge models bundled with Nova.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_pks_platform_list",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Supported platforms: shopify, salesforce, wordpress, jira, github."
    }
  ],
  "structuredContent": {
    "ok": true,
    "platforms": [
      "shopify",
      "salesforce",
      "wordpress",
      "jira",
      "github"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Platform Identification:** Check if target site runs on a recognized platform.

---

## 5. Related Tools

* [`nova.pks_platform_get`](nova-pks-platform-get.md)
