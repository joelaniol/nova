# Agent-Native Affordances

> Agents should not have to unlearn what they already know in order to use Nova.

Nova AI Workspace was built **with AI agents, as well as for them**. Their recurring expectations helped shape its interface: familiar action names, parameter conventions and client-specific spellings can lead to the same canonical Nova operation.

This is a core feature of Nova's cognitive runtime: the fit between the agent and the interface through which it perceives, acts, verifies and learns. Aliases are one concrete mechanism behind that fit.

**Affordances include naming compatibility, argument conventions, discoverability, repair guidance, and familiar interaction patterns.** The principle shapes both the names an agent recognizes and the way it discovers capabilities, recovers from a rejected call and chooses a level of control.

## Learned expectations as design input

An agent arrives with patterns learned from browser automation, computer-use tools and previous tasks. It may reach for `goto`, `fill` or `evaluate`, or describe a text payload as `value`. Here, **bias** means this learned expectation about how an interface works.

Nova uses recurring naming mismatches and established interaction conventions as feedback for interface design. Where an expectation has a clear equivalent, a compatibility bridge can make it useful instead of requiring another instruction explaining a different spelling.

This feedback is incorporated during development. Nova does not invent or install new aliases automatically during a browsing session.

## Three ways to reach a capability

| Route | How the agent finds its way |
| :--- | :--- |
| Explicit | Reads Nova's instructions and loads the canonical tool schema. |
| Semantic | Searches tool names and descriptions, or loads a task-specific capability bundle. |
| Familiar | Uses a supported name or argument convention it already knows; Nova resolves it to the canonical operation. |

These routes work together. Discovery supplies the precise contract; familiar conventions provide compatible entry points. Agents should still load the relevant bundle and follow Nova's instructions.

## What Nova supports today

### Familiar action names

Selected tool aliases connect common automation vocabulary to Nova's tools:

| Accepted alias | Canonical Nova tool |
| :--- | :--- |
| `nova.goto` | `nova.navigate` |
| `nova.fill` | `nova.type_selector` |
| `nova.evaluate` | `nova.eval` |
| `nova.screenshot` | `nova.capture_screenshot` |

These are name mappings to Nova operations. They do not reproduce every behavior of the framework from which a name is familiar.

### Familiar argument names

Nova also normalizes supported parameter spellings before validation and execution. For example, on text-input tools `value` can become `text`; on `nova.memory_note`, `kind` can become `memoryType`; on `nova.read_text`, `chars` can become `maxChars`.

Mappings are scoped to the operations where their meaning matches. A field named `value` remains `value` on operations such as cookie setting, where it is already canonical. If both an alias and its canonical field are supplied, **the canonical field wins**.

Nova also accepts supported parsable string forms for numeric and boolean arguments. Allowed values, bounds and required fields still apply.

### Client naming compatibility

Agents sometimes copy a client-visible name into a workflow step or an exact tool lookup. Nova recognizes supported flattened namespace spellings and client prefixes and resolves them to its canonical names.

Antigravity additionally has a dedicated proxy mode that presents compatible underscore names and translates calls back to Nova's dotted names. That client-specific projection leaves the standard catalog for other clients intact.

### Instructions and capability bundles

`nova.get_instructions` gives the agent its operating guidance. `nova.tools_bundle` provides task-specific discovery and schemas on demand. An agent can search in natural language, such as `query="table extraction"`, without knowing the tool's name. Together with the compatibility layer, these make the interface both discoverable and familiar.

See the [MCP discovery model](../../mcp-reference/README.md) and [agent integration guides](../../integration/README.md).

### Repair guidance and levels of control

Supported error and gate responses give the agent a concrete next step. For example, a perceive-first gate identifies the missing observation and directs the agent to `nova.perceive` with `mode='summary'`. Repair guidance helps an agent continue through the valid workflow rather than repeatedly guessing at a rejected call. See [AAG](../agent-awareness-gates-aag/README.md).

Nova also offers progressively lower levels of control: guarded workflow macros such as `nova.guarded_login`, individual selector and input operations, and Chrome DevTools Protocol (CDP) access. An agent can start with a task-level operation and move to finer control when the task requires it. Each level retains its own contract and permissions; lower-level access does not bypass safety gates.

## One operation, one contract

Aliases resolve into the existing canonical dispatch path. The same argument validation, permission checks, tab claims and awareness gates apply. A familiar spelling grants no extra authority.

Discovery lists canonical tools rather than adding every alias as another tool. Client-specific name projection is a separate compatibility layer. This keeps the catalog understandable while preserving supported alternative entry points.

An ambiguous name, a different unit or a different safety meaning requires an explicit contract decision. Nova's design principle is to accommodate a clear learned expectation while keeping the operation's meaning precise.

## How this fits the cognitive runtime

Agent-native affordances help an agent reach a capability. [AAG](../agent-awareness-gates-aag/README.md) checks whether it is ready to act, and the [closed-loop system](../closed-loop-system-cls/README.md) checks the outcome. [PKS](../learning/phenomenological-knowledge-store-pks/README.md), [task memory](../learning/episodic-task-memory-etm/README.md) and the [learning pipeline](../learning/agent-learning-pipeline-alp/README.md) support knowledge acquired through use.

The development feedback loop complements those runtime mechanisms: observed agent behavior helps shape Nova's interface itself. The intended benefit is less naming friction and unnecessary relearning; this page makes no quantified claim about speed or task success.

## Related documentation

* [Core features](../README.md)
* [MCP reference and discovery](../../mcp-reference/README.md)
* [Agent integration](../../integration/README.md)
* [Agent awareness gates](../agent-awareness-gates-aag/README.md)
* [Closed-loop system](../closed-loop-system-cls/README.md)

[All core features](../README.md)
