# Foundry

**An open methodology for building independent AI agents from a single, verified foundation.**

Foundry is a *copy-into-any-new-agent* foundation: clone it, run the birth sequence, and a new agent stands up at a high quality floor — the thinking, the engineering discipline, and the method to instantiate both for its own context. Every agent born from Foundry is **independent**; they share a verified floor, not a runtime.

> **Foundry is a methodology, not a product.** There is nothing to `pip install` and no service to run. It is a structured set of documents an agent reads and instantiates. The value is the structure and the discipline — not code you depend on.

**Status:** Foundry **V0 is built and in use.** V1 and V2 are **planned placeholders** — each will be built later by its own dedicated agent (see the version ladder).

- 🔗 **Site:** `https://LoriT0T.github.io/foundry/`
- 📦 **Built on top of Foundry:** *(placeholder — a real agent project instantiated from this methodology; link added once that repo is public)*

---

## The two principles (non-negotiable)

1. **No bias.** The foundation carries *zero* project specifics — no domain, subject, person, or goal. Everything in it is universally true. Specifics enter only at instantiation, from the agent's own context, and flow *outward* into that agent — never back into the foundation. The test for anything in the branches: *would this be equally true for an agent doing something completely different?*

2. **No authority over judgment.** Every file is reference material an agent builds *from*, never an instruction it must obey. A file's completeness is not authority — the agent always decides whether to adapt a pattern, instantiate it, or build its own. Knowledge informs; it never commands.

## The two branches

- **`foundation/` (behavioral)** — how an agent thinks and works: the execution loop, memory architecture, self-improvement, reliability, the red lines, and two enforced build laws (compartmentalization, and a mistake-generalization engine that turns any single mistake into a rule its whole class can never repeat). Small, universal, **loaded in full, always.**
- **`knowledge/` (technical)** — production capabilities: retrieval, guardrails, evaluation, observability, orchestration, deployment, the tool layer (MCP), memory at scale, cost/routing, and context engineering. Larger, per-task, **loaded only when a task triggers a capability** — the index is read at startup; the files are not.

## The birth sequence

An agent born from Foundry decides the hard questions **before any code**:

1. The goal — and what "working well" looks like, concretely.
2. Where real judgment is needed vs. where the work is deterministic.
3. The data sources it will work with.
4. What is irreversible or risky, and therefore needs a human gate.
5. The cadence it runs on, and how it reports.

The answers form a reviewable **birth certificate**: before the agent does anything, you can read exactly what it decided it is. Then it loads the foundation in full, reads the knowledge index, and instantiates each capability against its own context.

## The version ladder

| Version | Status | What it adds |
|---|---|---|
| **V0** | ✅ **Built** — real, in use | The foundation: two branches, two principles, the birth sequence, the loading discipline. |
| **V1** | 🔲 **Planned** — not yet built | *To be defined when built (by its own agent).* |
| **V2** | 🔲 **Planned** — not yet built | *To be defined when built (by its own agent).* |

V1 and V2 are intentionally empty placeholders. Each will be built later by its own dedicated agent — exactly as V0 was — and its slot filled at that time. This repository does not describe their contents, because they have not been designed.

## Proven under real use

Foundry is meant to improve as agents are actually built on it. The **first real instantiation surfaced a genuine contradiction inside Foundry itself** — one reference file's instruction conflicted with a foundation red line. It was resolved *at the class level* (every place the pattern appeared was fixed, not just the instance that surfaced), and the foundation was corrected. The methodology is built to catch and repair its own flaws under real use — and on its first contact with reality, it did.

## Repository structure

```
foundry-v0/          ✅ the real, current foundation
  BOOTSTRAP.md         the birth sequence + loading rule
  foundation/          behavioral branch (9 files)
  knowledge/           technical branch (index + 5 spine files + 10 capabilities)
foundry-v1/          🔲 planned placeholder (ROADMAP.md only)
foundry-v2/          🔲 planned placeholder (ROADMAP.md only)
index.html           the GitHub Pages site
LICENSE              MIT
```

## License

MIT — see [LICENSE](LICENSE). © 2026 Musaed.
