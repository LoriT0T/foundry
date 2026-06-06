# SKILL — Context Engineering

> **Status:** concept `[Established]` · tooling `[Current as of June 2026 — re-verify quarterly]` · **illustration: prose only — the standard and pattern are documented; no runnable code yet.** This is reference material to build *from*; it does not outrank your judgment, and you decide whether your context needs this capability at all.
> **Trigger:** load when a task assembles a model call's context — deciding what to include vs. retrieve, budgeting the window, versioning prompts, compacting history, or caching prefixes.
> **Phase:** Plan (decide what context the task needs, and whether to retrieve), Execute (assemble and cache the call).

## 1. Stable concept `[Established]`
The context window is **finite and not free**: every token adds latency and cost, and model quality *degrades as the window fills* — attention dilutes, and facts placed mid-window are missed ("lost in the middle"). So context is a **budget to manage, not a bucket to fill**: relevance beats volume, and more context often makes answers worse, not better. Five stable sub-concerns:

- **Window budgeting** — allocate the window across named line-items: system/instructions, tool definitions, retrieved context, conversation history, and *reserved output headroom*. Track usage against the budget; never let input crowd out the room the answer needs.
- **Long-context vs. retrieval (when NOT to use RAG — and when to).** A large window tempts "just stuff it all in," but cost and latency scale with tokens, quality degrades with fill, and nothing scales past the window. Decide by **fit, freshness, frequency**: content that is *small, stable, and used every call* belongs in the prompt (and cached); content that is *large, changing, or only selectively relevant* should be retrieved (the retrieval/RAG file). They are complements, not rivals — long-context for reasoning over a whole document you already hold; retrieval for selecting from a corpus too big or too dynamic to inline.
- **Prompt templating + versioning** — prompts are code. Externalize them as templates with typed variables, versioned and diffable, so a change is revertible and can be tied to an eval run (the evaluation file). Scattered inline strings are unversioned and untestable.
- **Compaction / summarization** — in long or multi-turn runs, history outgrows the budget. Compact it: summarize older turns, keep recent turns verbatim, and persist durable facts to external memory (the memory-systems file). Compaction is lossy — protect the load-bearing facts from being summarized away.
- **Prompt caching** — providers cache a stable prompt *prefix*; a cache hit cuts cost and latency sharply. So order context **stable → volatile** (fixed system prompt + tool defs + reusable reference first; per-task context and user input last) to maximize the cacheable, byte-stable prefix.

## 2. Current tooling `[Current as of June 2026 — re-verify]`
- **Token counting / budgeting:** model tokenizers and counters (e.g. `tiktoken`, plus model-specific counters). *(Verify the current counter per model.)*
- **Prompt templating / versioning:** template tooling in the major agent frameworks, plus prompt-registry features bundled into eval/observability backends (e.g. Langfuse, Braintrust carry versioned prompts). *(Verify current options.)*
- **Prompt caching:** provider-native — Anthropic prompt caching, OpenAI prompt caching, Google context caching; TTLs are short and minimum cacheable sizes vary. *(Verify current TTLs, minimum sizes, and pricing.)*
- **Compaction:** usually app-level (summarize-and-replace); some frameworks ship summary-memory helpers. *(Verify.)*
- **Long-context models:** windows range from ~100K up to ~1M+ tokens depending on model — but "fits" is not "free" or "accurate." *(Verify current window sizes.)*

> Volatile note: window sizes, cache TTLs, counters, and model names move; the §1 concept does not. When re-verifying, change names/limits here; leave the concept untouched.

## 3. Key pattern
A call assembles its context from named, budgeted parts in **stable → volatile** order: fixed system prompt + tool defs + reusable reference context first (mark it cacheable), then per-task retrieved/dynamic context, then the user input last. Count tokens against the budget *before* sending; if over, retrieve less, compact history, or drop low-relevance items — never eat the reserved output headroom and never silently truncate. Choose in-prompt vs. retrieve by fit/freshness/frequency (§1). Source prompts from versioned templates, not inline strings, and pin the version used in each run so a regression is traceable. This is the engineered form of the foundation's *"rehydrate only what the task needs"* and *"one home per fact"* — applied to the model's working context.

## 4. Failure modes it guards
| Failure | Guard |
|---|---|
| Key fact ignored mid-window ("lost in the middle") | budget + curate for relevance; put critical content at the window edges; retrieve the slice instead of inlining the whole |
| Runaway cost/latency from oversized context | per-call token budget; prefer retrieval over long-context for large/dynamic corpora |
| Used the big window where retrieval was right | the long-context-vs-RAG decision: fit / freshness / frequency |
| Cache never hits, cost stays high | order context stable→volatile; keep the prefix byte-stable so it caches |
| Multi-turn run overflows the window | compaction/summarization + durable facts pushed to external memory |
| A prompt edit silently regresses quality | versioned templates tied to eval runs (the evaluation file) |

## 5. Registry note
Context engineering is in-agent, build-time discipline plus per-call assembly logic — not a connectable tool, so no registry entry. It governs how *every* model call is constructed, and pairs tightly with three other files: cost-routing (caching + token budgets), memory-systems (what to persist vs. carry in-window), and retrieval/RAG (the in-prompt-vs-retrieve decision).
