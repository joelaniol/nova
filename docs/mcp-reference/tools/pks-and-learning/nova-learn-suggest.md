# `nova.learn_suggest`

> **Ranks the learning opportunities Nova has observed: patterns worth storing in the PKS and stored phenomena that are drifting.**

* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/learning/phenomenological-knowledge-store-pks/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.learn_suggest` is read-only. It groups Nova's interaction observations into clusters (for example repeated blocker dismissals, repeated successful actions, action failures, selector drift) and adds stored phenomena whose recent runs are failing (`silent_verify_drift`, `active_failure_drift`). Each entry gets a score and a plain-language suggestion. It does not return replacement selectors; `nova.learn_generate` turns suitable clusters into PKS candidates.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | No | — | — | Domain scope to filter suggestions for (e.g. 'github.com'). If omitted, returns cross-domain opportunities. In scaffold mode the scope comes from the target's page; omit it. |
| `limit` | `integer` | No | `5` | 1–20 | Maximum number of suggestions to return (1-20). Default 5. In scaffold mode: maximum tabs/buttons scanned. |
| `mode` | `string` | No | `"observations"` | `observations`, `scaffold` | observations (default): ranked opportunities from accumulated observations. scaffold: draft pks_upsert payloads from the page open in targetId; writes nothing. |
| `targetId` | `string` | No | — | — | Only with mode='scaffold': tab to read, from nova.tabs, or 'active'. |
| `surfaceType` | `string` | No | — | `chat_composer`, `tabs`, `buttons` | Only with mode='scaffold': chat_composer (input field + send control), tabs (role=tab elements), buttons (visible named buttons). |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_learn_suggest",
  "arguments": {
    "scope": "example.com",
    "limit": 5
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Top 1 learn opportunities for example.com:\n1. [4.1] Phenomenon 'lcj_4b1f0c9a2d7e' on example.com shows drift (consecutiveFailures=3, staleness=0.62). Consider updating selectors or deprecating."
    }
  ],
  "structuredContent": {
    "ok": true,
    "scope": "example.com",
    "count": 1,
    "opportunities": [
      {
        "contextHost": "example.com",
        "candidateKey": "lcj_4b1f0c9a2d7e",
        "dominantKind": "silent_verify_drift",
        "supportCount": 3,
        "successCount": 2,
        "failureCount": 3,
        "distinctSessions": 0,
        "score": 4.12,
        "suggestion": "Phenomenon 'lcj_4b1f0c9a2d7e' on example.com shows drift (consecutiveFailures=3, staleness=0.62). Consider updating selectors or deprecating.",
        "scoreBreakdown": null
      }
    ]
  }
}
```

Entries built from observation clusters carry `dominantKind` values such as `blocker_dismissed`, `action_success`, `action_failure` or `selector_drift` and a `scoreBreakdown` object (`supportScore`, `sessionBonus`, `successRateFactor`, `driftSignal`, `recencyBonus`). Without `scope`, opportunities across all domains are returned and `scope` is reported as `"*"`.

### Drafting entries on a new site (`mode='scaffold'`)

A site Nova has not learned yet has no observations, so the default mode returns nothing. `mode='scaffold'` reads the page that is open in `targetId` and drafts entries for one kind of surface: `chat_composer` (input field and send control), `tabs` or `buttons`. It stores nothing.

```json
{
  "name": "nova_learn_suggest",
  "arguments": { "mode": "scaffold", "targetId": "active", "surfaceType": "chat_composer" }
}
```

Each entry in `structuredContent.drafts` carries the chosen `selector`, a `verifyFirst` instruction and `upsertArgs` that can be passed to `nova.pks_upsert` unchanged once the check has passed:

```json
{
  "draftId": "scaffold.chat_composer.send.run",
  "part": "send",
  "selector": "button[aria-label=\"Run\"]",
  "verifyFirst": "Type a test message, nova.click_selector(selector='button[aria-label=\"Run\"]'), and confirm the message was sent ...",
  "upsertArgs": {
    "scope": "example.com",
    "phenomenon": {
      "id": "scaffold.chat_composer.send.run",
      "type": "custom",
      "fingerprint": { "signals": [ { "kind": "dom", "match": "button[aria-label=\"Run\"]" } ] },
      "playbook": { "policy": "custom", "actions": [ { "type": "click", "selector": "button[aria-label=\"Run\"]" } ] }
    }
  }
}
```

Only selectors that match exactly one element and do not depend on position or generated ids become drafts. Elements without such a selector appear in `skipped`, and every dropped candidate in `rejected`, each with the reason.

---

## 4. Operational Best Practices

* **New site:** When the default mode finds nothing, draft with `mode='scaffold'`, verify each draft on the live page, then store it with `nova.pks_upsert`; it starts in Shadow like any manual entry.
* **Maintenance pass:** Use it to find stored phenomena that need new selectors or deprecation, and clusters that `nova.learn_generate` can turn into candidates.

---

## 5. Related Tools

* [`nova.pks_match`](nova-pks-match.md)
* [`nova.revalidate`](nova-revalidate.md)
