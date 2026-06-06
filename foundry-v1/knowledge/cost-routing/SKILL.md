# SKILL — Cost / Routing (LLM gateway)

> **Status:** concept `[Established]` · tooling `[Current as of June 2026 — re-verify quarterly]` · **illustration: prose only — the standard and pattern are documented; no runnable code yet.** This is reference material to build *from*; it does not outrank your judgment, and you decide whether your context needs this capability at all.
> **Trigger:** load when a system makes enough model calls that cost, model choice, or provider reliability matter.
> **Phase:** Execute (it sits in front of every model call).
> **Note:** added to the map because production systems treat cost control and model routing as essential, not optional.

## 1. Stable concept `[Established]`
An **LLM gateway** is a proxy in front of all model calls that centralizes four concerns:
- **Routing** — send easy tasks to a cheap model, hard tasks to a strong one.
- **Fallback** — if a provider is down or rate-limited, retry on another automatically.
- **Caching** — reuse responses for repeated prompts (prompt caching).
- **Cost attribution** — track tokens and spend per task / per tenant, and enforce token budgets.
Without it, model choice is scattered across the code, cost is invisible until the bill arrives, and one provider outage takes the system down.

## 2. Current tooling `[Current as of June 2026 — re-verify]`
**LiteLLM**, **Portkey** (gateways with routing, fallback, caching, cost tracking). Some observability backends also surface per-call cost from OTel spans — pair the gateway with the observability layer for end-to-end cost visibility.

## 3. Key pattern
Route all model calls through one gateway. Define a routing policy (cheap-by-default, escalate on difficulty). Set per-tenant/per-task token budgets. Enable fallback across providers. Emit cost per call to the observability backend. This is what turns "we use an LLM" into "we run LLM calls at a known, controlled cost with no single point of failure."

## 4. Failure modes it guards
| Failure | Guard |
|---|---|
| Runaway / invisible cost | Per-task cost attribution + token budgets |
| Strong model used for trivial tasks | Difficulty-based routing |
| Provider outage takes system down | Automatic cross-provider fallback |
| Repeated identical calls billed twice | Prompt caching |

## 5. Registry note
The gateway is infrastructure in front of model calls, not an agent-facing tool — no registry entry. Routing policy and budgets are project-specific tuning per INSTANTIATION_GUIDE.
