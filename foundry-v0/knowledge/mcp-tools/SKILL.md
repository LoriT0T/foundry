# SKILL — Tool Layer / MCP

> **Status:** concept `[Established]` · tooling `[Current as of June 2026 — re-verify quarterly]` · **illustration: prose, plus RAG's `mcp_server.py` shows the pattern working in code.** Reference material to build *from*; it does not outrank your judgment.
> **Trigger:** load when a task exposes a capability to an agent as a callable tool.
> **Phase:** Execute.

## 1. Stable concept `[Established]`
**MCP (Model Context Protocol)** is the open standard for exposing tools, data, and prompts to an LLM so any compliant client can use them. It collapses the N×M problem (every model × every tool needing a custom connector) into N+M: build one server per capability, and any MCP-compatible agent can call it. It has three primitives — **tools** (actions), **resources** (read-only context), **prompts** (reusable templates) — over **JSON-RPC 2.0**, on two transports: **stdio** (local processes) and **HTTP/SSE** (remote). Two features enable human-in-the-loop: **sampling** (a server asks the model to reason mid-task) and **elicitation** (a server requests direct user input/confirmation).

## 2. Current tooling `[Current as of June 2026 — re-verify]`
MCP is an Anthropic-created open standard (Nov 2024), governed by the Linux Foundation since Dec 2025, with 500+ public servers and support across Anthropic, OpenAI, and Google. Build servers with **FastMCP** (Python) or the official SDKs. Register with a client (e.g. `claude mcp add --transport stdio <name> -- <command>`).

## 3. Key pattern
Build a capability as ordinary code → wrap the entry function as an MCP server (see `rag-retrieval/mcp_server.py` for a working instance) → register it. Now any agent connects it as a tool *without knowing the internals*. This is the mechanism the whole `tool-registry.md` + `DECISION_RULE.md` system sits on: every registered tool is an MCP server, keyed by its data source.

## 4. Failure modes it guards
| Failure | Guard |
|---|---|
| Custom connector per model×tool | One MCP server, any client |
| Tool internals leak into every agent | Server hides internals behind the protocol |
| Context bloat from over-connecting | Connect only on data-source match (BOOTSTRAP rule) |
| Server fetches untrusted content | Treat as injection vector; pair with guardrail retrieval rail |

## 5. Registry note
MCP *is* the tool mechanism — every registered tool instance (in a project's `TOOL_REGISTRY.md`, per the `tool-registry.md` schema) is an MCP server. This file is the "how the tools in the registry are built and connected" reference.
