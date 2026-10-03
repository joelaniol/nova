# `nova.tab_release`

Releases an active exclusive lease on a browser tab, optionally logging finalization decisions, task outcomes, or coverage status.

---

## 1. Overview

`nova.tab_release` relinquishes write ownership of a tab previously acquired via `nova.tab_claim` or an implicit auto-claim. Releasing a tab makes it immediately available for interaction by other AI agents or the human operator without waiting for the lease TTL to expire.

* **Capability Bundle:** `browser_automation`
* **Target Scope:** Tab-specific (`targetId` required).
* **Audit Trail:** Supports attaching finalization tokens, task success decisions, and coverage exhaustion notes to Nova's evidence ledger.

---

## 2. Key Capabilities & Features

### A. Instant Lock Removal
Clears the `claimOwner` entry in Nova's target registry and resets the lease countdown to zero.

### B. Task & ETM Finalization
When releasing a tab as part of an **Episodic Task Memory (ETM)** workflow:
* Pass `finalizeDecision: "success"` or `"aborted"`.
* Pass `finalizeReasonCode: "task_completed"` or a descriptive reason.
* If performing URL audits, pass `coverageExhausted: true` to certify that all planned URLs on the domain have been verified.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Tab to release (tabId, sandboxId like 'A', or 'active'). |
| `agentId` | `string` | No | `"default"` | — | Agent identity. Must match the claim owner. Defaults to 'default'. |
| `finalizationToken` | `string` | No | — | — | Required when finalizeDecision override is used. Must match token from nova.tab_claim. |
| `finalizeDecision` | `string` | No | — | `commit`, `skip` | Optional finalize override. 'commit' persists the completed task outcome and can enqueue finalize outbox work, 'skip' releases the claim without committing curated output. If omitted, the server uses LCJ auto-planning. |
| `finalizeReasonCode` | `string` | No | — | — | Optional reason code override for finalize decision. |
| `finalizeReasonText` | `string` | No | — | — | Optional human-readable reason for finalize decision. |
| `finalizeStats` | `object` | No | — | — | Optional finalize statistics override. Known counters mirror the LCJ/finalize planner summary; additional scalar or string-list metrics may be included for forward-compatible telemetry. |
| `finalizeStats.candidatesTotal` | `integer` | No | — | — | Preferred total LCJ candidates considered during finalize planning. |
| `finalizeStats.candidates_total` | `integer` | No | — | — | Compatibility alias for candidatesTotal. Total LCJ candidates considered during finalize planning. |
| `finalizeStats.candidatesVerified` | `integer` | No | — | — | Preferred verified LCJ candidates at finalize time. |
| `finalizeStats.candidates_verified` | `integer` | No | — | — | Compatibility alias for candidatesVerified. Verified LCJ candidates at finalize time. |
| `finalizeStats.candidatesPromotable` | `integer` | No | — | — | Preferred verified candidates that are promotable into long-term memory. |
| `finalizeStats.candidates_promotable` | `integer` | No | — | — | Compatibility alias for candidatesPromotable. Verified candidates that are promotable into long-term memory. |
| `finalizeStats.curatedUpserts` | `integer` | No | — | — | Preferred number of curated PKS/domain upserts emitted by finalize planning. |
| `finalizeStats.curated_upserts` | `integer` | No | — | — | Compatibility alias for curatedUpserts. Number of curated PKS/domain upserts emitted by finalize planning. |
| `finalizeStats.evidenceMinScore` | `number` | No | — | — | Preferred lowest evidence score observed across considered candidates. |
| `finalizeStats.evidence_min_score` | `number` | No | — | — | Compatibility alias for evidenceMinScore. Lowest evidence score observed across considered candidates. |
| `finalizeStats.evidenceAvgScore` | `number` | No | — | — | Preferred average evidence score observed across considered candidates. |
| `finalizeStats.evidence_avg_score` | `number` | No | — | — | Compatibility alias for evidenceAvgScore. Average evidence score observed across considered candidates. |
| `coverageExhausted` | `boolean` | No | — | — | Optional Learn-v3 override: set true only when additional coverage is genuinely exhausted. |
| `coverageExhaustedReason` | `string` | No | — | — | Required when coverageExhausted=true and learn coverage floors are not met. |
| `finalizeOutboxJobType` | `string` | No | — | `finalize.noop`, `pks.domain.save`, `finalize.memory.promote` | Optional finalize outbox job type used only with finalizeDecision='commit'. 'finalize.noop' stores no follow-up job, 'pks.domain.save' persists PKS domain/domain-context output, 'finalize.memory.promote' promotes stored memory candidates into long-term memory. Defaults to 'finalize.noop'. |
| `finalizeOutboxPayload` | `object` | No | — | — | Finalize outbox payload. Shape depends on finalizeOutboxJobType: omit or pass an empty object for 'finalize.noop', use {scope,data} for 'pks.domain.save', and use {claimTaskId,targetId,candidateIds} for 'finalize.memory.promote' (legacy aliases: taskId, tabId). |
| `finalizeOutboxPayload.scope` | `string` | No | — | — | Domain scope for 'pks.domain.save' jobs. |
| `finalizeOutboxPayload.data` | `object` | No | — | — | Serialized PKS domain payload for 'pks.domain.save'. Uses the same domain-data object the finalize pipeline persists. |
| `finalizeOutboxPayload.claimTaskId` | `string` | No | — | — | Canonical claim-lifecycle task ID for 'finalize.memory.promote'. Must match the active claim task and is distinct from ETM instanceId/taskInstanceId. |
| `finalizeOutboxPayload.taskId` | `string` | No | — | — | Legacy alias for claimTaskId on 'finalize.memory.promote'. Prefer claimTaskId for new callers. |
| `finalizeOutboxPayload.targetId` | `string` | No | — | — | Claim target ID for 'finalize.memory.promote'. Must match the active claimed target. Canonical field for new calls. |
| `finalizeOutboxPayload.tabId` | `string` | No | — | — | Legacy alias for targetId in 'finalize.memory.promote'. Must match targetId when both are provided. |
| `finalizeOutboxPayload.candidateIds` | `array` of `integer` | No | — | — | LCJ candidate IDs to promote for 'finalize.memory.promote'. |
<!-- /generated:parameters -->

---

## 4. Example Call

```json
{
  "name": "nova.tab_release",
  "arguments": {
    "targetId": "tab-2",
    "agentId": "subagent-pricing-1",
    "finalizeDecision": "success",
    "finalizeReasonCode": "extraction_complete"
  }
}
```

### Sample Response
```json
{
  "ok": true,
  "targetId": "tab-2",
  "claimed": false,
  "releasedBy": "subagent-pricing-1"
}
```

---

## See Also

* [`nova.tab_claim`](nova-tab-claim.md) — Claim an exclusive write lease.
* [`nova.tabs`](nova-tabs.md) — Inspect active tab claims.
* [Core Feature: Agent Awareness Gates (AAG)](../../../core-features/aag.md)
