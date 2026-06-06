# COMPARTMENTALIZATION — the build law

> **What this is.** The rule for how an agent structures everything it builds: break each distinct concern down to its smallest reusable unit, give each unit sole ownership of that concern, and wire the units together with one orchestrator that owns no concern of its own. Stated as a **law**, not a preference — it is enforced in the Test phase, not left to taste.
>
> **Where it sits.** `~/Foundry/foundation/COMPARTMENTALIZATION.md`. It governs the Execute phase of `THINKING.md`, and it is the structural half of `MISTAKE_ENGINE.md` — a unit is where a concern's guardrail lives.
>
> **Status.** `[Established]` as a principle; the size/coupling thresholds are defaults to tune per context. Bias-free: it names no concern, language, or domain — only the shape.

---

## 1. The law

**One concern, one unit. One orchestrator wires them. No unit reaches inside another.**

A "concern" is a single responsibility — one transformation, one job, nameable in a few words without the word "and." If you need "and" to describe what a unit does, it is two units.

- **Each concern gets its own unit** (its own file/module), small enough to hold in your head at once.
- **One orchestrator** imports every unit and composes them into the whole. It contains *wiring only* — sequencing, passing outputs to inputs, handling the seams. It owns **no** concern logic itself.
- **Units never import each other.** All composition flows through the orchestrator. A unit knows its own inputs and outputs and nothing about its siblings.

---

## 2. The shape

```
<system>/
├── components/
│   ├── <concern_a>.py        ← does exactly one thing; owns its rules + data contract
│   ├── <concern_a>_test.py   ← proves <concern_a> alone, with no other component present
│   ├── <concern_b>.py
│   ├── <concern_b>_test.py
│   └── ...
└── orchestrator.py           ← imports every component; wires them; contains NO concern logic
```

The same shape applies in any language; the names change, the structure does not.

---

## 3. The rules (each is checkable)

1. **One concern per unit.** Two nameable responsibilities → two units.
2. **No horizontal imports.** A component importing another component is a violation. Composition is the orchestrator's job, never a component's.
3. **A narrow interface.** Each unit exposes one clear entry point and hides its internals. Callers depend on the interface, never the insides.
4. **Its own test.** Each unit ships with a test that runs in isolation — without the orchestrator and without its siblings. A unit you cannot test alone is not isolated.
5. **It owns its concern's rules.** Every validation, format rule, and acceptance/rejection check for a concern lives *in that concern's unit* — not scattered across call sites. (This is the hook `MISTAKE_ENGINE.md` wires guardrails onto.)
6. **The orchestrator is wiring only.** If concern logic appears in the orchestrator, extract it into a unit. The orchestrator should read like a table of contents, not an implementation.

---

## 4. Lock the definition at the moment of creation

When a concern is first named, **stop and define it before using it:**
- what it takes in and what it produces (the data contract),
- what a valid output is (acceptance rules) and what must be rejected (rejection rules),
- where its inputs come from (source / method).

`name → define → use`. Never `name → infer → use`. A concern used before it is defined drifts, and every caller infers a slightly different version of it.

---

## 5. Enforcement (runs in the Test phase, not on trust)

Compartmentalization is a *law* because it is checked, every build, in Phase 4 of the loop. The audit flags:

- any unit over its responsibility/size budget (default: more than one nameable job, or past a line ceiling the agent sets per context);
- any **cross-component import** (rule 2);
- any **concern logic in the orchestrator** (rule 6);
- any unit **without an isolated test** (rule 4).

A flagged build is not "done." The agent either fixes the structure or records, explicitly, why an exception is justified — silent monoliths are not allowed. (Encode this as a small `audit_modularity` check the agent runs; it is part of verification, like syntax and tests.)

---

## 6. Why this is the law (the three payoffs)

- **Fix in isolation.** When one part breaks, you repair *that unit* — open it, fix it, run its test — without touching, or risking, the rest. Debugging collapses from "search the whole system" to "open the one unit."
- **Reuse across agents.** A unit with a narrow interface and its own passing test is *portable*: lift it into a different system untouched, because it depends on nothing around it. Capability you build once becomes capability every future agent can borrow.
- **A home for every rule.** Each unit is the single place its concern's rules are enforced. Fix a rule once, in the owning unit, and it holds for *every* input that unit will ever see — which is exactly what makes `MISTAKE_ENGINE.md` able to stop a mistake from ever recurring.

> **The unification.** Compartmentalization and the mistake engine are one idea from two directions: **isolate each concern into its own unit, then bolt that concern's rule onto that unit.** Isolation gives every guardrail a home; the guardrail makes the isolation correct.

---

## 7. Failure modes + the guard that catches each

| Failure | Cause | Guard |
|---|---|---|
| Two concerns tangled in one file | decomposition skipped | one-concern rule + responsibility/size audit (§5) |
| Fixing A silently breaks B | hidden coupling via cross-import | no-horizontal-import rule; wire only through the orchestrator |
| A part can't be reused elsewhere | it depends on its siblings | narrow interface + isolated test; a unit that passes alone is portable |
| The orchestrator became a monolith | concern logic leaked upward | orchestrator-is-wiring-only audit |
| A rule fix doesn't stick | the rule was scattered across call sites | the rule lives in the owning unit (§3.5, `MISTAKE_ENGINE.md`) |

> **For working memory:** One concern, one unit. Orchestrator wires, owns nothing. No unit reaches inside another. Each unit owns its rule and its test. Checked every build.
