# `nova.get_instructions`

> **Retrieves the complete Nova AI operational contract, conventions, and agent guidelines.**

* **Core Feature Guide:** [Agent Awareness Gates (AAG)](../../../core-features/aag.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.get_instructions` returns Nova's agent operating contract as text: tool usage conventions, debugging/escalation guidance, and (in `task` mode) the evidence-verification rules (EVM). The same content is mirrored into `structuredContent`, plus structured addenda (PKS domain hints, operator notes, task awareness, native-dialog state, and more) that only populate when the matching optional parameters are supplied.

Use `nova.get_instructions(topic='bug_report')` to prepare a GitHub bug ticket or work-session feedback. This topic returns reporting rules and separate Markdown templates covering the goal, last relevant actions, successful steps, friction, expected and observed behavior, performance, environment, evidence, and workarounds. Both detail levels return the complete guide. Only `topic`, optional `mode='task'`, and `detail` are accepted for this topic.

The reporting response contains `structuredContent.mode='task'`, `structuredContent.topic='bug_report'`, `structuredContent.instructionsText`, and `structuredContent.bugReport` (`guidanceVersion`, `issuesUrl`, `securityReportUrl`, `repository`, `forms.bug` / `forms.feedback` / `forms.crash`, `collectsUserData=false`, `submitsIssue=false`, `rules`, and `templates.bug` / `templates.feedback`). The guide also names the submission route: show the user the draft and get approval, then submit with the GitHub CLI or hand the user the draft and the matching issue form. It does not collect tabs, logs, or personal data, alter learn-mode state, or create an issue. Website URLs and evidence must be reviewed and sanitized before publication; secrets can appear in URL paths as well as query parameters. Security vulnerabilities belong in private reports. See [alpha reporting policy](../../../../ALPHA.md#what-to-report).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `mode` | `string` | No | `"task"` | `task`, `learn` | Agent mode: 'task' for execution flows, 'learn' for Learn Mode v3 (evidence-backed exploration + PLATFORM_PLAYBOOK deliverable). |
| `topic` | `string` | No | — | `bug_report` | Optional focused guide: 'bug_report' returns static bug-ticket and work-feedback rules with Markdown templates instead of the operational contract. Only topic, mode='task' (or omitted), and detail are accepted; both detail levels return the complete guide. No page/log collection, learn-state changes, or issue submission. |
| `scope` | `string` | No | `"target"` | `target`, `allOwnerClaims` | Learn-mode claim activation scope: 'target' (default, current/explicit target only) or 'allOwnerClaims' (explicit owner-wide activation). |
| `targetId` | `string` | No | — | — | Optional target for learn-mode claim activation. Uses the same target semantics as other tab tools. |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity for learn-mode claim ownership resolution. Defaults to 'default'. |
| `domain` | `string` | No | — | — | Optional domain for domain-specific hints (e.g. 'chatgpt.com'). Legacy primary name; scopeDomain/domainScope are equivalent aliases. |
| `scopeDomain` | `string` | No | — | — | Preferred alias for the domain-scoped hint target. Must match domain/domainScope if multiple aliases are provided. |
| `domainScope` | `string` | No | — | — | Compatibility alias for the domain-scoped hint target. Must match domain/scopeDomain if multiple aliases are provided. |
| `taskKeywords` | `array` of `string` | No | — | — | Optional: 3-5 keywords from the user's request. Returns matching operator notes for task-relevant context. |
| `detail` | `string` | No | `"compact"` | `full`, `compact` | Response detail level. 'compact' (default, ~5KB): safety essentials + bootstrap + domain hints + operator notes + task hints — small enough to always receive, including the mandatory bootstrap call #1. 'full': the complete agent contract with all operational, execution, claim, and memory sections (~50KB; the text is mirrored into structuredContent so it is roughly double on the wire — request it only when you actually need the full static contract). Oversized responses are truncated with a pointer rather than blocked. Trust & Safety + Session Bootstrap are always included regardless of detail level. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_get_instructions",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "... (the instructions text; compact detail is roughly 5 KB, full roughly 50 KB) ..."
    }
  ],
  "structuredContent": {
    "contractVersion": "v3",
    "mode": "task",
    "domain": null,
    "instructionsText": "... (same text as content, mirrored into structuredContent) ...",
    "sessionId": "sess-...",
    "serviceDiscovery": null,
    "screenshotPolicy": { "...": "..." },
    "evm": {
      "version": "v1",
      "rules": {
        "criticalSourceMinimum": 2,
        "nonCriticalSourceMinimum": 1,
        "unknownRequiresNextStep": true,
        "stopOnAllTestsPassed": true
      },
      "criticalDomains": ["security", "medical", "legal", "financial", "political", "pricing", "deadlines", "current_state"]
    },
    "tabAwareness": { "...": "..." },
    "nativeDialog": { "...": "..." },
    "outputBudget": {
      "toolName": "nova.get_instructions",
      "instructionsTextChars": 5120,
      "maxInstructionsTextChars": 50000,
      "estimatedStructuredAddendaChars": 1200,
      "maxStructuredAddendaChars": 16000,
      "omittedStructuredFields": null
    }
  }
}
```

This example is shortened; the real response carries additional fields (`learnMode`, `domainHints`, `frameworkHints`, `operatorNotes`, `taskAwareness`, `instanceEvidenceSummary`, `siteUrlIndex`, `surfaceExplorer`, `activeTabDiscovery`, `aagGates`), most of them `null` unless the matching optional parameter (`domain`, `taskKeywords`, ...) was passed.

---

## 4. Operational Best Practices

* **Session Warm-up:** Execute during agent boot or context resets to refresh operational rules.
* **Bug reports and feedback:** Call with `{"topic":"bug_report"}`, fill the appropriate template using observed facts, and distinguish measured durations from subjective impressions. Missing evidence stays unknown. Review the draft for secrets and personal data before any separately authorized publication.

---

## 5. Related Tools

* [`nova.tools_bundle`](nova-tools-bundle.md)
* [`nova.get_onboarding`](nova-get-onboarding.md)
