# `nova.learn_suggest`

> **Ranks the learning opportunities Nova has observed: patterns worth storing in the PKS and stored phenomena that are drifting.**

* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/phenomenological-knowledge-store-pks/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.learn_suggest` is read-only. It groups Nova's interaction observations into clusters (for example repeated blocker dismissals, repeated successful actions, action failures, selector drift) and adds stored phenomena whose recent runs are failing (`silent_verify_drift`, `active_failure_drift`). Each entry gets a score and a plain-language suggestion. It does not return replacement selectors; `nova.learn_generate` turns suitable clusters into PKS candidates.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | No | — | — | Domain scope to filter suggestions for (e.g. 'github.com'). If omitted, returns cross-domain opportunities. |
| `limit` | `integer` | No | `5` | 1–20 | Maximum number of suggestions to return (1-20). Default 5. |

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

---

## 4. Operational Best Practices

* **Maintenance pass:** Use it to find stored phenomena that need new selectors or deprecation, and clusters that `nova.learn_generate` can turn into candidates.

---

## 5. Related Tools

* [`nova.pks_match`](nova-pks-match.md)
* [`nova.revalidate`](nova-revalidate.md)
