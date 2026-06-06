# ORCHESTRATION — do it, delegate it, or schedule it

> **What this is.** How an agent decides whether to do a piece of work itself, hand it to a sub-agent, or put it on a schedule — and how it splits *deciding* from *doing* so the operation runs like a business, not a single overloaded mind.
>
> **Where it sits.** `~/Foundry/foundation/ORCHESTRATION.md`. It serves the Plan phase of `THINKING.md`. Its *engineered* form — durable workflows that checkpoint, retry, resume, and pause for human approval — is `knowledge/orchestration/SKILL.md`; the way agents expose capabilities to each other is `knowledge/mcp-tools/SKILL.md`.
>
> **Status.** `[Established]`. Bias-free.

---

## Two roles: strategist and operators

Split the system the way a well-run business splits deciding from doing:

- **The strategist** (runs periodically): ingests reality, decides what to do next, writes a concrete plan, and **grows the system's capability**. It thinks; it does not execute.
- **The operators** (run on their cadence): take the plan and **execute it reliably**, again and again, making no strategic decisions of their own. If the plan is missing, they fall back to a safe default.

The handoff between them is a **durable file** (a plan/queue the strategist writes and the operators read). Clean, debuggable, survives restarts. The strategist decides, the operators do, results feed back, the strategist gets smarter — that loop is the whole machine.

---

## Self vs delegate vs schedule

**Do it yourself** when: the task needs this conversation's context · it's small and single-domain · the principal is actively iterating with you.

**Delegate** (spawn a sub-agent) when: it's a reasoning-heavy subtask you'd rather not flood your context with · independent workstreams can run in parallel · large intermediate outputs would bloat your context (scraping, file processing, broad search).

**Schedule** when: exact timing matters · the task needs isolation · it's a one-shot reminder or a recurring periodic check better run standalone. Anything that would otherwise nag for permission every run belongs here, approved once at creation (`RED_LINES.md`: autonomy means it runs without being asked).

---

## The delegation contract (every sub-agent gets all five)

A sub-agent has **zero memory of your conversation.** Delegation without a contract is throwing work over a wall. Every spawn includes:

1. **Exact deliverable** — what comes back, in what form.
2. **Success criteria** — specific and verifiable.
3. **Context** — file paths, constraints, prior decisions, error messages. Everything it needs and cannot infer.
4. **Allowed tools** — least privilege; only what the task requires.
5. **Failure surface** — what to do if blocked: surface the blocker, or retry — say which.

Then **review the result against the criteria** before accepting it. Fail → one targeted revision → escalate or re-plan. Never ship a sub-agent's output without your own Test phase.

---

## The two-file sub-agent bootstrap

A persistent sub-agent needs the minimum to be itself and to operate — two files:

- **A minimal identity** — who this sub-agent is and the one job it owns (a tight instance of `identity/SOUL.template.md`).
- **An operating contract** — its inputs, outputs, the standard it's held to, and how it reports back.

Register it where the runtime tracks agents, with its id, its model, and its thinking level. It inherits the same `foundation/` discipline as its parent — the loop, the red lines, the mistake engine. Sub-agents are smaller, not sloppier.

---

## Parallelize, then converge
Independent subproblems run concurrently; dependent ones wait. Fan out the independent work, hold a barrier only where a step genuinely needs all prior results together, then converge and verify. Parallelism is for *independent* work — forcing a barrier where none is needed wastes the slack.

> **From discipline to durability.** This file is the universal judgment of who-does-what. When a workflow must survive crashes, retry flaky steps without double effect, or pause for hours awaiting a human, that is the *durable-execution* concern — load `knowledge/orchestration/SKILL.md`. Coordination here; durability guarantees there.

> **For working memory:** Strategist decides, operators do, a file is the handoff. Self / delegate / schedule — decide explicitly. Every delegation: deliverable + criteria + context + tools + failure surface, then review.
