# `nova.pks_list`

> **Lists the domains that have PKS knowledge, with counts, health and classification, filtered and paginated.**

* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.pks_list` returns one entry per PKS domain, not individual phenomena. Each entry counts the domain's active phenomena (`phenomenonCount`, deprecated ones separately in `deprecatedCount`), reports their average 30-day success rate and the phenomenon types, and carries the domain's trust level and service categories. Filters: domain `prefix`, phenomenon `type`, `trust`, `serviceCategory` and `minHealth`. Use `nova.pks_get` to read the phenomena of one domain.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `prefix` | `string` | No | — | — | Optional domain prefix filter. |
| `type` | `string` | No | — | `consent_cmp`, `modal`, `paywall`, `login_wall`, `layout_shift`, `native_dialog`, `popover_open`, `custom` | Optional phenomenon type filter. Phenomenon type. 'consent_cmp' = cookie/consent manager surface, 'modal' = generic blocking overlay or dialog, 'paywall' = subscription/payment gate, 'login_wall' = sign-in gate, 'layout_shift' = disruptive UI shift without a classic overlay, 'native_dialog' = browser/native prompt such as permission or file picker, 'popover_open' = anchored popover/dropdown surface, 'custom' = uncategorized site-specific phenomenon. |
| `minHealth` | `number` | No | — | 0–1 | Optional: only domains with avg success rate >= this value (0.0-1.0). |
| `trust` | `string` | No | — | `unknown`, `low`, `medium`, `high` | Optional trust level filter. Trust level. 'unknown' = not reviewed yet, 'low' = weak or unstable evidence, 'medium' = usable but still needs confirmation, 'high' = repeatedly verified and reliable. |
| `serviceCategory` | `string` | No | — | `adult`, `ai`, `banking`, `communication`, `community_forum`, `creator_platform`, `dating`, `developer`, `education`, `email`, `entertainment`, `gambling`, `gaming`, `government`, `health`, `marketplace`, `news`, `productivity`, `search`, `shopping`, `social`, `streaming`, `travel`, `other` | Optional service-category filter. Service category. 'adult' = adult content, 'ai' = AI assistants/tools, 'banking' = finance or payments, 'communication' = chat/messaging/meetings, 'community_forum' = discussion forum/community, 'creator_platform' = publishing or creator backend, 'dating' = matchmaking, 'developer' = developer docs/tools/repos, 'education' = learning/course platform, 'email' = mail service, 'entertainment' = general media/entertainment, 'gambling' = betting/casino, 'gaming' = games or launchers, 'government' = public-sector service, 'health' = health or medical service, 'marketplace' = multi-seller marketplace, 'news' = news/publishing, 'productivity' = work/productivity app, 'search' = search/discovery, 'shopping' = retail/e-commerce, 'social' = social network, 'streaming' = video/audio streaming, 'travel' = travel/maps/transport, 'other' = uncategorized service. |
| `limit` | `integer` | No | `200` | 1–500 | Optional page size (1-500). Default 200. |
| `offset` | `integer` | No | `0` | ≥ 0 | Optional pagination offset (>=0). Default 0. |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_pks_list",
  "arguments": {
    "prefix": "example",
    "type": "consent_cmp",
    "limit": 20
  }
}
```

### JSON-RPC Response

Shortened to the main fields of one entry:

```json
{
  "content": [
    {
      "type": "text",
      "text": "1/1 domain(s) returned."
    }
  ],
  "structuredContent": {
    "count": 1,
    "returned": 1,
    "offset": 0,
    "limit": 20,
    "hasMore": false,
    "domains": [
      {
        "scope": "example.com",
        "phenomenonCount": 1,
        "deprecatedCount": 0,
        "avgSuccessRate30d": 0.95,
        "verifiedPhenomenonCount": 1,
        "types": ["consent_cmp"],
        "trust": "medium",
        "updatedAtUtc": "2026-10-01T14:02:00.0000000Z",
        "serviceCategories": ["shopping"],
        "primaryServiceCategory": "shopping",
        "mcpDiscovery": null
      }
    ]
  }
}
```

Each entry also carries the domain's stored `auth` context. `mcpDiscovery` is filled when Nova has probed the site for an MCP server, `llms.txt`, an A2A agent or OAuth metadata.

---

## 4. Operational Best Practices

* **Domain inventory:** Query before a task to see which domains already have stored knowledge, then read the details with `nova.pks_get`.
* **Paginate:** Use `offset` and `hasMore` when `count` is larger than `limit`.

---

## 5. Related Tools

* [`nova.pks_get`](nova-pks-get.md)
* [`nova.pks_match`](nova-pks-match.md)
