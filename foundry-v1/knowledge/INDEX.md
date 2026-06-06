# INDEX — Knowledge Layer Capability Map

> **What this is.** The map of the technical layer. Every `knowledge/` file is listed here with the task that triggers it, its maturity, and the execution phase it serves. An agent reads this map at startup (per `BOOTSTRAP`) and loads the underlying files *only on trigger*.
>
> **Where it sits.** `~/Foundry/knowledge/INDEX.md`. Siblings: `tool-registry.md` (the data-keyed tool menu), `DECISION_RULE.md` (reuse-or-instantiate logic), and `INSTANTIATION_GUIDE.md` (the runbook an agent follows to turn these patterns into its own instances).
>
> **How to use it.** Match your current task against the **Trigger** column. Load only the rows that match. Respect the **Maturity** tag — never treat `[Reference]` content as proven house style. Check the **Phase** column to know *when* in the loop the knowledge applies.

---

## How to read a row

| Field | Meaning |
|---|---|
| **Capability** | The technical concern the file covers. |
| **File** | The knowledge file to load when triggered. |
| **Trigger** | The task condition that justifies loading it. Phrased around *what the task does*, not the category. |
| **Illustration** | How complete the worked example is: *runnable code* (read and run to see the pattern) or *prose standard* (concept + tooling + pattern + failure modes, no code yet). Not an authority ranking — see status note below. |
| **Phase** | Which execution-loop phase the knowledge plugs into (Plan / Execute / Test / Improve). |
| **Tool?** | Whether this capability is realized as a runnable tool (instances registered in the project layer, per the `tool-registry.md` schema). |

---

## The map

> **Status (honest, one authority level).** Every file here is **reference knowledge the agent builds from** — none is a blessed or deploy-ready answer, and none outranks the agent's judgment about its own context. The only difference between files is *how complete the illustration is*, not how much authority it carries: **RAG** includes a runnable illustration (code you can read and run to see the pattern concretely); the **other ten** document the standard in prose (concept + key pattern + failure modes, plus current tooling where the capability has any) without code yet. A fuller illustration is easier to learn from — it is **not** a reason to prefer that capability. The agent always decides whether to adapt an illustration, instantiate a pattern, or build something else its context requires. "Illustration" below states how complete each one's worked example is.

| Capability | File | Trigger | Illustration | Phase | Tool? |
|---|---|---|---|---|---|
| **Retrieval (RAG)** | `rag-retrieval/SKILL.md` | Task needs the agent to answer from a body of documents/knowledge it wasn't trained on | Runnable code | Plan, Execute | Yes |
| **Guardrails** | `guardrails/SKILL.md` | Task touches untrusted input, sensitive/PII data, exposes tools, or deploys off localhost | Prose standard | Execute | Sometimes |
| **Evaluation** | `evaluation/SKILL.md` | Task changes a prompt, skill, model, or retrieval setup and needs to know if quality moved | Prose standard | Test | No |
| **Observability** | `observability/SKILL.md` | Task builds/reviews a production agent / needs tracing, cost, or latency visibility | Prose standard | Test, Improve | No |
| **Orchestration** | `orchestration/SKILL.md` | Task runs a multi-step or long-running workflow needing retries, resume, branching, or human approval | Prose standard | Plan, Execute | No |
| **Deployment** | `deployment/SKILL.md` | Task moves a system off localhost / needs containers, CI/CD, IaC, or environments | Prose standard | Execute | No |
| **Tool layer (MCP)** | `mcp-tools/SKILL.md` | Task exposes a capability to an agent as a callable tool | Prose + RAG's `mcp_server.py` shows it working | Execute | N/A (this IS the tool mechanism) |
| **Memory (technical)** | `memory-systems/SKILL.md` | Task needs durable agent memory beyond the foundation's markdown brain, at scale | Prose standard | Plan | Sometimes |
| **Cost / Routing** | `cost-routing/SKILL.md` | System makes enough model calls that cost, model choice, or provider reliability matter | Prose standard | Execute | No |
| **Context engineering** | `context-engineering/SKILL.md` | Task assembles a model call's context — choosing in-prompt vs. retrieval, budgeting the window, versioning prompts, compacting history, or caching prefixes | Prose standard | Plan, Execute | No |
| **Regulatory architecture** | `regulatory-architecture/SKILL.md` | The project operates in a regulated domain — it handles data or actions an external authority can penalize (personal/health/financial/legal data, identity assurance, retention, cross-border flows), or the principal names a jurisdiction + domain with binding rules. Recognize via the file's §1 check; if negative, never load. | Prose standard (discipline — no code) | Plan, Execute | Sometimes |

---

## Maintenance loop (so the map doesn't rot)

- **On adding a file:** add its row here *in the same change*. A knowledge file not in the INDEX is invisible to every agent — the INDEX is the only entry point.
- **On promoting maturity:** update the tag here when a `[Reference]` file is actually built and verified, or when a `[Current as of DATE]` file's volatile tooling is re-checked.
- **Volatile-tooling note:** capabilities whose *tools* move fast (observability backends, orchestration frameworks, guardrail libraries) carry a re-verify date inside the file. The concept is stable; the tool list is a snapshot. This INDEX tracks the concept's maturity; the file tracks its tools' freshness.

**Maturity of this INDEX itself:** `[Established — verified 2026-06-01]`. The row schema and loading contract were confirmed against a fresh, context-less agent: it read this map at startup, loaded no capability file there, and on a triggering task pulled exactly the one matching file (and none irrelevant) — see `~/Foundry/MAINTENANCE.md` §6.
