# `nova.memory_stats`

Reports memory engine metrics, commit rates, verification health, and outbox queues.

---

## 1. Overview

`nova.memory_stats` reads health and performance metrics for the Learning Candidate Journal (LCJ) and several heuristic subsystems: candidate verification and curation rates, the finalize/outbox commit pipeline, and attempt/success rates for scroll, click-navigation, dismiss-blockers and app-screenshot heuristics, including whether their rollout thresholds are currently met.

* **Core Architecture Guide:** [Agent Learning Pipeline (ALP) & Learning Candidate Journal (LCJ)](../../../core-features/agent-learning-pipeline-alp/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `windowHours` | `integer` | No | `24` | — | Lookback window in hours for windowed metrics (1-720). Default 24. |
| `topComponents` | `integer` | No | `8` | — | Top LCJ components to include (1-20). Default 8. |
| `maxSkipReasons` | `integer` | No | `8` | — | Skip reason buckets to include (1-20). Default 8. |
| `topRoutes` | `integer` | No | `8` | — | Top scroll_smart routes to include (1-20). Default 8. |
| `topHosts` | `integer` | No | `8` | — | Top scroll_smart hosts to include (1-20). Default 8. |
| `topSelectors` | `integer` | No | `8` | — | Top scroll_smart selector candidates to include (1-20). Default 8. |
| `componentFilter` | `string` | No | — | — | Optional LCJ component filter. When set, LCJ candidate/curation aggregates are scoped to this component only (e.g. 'evm'). |

Capability bundles: `pks_learning`, `task_memory`.
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.memory_stats",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Memory stats (24h): decisions=12 (commit=10, skip=2, commitRate=83.3%), outbox pending=0, failed=0, lcj candidates=5 (verified=4), curated=3, scroll_smart attempts=20 (moved=18, decoy=1, successRate=90.0%), click_nav expected=15 (mismatchRate=6.7%), dismiss attempts=4 (blockedRate=0.0%), capture_app attempts=2 (fallbackRate=0.0%), rollout=enable_defaults."
    }
  ],
  "structuredContent": {
    "windowHours": 24,
    "componentFilter": null,
    "windowSinceUtc": "2026-10-02T12:00:00Z",
    "kpis": {
      "commitRateTotal": 0.8,
      "commitRateWindow": 0.833,
      "verificationRateWindow": 0.8,
      "curationRateWindowFromVerified": 0.75,
      "outboxSuccessRate": 1.0,
      "scrollSmartSuccessRate": 0.9,
      "clickNavigationMismatchRate": 0.067,
      "dismissBlockersBlockedRate": 0.0,
      "rolloutDefaultsReady": true
    },
    "finalize": { "...": "finalize/outbox decision + queue counters" },
    "lcj": { "...": "LCJ candidate/verification/curation counters, per-component breakdown" },
    "scrollSmart": { "...": "scroll_smart attempt/outcome counters, top routes/hosts/selectors" },
    "clickNavigation": { "...": "click-navigation expectation/outcome counters, top routes/hosts" },
    "dismissBlockers": { "...": "dismiss-blockers attempt/outcome counters, top routes/hosts" },
    "screenshotCapture": { "...": "app-screenshot attempt/fallback counters, top routes/hosts" },
    "rolloutReadiness": { "...": "current rate snapshot per heuristic" },
    "rolloutDecision": { "...": "per-heuristic ready/blockers against configured thresholds" }
  }
}
```

This example is shortened; `kpis` has more fields, and `finalize`, `lcj`, `scrollSmart`, `clickNavigation`, `dismissBlockers`, `screenshotCapture`, `rolloutReadiness` and `rolloutDecision` are each full objects with counts, rates and top-N breakdowns rather than the placeholder strings shown here. There is no top-level `ok` field.

---

## 4. Operational Best Practices

* **System Diagnostics:** Inspect during long benchmark runs to check LCJ verification/curation rates and whether a heuristic's rollout thresholds are met.
* **Component Scoping:** Pass `componentFilter` to narrow LCJ candidate and curation aggregates to a single component (e.g. `evm`).

---

## 5. Related Tools

* [`nova.memory_add_candidate`](nova-memory-add-candidate.md)
* [`nova.learn_feedback`](../pks-and-learning/nova-learn-feedback.md)
