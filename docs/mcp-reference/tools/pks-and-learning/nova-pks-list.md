# `nova.pks_list`

> **Lists stored phenomenological knowledge playbooks with pagination and domain filters.**

* **Capability Bundle:** `pks_learning`
* **Security Tier:** Tier 1 (Read-Only Catalog)
* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.pks_list` enumerates all learned phenomena stored in the local SQLite knowledge database, returning IDs, domains, confidence scores, and usage counts.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `limit` | `integer` | No | Optional page size (1-500). Default 200. |
| `minHealth` | `number` | No | Optional: only domains with avg success rate >= this value (0.0-1.0). |
| `offset` | `integer` | No | Optional pagination offset (>=0). Default 0. |
| `prefix` | `string` | No | Optional domain prefix filter. |
| `serviceCategory` | `string` | No | Optional service-category filter. Service category. 'adult' = adult content, 'ai' = AI assistants/tools, 'banking' = finance or payments, 'communication' = chat/messaging/meetings, 'community_forum' = discussion forum/community, 'creator_platform' = publishing or creator backend, 'dating' = matchmaking, 'developer' = developer docs/tools/repos, 'education' = learning/course platform, 'email' = mail service, 'entertainment' = general media/entertainment, 'gambling' = betting/casino, 'gaming' = games or launchers, 'government' = public-sector service, 'health' = health or medical service, 'marketplace' = multi-seller marketplace, 'news' = news/publishing, 'productivity' = work/productivity app, 'search' = search/discovery, 'shopping' = retail/e-commerce, 'social' = social network, 'streaming' = video/audio streaming, 'travel' = travel/maps/transport, 'other' = uncategorized service. |
| `trust` | `string` | No | Optional trust level filter. Trust level. 'unknown' = not reviewed yet, 'low' = weak or unstable evidence, 'medium' = usable but still needs confirmation, 'high' = repeatedly verified and reliable. |
| `type` | `string` | No | Optional phenomenon type filter. Phenomenon type. 'consent_cmp' = cookie/consent manager surface, 'modal' = generic blocking overlay or dialog, 'paywall' = subscription/payment gate, 'login_wall' = sign-in gate, 'layout_shift' = disruptive UI shift without a classic overlay, 'native_dialog' = browser/native prompt such as permission or file picker, 'popover_open' = anchored popover/dropdown surface, 'custom' = uncategorized site-specific phenomenon. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_pks_list",
  "arguments": {
    "scope": "example.com",
    "limit": 20
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 4 phenomena for example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "total": 4,
    "phenomena": [
      {
        "id": "phenom-login",
        "confidence": 0.98,
        "executions": 54
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Domain Inventory:** Query before beginning tasks to identify pre-existing automation fast-paths.

---

## 5. Related Tools

* [`nova.pks_get`](nova-pks-get.md)
* [`nova.pks_match`](nova-pks-match.md)
