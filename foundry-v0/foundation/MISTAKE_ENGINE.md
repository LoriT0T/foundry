# MISTAKE_ENGINE — how a mistake is made impossible to repeat

> **What this is.** The machinery that turns a single mistake into a permanent guarantee against its whole class. Most agents record a mistake at the level of the *instance* ("this one thing was wrong"), fix that instance, and then repeat the identical mistake the next time a slightly different instance appears. This engine prevents that by recording at the level of the **invariant** and wiring the fix to a **guardrail at the owning unit**, so the error cannot recur on any future instance.
>
> **Where it sits.** `~/Foundry/foundation/MISTAKE_ENGINE.md`. It is the engine behind Phase 6 (Improve) in `THINKING.md`, it depends on `COMPARTMENTALIZATION.md` (the guardrail needs a unit to live in), and it produces entries in the project layer's `FAULTS` and `LESSONS` files.
>
> **Status.** `[Established]` as a method. Bias-free: the worked example below uses a deliberately generic shape, not any real domain.

---

## The problem it solves (stated plainly)

> *"I tell the agent a value is wrong — say, a field saved in a malformed format. It fixes that value. But when a new value arrives, or the field is edited later, the same mistake happens again. It learned the instance, not the rule."*

That is the universal failure of instance-level memory. The fix is not "remember harder." It is to **climb from the instance to the invariant, then enforce the invariant where it cannot be bypassed.**

---

## 1. The abstraction ladder (climb before you record)

When a mistake happens, do **not** record what concretely went wrong. Climb three rungs:

```
INSTANCE   The one concrete thing that went wrong, this once.
   ↓ "what category of thing is this an example of?"
CLASS      The family of cases that share this failure.
   ↓ "what universal rule, if always true, would prevent the entire family?"
INVARIANT  The rule to enforce — the thing recorded.
```

**Worked example (generic):**
- **Instance:** a text field was saved in a malformed format (it slipped through because it was only checked the first time it was set).
- **Class:** any value written to that field can be malformed; "first-time-only" checking misses every later write.
- **Invariant:** *every write to a constrained field is validated against the field's format spec — on every write, not just the first.*

You record the **invariant**, with the instance kept only as an illustrating example. The next malformed value — different content, different moment — is the *same invariant violation*, and the guardrail catches it.

---

## 2. Lesson → guardrail wiring (a lesson is not done until it is enforced)

Writing the invariant down is necessary but **not sufficient** — a written rule an agent has to *remember* is exactly what failed last time. The invariant is only safe once it is wired to a **guardrail**: a validator or test that runs automatically at the point the class of mistake would occur, and **blocks or rewrites**, not merely logs.

- The guardrail lives in the **owning unit** — the smallest module responsible for that concern (`COMPARTMENTALIZATION.md`). The field's format rule lives in the field's unit; that unit validates on every write. Fix it once there → enforced for every future value, forever.
- The guardrail runs at a definite point in the loop — usually the Execute boundary (reject bad input/output as it crosses) or the Test phase (`RELIABILITY.md`).
- The lesson entry **links to** the guardrail; the guardrail **cites** the lesson. Neither is orphaned.

> **The rule:** a mistake's entry stays **OPEN** until its guardrail is built and live. Recording the lesson is not the fix. Wiring the guardrail is the fix.

---

## 3. Stable IDs + dedup (so the record never rots)

Instance-level logging tends to rot in two ways, both of which this engine forbids:

- **Colliding IDs** — the same identifier reused for many different mistakes, so nothing can be referenced. **Forbidden.** Every entry gets a **stable, monotonically increasing ID** (`M-001`, `M-002`, …) that is **never reused**.
- **Blind appends** — the same mistake re-filed again and again as near-identical new entries. **Forbidden.** Before filing anything, **search existing entries by invariant**. If the invariant is already tracked, do **not** append a twin — increment that entry's **recurrence counter** and update its date.

This is what stops a fault log from filling with seventeen copies of one unresolved problem.

---

## 4. The recurrence trigger (recurrence is a build signal, not noise)

The recurrence counter is not bookkeeping — it is an alarm:

- **Recurrence on an `OPEN` entry** (guardrail not yet built) → the lesson alone is failing. **Escalate: build the guardrail now.** Stop re-logging.
- **Recurrence on an `ENFORCED` entry** (guardrail exists) → the guardrail is wrong, too narrow, or bypassable. **Fix the guardrail**, and widen the invariant if the new case revealed a bigger class.

Either way, a second occurrence triggers *engineering*, never another log line.

---

## 5. The record format

Each mistake is one entry (in the project layer's `FAULTS`/`LESSONS` file, per their templates):

```
ID:          M-007                         (stable, monotonic, never reused)
First seen:  <date>   ·   Recurrences: 0   ·   Status: OPEN | ENFORCED
INSTANCE:    <the one concrete thing that went wrong>
CLASS:       <the family of cases it belongs to>
INVARIANT:   <the universal rule to enforce>
OWNING UNIT: <the smallest module that should enforce it>     (COMPARTMENTALIZATION)
GUARDRAIL:   <the validator/test + where it runs>             (empty while OPEN)
```

In the **project layer** this ID is realized as `F-NNN` in `project/FAULTS.md` (mistakes tracked until guarded) and `L-NNN` in `project/LESSONS.md` (the durable rules they graduate into) — the same discipline, one ID namespace per file. `Status: OPEN` means recorded-but-not-yet-enforced. `Status: ENFORCED` means the guardrail is live — only then is the mistake truly closed against recurrence.

---

## 6. The procedure (run in Phase 6, on every mistake)

1. **Capture the instance** — what concretely went wrong.
2. **Climb the ladder** — instance → class → invariant (§1).
3. **Dedup** — search existing entries by invariant. Match? Increment recurrence, go to §4. No match? Assign the next `M-ID`.
4. **Name the owning unit** — the smallest module that should enforce the invariant (`COMPARTMENTALIZATION.md`).
5. **Wire the guardrail** — build the validator/test in that unit; set it to block or rewrite at the right loop boundary. Flip status to `ENFORCED`.
6. **Cross-link** — lesson ↔ guardrail. Update the project layer in the same turn (`SELF_IMPROVEMENT.md` sync pass).

If the guardrail cannot be built this turn, the entry stays `OPEN` and is surfaced explicitly as outstanding — never silently left as "logged."

---

## 7. Failure modes + the guard that catches each

| Failure | Cause | Guard |
|---|---|---|
| Same mistake recurs on a new instance | recorded the instance, not the invariant | climb the abstraction ladder (§1) |
| A written lesson is forgotten under pressure | enforcement left to memory | wire a guardrail at the owning unit (§2) |
| Fault log fills with duplicates | blind append, colliding IDs | stable IDs + dedup-by-invariant (§3) |
| A "fixed" mistake comes back | guardrail too narrow / bypassable | recurrence trigger → fix/ widen the guardrail (§4) |
| Lesson and fix drift apart | no link between them | lesson ↔ guardrail cross-reference (§5–6) |

> **For working memory:** Climb to the invariant. Wire a guardrail at the owning unit. Stable IDs, dedup by invariant, count recurrences. Recurrence means build, not log. OPEN until enforced.
