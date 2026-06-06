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
- **For high-stakes work, verify a second, independent way.**

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

> **For working memory:** Deterministic critical path, model for judgment, fallback always. No "done" without evidence — look at the artifact. Idempotent + atomic + isolated. Degrade, never die. Pulse every run.
