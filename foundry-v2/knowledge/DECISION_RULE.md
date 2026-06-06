# DECISION RULE — Reuse or Instantiate

> **What this is.** The literal logic a fresh agent runs when its task needs a tool. It sits between the agent and `tool-registry.md` and answers one question: *do I connect to something that exists, or build something new — and if I build, how do I avoid sprawl?*
>
> **Where it sits.** `~/Foundry/knowledge/DECISION_RULE.md`. Applied against your **project's** tool registry (whose schema is `tool-registry.md`), using patterns documented in the `knowledge/` files mapped by `INDEX.md`.
>
> **The core principle.** The deciding question is never *"am I a different agent or project?"* It is always ***"is this a different knowledge base?"***. Same data → reuse. Different data → instantiate the pattern. Either way → register.

---

## The rule

```
WHEN a task needs a tool (e.g. retrieval over some body of data):

  STEP 1 — Identify the data source.
    Name the specific knowledge base your task needs.
    (Not "I need RAG" — "I need to answer from <this specific document set>".)

  STEP 2 — Match against the registry.
    Look in your project's tool registry (project/<name>/TOOL_REGISTRY.md) for a LIVE
    entry whose `data source` = your data source.  (Its schema is knowledge/tool-registry.md.)

  STEP 3 — Decide.
    IF a matching live entry exists:
        → Connect to it.   (claude mcp add ... per the entry's connect command)
        → Do NOT build anything.
        → STOP.

    IF no matching entry exists:
        → Instantiate the relevant knowledge/ PATTERN against your data source.
          (This reuses documented code pointed at a new database —
           it is NOT writing a tool from scratch.)
        → Register the new instance in the PROJECT layer (the project's own tool
          registry), in the same change — never in knowledge/. (tool-registry.md
          defines the schema + discipline; instances stay out of knowledge/, per RED_LINES.)
        → Connect to it.
        → STOP.
```

---

## The trap to avoid (why "relates to the tool" is not enough)

"Connect when your task relates to the tool" is too loose, because two agents working on *different* document sets *both* "relate to" RAG — they both do retrieval. But they relate to **different knowledge bases**, so they correctly get **different instances**. The category being shared is a trap.

**So the match in STEP 2 is on the *data source*, never the function.** This is why every registry trigger names the data, not the capability. If you ever find yourself matching on "this task uses RAG," you're about to either wrongly share one instance across two data sets, or wrongly build a duplicate over the same data. Match on the data.

---

## What "instantiate the pattern" means (so it's never "build from scratch")

The maintenance fear — "every new agent has to build its own tools" — dissolves here. Nobody builds from scratch:

- The **code** lives once, as a documented pattern in the relevant `knowledge/` file (e.g. `rag-retrieval/SKILL.md`).
- An **instance** is that same code pointed at a different data source — a different database, a different document set.
- So a new data source costs you a new *instance* (cheap: configure + index + register), never a new *implementation* (expensive: design + write + debug).

Pattern documented once → instances as the data demands → registry remembers every instance → capability compounds.

---

## The three-line summary (for the agent's working memory)

> 1. Name your data source.
> 2. Registry has it? Connect and stop. Registry doesn't? Instantiate the pattern, register it, connect, stop.
> 3. Match on data, never on function.

**Maturity:** `[Draft — structural]`. Verify the first time two real agents apply this: one whose data source matches an existing entry (must reuse), one whose data source is new (must instantiate + register). Promote to `[Established]` once both paths are observed working.
