# SKILL — Observability

> **Status:** concept `[Established]` · tooling `[Current as of June 2026 — re-verify quarterly]` · **illustration: prose only — the standard and pattern are documented; no runnable code yet.** This is reference material to build *from*; it does not outrank your judgment, and you decide whether your context needs this capability at all.
> **Trigger:** load when building or reviewing any agent that will run in production, or when cost/latency/quality must be visible.
> **Phase:** Test, Improve.

## 1. Stable concept `[Established]`
In one task an agent makes many model and tool calls. When it fails, costs too much, or runs slow, you must see *inside the chain*, not just the final outcome. **Instrumentation** wraps each step so it emits a **span** — one operation with its inputs, outputs, timing, token count, and cost. Spans nest into a **trace** — the full tree of one task's run. You ship spans to a backend that visualizes and queries them. Step-level tracing is the *minimum viable signal* for a production agent, because binary health checks miss semantically-wrong-but-successful runs.

## 2. Current tooling `[Current as of June 2026 — re-verify]`
- **Transport standard:** **OpenTelemetry GenAI semantic conventions** — the vendor-neutral default; instrument once, swap backends freely. *Caveat: as of spec v1.41 the `gen_ai.*` attributes are still marked "Development," so attribute names can change — treat them as not-yet-frozen.*
- **Backends, by deployment model:** self-hosted **Langfuse** / **Arize Phoenix** (data residency, cost control); managed **LangSmith** / **Braintrust** (speed, built-in evals); proxy **Helicone** (zero-code-change cost tracking).
- OTel + auto-instrumentation covers ~80%; add a vendor SDK only for its UI.

## 3. Key pattern
Instrument on OTel, point `OTEL_EXPORTER_OTLP_ENDPOINT` at a self-hosted backend for residency. Capture model spans (tokens, cost), tool spans, retrieval spans. This is the engineered version of the foundation's hand-written daily logs — automatic, structured, queryable.

## 4. Failure modes it guards
| Failure | Guard |
|---|---|
| Silent wrong-but-successful runs | Step-level traces, not pass/fail checks |
| Unexplained cost/latency spikes | Per-span token + latency capture |
| Vendor lock-in | OTel transport, swappable backend |
| PII in traces | Redaction (Presidio) in the collector before export |

## 5. Registry note
The backend is infrastructure, not an agent tool — no standard registry entry. The instrumentation is library code inside every production agent.
