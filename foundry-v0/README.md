# Foundry V0

The first and current built version of Foundry. Everything in this folder is real and in use.

- **`BOOTSTRAP.md`** — the birth sequence + loading rule a fresh agent runs first.
- **`foundation/`** — the *behavioral* branch: how an agent thinks and works. Loaded in full by every agent, always. (9 files: the execution loop, memory architecture, self-improvement, orchestration, reliability, the quality rubric, the red lines, and two enforced build laws — compartmentalization and the mistake engine.)
- **`knowledge/`** — the *technical* branch: production capabilities. The index (`knowledge/INDEX.md`) is read at startup; individual capability files load **only when a task triggers them**. Spine: `INDEX.md`, `DECISION_RULE.md`, `tool-registry.md`, `INSTANTIATION_GUIDE.md`, `BOOTSTRAP_loading_section.md`. Capabilities: retrieval, guardrails, evaluation, observability, orchestration, deployment, the tool layer (MCP), memory systems, cost/routing, context engineering.

**Where to start:** read `BOOTSTRAP.md`, then `knowledge/INDEX.md`. The two non-negotiable principles — *no bias* and *no authority over judgment* — are explained in the top-level README and on the site.
