# Phenomenological Knowledge Store & Self-Learning

Cross-session procedural UI memory, learned interaction playbooks, fingerprint matching, and health telemetry.

* **Capability Bundle(s):** `pks_learning`
* **Core Architecture Guide:** [Core Features: pks.md](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (21 Tools)

| Tool | What it does |
| :--- | :--- |
| **[`nova.explain`](nova-explain.md)** | Explains why a PKS phenomenon resides at its current learning level, returning a detailed per-gate breakdown of promotion requirements, failure reasons, and remediation hints. |
| **[`nova.learn_feedback`](nova-learn-feedback.md)** | Submits reinforcement feedback (positive or negative) on a learned phenomenon pattern. |
| **[`nova.learn_generate`](nova-learn-generate.md)** | Synthesizes a proposed phenomenon interaction playbook from recorded execution trajectories. |
| **[`nova.learn_onboarding_confirm`](nova-learn-onboarding-confirm.md)** | Confirms that a learned onboarding flow step was successfully completed. |
| **[`nova.learn_onboarding_recall`](nova-learn-onboarding-recall.md)** | Recalls learned onboarding tutorial dismissal steps for a domain. |
| **[`nova.learn_promote`](nova-learn-promote.md)** | Promotes a candidate phenomenon playbook from staging into active production PKS memory. |
| **[`nova.learn_resolve_opportunity`](nova-learn-resolve-opportunity.md)** | Resolves or closes a learning opportunity opportunity flagged during autonomous browsing. |
| **[`nova.learn_suggest`](nova-learn-suggest.md)** | Suggests alternative interaction selectors based on historical pattern performance. |
| **[`nova.phenomenon_apply`](nova-phenomenon-apply.md)** | Executes a stored PKS phenomenon fast-path interaction sequence directly on the page. |
| **[`nova.pks_deprecate`](nova-pks-deprecate.md)** | Marks an obsolete or broken PKS phenomenon playbook as deprecated. |
| **[`nova.pks_get`](nova-pks-get.md)** | Retrieves domain-scoped Phenomenological Knowledge Store (PKS) entries, playbooks, interaction fingerprints, and contextual environment markers. |
| **[`nova.pks_list`](nova-pks-list.md)** | Lists stored phenomenological knowledge playbooks with pagination and domain filters. |
| **[`nova.pks_match`](nova-pks-match.md)** | Matches live page observations against registered Phenomenological Knowledge Store (PKS) fingerprints and global platform templates to identify active UI phenomena. |
| **[`nova.pks_patch`](nova-pks-patch.md)** | Applies partial updates or selector refinements to an existing PKS phenomenon playbook. |
| **[`nova.pks_platform_get`](nova-pks-platform-get.md)** | Retrieves pre-trained platform-level UI pattern definitions (Shopify, WordPress, Jira). |
| **[`nova.pks_platform_list`](nova-pks-platform-list.md)** | Lists supported platform UI frameworks and common component models. |
| **[`nova.pks_platform_seed`](nova-pks-platform-seed.md)** | Seeds the platform knowledge base with pre-trained platform component models. |
| **[`nova.pks_upsert`](nova-pks-upsert.md)** | Stores or updates a verified phenomenon, behavioral playbook, and detection fingerprint in the Phenomenological Knowledge Store (PKS). |
| **[`nova.pks_upsert_hint`](nova-pks-upsert-hint.md)** | Attaches or updates a human operator guidance hint on a phenomenon pattern. |
| **[`nova.revalidate`](nova-revalidate.md)** | Re-verifies validity of a learned phenomenon against current live website markup. |
| **[`nova.telemetry_report`](nova-telemetry-report.md)** | Reports empirical execution outcomes (`success`, `failure`, or `not_applicable`) for a PKS phenomenon interaction, updating health scores and driving automatic promotion and deprecation gates. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
