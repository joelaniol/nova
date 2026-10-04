# Phenomenological Knowledge Store & Self-Learning

Cross-session procedural UI memory, learned interaction playbooks, fingerprint matching, and health telemetry.

* **Core Architecture Guide:** [Core Features: pks.md](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (21 Tools)

Capability bundles of these tools: `pks_learning`, `task_memory`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.explain`](nova-explain.md)** | Explains why a PKS phenomenon resides at its current learning level, returning a detailed per-gate breakdown of promotion requirements, failure reasons, and remediation hints. |
| **[`nova.learn_feedback`](nova-learn-feedback.md)** | Lists recent learning-level changes (promotions, demotions, deprecations, revivals, generated candidates) in the PKS. |
| **[`nova.learn_generate`](nova-learn-generate.md)** | Synthesizes a proposed phenomenon interaction playbook from recorded execution trajectories. |
| **[`nova.learn_onboarding_confirm`](nova-learn-onboarding-confirm.md)** | Confirms the learn-mode onboarding for a domain with a paraphrase of its contract, so the onboarding gate stops blocking. |
| **[`nova.learn_onboarding_recall`](nova-learn-onboarding-recall.md)** | Re-reads the PKS learn-mode onboarding briefing for a domain without re-triggering the gate. |
| **[`nova.learn_promote`](nova-learn-promote.md)** | Evaluates and applies learning-level transitions (promotion, demotion, deprecation, revival) for the PKS entries of one domain. |
| **[`nova.learn_resolve_opportunity`](nova-learn-resolve-opportunity.md)** | Closes a semantic learning opportunity that Nova raised in a tool result (`pksSemanticLearning`). |
| **[`nova.learn_suggest`](nova-learn-suggest.md)** | Ranks the learning opportunities Nova has observed: patterns worth storing in the PKS and stored phenomena that are drifting. |
| **[`nova.phenomenon_apply`](nova-phenomenon-apply.md)** | Executes a stored PKS phenomenon fast-path interaction sequence directly on the page. |
| **[`nova.pks_deprecate`](nova-pks-deprecate.md)** | Marks an obsolete or broken PKS phenomenon playbook as deprecated. |
| **[`nova.pks_get`](nova-pks-get.md)** | Retrieves domain-scoped Phenomenological Knowledge Store (PKS) entries, playbooks, interaction fingerprints, and contextual environment markers. |
| **[`nova.pks_list`](nova-pks-list.md)** | Lists the domains that have PKS knowledge, with counts, health and classification, filtered and paginated. |
| **[`nova.pks_match`](nova-pks-match.md)** | Matches live page observations against registered Phenomenological Knowledge Store (PKS) fingerprints and global platform templates to identify active UI phenomena. |
| **[`nova.pks_patch`](nova-pks-patch.md)** | Applies partial updates or selector refinements to an existing PKS phenomenon playbook. |
| **[`nova.pks_platform_get`](nova-pks-platform-get.md)** | Reads one stored platform entry with its pattern templates and aliases. |
| **[`nova.pks_platform_list`](nova-pks-platform-list.md)** | Lists supported platform UI frameworks and common component models. |
| **[`nova.pks_platform_seed`](nova-pks-platform-seed.md)** | Creates or updates a platform entry (for example a cookie-consent vendor) with pattern templates and lookup aliases. |
| **[`nova.pks_upsert`](nova-pks-upsert.md)** | Stores or updates a verified phenomenon, behavioral playbook, and detection fingerprint in the Phenomenological Knowledge Store (PKS). |
| **[`nova.pks_upsert_hint`](nova-pks-upsert-hint.md)** | Creates or updates a domain hint: CSS selectors that mark ad containers, noise regions or result items on a site. |
| **[`nova.revalidate`](nova-revalidate.md)** | Checks stale PKS phenomena of a domain against the live page in a tab and records the outcome. |
| **[`nova.telemetry_report`](nova-telemetry-report.md)** | Reports empirical execution outcomes (`success`, `failure`, or `not_applicable`) for a PKS phenomenon interaction, updating health scores and driving automatic promotion and deprecation gates. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
