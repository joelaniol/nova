# `nova.get_instructions`

> **Retrieves the complete Nova AI operational contract, conventions, and agent guidelines.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 1 (Read-Only Guidance)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.get_instructions` returns Nova's core operating instructions: tool semantics, security tier boundaries, timeout guidelines, and safety practices.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for learn-mode claim ownership resolution. Defaults to 'default'. |
| `detail` | `string` | No | Response detail level. 'compact' (default, ~5KB): safety essentials + bootstrap + domain hints + operator notes + task hints — small enough to always receive, including the mandatory bootstrap call #1. 'full': the complete agent contract with all operational, execution, claim, and memory sections (~50KB; the text is mirrored into structuredContent so it is roughly double on the wire — request it only when you actually need the full static contract). Oversized responses are truncated with a pointer rather than blocked. Trust & Safety + Session Bootstrap are always included regardless of detail level. |
| `domain` | `string` | No | Optional domain for domain-specific hints (e.g. 'chatgpt.com'). Legacy primary name; scopeDomain/domainScope are equivalent aliases. |
| `domainScope` | `string` | No | Compatibility alias for the domain-scoped hint target. Must match domain/scopeDomain if multiple aliases are provided. |
| `mode` | `string` | No | Agent mode: 'task' for execution flows, 'learn' for Learn Mode v3 (evidence-backed exploration + PLATFORM_PLAYBOOK deliverable). |
| `scope` | `string` | No | Learn-mode claim activation scope: 'target' (default, current/explicit target only) or 'allOwnerClaims' (explicit owner-wide activation). |
| `scopeDomain` | `string` | No | Preferred alias for the domain-scoped hint target. Must match domain/domainScope if multiple aliases are provided. |
| `targetId` | `string` | No | Optional target for learn-mode claim activation. Uses the same target semantics as other tab tools. |
| `taskKeywords` | `array` | No | Optional: 3-5 keywords from the user's request. Returns matching operator notes for task-relevant context. |

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
      "text": "Nova Agent Operating Guidelines returned (14 sections)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "version": "2026.10",
    "guidelinesCount": 14
  }
}
```

---

## 4. Operational Best Practices

* **Session Warm-up:** Execute during agent boot or context resets to refresh operational rules.

---

## 5. Related Tools

* [`nova.tools_bundle`](nova-tools-bundle.md)
* [`nova.get_onboarding`](nova-get-onboarding.md)
