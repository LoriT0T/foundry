# TOOL REGISTRY — Runnable Tools, Keyed by Data Source

> **What this is.** The **schema and registration discipline** for *running tools* (MCP servers), keyed by data source. Distinct from `INDEX.md`: the INDEX maps *knowledge* (how to build things); this defines how *tool instances* (things already built and callable) are catalogued. **The instances themselves are registered in the project layer, never in this file** — it must stay bias-free (`foundation/RED_LINES.md`: no project specifics in `knowledge/`). Knowledge is loaded; tools are connected.
>
> **Where it sits.** `~/Foundry/knowledge/tool-registry.md`. Paired with `DECISION_RULE.md`, which is the logic an agent applies *against* this registry.
>
> **The one rule that makes this work:** **entries are keyed by DATA SOURCE, not by function.** Two agents that both "do RAG" over *different* knowledge bases need *different* tool instances. Two agents over the *same* knowledge base share *one*. So the trigger names the data, never the category. "Connect when your task needs the *enterprise-client knowledge base*" — never "connect when your task needs RAG."

---

## How to read an entry

| Field | Meaning |
|---|---|
| **Tool name** | The registered MCP server name (used in `claude mcp list`). |
| **Data source** | The specific knowledge base / data this instance serves. **This is the key.** |
| **Trigger** | Connect when your task needs *this data source*. |
| **Context cost** | Rough size its tool definitions add to context once connected. Informs "is it worth connecting." |
| **Scope** | `user` (all projects on the machine) · `project` (one project, via `.mcp.json`). |
| **Connect command** | The literal command to wire it up. |
| **Pattern** | Which `knowledge/` file this instance was built from (so it can be rebuilt/extended consistently). |
| **Status** | `live` · `planned` · `retired`. |

---

## No instance rows live here

This file holds **no registered tools — not even an example one.** A populated row is an *instance* (it names a real data source), and instances are project specifics that never enter `knowledge/` (`foundation/RED_LINES.md`). The **row shape** is illustrated in the project-layer scaffold `~/Foundry/project/TOOL_REGISTRY.template.md`, where real rows are written. This file defines the *fields* (above) and the registration *discipline* (below); the project's `TOOL_REGISTRY.md` holds the *instances*.

---

## The register-on-creation rule (the anti-sprawl mechanism)

This is what stops every new agent from rebuilding tools that already exist.

1. **Before building a tool**, the agent checks this registry for an existing entry whose **data source** matches its task's data. (This is `DECISION_RULE.md`.)
2. **If a match exists →** connect to it. Do not build. Stop.
3. **If no match →** instantiate the relevant `knowledge/` *pattern* against the new data source. This is *not* writing a tool from scratch — it's pointing an existing, documented pattern at a new database.
4. **Immediately register the new instance in the project layer** (the project's own tool registry), in the same change — **never in this file**, which stays bias-free (`foundation/RED_LINES.md`). An unregistered tool is invisible to the next agent in that project, which would then wastefully rebuild it. Registration is what makes capability *compound* instead of *duplicate*.

---

## When a second instance is correct (and when it's sprawl)

- **Correct (different data):** two different document sets (Dataset A and Dataset B) are different knowledge bases → two instances of the *same* RAG pattern, pointed at different databases. Not sprawl.
- **Sprawl (same data):** two agents each standing up their own RAG server over the *same* document set → waste, double indexing, guaranteed drift. The registry exists to prevent exactly this.

The test: **same data → reuse. Different data → instantiate the pattern. Always → register.**

**Maturity:** `[Draft — structural]`. The data-keyed schema and register-on-creation rule are proposed; verify the first time two real agents hit the registry with one matching and one non-matching data source. *Registration location clarified to the project layer (2026-06-04, first real instantiation) — resolves a contradiction with `foundation/RED_LINES.md`; see `MAINTENANCE.md` §7.*
