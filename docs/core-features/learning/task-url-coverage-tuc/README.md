# Task URL Coverage (TUC)

Task URL Coverage records which URLs in a task instance have been covered and what evidence supports that coverage. [Episodic Task Memory (ETM)](../episodic-task-memory-etm/README.md) manages the task profile, instance and overall completion condition.

## URL units and coverage evidence

For tasks that must cover a list of URLs (audits, accessibility or link checks), TUC adds URL units to an instance:
* **Unit sources:** `unitSource` on `nova.task_instance_create` fills URL units from Nova's site URL index (`site_urls` or `crawler` with `scopeDomain`) or from an explicit URL list (`explicit`).
* **Server-trusted evidence:** `nova.coverage_scan` runs a registered scan script on the page and checks its result on the server before the matching URL unit counts as covered by trusted evidence. Units the agent marks as checked itself are recorded as agent claims.
* **Pattern grouping:** Parameterized routes such as `/products/{id}` are grouped for reporting, so large URL sets stay readable.
* **Completion gate:** In Block mode, `nova.task_instance_complete` is refused (`url_units_remaining`) while URL units remain open; a URL that does not apply has to be excluded explicitly. In the default Warn mode, open URL units do not block completion on their own; a rejected completion includes the URL coverage status.

---

## Coverage tools

* **Coverage Auditing:**
  * `nova.coverage_scan`: Runs a registered scan script on a tab to produce trusted coverage evidence.
  * `nova.task_instance_reconcile_coverage`: Compares recorded observations with open URL units and proposes updates.

## Implementation notes

| Component | Responsibility |
|---|---|
| **`TaskUrlCoverageTracker`** | Records coverage observations after tool calls and advances URL units on trusted evidence. |
| **`TaskKindResolver`** | Resolves the sampling policy for grouped URLs from the declared, profile and keyword-based task kind; the stricter one wins. |

## Related documentation

- [Episodic Task Memory (ETM)](../episodic-task-memory-etm/README.md)
- [Tool Observation Bus (TOB)](../../tool-observation-bus-tob/README.md)

[Learning overview](../README.md) · [All core features](../../README.md)
