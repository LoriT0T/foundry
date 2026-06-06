# SKILL — Orchestration

> **Status:** concept `[Established]` · tooling `[Current as of June 2026 — re-verify quarterly]` · **illustration: prose only — the standard and pattern are documented; no runnable code yet.** This is reference material to build *from*; it does not outrank your judgment, and you decide whether your context needs this capability at all.
> **Trigger:** load when a task runs a multi-step or long-running workflow needing retries, resume, branching, or human approval.
> **Phase:** Plan, Execute.

## 1. Stable concept `[Established]`
An agent framework gives you the scaffolding for the agent loop — tool-calling, multi-step reasoning, state, multi-agent coordination — so you don't hand-build it. **Durable execution** is the deeper need: a workflow that persists its state after each step so it can *resume* from the last completed step after a crash, **retry** failures with backoff, stay **idempotent** (a step running twice does no double damage), and **pause** for hours/days awaiting a human, then continue. Framework choice is not cosmetic — the same model can swing materially on identical tasks depending on the orchestration scaffold.

## 2. Current tooling `[Current as of June 2026 — re-verify]`
- **LangGraph** — production standard for stateful, auditable workflows; graph of nodes with checkpointing and time-travel; best where audit trails and human-approval steps matter (regulated environments). Most control, most boilerplate.
- **CrewAI** — fastest path to a working multi-agent prototype (role-based).
- **OpenAI Agents SDK** — clean handoff model, OpenAI-centric.
- **Claude Agent SDK** — Anthropic-native.
- **Google ADK** — hierarchical agent tree.
- **Durable execution engine:** **Temporal** (the heavy-duty option for resume/retry/idempotency at scale).

## 3. Key pattern
Model the workflow as explicit steps with dependencies (this maps cleanly to the foundation's own dependency-graph thinking). Make independent steps parallel, long/risky steps checkpointed, and human approvals explicit interrupts. The foundation's cron+state+git is the hand-rolled version of what LangGraph checkpointing / Temporal *guarantee*.

## 4. Failure modes it guards
| Failure | Guard |
|---|---|
| Crash restarts whole workflow | Checkpointed/durable state, resume from last step |
| Flaky tool kills the run | Automatic retry with backoff |
| Step runs twice, double effect | Idempotency keys |
| No human gate on risky action | Explicit human-in-the-loop interrupt |

## 5. Registry note
The framework is a build-time dependency, not a connectable tool — no registry entry. Sub-agents it spawns follow the foundation's orchestration discipline.
