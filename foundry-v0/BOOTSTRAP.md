# BOOTSTRAP — how a fresh agent becomes itself

> **What this is.** The first file a new agent runs. It turns the Foundry folder from documentation into a working agent: it states the loading rule that governs both branches, then walks the birth sequence that produces an agent tuned to one specific context — without copying anyone else's specifics, and without rebuilding what already exists.
>
> **Where it sits.** `~/Foundry/BOOTSTRAP.md`. It references `foundation/` (the thinking), `knowledge/INDEX.md` (the technical map), `knowledge/DECISION_RULE.md` + `knowledge/tool-registry.md` (tools), and `knowledge/INSTANTIATION_GUIDE.md` (the technical runbook in full).
>
> **The rule it enforces, in one line.** *Foundation: load all, always. Knowledge: read the index always, load files on task-trigger. Tools: connect only when your task's data matches the registry.*

---

## Part 0 — The loading rule (the integration contract between the two branches)

The two branches have different loading rules on purpose. `foundation/` is bounded and universal — loading it fully has a fixed, small cost and a guaranteed benefit. `knowledge/` is open-ended and per-task — loading it fully has an unbounded, growing cost and an often-zero benefit. That asymmetry is why they are separate folders, and it is why a fresh agent loads in this exact order:

1. **Load all of `foundation/` — fully, always.** Small, universal, behavioral. Every agent needs the thinking, the loop, the memory architecture, the red lines. No selective gate. Read it all, internalize it, never edit it.

2. **Read `knowledge/INDEX.md` — always, but only the index.** The INDEX maps the technical layer: which files exist, what task each is *for* (its trigger), how mature it is, which execution phase it serves. Reading the map is cheap. Loading the territory is not — stop at the map.

3. **Load a `knowledge/` file ONLY when the current task triggers it.** Match the task against the INDEX triggers; load the minimum set the task actually needs. An unloaded knowledge file costs nothing — it is documentation on disk, not context.

4. **Connect a tool ONLY when the task's *data source* matches the registry.** Read `knowledge/tool-registry.md` (the registration *schema*) and your project's `TOOL_REGISTRY.md` (its live instances); apply `knowledge/DECISION_RULE.md`. Match on the *data source*, never the function: same data → reuse the live instance; different/new data → instantiate the pattern against it and register it **in your project layer**, in the same change. Connecting a tool loads its definitions into context — connect only what the task's data demands, nothing speculative.

> **For working memory:** Foundation load-all. Knowledge index-then-trigger. Tools data-match-only.

*(This section is the master copy of `knowledge/BOOTSTRAP_loading_section.md`, folded in here as required. It is a section of this bootstrap, not a competing one.)*

---

## Part 1 — The birth sequence (run once, at creation)

```
STEP 0 — Digest the foundation.
  Load all of foundation/ (behavioral, universal). Read knowledge/INDEX.md (the
  map only). Do NOT load individual knowledge files yet.

STEP 1 — Gather your context.  ← the ONLY place your specifics enter, ever.
  Answer the birth questions below from YOUR own goal/subject — never from the
  foundation. The foundation does not know what you work on, and must not.

STEP 2 — Become someone.
  Fill the identity/ templates → your living SOUL / USER / TOOLS. This is where
  the agent gets a name, a voice, a principal to serve, and an environment.

STEP 3 — Scaffold your first project.
  Copy the project/ templates into the project's home. They start empty; you
  fill them as the work produces state, faults, lessons, and architecture.

STEP 4 — Select the capabilities you need.
  Walk knowledge/INDEX.md and pick the MINIMUM set of capabilities your goal
  requires. Selecting is not loading everything — load each file only as you
  apply it.

STEP 5 — Instantiate tools (per capability that has one).
  Run knowledge/DECISION_RULE.md against your project's TOOL_REGISTRY.md (its
  schema is knowledge/tool-registry.md): name your data source → reuse the
  matching live instance, or instantiate the pattern against your data and
  REGISTER it in your project layer. Full runbook: knowledge/INSTANTIATION_GUIDE.md.

STEP 6 — Run one loop end-to-end, verify, record.
  Execute one full pass of the execution loop (foundation/THINKING.md) on a real
  task. Verify against STEP 1's "working well." Record what you instantiated and
  why in your project layer. Then the agent is alive — at a high floor, tuned to
  its own context, with none of any other agent's specifics inside it.
```

### The birth questions (answer from YOUR context, not from the foundation)

1. **Goal** — in one sentence. And what does *"this is working well"* look like, concretely and verifiably?
2. **Judgment vs. determinism** — where does the task need real judgment (reserve the model there) and where is it just rules and math (make that deterministic and reliable)?
3. **Data** — what data sources will it work with? Name each *distinct knowledge base*. What language / domain does that data sit in?
4. **Irreversibility** — what actions are risky or irreversible (money, public messages, deletions)? Those get a human gate or a hard coded limit — never a free hand.
5. **Cadence** — what rhythm does it run on, and how should it keep its principal informed?

Start small: one reliable loop end-to-end, proven and reporting, before adding power.

---

## Part 2 — The standing loop (every run after birth)

Each automated run is a **fresh mind with no memory of before.** So the first act of every run is to *rehydrate*:

1. **Rehydrate.** Load `foundation/` (the thinking). Read `knowledge/INDEX.md` (the map). Read the agent's own `identity/` and the relevant `project/` state.
2. **Run the execution loop** (`foundation/THINKING.md`). In the **Plan** phase, ask explicitly: *does this task trigger a knowledge file or a tool?* If yes, load the minimum set (Part 0, steps 3–4). If no, proceed on the foundation alone.
3. **Execute compartmentalized** (`foundation/COMPARTMENTALIZATION.md`): smallest units, one orchestrator, fix at the root.
4. **Verify with evidence**, then **record**: update `project/` state and `runtime/` logs. On any mistake, run the **mistake engine** (`foundation/MISTAKE_ENGINE.md`) — climb to the invariant, wire the guardrail.
5. **Never edit `foundation/` or `knowledge/`.**

---

## What you may and may not edit

| Area | Rule |
|---|---|
| `foundation/` | **Never edit.** Universal thinking, inherited unchanged. |
| `knowledge/` | **Never edit existing files.** Extend only by *adding* a new bias-free file plus its `INDEX.md` row, in the same change. |
| `identity/` | **Fill in once** at birth; thereafter edit deliberately as the agent evolves. |
| `project/`, `runtime/`, the agent's own `skills/` | **Write freely** — this is where the agent's specific life accumulates. |

---

## Maturity

**`[Established — verified 2026-06-01]`** (loading contract). A fresh, context-less agent booted against this rule and exhibited the required behavior: `foundation/` loaded fully, only `knowledge/INDEX.md` read, no knowledge file pulled until a task triggered one, specifics confined to STEP 1 (`MAINTENANCE.md` §6). **Still `[Draft — structural]`:** the build-time tool steps this boot did not exercise — STEP 4–5 instantiation via `knowledge/DECISION_RULE.md` + `tool-registry.md` — promote separately when an agent first builds a tool.
