# Ambient Auto-Apply

Ambient Auto-Apply uses learned PKS playbooks to handle eligible blockers during agent work. It builds on the outcome checks of the [Closed-Loop System (CLS)](../../closed-loop-system-cls/README.md).

## Eligibility, confirmation and recovery

Beyond explicit agent commands, Nova can apply known PKS playbooks on its own:
* **When it runs:** On page loads and route changes that an agent's navigation request caused, and at the agent's `nova.perceive` calls. Ordinary browsing by the user does not trigger it.
* **What qualifies:** Only active (L2) phenomena with a healthy record whose last confirmation is less than 60 days old. Login and transactional actions (submit, send, checkout, payment and similar) are never auto-applied.
* **Confirmation:** By default Nova asks before each ambient application ("always ask"); this can be changed to once per session or never ask, or the feature can be turned off.
* **Self-protection:** A playbook whose success rate drops below 80% is put under watch. Under watch, 3 consecutive failures, a success rate below 60%, or a severe misfire quarantine it; a quarantined playbook without verified recovery is deprecated after 14 days.

For example, a learned cookie-rejection playbook can clear a familiar blocker during an agent's navigation, but only if it meets the ambient eligibility, consent-policy and confirmation rules. A login wall may also be recognized by PKS; that does not make signing in an ambient action.

**Trusted knowledge and permission to apply it automatically are separate decisions.** The ambient watch/quarantine lifecycle also complements PKS promotion and demotion; its thresholds serve a different decision and should not be read as replacements for the [PKS trust gates](../phenomenological-knowledge-store-pks/README.md#learning-trust-levels).

---

## Related documentation

Ambient eligibility, risk class and playbook health are evaluated by **`AutoApplyController`**.

- [Closed-Loop System (CLS)](../../closed-loop-system-cls/README.md)
- [Phenomenological Knowledge Store (PKS)](../phenomenological-knowledge-store-pks/README.md)

[Learning overview](../README.md) · [All core features](../../README.md)
