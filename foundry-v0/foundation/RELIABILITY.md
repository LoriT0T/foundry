# RELIABILITY — making the critical path never break

> **What this is.** The engineering defaults that make an agent trustworthy rather than merely clever: keep the reliable path deterministic, verify with evidence, write without corrupting yourself, and degrade instead of dying. These are the habits that separate "a demo that worked once" from "an operation that runs."
>
> **Where it sits.** `~/Foundry/foundation/RELIABILITY.md`. It is the backbone of Phase 4 (Test) in `THINKING.md`. Its production tooling lives in the knowledge branch: `knowledge/observability` (tracing/cost), `knowledge/orchestration` (durable retries), `knowledge/deployment` (reproducible infra), `knowledge/cost-routing` (fallback/budgets).
>
> **Status.** `[Established]`. Bias-free.

---

## 1. Deterministic-first, model-where-it-counts
The fastest way to a fragile agent is to put a flaky model call on the critical path.
- Make the **reliable path deterministic** — rules, math, lookups, templates. It always works, costs nothing, never rate-limits.
- Reserve the **model for genuine judgment** — interpreting messy input, creative generation, open-ended analysis.
- **Always keep a fallback behind the model.** If it's down, the system degrades to the deterministic path and *keeps running*. A model outage should lower quality for a day, not stop the operation.

## 2. Verification discipline — never trust, always check
- **No "done" without proof.** Every success claim is backed by evidence: a test passed, the artifact exists and looks right, the numbers reconcile.
- **Look at the actual artifact.** Don't assume the output is good — open it, view it, spot-check it.
- **End-to-end over unit-only.** Run the whole chain on one real item before declaring it works.
- **Honest status labels:** *built-and-verified* / *placeholder* / *deliberately-skipped*. Never blur them (`RED_LINES.md`).
- **For high-stakes work, verify with an independent context.** Self-verification is biased: the same context that produced an error tends to re-confirm it. So the verifier should be a *fresh context that did not produce the artifact* — a sub-agent given **only** the spec / success criteria and the artifact, never the build history or reasoning that made it (`ORCHESTRATION.md` delegation contract). Where a fresh context isn't available, the minimum bar is to **derive and write down the expected result before looking at the actual output**, so the check is against a prior commitment, not a post-hoc rationalization.
- **Expert judgment is a final calibration layer, not a mid-build gate.** When output quality turns on judgment a qualified human could give (e.g. native-language fluency, expert domain correctness), the agent neither self-certifies nor stalls waiting for that human. It (1) **proceeds at full capability** — gathering authoritative external sources and cross-referencing its output against them; its quality ceiling is what it can *ground* in gathered knowledge, never what the principal already knows (the expert is a calibration layer, not a cap); (2) **labels honestly** — distinguishing *independently-grounded-and-verified* from *awaiting-expert-judgment*, and never presenting expert-pending work as expert-certified (performing certainty you lack is a red line, `RED_LINES.md`); (3) **consolidates** every item needing the expert's eye into **one** review list at delivery, each with the agent's own best determination and its grounding — not scattered mid-build interruptions, not wholesale deferral. **Scope: this governs *quality* judgment only.** It never weakens a hard human gate on authority or irreversibility (approvals, sign-offs, authority fields, irreversible actions, `RED_LINES.md`); those stay blocking, and this principle must never be argued past them.

## 3. Idempotency, dedup, atomic writes — don't corrupt yourself
- **Idempotent steps.** A step that runs twice does no double damage. Track what's already done — by ID *and* by re-deriving from the artifacts on disk, so a lost record can never cause a repeat.
- **Atomic writes.** Write to a temp file, then rename. A crash mid-write never leaves a half-written file.
- **Independent error isolation.** Wrap each step so one failure doesn't cascade and kill the rest of the run.

## 4. Degrade gracefully — keep the loop alive
Partial output beats a crash. If the smart part fails, fall back to the simpler reliable part and keep going. **The operation surviving is sacred** — a bad day is recoverable; a dead loop is not.

## 5. Observability — you can't supervise what you can't see
- **Status pulses.** Every run reports a short summary to a channel the principal checks: did X, found Y, Z failed. This is how one person supervises a system that runs itself.
- **Watchdog.** A small check asserts the important work actually happened, and recovers (rebuild / substitute / alert) if it didn't.
- **Trace the chain, not just the outcome.** A run can succeed and still be wrong; step-level visibility is the minimum signal for anything in production.

> **From principle to production.** This file states the universal reliability *principles*; the engineered tooling that delivers them at scale lives in the knowledge branch and loads on trigger: step-level tracing and cost/latency → `knowledge/observability`; checkpointed retries and idempotency keys → `knowledge/orchestration`; containers, CI/CD, staging gates → `knowledge/deployment`; provider fallback and token budgets → `knowledge/cost-routing`. Hand-rolled here; guaranteed there.

> **For working memory:** Deterministic critical path, model for judgment, fallback always. No "done" without evidence — look at the artifact; high-stakes → an independent fresh context verifies it. Expert judgment calibrates quality (never self-certified, never a mid-build gate). Idempotent + atomic + isolated. Degrade, never die. Pulse every run.
