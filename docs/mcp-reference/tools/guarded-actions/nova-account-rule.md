# `nova.account_rule`

Sets how fast agents may act on one site in one account, and keeps two agents from posting the same thing twice.

---

## 1. Overview

Some sites restrict or close an account when it acts faster than a person would, or when the same listing or
message arrives twice. `nova.account_rule` lets an agent put limits on one site for one account. Nova then holds
**every** agent working on that site in that account to those limits, not only the agent that set them.

* **Account:** a sandbox, the normal browser tabs, or private tabs. A rule for one sandbox does not slow down another.
* **Limits:** least time between two page actions, least time between two submits, most submits in 24 hours.
* **Unclear submits:** when a submit was sent but its outcome is unknown (time-out, no confirmation), Nova refuses the
  next submit on that site and account until an agent has checked the page and recorded what happened. Waiting alone
  never releases it, because the first submit may already be live.
* **Without a rule nothing changes:** Nova adds no delay to any site that has no rule.

Rules the user creates in Nova's settings apply together with agent rules; the strictest value of each limit wins.
An agent can read the user's rules but cannot change or remove them.

Any agent can make an agent rule stricter at once. Making it weaker (a shorter gap, a higher or no daily limit, fewer
subdomains, a submit hint removed) or deleting it always asks the user in Nova first, even when Nova is set to never
ask before agent actions. The rule is there to slow agents down, so the agent it slows cannot lift it alone.

---

## 2. Key Behaviour

### A. Actions
* `set` creates or replaces the agent rule for the site and account. There is one agent rule per site and account,
  shared by all agents. At least one limit must be above 0. A `set` that weakens the rule waits for the user's answer.
* `list` returns the rules (all; for a `domain` in every account; for a `targetId`, `sandboxId` or `scope` in that
  account), the effective limits and the unresolved submits.
* `delete` removes an agent rule by `ruleId`, after the user agreed.

If the user says no, the call returns `account_rule.user_declined` and the rule stays; keep working within it. In a
run nobody watches (a fastlane run) the answer is `account_rule.approval_required`. If another agent changed the
rule while the question was open, the answer is `account_rule.changed` and nothing is stored.
* `resolve` records whether an unresolved submit went through (`committed`) or not (`failed`).

### B. What counts as a submit
Guarded submit, send and login tools, a click on a selector that is a commit point, Enter, a page script that submits a
form, and any click whose selector or expected text contains one of the rule's `submitHints`. A click on a
perceived `ctaRef`, or at screen coordinates, counts by the element it lands on: Nova looks at that element
first (a form's submit button, a commit point, or a `submitHints` match makes it a submit).

On a site with a bot detector but no rule, the first click or input of a session carries `accountRuleHint`
(`antibot.pace_rule_available`) with the detector and a ready `set` call. Nova never sets a rule by itself.

### C. When a call is held
The call returns `isError: true` with `gateId: "safety.account_rule"` and nothing is sent to the page
(`actionDispatched: false`):

| `reasonCode` | Meaning | What to do |
| :--- | :--- | :--- |
| `account_rule.deferred` | Too soon after the last action or submit. | Wait `retryAfterMs`, then repeat the call. |
| `account_rule.daily_limit` | The 24-hour submit limit is used. | Wait `retryAfterMs` or stop for today. |
| `account_rule.submit_in_progress` | Another agent's submit is running on this site and account. | Wait, then check the page before submitting. |
| `account_rule.previous_submit_unknown` | An earlier submit ended without a known outcome. | Check the page, then `resolve` with `actionId` = `blockingActionId`. |
| `account_rule.locked` | The site blocked this account; no submit goes out there. | Do not look for another way to post; tell the user what the page says. |
| `account_rule.store_unavailable` | The site has rules, but Nova cannot read or record them. | Nothing was done; tell the user. |

### D. Blocked accounts
When a site shows that it blocked the account (a ban notice, "account suspended", a forced verification), no agent
should submit there again until the user has sorted it out with the site. Two ways lead to a lock:

* **The agent reports it:** `action='lock'` with `reason` set to what the page says. This works on any site, also one
  without a rule.
* **Nova sees it:** a site with an account rule answers with a block page (HTTP 403, 429 or 503 that is not a
  human-verification check). The tool's answer then says the account was locked.

While locked, every submit on the site and its subdomains in that account returns `account_rule.locked`. Reading and
navigating still work. `list` shows the locks. Only the user lifts a lock: `action='unlock'` asks them in Nova.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `action` | `string` | Yes | — | `set`, `list`, `delete`, `resolve`, `lock`, `unlock`, `wait` | 'set' create or replace the agent rule for the site and account (shared by all agents; weakening needs the user's yes); 'list' rules (all; for a domain in every account; for targetId/sandboxId/scope in that account) plus unresolved submits; 'delete' remove an agent rule by ruleId; 'resolve' record the outcome of an unresolved submit by actionId; 'lock' report that the site blocked this account (needs reason: what the page says) - no submits there until the user lifts it; 'unlock' ask the user to lift a lock; 'wait' wait (up to maxWaitMs) until the rule lets the next submit (or kind='action') through on the site and account of targetId/domain - ready=true then, else retryAfterMs; ends at once on an unresolved submit or a lock, which waiting does not clear. |
| `targetId` | `string` | No | — | — | A tab showing the site. Gives the host and the account (its sandbox, or browser tabs, or private) when domain/sandboxId/scope are omitted. |
| `domain` | `string` | No | — | — | The site, as host or URL (e.g. 'kleinanzeigen.de'). 'www.' and the port are ignored. |
| `sandboxId` | `string` | No | — | — | The account as sandbox letter id; needs sandboxRef. Omit to take the account of targetId. |
| `sandboxRef` | `string` | No | — | — | The sandbox's sandboxRef from nova.tabs or nova.sandbox_context; proves which account a reused letter id means. |
| `scope` | `string` | No | — | `browser-tabs`, `private` | Account context when it is not a sandbox: normal browser tabs, or private tabs. |
| `includeSubdomains` | `boolean` | No | — | — | set: the rule also covers subdomains (m.example.com for example.com), counted together. Default false. |
| `minActionGapMs` | `integer` | No | — | 0–86400000 | set: least time in milliseconds between two page actions (navigate, click, type, select, acting script) on this site and account. 0 = no gap. |
| `minSubmitGapMs` | `integer` | No | — | 0–86400000 | set: least time in milliseconds between two submits (publish, send, post, log in, Enter). 0 = no gap. |
| `maxSubmitsPerDay` | `integer` | No | — | 0–1000 | set: most submits in any 24 hours. 0 = no cap. |
| `submitHints` | `array` of `string` | No | — | ≤ 20 items | set: button texts or selector parts that mean 'submit' on this site (e.g. 'Anzeige aufgeben', '#pstad-submit'), so clicks on them count as submits. Guarded tools, commit-point selectors, Enter and form.submit() count without hints. |
| `inputMode` | `string` | No | — | `native`, `keyboard` | set: how agents type on this site and account when a call names no inputMode. 'keyboard' = type_selector, select_option, choose_option (one option per call) and input_text use real key presses and clicks (result.accountRuleInputMode='keyboard'; a call with more text than the keyboard limit (500 characters) or several options at once is refused with how to split it). An inputMode in the call always wins. Default 'native'; going back from 'keyboard' is a loosening. |
| `reason` | `string` | No | — | ≤ 500 characters | set/delete/unlock: why, shown to the user and other agents (and in the confirmation when the call weakens, removes or unlocks). lock: what the page says about the block (required). |
| `ruleId` | `string` | No | — | — | delete: the ruleId from action='list'. |
| `actionId` | `integer` | No | — | — | resolve: blockingActionId of the refusal, or unresolvedSubmits[].actionId from action='list'. |
| `outcome` | `string` | No | — | `committed`, `failed` | resolve: 'committed' when the page shows the submit went through, 'failed' when it did not. |
| `kind` | `string` | No | — | `submit`, `action` | wait: what you want to do next: 'submit' (default; publish, send, post, log in) or 'action' (any other page action). |
| `maxWaitMs` | `integer` | No | — | 0–290000 | wait: longest wait in this call (default 50000, below the 60 s many clients allow a call). Call again for longer gaps. |
| `agentId` | `string` | No | — | — | Optional agent identity, recorded as the rule's author when your client sends no session id. |

Capability bundle: `form_submission` (load it with `nova.tools_bundle(bundle='form_submission')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 4. Example Call

```json
{
  "name": "nova.account_rule",
  "arguments": {
    "action": "set",
    "targetId": "tab-1",
    "minActionGapMs": 3000,
    "minSubmitGapMs": 600000,
    "maxSubmitsPerDay": 5,
    "submitHints": ["Publish listing"],
    "reason": "New account, keep a human pace"
  }
}
```
