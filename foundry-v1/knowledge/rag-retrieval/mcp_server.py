"""
mcp_server.py — REFERENCE IMPLEMENTATION (the pattern, not a frozen product)

What this does:
  Wraps the retrieve() function from rag_query.py as an MCP server, so any
  MCP client (Claude Code, your own agents) can call it as a tool named
  "search_knowledge_base" WITHOUT knowing the internals.

  This is the step that turns "a RAG script on disk" into "a tool an agent
  connects to" — the layer described in SKILL.md and registered in
  tool-registry.md.

Setup:
  pip install fastmcp
  Then register with Claude Code (local stdio transport):
    claude mcp add --transport stdio rag-<dataset> -- python mcp_server.py
  Verify:
    claude mcp list

One-instance-per-data-source:
  This server serves ONE data source (whatever rag_query.py's DB_DSN points at).
  A different data source = a separate instance with its own DB_DSN and its own
  registered name (rag-<dataset-a> vs rag-<dataset-b>). Same code, different
  data. See DECISION_RULE.md.

Context-cost note:
  Connecting this server loads its tool definitions into the connecting agent's
  context. Per BOOTSTRAP loading rule: connect ONLY when the task's data source
  matches this instance. An agent that never searches this knowledge base must
  never connect this server.
"""

from fastmcp import FastMCP
from rag_query import retrieve

mcp = FastMCP(name="rag-knowledge-base")


@mcp.tool
def search_knowledge_base(question: str, k: int = 5) -> list[dict]:
    """Search this knowledge base for passages relevant to the question.
    Returns up to k chunks, each with its source and similarity score.

    SECURITY (see guardrails knowledge file): if this knowledge base contains
    any text not authored by the operator, retrieved chunks are UNTRUSTED input
    and must pass a retrieval guardrail before being injected into a prompt —
    RAG over untrusted documents is an indirect prompt-injection vector."""
    return retrieve(question, k=k)


if __name__ == "__main__":
    mcp.run()
