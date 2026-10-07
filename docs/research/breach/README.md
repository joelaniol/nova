# BREACH — Baseline Reorganization through Explicit Assumption Change & Hypothesis

Author: Joel Aniol · First draft: 7 March 2026 · First published: 22 March 2026 · Status: experimental

**Video:** [BREACH explained on YouTube](https://www.youtube.com/watch?v=RQBagueu0K4)

BREACH is a working method for turning a topic into concepts that are **structurally new** and **operationally viable**. It can be run by a person or handed to a language model as a structured prompt ([the prompt](prompt.md)).

The core is not brainstorming, not "more features" and not cosmetic variation. The core is **breaking one load-bearing assumption** and then **fully reorganizing** the system under the new condition.

## The problem it addresses

Idea work — by people and by language models alike — tends to stay in the same space:

- the same target group
- the same value logic
- the same operational mechanics
- the same cost structure
- the same risks

The result is variations of what already exists. A language model in particular converges quickly on its most probable answer. Raising the sampling temperature adds randomness, but randomness is not direction: it produces different wording far more often than a different structure.

BREACH widens the solution space **structurally instead of stochastically**. The model is not asked to be more random; it is forced to work under a condition in which its default answer can no longer exist.

## Why it works

### Convergence is a property of the distribution, not of the sampler

A language model produces an answer y to a prompt x by sampling from a conditional distribution p(y | x). For open-ended tasks this distribution is strongly peaked: a few "typical" solutions carry most of the probability mass. Preference tuning sharpens this further — instruction-tuned models measurably produce less diverse outputs than their base models (Kirk et al., 2024), an effect often called *mode collapse*.

There are two places to intervene:

| Lever | What it changes | What it cannot change |
|---|---|---|
| **Sampling** (temperature, top-p, repeated sampling) | How far the sampler strays from the peak of p(y \| x), token by token | Where the peak is. The model still conditions on the same problem framing. |
| **Conditioning** (BREACH) | The distribution itself: p(y \| x, ¬A) for a removed or inverted assumption A | Nothing is randomized; the variation is chosen, not drawn |

Temperature acts locally, on each next token. Structural novelty — a different value logic, a different owner of the core step — is a property of the whole answer. Raising the temperature therefore mostly varies wording and details, and at high values it degrades coherence before it changes structure (Holtzman et al., 2020).

BREACH moves the peak instead. If the typical solution depends on assumption A, then under the condition ¬A that solution is no longer admissible, and the probability mass has to move to solutions that are consistent with ¬A. Every iteration therefore samples near the mode of a *different* distribution. Because the variation comes from the conditioning, ordinary temperature is enough, and the method does not depend on a particularly large model. The second point is an observation from use, not a measured result (see hypothesis H3 below).

### Why the individual rules matter

Each rule of the method closes a specific way in which a model slips back to its default answer:

- **A strong baseline first.** The baseline makes the model's default answer explicit. Novelty can then be judged against it instead of against a straw man.
- **Explicit assumptions in "If X holds, then Y can work" form.** This turns implicit framing into named, testable dependencies. Only what is named can be broken deliberately.
- **Remove or invert, never weaken.** A softened assumption ("a bit more flexible") keeps the old solution admissible, and the model returns to it. Only a complete break makes the old mode inconsistent.
- **Full reorganization.** Without it, the model answers ¬A by attaching a patch to the old structure. Requiring new structure, functional logic, value logic and mechanics forces a consistent solution under the new condition.
- **Orthogonal iterations.** Breaking assumptions on different axes (process, value, trust) samples from distributions that are far apart, instead of three neighbours of the same mode.
- **Hypotheses, failure modes and test plans.** These keep the reorganization falsifiable and filter out ideas that are new but not viable.
- **No hidden reintroduction in the synthesis.** Merging is where models most often fall back to the baseline; the rule makes that fallback detectable.

### Relation to earlier work

The idea of producing novelty by breaking assumptions is old in creativity research and philosophy of science: deliberate provocation in lateral thinking (de Bono, 1970), resolving contradictions in TRIZ (Altshuller), paradigm change as a change of foundational assumptions (Kuhn, 1962), and falsifiable hypotheses (Popper, 1959). On the language-model side, self-consistency (Wang et al., 2023) and Tree of Thoughts (Yao et al., 2023) widen the search by sampling or branching several reasoning paths, and verbalized sampling (Zhang et al., 2025) counters mode collapse by asking the model for a distribution of answers.

BREACH combines these lines in one procedure: it makes the variation explicit and structural (assumption breaks instead of sampling), forces orthogonal directions, and binds every result to hypotheses and a test plan.

## Three movements

1. **Destabilization** — one structural assumption is removed or inverted completely.
2. **Shift** — after the break, the value logic, the operational mechanics or the system structure has to move to a different axis.
3. **Iteration** — this is repeated with different assumptions, so that the first reorganization is not mistaken for the baseline.

## Destabilization

Destabilization does not just produce "wilder ideas". It produces a controlled structural break:

- an assumption that used to carry the model loses its status as a foundation
- the existing model becomes deliberately unstable
- value logic, process logic or operational mechanics must reorganize along another axis
- at best, the result is not a variant but a new category or a new building block

If everything stays essentially the same after the break, the destabilization was too weak or not honest.

Destabilization means an assumption is **removed** or **inverted** — not weakened, not made "a bit more flexible", and not quietly reintroduced later:

- weak: "the process stays manual, but with a bit more automation"
- strong: "the process no longer needs a manual operator as a structural precondition"

If the result only looks faster, cheaper or more convenient but keeps the same core logic, it is not a BREACH idea. The question is always: *was a load-bearing assumption really broken, and did the system have to reorganize afterwards?*

### Choosing the right assumption

The method depends on breaking the **right kind** of assumption — one that actually carries the model, for example:

- who creates the core value
- when the value is created
- where decision authority sits
- what counts as the scarce resource
- how trust is established
- how success is recognized operationally
- which precondition has so far been treated as indispensable

Rule of thumb:

- If removing the assumption changes only a detail, it is too weak.
- If removing it breaks the structure, the flow or the value logic, it is probably load-bearing.
- Good destabilization hits a foundation, not a parameter.

> Which assumption has to fall so that the current model cannot survive in its current form?

## Shift

After a real destabilization it is not enough to carry the same logic forward in new packaging. The system has to move to a different axis:

- **Value logic** — the benefit is created differently.
- **Operational mechanics** — a different process carries the flow.
- **Responsibility** — a different role, instance or level takes over the core.
- **Time logic** — the critical step happens earlier, later, continuously or only on events.
- **Cost logic** — effort and scarcity move to a different place.
- **Trust logic** — the system is trusted because of verification, feedback or transparency instead of assertion.

Destabilization breaks the old foundation. The shift decides **where** the system reorganizes afterwards.

## Real and fake iterations

An iteration is **real** when:

- a load-bearing assumption genuinely no longer holds
- the reorganization creates visibly new structure
- the value logic or operational logic works noticeably differently
- new trade-offs appear that did not exist in the baseline
- the result cannot be described as "baseline plus an add-on"

An iteration is **fake or too weak** when:

- only a feature is added
- the same core logic survives under new wording
- the broken assumption quietly returns later
- all advantages remain but hardly any new costs or risks appear
- A, B and C are variants of the same idea

> If the result can be summarized as "basically the same as before, just better", there was no real destabilization.

## Orthogonal iterations

Orthogonal means: not the same idea phrased three ways.

- Iteration A breaks an assumption of the process logic.
- Iteration B breaks an assumption of the value logic.
- Iteration C inverts a seemingly self-evident assumption of the usage or trust logic.

Test: if A, B and C all end up preferring the same kind of solution, the choice was not orthogonal enough. If each iteration produces different risks, strengths and operational consequences, the axes were well chosen.

## Examples

**Too weak.** Baseline: "A browser gets better when it gets more assistance features." Apparent destabilization: "The browser gets even stronger assistance features." No load-bearing assumption was broken — this is an incremental extension.

**Real destabilization.** Baseline: "A browser is a passive tool; learning happens outside the browser." The assumption is inverted: the browser learns along. Value no longer comes only from operation but from persistently accumulated experience; the mechanics shift towards observation, evaluation and reuse. That is not "more browser" but a different product logic.

**Another axis.** Baseline: "An action is successful once it has been executed." Destabilization: success counts only once it has been verified. Trust moves from dispatch to evidence; the mechanics need checking instead of blind continuation. Nova's [visual evidence approach (EVM)](../../core-features/evidence-verification-mode-evm/README.md) was the first concept that came out of BREACH.

## Procedure

1. **Translate the topic into a baseline model.** Who is it for, which problem does it solve, how does it work, how does it create value, how is it carried operationally. The baseline must be deliberately strong, so that later iterations work against something real rather than a straw man.
2. **Make the structural assumptions explicit.** Write down 6–10 assumptions that carry the baseline, in the form "If X holds, then Y can work this way." Only structural carriers count, no trivialities.
3. **Break one assumption radically.** For each iteration, exactly one load-bearing assumption is removed or inverted — no middle ground, no hybrid at this point, no return to the baseline logic.
4. **Reorganize the whole system.** New structure, new functional logic, new value logic, new operational mechanics. This consistent reorganization, not the break alone, is the actual core of the innovation.
5. **Hypotheses instead of claims.** Uncertain statements are marked as hypotheses. Each iteration needs an MVP or experiment, success criteria, failure modes and countermeasures.
6. **Repeat orthogonally.** Different assumption, different value logic, different operational consequence. At least one iteration should be counter-intuitive and remove at least one pain point of the baseline.
7. **Final synthesis.** Only after several real destabilizations is a consolidated hybrid built. It may only take elements that stayed viable in the iterations, and it must not quietly restore any broken assumption.

BREACH is not free-form creativity. Every iteration has to include a measurable improvement against the goal criteria, explicit trade-offs, an implementation route, a risk and misuse assessment, and a test plan.

## When to use it

BREACH is meant for the moments where ordinary feature planning becomes too narrow:

- existing assumptions keep leading to variants of the same thing
- new product or system axes are needed
- a loose topic first has to become a viable innovation framework
- a new approach should be tested right away against reality: usability, risk and feasibility

The goal is not to rescue every idea. The goal is to produce structurally new candidates and then filter them through real practice. The method itself is under test as well: does it repeatedly produce robust novelty or only interesting theory, does it make the invention process more reliable, and does it carry over to fields outside software?

## Input and output

**Input.** Required is only the topic. Optional: target group, goal criteria (top 3–5, measurable), constraints, context or use case, and exclusions. If goal criteria are missing, exactly one follow-up question is allowed — *"Which 3 goal criteria matter most (measurable)?"* — and without a clear answer the work continues on explicitly stated assumptions.

**Output.** The prompt always produces exactly ten blocks:

1. Goal & context
2. Working definition
3. Baseline model
4. Assumption list
5. Iteration A — targeted
6. Iteration B — orthogonal
7. Iteration C — counter-intuitive
8. Final synthesis
9. Guardrails
10. Closing

The closing is deliberately fixed to one sentence, *"Start now with step 1."*, so that the framework turns directly into an operational work flow instead of ending as a document.

The full text is in [the BREACH prompt](prompt.md).

## Quality check

A good BREACH result answers every question with "yes":

- Was at least one load-bearing assumption genuinely removed or inverted?
- Did the system have to reorganize structurally afterwards?
- Does the value logic visibly change?
- Are there clear trade-offs instead of pure marketing advantages?
- Is a real implementation route described?
- Are risks and misuse cases named?
- Is there a test plan for the unproven parts?

If not, the result is probably just a variation of the starting model.

## What BREACH is not

BREACH is not a generic idea collection, a feature backlog, an automatic "AI-first" solution reflex or the rebranding of an existing concept.

BREACH is a structured compiler: **topic → baseline → assumption break → reorganization → synthesis**.

## Status and open hypotheses

BREACH is experimental. It is used in the development of Nova AI Workspace, but it is not tied to browsers or software. Its effects have not yet been measured in a controlled study. The claims above are stated as hypotheses:

- **H1 — structural diversity.** At equal output budget, BREACH produces more structurally distinct solutions than repeated sampling of the same prompt at elevated temperature.
- **H2 — viability.** BREACH solutions are rated at least as viable as temperature-sampled ones, because diversity comes from conditioning rather than from noise.
- **H3 — model size.** The advantage over plain prompting remains with smaller models at normal temperature.
- **H4 — transfer.** The method carries over to fields outside software, such as research questions and organizational design.

A fair test compares, for the same topics and the same token budget: (a) one plain prompt, sampled several times at elevated temperature, against (b) BREACH. Blinded raters judge pairs of solutions for structural difference (different value logic, different mechanics or different owner of the core step, not just different wording) and for viability. Embedding distances can serve as a secondary, automatic measure.

Known limits: the quality of the result depends on choosing assumptions that really carry the model; a weak assumption list yields weak iterations. The model can also reintroduce a broken assumption without saying so — the guardrails make this visible, but they do not prevent it.

## History and first publication

BREACH was developed by Joel Aniol on his own.

- **7 March 2026 — first draft.** A short working prompt titled "Innovation destabilization": build a classic base concept, list its 5–7 central assumptions, break one radically, reorganize the whole system, check whether a worse version or a structurally new category came out, repeat at least three times. The text is preserved in [the BREACH prompt](prompt.md#the-first-draft-7-march-2026).
- **22 March 2026 — BREACH.** The draft became the full method with its name, the explicit assumption form, orthogonal iterations, hypotheses and test plans, the ten-block meta-prompt — and its first public presentation.

Public records of the method:

- Aniol, J. *BREACH* — first public post on LinkedIn, 22 March 2026: <https://www.linkedin.com/posts/joelaniol_artificialintelligence-aiagents-futureofwork-activity-7441558430269706240-PsHJ>
- Aniol, J. *BREACH* — video explanation on YouTube: <https://www.youtube.com/watch?v=RQBagueu0K4>

## References

- Altshuller, G. S. *Creativity as an Exact Science: The Theory of the Solution of Inventive Problems.* Gordon and Breach, 1984.
- de Bono, E. *Lateral Thinking: Creativity Step by Step.* Harper & Row, 1970.
- Holtzman, A., Buys, J., Du, L., Forbes, M., Choi, Y. *The Curious Case of Neural Text Degeneration.* ICLR 2020.
- Kirk, R., Mediratta, I., Nalmpantis, C., Luketina, J., Hambro, E., Grefenstette, E., Raileanu, R. *Understanding the Effects of RLHF on LLM Generalisation and Diversity.* ICLR 2024.
- Kuhn, T. S. *The Structure of Scientific Revolutions.* University of Chicago Press, 1962.
- Popper, K. *The Logic of Scientific Discovery.* Hutchinson, 1959.
- Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., Zhou, D. *Self-Consistency Improves Chain of Thought Reasoning in Language Models.* ICLR 2023.
- Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., Narasimhan, K. *Tree of Thoughts: Deliberate Problem Solving with Large Language Models.* NeurIPS 2023.
- Zhang, J., et al. *Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity.* arXiv, 2025.

## Citing

> Aniol, J. (2026). *BREACH — Baseline Reorganization through Explicit Assumption Change & Hypothesis.* First documented March 2026 (LinkedIn, 22 March 2026).

Next: [the BREACH prompt](prompt.md)
