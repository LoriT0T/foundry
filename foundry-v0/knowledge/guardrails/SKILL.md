# SKILL — Guardrails

> **Status:** concept `[Established]` · tooling `[Current as of June 2026 — re-verify quarterly]` · **illustration: prose only — the standard and pattern are documented; no runnable code yet.** This is reference material to build *from*; it does not outrank your judgment. Because guardrails are safety-critical, treat anything you build from this as needing real testing before production reliance.
> **Trigger:** load when a task touches untrusted input, handles sensitive/PII data, exposes tools, or deploys outside localhost.
> **Phase:** Execute (rails run before and after the main model and around tool calls).

## 1. Stable concept `[Established]`
Guardrails are lightweight checks that run *around* the main model — before input reaches it, after output leaves it, and on both sides of any tool call. They are an enforcement layer, not a prompt instruction: the model's own training is not a policy boundary, so a separate layer blocks, redacts, or rewrites traffic. The reference threat list is the **OWASP Top 10 for LLM Applications**; the three that dominate production are **prompt injection** (direct, and indirect via retrieved/processed content), **sensitive-information disclosure** (PII/secret leakage), and **excessive agency** (a tool call doing more than intended).

The architecture is *defense in depth* — no single rail covers everything:
- **Input rail** — detect jailbreak/injection, redact PII before the model sees it.
- **Retrieval rail** — filter retrieved chunks before they enter the prompt. Required for RAG over any non-authored text, because RAG alone does not stop indirect injection.
- **Execution rail** — validate a tool call's name and parameters before it runs, and inspect the result before it re-enters context.
- **Output rail** — block leakage/off-policy content; sanitize before output is passed to SQL/HTML/shell.

## 2. Current tooling `[Current as of June 2026 — re-verify]`
- **Orchestration:** NVIDIA **NeMo Guardrails** (models full dialog, multi-turn). *Caveat: NVIDIA flags it as not production-ready as-is — additional hardening required.*
- **Fast injection gate:** **Llama Prompt Guard** (first-pass, ~20–50ms).
- **Hazard classification:** **Llama Guard** / ShieldGemma.
- **PII:** Microsoft **Presidio** (redaction, can run in a sidecar / OTel collector).
- **Alternatives:** **LLM Guard** (middleware scanners), **Guardrails AI** (structured-output validation). Most production stacks combine 2–3.

## 3. Key pattern (what an implementation does)
A request passes input rail → (retrieval rail if RAG) → model → execution rail around any tool → output rail. Each rail is a small classifier or rule set; failures block or rewrite, not just log. Strictness is tuned to the project's risk tolerance — that tuning is project-specific (see INSTANTIATION_GUIDE), the *existence* of the rails is universal.

## 4. Failure modes it guards
| Failure | Guard |
|---|---|
| Direct prompt injection | Input rail + jailbreak classifier |
| Indirect injection via documents | Retrieval rail on RAG chunks |
| PII / secret leakage | Presidio redaction on input and output |
| Tool call exceeds intent | Execution rail: validate params pre-run, inspect result post-run |
| Output injected into SQL/HTML/shell downstream | Output sanitization |

## 5. Registry note
Guardrails are usually *library code inside the agent*, not always a standalone MCP tool — but a shared classifier (e.g. a hosted injection detector) can be registered as a tool keyed to its function. Default: build as in-agent rails per the pattern.
