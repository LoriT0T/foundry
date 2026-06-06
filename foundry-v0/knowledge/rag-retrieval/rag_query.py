"""
rag_query.py — REFERENCE IMPLEMENTATION (the pattern, not a frozen product)

What this does:
  Phase 2 of RAG — RETRIEVAL. Embeds a question, finds the nearest stored
  chunks by meaning, and returns them. The LLM generation step is shown but
  kept minimal — in a real agent the retrieved context is handed to whatever
  model the agent already uses.

This is the function you wrap as an MCP tool (see mcp_server.py + SKILL.md).

Stable vs volatile:
  STABLE  — embed question -> nearest-neighbour search -> return chunks.
  VOLATILE— the embedding model, the reranker choice, the client library.
"""

import os
import psycopg
from openai import OpenAI

DB_DSN      = os.environ.get("RAG_DB_DSN", "postgresql://localhost/rag")
EMBED_MODEL = os.environ.get("RAG_EMBED_MODEL", "text-embedding-3-small")  # VOLATILE
TOP_K       = int(os.environ.get("RAG_TOP_K", "5"))

client = OpenAI()


def embed(text: str) -> list[float]:
    resp = client.embeddings.create(model=EMBED_MODEL, input=text)
    return resp.data[0].embedding


def retrieve(question: str, k: int = TOP_K) -> list[dict]:
    """The core retrieval step. Returns the k nearest chunks by cosine distance.
    NOTE: this is dense-only retrieval. SKILL.md explains why production adds
    hybrid (keyword + dense) search and a reranker on top, which matter most
    where dense-only recall is weak for your content's language or domain."""
    q_vec = embed(question)
    with psycopg.connect(DB_DSN) as conn:
        from pgvector.psycopg import register_vector
        register_vector(conn)
        rows = conn.execute(
            """
            SELECT source, content, 1 - (embedding <=> %s) AS similarity
            FROM chunks
            ORDER BY embedding <=> %s
            LIMIT %s
            """,
            (q_vec, q_vec, k),
        ).fetchall()
    return [{"source": s, "content": c, "similarity": sim} for (s, c, sim) in rows]


def answer(question: str) -> str:
    """Optional generation step — retrieval + a grounded answer. In an agent,
    you'd usually return the chunks and let the agent's own model generate."""
    chunks = retrieve(question)
    context = "\n\n---\n\n".join(c["content"] for c in chunks)
    resp = client.chat.completions.create(
        model=os.environ.get("RAG_GEN_MODEL", "gpt-4o-mini"),  # VOLATILE
        messages=[
            {"role": "system",
             "content": "Answer using ONLY the provided context. If the context "
                        "doesn't contain the answer, say so plainly."},
            {"role": "user",
             "content": f"Context:\n{context}\n\nQuestion: {question}"},
        ],
    )
    return resp.choices[0].message.content


if __name__ == "__main__":
    import sys
    q = " ".join(sys.argv[1:]) or "test question"
    for i, ch in enumerate(retrieve(q), 1):
        print(f"[{i}] ({ch['similarity']:.3f}) {ch['source']}")
        print(ch["content"][:200], "...\n")
