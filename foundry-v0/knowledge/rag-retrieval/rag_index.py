"""
rag_index.py — REFERENCE IMPLEMENTATION (the pattern, not a frozen product)

What this does:
  Phase 1 of RAG — INDEXING. Reads documents from a folder, splits each into
  chunks, embeds each chunk, and stores text+vector in Postgres (pgvector).
  Run this once when documents change.

How to instantiate (per DECISION_RULE.md):
  This is the PATTERN. To create an instance for a specific data source:
    1. Point DOCS_DIR at that data source's documents.
    2. Point DB_DSN at that instance's own database (one DB per data source).
    3. Choose EMBED_MODEL to match your content's language and domain
       (see SKILL.md "Match retrieval to your content" — embedding models
       are not equally accurate across all languages/domains).
    4. Register the instance in tool-registry.md.

Stable vs volatile:
  STABLE  — the flow (chunk -> embed -> store), the schema, the two-phase split.
  VOLATILE— the embedding model name and the client library version.
            Re-verify against current docs (see SKILL.md "Current tooling" date).

Setup (sane default):
  pip install openai psycopg[binary] pgvector
  Postgres with the pgvector extension enabled:  CREATE EXTENSION vector;
  export OPENAI_API_KEY=...    (never hardcode — see RED_LINES in foundation/)
"""

import os
import glob
import psycopg
from openai import OpenAI

# --- Configuration (the per-instance knobs) --------------------------------
DOCS_DIR    = os.environ.get("RAG_DOCS_DIR", "./docs")
DB_DSN      = os.environ.get("RAG_DB_DSN", "postgresql://localhost/rag")
EMBED_MODEL = os.environ.get("RAG_EMBED_MODEL", "text-embedding-3-small")  # VOLATILE
EMBED_DIM   = 1536          # must match the model's output dimension
CHUNK_CHARS = 1200          # ~250-300 words; see SKILL.md "Chunking"
CHUNK_OVERLAP = 200         # carry context across chunk boundaries

client = OpenAI()


def chunk_text(text: str, size: int = CHUNK_CHARS, overlap: int = CHUNK_OVERLAP):
    """Naive character chunker with overlap. The PATTERN — see SKILL.md for
    why semantic/structural chunking beats this for real content."""
    chunks, start = [], 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start = end - overlap
    return [c.strip() for c in chunks if c.strip()]


def embed(text: str) -> list[float]:
    """One text in, one vector out. This is the whole 'embedding' step."""
    resp = client.embeddings.create(model=EMBED_MODEL, input=text)
    return resp.data[0].embedding


def ensure_schema(conn):
    conn.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS chunks (
            id        BIGSERIAL PRIMARY KEY,
            source    TEXT NOT NULL,
            content   TEXT NOT NULL,
            embedding VECTOR({EMBED_DIM})
        );
    """)
    # HNSW index for fast nearest-neighbour search (see SKILL.md "Indexing")
    conn.execute("""
        CREATE INDEX IF NOT EXISTS chunks_embedding_idx
        ON chunks USING hnsw (embedding vector_cosine_ops);
    """)


def index_documents():
    paths = glob.glob(os.path.join(DOCS_DIR, "**/*"), recursive=True)
    paths = [p for p in paths if os.path.isfile(p)]
    with psycopg.connect(DB_DSN, autocommit=True) as conn:
        from pgvector.psycopg import register_vector
        register_vector(conn)
        ensure_schema(conn)
        conn.execute("TRUNCATE chunks;")  # full reindex; see SKILL.md for incremental
        total = 0
        for path in paths:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
            for chunk in chunk_text(text):
                vec = embed(chunk)
                conn.execute(
                    "INSERT INTO chunks (source, content, embedding) VALUES (%s, %s, %s)",
                    (path, chunk, vec),
                )
                total += 1
        print(f"Indexed {total} chunks from {len(paths)} files into {DB_DSN}")


if __name__ == "__main__":
    index_documents()
