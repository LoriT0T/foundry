# SKILL — Memory Systems

> **Status:** concept `[Established]` · tooling `[Current as of June 2026 — re-verify quarterly]` · **illustration: prose only — the standard and pattern are documented; no runnable code yet.** This is reference material to build *from*; it does not outrank your judgment, and you decide whether your context needs this capability at all.
> **Trigger:** load when a task needs durable agent memory beyond the foundation's markdown brain, at scale.
> **Phase:** Plan.

## 1. Stable concept `[Established]`
Sessions end and the model forgets, so durable state must live outside the context window. The engineered version distinguishes memory *types*:
- **Short-term / working** — the current context.
- **Long-term**, split into **semantic** (stable facts), **episodic** (what happened, when), **procedural** (how-to / reusable procedures), and **preferences**.
Mature systems add **confidence scoring** and **decay** so memories age and update rather than accumulating as noise, and **rerank** retrieved memories before they hit the context window. A production footgun the field has settled: **async memory writes by default**, because blocking writes add latency the user feels.

## 2. Current tooling `[Current as of June 2026 — re-verify]`
**Mem0** (LLM-driven classification; offers an OpenMemory **MCP** path), **Zep** (context-engineering / RAG-oriented), **LangMem**. These are memory libraries you integrate; some are MCP-native so any client connects without code changes.

## 3. Key pattern
This is the engineered form of the foundation's own MEMORY / LESSONS / daily-log split — the foundation independently arrived at typed memory (narrative vs. rules vs. facts). At scale, back each type with a store, write async, rerank on retrieval, and decay stale entries. The foundation's "one home per fact" rule still governs *which* store owns *what*.

## 4. Failure modes it guards
| Failure | Guard |
|---|---|
| Agent forgets across sessions | External, typed durable stores |
| Memory writes add felt latency | Async writes by default |
| Stale facts pollute reasoning | Confidence scoring + decay |
| Right memory retrieved, wrong order | Rerank before context injection |

## 5. Registry note
A shared memory service can be exposed via MCP and registered as a tool keyed to its data; an in-agent memory library is build-time. Choose per scale.
