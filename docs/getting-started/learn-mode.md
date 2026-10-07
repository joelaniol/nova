# Use Learn Mode for Recurring Website Work

After your first task in Nova, think about the websites you use repeatedly. If you want your agent to understand how a site works and prepare for later tasks, ask it to use **Nova's Learn Mode**.

## What changes compared with a normal task?

A normal task aims to finish the work you asked for now. Learn Mode aims to explore the website, verify its workflows, and document a reusable understanding of it.

| Your request | What the agent should deliver |
|---|---|
| “Find three relevant products on this website.” | The requested products, with checked details and source links. |
| “Use Nova's Learn Mode to understand how product search and comparison work on this website.” | A verified map of the relevant website features, repeatable steps, prerequisites, fragile areas and remaining unknowns. |

Learn Mode usually takes longer than a single task: the agent explores different pages and states and checks whether the steps actually work. The benefit is a foundation for later tasks, rather than having to rediscover every workflow.

## Does Nova learn without Learn Mode?

**Yes. Your agent and Nova also build website knowledge during normal tasks.** Nova collects evidence from successful interactions, recognizes recurring situations and checks whether that experience is reliable enough to reuse.

This learning happens gradually as you use the website. It usually takes more tasks or visits to build a useful understanding, because the agent focuses on your immediate goal and only encounters the parts of the site needed for that task.

**Learn Mode makes learning the goal of the session.** The agent deliberately explores navigation, different states and workflows, verifies what works, and produces a structured playbook. That focused exploration can build a useful understanding sooner than waiting for the same experience to accumulate during everyday tasks. It still needs evidence; choosing Learn Mode does not make untested steps reliable.

You can keep using Nova normally and let knowledge grow over time, or ask for Learn Mode when you want to prepare a recurring workflow more deliberately.

## When should I use it?

Use Learn Mode when you want to understand an unfamiliar website or expect to repeat work there, for example:

- Searching and comparing items in the same catalog.
- Finding records and understanding filters in a portal you use regularly.
- Learning where a website's main features are and what is needed to use them.
- Checking an existing workflow again after a site changed.

For a one-off lookup, give your agent the task directly. You can ask for Learn Mode later if the same website becomes part of your regular work.

## How to ask your agent

First check that your agent is [connected to Nova](quickstart.md#3-restart-your-ai-program). Then paste this into your AI program and replace the website and workflow:

> Use Nova's Learn Mode to understand [website URL]. I expect to repeat [workflow]. Explore the relevant navigation and states, verify the steps you can safely test, and produce a reusable platform playbook. Explain prerequisites, fragile areas and anything you could not verify. Ask me if the intended scope is unclear. Do not make purchases, send messages, delete data or change my account without my approval.

For example:

> Use Nova's Learn Mode to understand this catalog: [URL]. I regularly compare products by technical specifications. Learn how search, filters and product details work, and how to verify a comparison. Keep the exploration read-only and show me the playbook and any blockers.

You supply the website, your intended workflow and the allowed boundaries. The agent retrieves Nova's learning instructions, handles the tools and checks the results. You do not need to write tool calls or configure an output mode.

If login is needed, tell the agent which Nova sandbox contains the appropriate session. If access or your instructions prevent part of the exploration, the agent should report that part as blocked rather than claim it was tested.

## What should I get back?

Learn Mode's final result is a **`PLATFORM_PLAYBOOK`**. Ask the agent to explain it in ordinary language. It should show:

- What the website does and which areas were explored.
- How to reach relevant features and what access they require.
- Repeatable workflows, with checked steps and evidence.
- Where the workflow is fragile, blocked or still uncertain.

The playbook documents what was learned. Nova's website memory can also retain verified procedural knowledge for later agent sessions; a written playbook alone does not mean every step has become an active, automatically executed rule. Learned knowledge is checked for reliability and can become outdated when the site changes.

## Use what was learned in the next task

Next time, give your agent the actual task and refer to the learned workflow:

> Use Nova and the website knowledge we verified for [website] to do [task]. Check that the workflow still matches the site today. If it changed, tell me what needs to be checked again before proceeding.

If the previous playbook exists only in an earlier conversation or a saved document, provide it to the agent or tell it where to find it. The agent still needs a working Nova connection and authorization for the task.

**Project onboarding and Learn Mode serve different purposes.** [Project onboarding](advanced-onboarding.md) puts Nova references in your working folder so later agent sessions can find its instructions. Learn Mode explores a website and its workflows. Neither grants permission for purchases, sending messages or account changes.

You can watch the exploration in Nova and use [Emergency Stop](emergency-stop.md) to interrupt it. For deeper technical explanations, see [Website memory (PKS)](../core-features/pks.md) and [the learning pipeline](../core-features/learning-pipeline-alp.md).
