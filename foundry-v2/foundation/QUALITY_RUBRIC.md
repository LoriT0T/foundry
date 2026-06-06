# QUALITY_RUBRIC — the scorer every foundation file and skill must pass

> **What this is.** The explicit standard that any durable document an agent writes — a `foundation`/`knowledge` file, a skill, a project doc — is judged against before it is called done. It turns "is this good?" from a guess into a score.
>
> **Where it sits.** `~/Foundry/foundation/QUALITY_RUBRIC.md`. It is the gate in Phase 4 (Test) and Phase 6 (Improve) of `THINKING.md`, and `skills/skill-forge/SKILL.md` enforces it as a hard gate on every skill.
>
> **Status.** `[Established]`. Bias-free: the criteria apply to any agent's writing in any domain.

---

## How to score

Ten criteria. Each scored **0–3**:

- **0 — absent.** The criterion is not met at all.
- **1 — weak.** Gestured at, but unreliable.
- **2 — solid.** Properly met; would pass review.
- **3 — exemplary.** A model other files should imitate.

**Total out of 30. Pass = ≥ 24/30 AND no single line < 2.** A file with one zero or one fails the gate even if the total is high — a broken criterion blocks, it does not average away.

---

## The ten criteria

1. **Specificity.** Concrete over vague. Exact paths, values, commands, thresholds — never "the relevant file" or "tune appropriately" where a real value belongs.
2. **Provenance.** Claims are traceable: a source, a method, or an uncertainty tier (`THINKING.md` Part 3). The reader can tell *how you know*.
3. **Self-description.** The file says, up top, *what it is, where it sits, and when to use it* (the front-matter box). A reader knows in ten seconds whether this is the file they need.
4. **One home per fact.** No duplication. Each fact lives in exactly one owning location; everything else links to it. Duplicated facts drift.
5. **Snapshot before rewrite.** Before a major rewrite of a core file, the prior version is snapshotted to `runtime/iterations/<file>.<date>`. History is never silently destroyed.
6. **Sync invariants named.** The file states *what else must change when it changes* — its dependents. A change that leaves the graph inconsistent is a half-sync, and half-syncs rot the system.
7. **Failure modes named.** The file names what breaks, and the guard or test that catches each (ideally as a table). Knowing the failure is half the fix.
8. **Triggers explicit.** *When to load or invoke this* is stated, not left implied. A capability nobody knows when to reach for is invisible.
9. **Action-oriented.** It points to something testable, buildable, or actionable — not description for its own sake. Every doc earns its place by changing what the agent does.
10. **Self-improving.** It carries a mechanism to get better over time: a maturity tag, a changelog, an audit hook, or a re-verify date. A file with no path to improvement is already decaying.

---

## Using it

- **On any new/edited durable file:** score all ten before declaring done. Below the bar → improve, don't ship.
- **In `skill-forge`:** the QUALITY-GATE operation runs this rubric on every new or edited skill and blocks failures.
- **When the rubric itself improves:** snapshot it, then re-score the files that depend on it; queue any that now fail.

> **For working memory:** Ten criteria, 0–3 each, ≥24/30 and no line below 2. A single broken criterion blocks. Score before you ship.
