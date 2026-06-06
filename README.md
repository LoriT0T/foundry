# Foundry

**An open methodology for building independent AI agents from a single, verified foundation.**

Foundry is a *copy-into-any-new-agent* foundation: clone it, run the birth sequence, and a new agent stands up at a high quality floor — the thinking, the engineering discipline, and the method to instantiate both for its own context. Every agent born from Foundry is **independent**; they share a verified floor, not a runtime.

> **Foundry is a methodology, not a product.** There is nothing to `pip install` and no service to run. It is a structured set of documents an agent reads and instantiates. The value is the structure and the discipline — not code you depend on.

**Status:** Foundry **V0, V1, and V2 are built and in use.** V0 is the foundation; V1 adds operating under regulation; V2 adds knowing *which problem* to solve first (see the version ladder). Each version is a single evolving tree; older slots are frozen snapshots.

- 🔗 **Site:** `https://LoriT0T.github.io/foundry/`
- 📦 **Built on top of Foundry:** a real, safety-critical agent instantiated from this methodology — [site](https://lorit0t.github.io/agentic-reschedule-assistant/) · [repo](https://github.com/LoriT0T/agentic-reschedule-assistant)

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

As of V2 the sequence is bracketed by two mandatory recognition questions that carry **zero** specifics of their own: **first** — *is the problem real, or merely assumed?* (V2); and before building — *does this domain operate under external regulation?* (V1). A "yes/assumed" routes to the matching capability's research playbook; a "no/verified" loads nothing and the agent proceeds exactly as a V0-born one.

The answers form a reviewable **birth certificate**: before the agent does anything, you can read exactly what it decided it is. Then it loads the foundation in full, reads the knowledge index, and instantiates each capability against its own context.

## The version ladder

| Version | Status | What it adds |
|---|---|---|
| **V0** | ✅ **Built** — real, in use | The foundation: two branches, two principles, the birth sequence, the loading discipline. |
| **V1** | ✅ **Built** — real, in use | **Regulatory architecture** — recognizing a regulated domain and letting its *current, researched* rules drive the build, while the file itself carries zero rules, regimes, or jurisdictions. |
| **V2** | ✅ **Built** — real, in use | **Problem discovery** — determining *which problem* in a domain is actually worth solving, before building, while carrying zero markets, domains, or problems. Runs **first**, upstream of V1 and the build. |

Each version added a capability that holds **only the method**, never the specifics — a regulated agent researches its own rules (V1); an agent finds its own domain's real problem (V2). Both stay bias-free: an unregulated, problem-verified agent loads neither and behaves exactly as a V0-born one. `foundry-v0/` and `foundry-v1/` are frozen snapshots; the working foundation is a single evolving tree whose current state is V2.

## Proven under real use

Foundry is meant to improve as agents are actually built on it. The **first real instantiation surfaced a genuine contradiction inside Foundry itself** — one reference file's instruction conflicted with a foundation red line. It was resolved *at the class level* (every place the pattern appeared was fixed, not just the instance that surfaced), and the foundation was corrected. The methodology is built to catch and repair its own flaws under real use — and on its first contact with reality, it did.

## Repository structure

```
foundry-v0/          ✅ frozen snapshot — the original foundation
  BOOTSTRAP.md         the birth sequence + loading rule
  foundation/          behavioral branch (9 files)
  knowledge/           technical branch (index + 5 spine files + 10 capabilities)
foundry-v1/          ✅ frozen snapshot — V0 + regulatory architecture (11 capabilities)
foundry-v2/          ✅ current — V1 + problem discovery (12 capabilities)
index.html           the GitHub Pages site
LICENSE              MIT
```

## License

MIT — see [LICENSE](LICENSE). © 2026 Musaed Alqanaie.
