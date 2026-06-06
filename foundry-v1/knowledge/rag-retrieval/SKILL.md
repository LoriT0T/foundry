# SKILL — Retrieval (RAG)

> **What this is.** A reference knowledge file for retrieval — the same authority level as every other file in this branch. It documents the correct standard for RAG and carries a *worked illustration in runnable code* so the pattern is concrete. It also happens to be the most complete illustration, so other files mirror its shape — but its completeness gives it **no extra authority**: like every reference here, you adapt it, instantiate it, or build your own as your context requires. It does not decide for you.
>
> **Where it sits.** `~/Foundry/knowledge/rag-retrieval/SKILL.md`, with three runnable illustration scripts beside it: `rag_index.py`, `rag_query.py`, `mcp_server.py`.
>
> **Status:** concept `[Established]` · tooling `[Current as of June 2026 — re-verify quarterly]` · **the code is a worked illustration of the pattern — learn from it and adapt it; it is NOT a blessed, deploy-ready solution, and its existence is not a reason to use RAG when your context calls for something else.**
>
> **Trigger (from INDEX.md):** load this when a task needs the agent to answer from documents it wasn't trained on — *and you have judged RAG the right approach for your context.*

---

## The shared shape (every knowledge file follows this)

1. **Stable concept** — the mechanism, safe to build behavior on; does not age.
2. **Current tooling** — specific tools + a re-verify date; the part that ages.
3. **Worked illustration** — runnable code showing the pattern concretely, *to learn from and adapt* — not a product to ship blind, and not a default you must use.
4. **How to instantiate** — turning the pattern into an instance for a specific data source, *if you've judged it the right approach.*
5. **Wire as a tool** — exposing it via MCP and registering it.
6. **Failure modes** — what breaks, and the guardrail/test that catches it.
7. **The registry entry it produces.**

---

## 1. Stable concept `[Established]`

An LLM can only use what's in its training data plus what fits in its context window. To answer from a large body of documents, you retrieve the relevant pieces at question-time and put them in the prompt. That's RAG, and it rests on **embeddings**: an embedding model turns text into a vector (a list of numbers) positioned so that *similar meaning sits close together* in vector space. Retrieval is then "find the stored vectors nearest to the question's vector."

Two phases:

- **Indexing (once, ahead of time):** split documents into **chunks**, embed each, store text + vector in a **vector database**.
- **Retrieval (every query):** embed the question, ask the DB for the nearest chunks (**semantic search**), hand those chunks to the LLM to generate a grounded answer.

Two production refinements, both stable as concepts:
- **Hybrid search** — run semantic + keyword search in parallel and merge, because exact terms sometimes matter.
- **Reranking** — retrieve ~20 fast, then a second model re-scores and keeps the best 5. Cheap quality lift; matters most where dense retrieval is weak.

This is the engineered version of the foundation's markdown `session_search`: same idea (find relevant past text), but searching by *meaning* at scale instead of by string match.

## 2. Current tooling `[Current as of June 2026 — re-verify quarterly]`

- **Vector DB:** `pgvector` (a Postgres extension) is the default under ~5M vectors — mature, production-used, no second database to run. Move to **Qdrant** only when volume/latency forces it. *(Verify: pgvector scale ceiling, current version.)*
- **Embedding model:** a general default such as `text-embedding-3-small` (OpenAI). **The model must match your content's language and domain — see §Match retrieval to your content.** *(Verify: current model names + dimensions.)*
- **Reranker:** Cohere Rerank or a self-hosted cross-encoder. *(Verify: current options.)*
- **Indexing algorithm:** HNSW (good speed/accuracy balance) is the standard in-DB index.

> Volatile note: model names, library versions, and the pgvector scale ceiling move. The §1 concept does not. When re-verifying, change tool names here; leave the concept untouched.

## 3. Worked illustration `[runnable — to learn from, not to ship blind]`

Three real scripts sit beside this file (syntax-verified):

- **`rag_index.py`** — Phase 1. Chunk → embed → store in pgvector. Run when docs change.
- **`rag_query.py`** — Phase 2. Embed question → nearest-neighbour search → return chunks (+ optional grounded answer).
- **`mcp_server.py`** — wraps `retrieve()` as an MCP tool an agent can connect to.

They run as-is on a sane default (local Postgres + pgvector, `OPENAI_API_KEY` set), so you can *see the pattern working* rather than read it in the abstract. They are an **illustration of the pattern** — correct and runnable, meant to be read, adapted, or replaced for your context — never a frozen production system and never a default you must adopt. The per-instance knobs (`DOCS_DIR`, `DB_DSN`, `EMBED_MODEL`, chunk size) are environment variables precisely so the same code can become many instances *when RAG is the right call*. Whether RAG is the right call is your judgment, not this file's.

## 4. How to instantiate (per `DECISION_RULE.md`)

```
1. Identify the data source.          e.g. "<the document set this task answers from>"
2. Check your project's registry.     Does a live instance already serve it?
      → yes: connect to it. STOP. (Do not rebuild.)
      → no:  continue.
3. Point the pattern at the data:
      RAG_DOCS_DIR   = path to that data source's documents
      RAG_DB_DSN     = a NEW database for this instance (one DB per data source)
      RAG_EMBED_MODEL= chosen to match your content's language/domain
4. Run rag_index.py once to build the index.
5. Wire as a tool (§5) and REGISTER it in your project's TOOL_REGISTRY.md, same change.
```

Same data → reuse. Different data → new instance of this same code. Always → register.

## 5. Wire as a tool + register

```bash
pip install fastmcp
claude mcp add --transport stdio rag-<dataset> -- python mcp_server.py
claude mcp list          # verify it connected
```

Then add the row to your project's `TOOL_REGISTRY.md` (row shape in §7; the schema lives in `knowledge/tool-registry.md`). The instance is now a tool any agent can connect to **when its task's data source matches** — and must NOT connect otherwise (context cost; see BOOTSTRAP loading rule).

## 6. Failure modes + the guard that catches each

| Failure | Cause | Guard (where it's enforced) |
|---|---|---|
| Retrieves irrelevant chunks | Chunks too big/small; dense-only recall weak | Tune chunk size; add hybrid + rerank. Verify with a small eval set (see evaluation knowledge file) in Phase 4. |
| Answers confidently from nothing | No "I don't know" fallback | Generation prompt instructs "say so if context lacks it" (already in `rag_query.py`). |
| Recall worse in one language/domain than another | Embedding model not suited to that content | Use an embedding model that fits your content's language/domain; measure with an eval set. |
| Prompt injection via a document | RAG over untrusted text is an indirect-injection vector | **Retrieval guardrail** before chunks enter the prompt (see guardrails knowledge file). Non-optional if the KB contains text you didn't author. |
| Dimension mismatch error | `EMBED_DIM` ≠ model output | Keep `EMBED_DIM` in lockstep with the model; reindex on model change. |

## Match retrieval to your content (the principle, domain-neutral)

Dense retrieval quality depends almost entirely on the embedding model, and **embedding models are not equally accurate across all languages and domains** — most are strongest on the language and content they were trained most heavily on. This is a general truth of RAG, independent of any specific language or subject:

- **Choose an embedding model suited to your content's language and domain**, not a generic default, when your content sits outside the model's strong zone.
- **Reranking matters more where dense recall is weaker** for your content — the rerank pass recovers quality the embedding step misses.
- **Build a small eval set** (question → expected passage) so you *measure* recall for your specific content rather than assume it. This ties RAG to the evaluation knowledge file.

Whatever the content — a particular language, a technical domain, a regulated corpus — the move is the same: match the model to the content, lean on reranking where recall is weak, and measure. The *specifics* of your content (which language, which domain) come from your project context at instantiation — they are never baked into this foundation file.

## 7. The registry entry this produces (written to your project's `TOOL_REGISTRY.md`, never to `knowledge/`)

```
| Tool name           | Data source            | Trigger                                  | Context cost | Scope    | Connect command                                                  | Pattern                | Status |
| rag-<dataset>       | <the specific KB>      | Task needs to answer from <that KB>      | ~1 def, small| project | claude mcp add --transport stdio rag-<dataset> -- python mcp_server.py | rag-retrieval/SKILL.md | live   |
```

---

### Checklist before this file is "done" for a given instance
- [ ] Data source identified and checked against the registry (no duplicate).
- [ ] Pattern pointed at the right docs + its own DB; index built.
- [ ] Embedding model chosen deliberately to fit the content's language/domain.
- [ ] Wrapped as MCP server, connected, verified with `claude mcp list`.
- [ ] Registered in the project's `TOOL_REGISTRY.md` in the same change.
- [ ] Retrieval guardrail in place if the KB holds any non-authored text.
- [ ] A small eval set exists so recall is measured, not assumed.
