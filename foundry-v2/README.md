# Foundry — the foundation a new agent inherits

> **What this is.** The folder a new agent copies to boot itself to a high floor — the *thinking*, the engineering *standard*, and the *method* to instantiate both for its own context. Copy Foundry, follow `BOOTSTRAP.md`, and an agent stands up coherent, disciplined, and production-aware from its first run.
>
> **Where it sits.** `~/Foundry/`. Two branches (`foundation/`, `knowledge/`) plus the template and runtime areas (`identity/`, `project/`, `skills/`, `runtime/`).
>
> **The one idea.** *The architecture is the product; the model is a component dropped into it.* Foundry is that architecture, made copyable. A capable model given this folder should internalize it, instantiate it for its own goal, and then keep improving it — it is a floor to build on, never a ceiling to obey.

---

## The two axes

Foundry is organized along two independent splits. Understand these two and the whole layout is obvious.

### Axis 1 — Behavioral vs Technical (the two branches)

- **`foundation/`** — *how an agent thinks and acts.* Universal, small, behavioral. **Loaded fully, always.**
- **`knowledge/`** — *how an agent builds real systems:* retrieval, guardrails, evaluation, observability, orchestration, deployment, the tool layer, memory-at-scale, cost/routing. Larger, technical, per-task. **Its index is read always; its files load only when a task triggers them.**

They are **siblings, not nested**, because they have *different loading rules*. Loading the technical branch wholesale would flood the context window with detail the current task doesn't need. The full reason is stated in `BOOTSTRAP.md`. If a maintainer ever moves technical content into `foundation/`, the loading rule breaks — keep technical content in `knowledge/`.

### Axis 2 — What you inherit vs what you fill in

- **Inherit unchanged:** `foundation/`, `knowledge/`, the universal `skills/`. Copy verbatim; never edit. (Extend `knowledge/` only by *adding* a new bias-free file plus its `INDEX.md` row.)
- **Fill in once:** `identity/` — templates the agent completes at birth to become *someone serving someone*.
- **Starts empty:** `project/` (scaffolds copied per project) and `runtime/` (where the live agent writes as it works).

---

## The layout

```
~/Foundry/
├── README.md            ← you are here: the map
├── BOOTSTRAP.md         ← the seed: how a fresh agent becomes itself (run first)
├── MAINTENANCE.md       ← how the foundation stays alive (re-verify, promotion log)
│
├── foundation/          ← BEHAVIORAL · universal · load ALL, ALWAYS · never edit
│   ├── THINKING.md              the execution loop · mental models · uncertainty tiers
│   ├── MEMORY_ARCHITECTURE.md   rehydrate-first · one home per fact · what goes where
│   ├── SELF_IMPROVEMENT.md      the iteration loop · constraints-are-bugs · sync invariants
│   ├── ORCHESTRATION.md         self vs delegate vs schedule · the sub-agent contract
│   ├── RELIABILITY.md           deterministic-first · idempotency · degrade gracefully · verify
│   ├── QUALITY_RUBRIC.md        the scorer every foundation file and skill must pass
│   ├── COMPARTMENTALIZATION.md  ★ the build law — smallest reusable units (upgrade #1)
│   ├── MISTAKE_ENGINE.md        ★ never-repeat machinery — invariant + guardrail (upgrade #2)
│   └── RED_LINES.md             the non-negotiables
│
├── knowledge/           ← TECHNICAL · universal · INDEX always, files on trigger · never edit
│   ├── INDEX.md                 the capability map (read this at startup)
│   ├── BOOTSTRAP_loading_section.md   the loading rule (folded into BOOTSTRAP.md)
│   ├── DECISION_RULE.md         reuse-or-instantiate logic
│   ├── tool-registry.md         tool registration schema, keyed by data source
│   ├── INSTANTIATION_GUIDE.md   the runbook: pattern + your context = your instance
│   └── <capability>/SKILL.md    twelve capability files (one, RAG, carries runnable code)
│
├── identity/            ← FILL IN ONCE at birth (templates → the agent's living identity)
│   ├── SOUL.template.md         name · mode · voice · tone
│   ├── USER.template.md         the principal · their hierarchy · their hard rules
│   └── TOOLS.template.md        environment · tool roster · where secrets live
│
├── project/            ← COPY EMPTY, per project (scaffolds)
│   ├── AGENT.template.md · ARCHITECTURE.template.md · FAULTS.template.md
│   ├── LESSONS.template.md · CHANGELOG.template.md · NEXT_SESSION.template.md
│
├── skills/             ← reusable procedures (universal ones inherited; the agent grows its own)
│   ├── _TEMPLATE/SKILL.md       the SKILL.md shape
│   ├── skill-forge/SKILL.md     the meta-skill: the skill that makes and audits skills
│   └── brain-bootstrap/SKILL.md the session-start loader
│
└── runtime/            ← the live agent writes here (starts empty)
    ├── memory/                  daily logs YYYY-MM-DD.md
    └── iterations/              snapshots taken before any rewrite
```

---

## The contamination boundary (why this stays reusable forever)

`foundation/` and `knowledge/` contain **zero specifics** — no agent name, no user, no domain, no subject, no project name, no goal. Every statement in them is *universally true*. Specifics live **only** in `identity/` and `project/`, and they enter **only** at instantiation, from the agent's own context. Nothing specific ever flows back into the two branches.

**The test for any edit to `foundation/` or `knowledge/`:** *would this be equally true and useful for an agent working on something completely different?* If not, it is contamination — it belongs in `identity/` or `project/`, not here.

---

## How a new agent uses Foundry

1. **Copy** `~/Foundry/` into the new agent's home (or reference it in place).
2. **Follow `BOOTSTRAP.md`:** load `foundation/` fully → read `knowledge/INDEX.md` → fill the `identity/` templates → scaffold `project/` → run one loop end-to-end → verify.
3. **Live:** every run, rehydrate; load knowledge files and connect tools *only* on task-trigger; instantiate patterns to the agent's own context; record to `runtime/` and `project/`; never edit the two branches.

---

## The two upgrades this foundation adds

Beyond a conventional agent brain, Foundry bakes in two capabilities that are stated as **enforced laws**, not advice:

- **Compartmentalization** → `foundation/COMPARTMENTALIZATION.md`. Every distinct concern is broken to its smallest reusable unit; one orchestrator wires them; no unit reaches inside another. Result: fix one broken part in isolation, and lift one part into another agent untouched.
- **The Mistake Engine** → `foundation/MISTAKE_ENGINE.md`. A mistake is never recorded as a one-off. It is climbed to its *invariant* and wired to a *guardrail at the owning unit*, so the same class of error cannot recur on a new instance. The two upgrades are one idea from two directions: **isolate each concern, then bolt that concern's rule onto its unit.**

---

## Maturity

**`[Established — structural, verified 2026-06-01]`** for the integration contract — a fresh, context-less agent boot confirmed it (`MAINTENANCE.md` §6): `foundation/` loaded fully, only the `knowledge/INDEX.md` map read, no knowledge file pulled until a task triggered one, and both branches read as bias-free and authority-neutral. **Still `[Draft — structural]`:** the reuse-or-instantiate tool path (`knowledge/DECISION_RULE.md`, `tool-registry.md`) and a full STEP 0–6 instantiation (`knowledge/INSTANTIATION_GUIDE.md`) — these fire only when an agent actually builds a tool, which this boot deliberately did not. The `knowledge/` capability files carry their own per-file tags (`[Established]` concepts; `[Current as of June 2026 — re-verify quarterly]` tooling).
