# BOOTSTRAP — Loading Rule (knowledge layer)

> **What this is.** The instruction a fresh agent follows at session start to decide *what to load*. This file is the loading section only — it slots into the larger `BOOTSTRAP.md` your foundation agent owns. It governs the boundary between the two branches: `foundation/` (behavioral) and `knowledge/` (technical).
>
> **Where it sits.** `~/Foundry/BOOTSTRAP.md` (this section), referencing `knowledge/INDEX.md`, `knowledge/tool-registry.md`, and `knowledge/DECISION_RULE.md`.
>
> **Why it exists.** The two branches have *different loading rules*. Loading everything always would flood the context window with technical detail the current task doesn't need. This rule keeps the floor high and the context lean.

---

## The rule, in four steps

A fresh agent, on first wake, loads in this order:

1. **Load all of `foundation/` — fully, always.**
   The behavioral layer is small, universal, and identical across every project. Every agent needs the thinking, the loop, the memory architecture, the red lines. There is no selective gate here. Read it all, internalize it, never edit it.

2. **Read `knowledge/INDEX.md` — always, but only the index.**
   The INDEX is the map of the technical layer: what knowledge files exist, what task each one is *for* (its trigger), how mature it is, and which execution phase it plugs into. Reading the map is cheap. Loading the territory is not — so stop at the map.

3. **Load a `knowledge/` file ONLY when the current task triggers it.**
   Match the task against the INDEX triggers. A task that builds retrieval loads the RAG file; a task that posts content does not. Load the minimum set the task actually needs. An unloaded knowledge file costs nothing — it is documentation sitting on disk, not context.

4. **Connect a tool ONLY when the task's *data* matches the registry.**
   Read `knowledge/tool-registry.md`. Apply `knowledge/DECISION_RULE.md`: match your task's knowledge base against the registry, then reuse the existing tool or instantiate the pattern. Connecting a tool loads its definitions into context — so connect only what the task's data demands, nothing speculative.

---

## The one-line version (for the agent's working memory)

> Foundation: load all, always. Knowledge: read the index always, load files on task-trigger. Tools: connect only when your task's data matches the registry.

---

## Why this is safe to state as a hard rule

- `foundation/` is bounded and universal — loading it fully has a fixed, small cost and a guaranteed benefit.
- `knowledge/` is open-ended and per-task — loading it fully has an unbounded, growing cost and an often-zero benefit.
- The asymmetry is the whole reason the two branches are separate folders with separate rules. If a future maintainer ever moves a technical file into `foundation/`, this rule breaks — keep technical content in `knowledge/`.

**Maturity:** `[Established — verified 2026-06-01]`. A fresh, context-less agent booted against this rule and confirmed it: loaded `foundation/` fully, read only the index, and pulled no knowledge file until a task triggered one (`~/Foundry/MAINTENANCE.md` §6).
