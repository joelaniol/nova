# Learning Candidate Journal (LCJ)

The Learning Candidate Journal holds observations and candidate evidence. [Agent Learning Pipeline (ALP)](../agent-learning-pipeline-alp/README.md) uses that evidence to rank opportunities, generate candidates and evaluate their trust.

## Evidence and storage

The LCJ lives in its own database (`memory.db` in the `Memory` folder of Nova's profile), separate from `pks.db`.

The journal holds observations and candidate evidence. `nova.learn_generate` can already store a new phenomenon in PKS at L0, linked to that evidence by its candidate key. `nova.learn_promote` evaluates existing PKS entries against LCJ evidence; L0 therefore does not mean that an entry exists only in the journal. See [PKS learning levels](../phenomenological-knowledge-store-pks/README.md#5-why-knowledge-needs-trust-levels).


## Journal tools

`nova.memory_stats` and `nova.memory_add_candidate` belong to the journal, rather than to Browser Memory. See the [technical tool reference](../../mcp-reference/tools/pks-and-learning/README.md) for their contracts.

## Related documentation

- [Agent Learning Pipeline (ALP)](../agent-learning-pipeline-alp/README.md)
- [Phenomenological Knowledge Store (PKS)](../phenomenological-knowledge-store-pks/README.md)
- [Tool Observation Bus (TOB)](../tool-observation-bus-tob/README.md)

[All core features](../README.md)
