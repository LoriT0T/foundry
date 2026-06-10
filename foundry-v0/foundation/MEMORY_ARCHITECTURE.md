# MEMORY_ARCHITECTURE — how the agent remembers and stays itself

> **What this is.** Where memory lives, why it lives outside the conversation, and the one-home-per-fact discipline that keeps it from rotting. An agent that cannot remember well cannot improve, because it relearns instead of compounding.
>
> **Where it sits.** `~/Foundry/foundation/MEMORY_ARCHITECTURE.md`. It underpins Phase 0 (rehydrate) and Phase 6 (record) of `THINKING.md`. For durable memory *at production scale*, it hands off to `knowledge/memory-systems/SKILL.md` (the engineered version).
>
> **Status.** `[Established]`. Bias-free: it describes the structure of memory, not any agent's contents.

---

## The core problem

An automated agent does not run as one long conversation. **Each run is a fresh mind with no memory of before.** So memory cannot live in the chat — it must live **outside**, in durable files the agent re-reads at the start of every run. This single fact shapes everything: the first act of any run is to **rehydrate** — read the memory, remember who you are and what you've learned, *then* act.

## The two laws

1. **If a fact would be costly to rediscover, write it down.** Memory is cheap; relearning is expensive. No mental notes — if it should persist, it goes to a file.
2. **The agent updates its own memory.** When it learns something or makes a mistake, it edits the durable files itself. A memory only humans can write to stops growing.

## The two laws, applied *during* a task (in-run durability)

The laws don't wait for Phase 6. On a long task the live context is **volatile** — an interruption or a compaction can erase everything not yet written down. So apply both laws *within* the run: at every milestone, externalize the **decisions made, progress reached, and open questions** to the `project/` layer — not only at the close. Anything costly to reproduce is committed the moment it exists, so a mid-task loss costs minutes, not the whole run. This is not a new rule — it is *"if it's costly to rediscover, write it down"* and *"the agent updates its own memory"* running continuously, applied during execution (`THINKING.md` Phase 3).

---

## Where things go (one home per fact)

| Surface | Holds | Written |
|---|---|---|
| `identity/` (filled) | Who the agent is; who it serves; its environment | Deliberately, as identity evolves |
| `project/<...>` state | Per-project goal, current state, known gaps, next action, log | Every session touching that project |
| `project/<...>` LESSONS + FAULTS | Durable rules and tracked mistakes (via `MISTAKE_ENGINE.md`) | On any real mistake |
| `runtime/memory/YYYY-MM-DD.md` | Raw daily log — what happened, decisions, blockers | Every session with significant work |
| Curated long-term memory | Distilled narrative of what matters, pruned | Periodic distill; significant events |
| `skills/<...>/SKILL.md` | Reusable procedures | When a workflow repeats 3+ times |
| `runtime/iterations/<file>.<date>` | Snapshots of core files before a rewrite | Before any major rewrite |
| Compact key-value memory (if the runtime offers one) | Small stable facts / preferences, auto-loaded next run | On a preference or correction |

**At scale,** when markdown files are no longer enough (many memories, fast retrieval, decay, confidence scoring), this maps onto an engineered memory system — typed stores (semantic / episodic / procedural / preference), async writes, rerank-on-retrieval. That is a *technical* concern: load `knowledge/memory-systems/SKILL.md` when the task triggers it. The "one home per fact" rule still governs which store owns what.

---

## Hygiene rules

- **One home per fact.** Compact facts in key-value memory; narrative in files; never both. Duplication drifts.
- **Raw vs curated.** The daily log is raw and append-only; curated memory is distilled from it, periodically, and pruned. Curated ≠ bloated.
- **Snapshot before rewrite.** Before rewriting a core file, copy it to `runtime/iterations/<file>.<date>` (`QUALITY_RUBRIC.md` criterion 5). Then patch rather than full-rewrite unless the file is structurally wrong.
- **Distill on a rhythm.** Periodically walk the daily logs, fold what lasts into curated memory, propose lessons, and surface any sync-invariant violations (`SELF_IMPROVEMENT.md`).

---

## The boundary with the foundation

Memory is where the agent's **specifics** accumulate — its projects, its lessons, its logs. None of it lives in `foundation/` or `knowledge/`; those stay universal. Memory flows *out* of runs into `project/` and `runtime/`, never *back* into the two inherited branches (`README.md`, the contamination boundary).

> **For working memory:** Fresh mind every run → rehydrate first. Write what's costly to relearn — *in-run too*: externalize to `project/` at every milestone, the live context is volatile. One home per fact. Raw daily, curated distilled. Snapshot before rewrite. Scale → `knowledge/memory-systems`.
