# INSTANTIATION GUIDE — From Foundation to a Working Agent

> **What this is.** The runbook a fresh agent follows after it has digested the foundation. It turns a folder of patterns into a working setup *for one specific context* — without copying anyone else's specifics, and without rebuilding what already exists.
>
> **Where it sits.** `~/Foundry/knowledge/INSTANTIATION_GUIDE.md`. It is the connective tissue that ties the spine together: `BOOTSTRAP` (loading), `INDEX` (what knowledge exists), `tool-registry` (what tools exist), `DECISION_RULE` (reuse or instantiate).
>
> **The core idea.** The foundation carries **patterns and universal engineering knowledge** — never specifics. *Specifics come from the agent's own context, supplied here, at instantiation.* The agent inherits the expertise; it supplies the particulars.

---

## The bias rule (read first — it is non-negotiable)

**The foundation contains zero specifics.** No languages, no domains, no subjects, no project names, no goals, no personal context. Every knowledge file states only what is **universally true** for that capability (e.g. "the embedding model must match your content's language/domain") and leaves every particular (which language, which domain, which data) to be filled in *here*, at instantiation, from the agent's own context.

If you are an agent reading this: the foundation does **not** know what you work on, and it must not. You bring that knowledge. You apply the universal patterns to your particulars. Nothing you fill in flows back into the foundation.

If you are extending the foundation (adding a knowledge file): state the general principle, never an example drawn from one project. A knowledge file that names a specific language, domain, or client is contaminated — strip it. The test: *would this file be equally true and useful for an agent working on something completely different?* If not, it has a bias to remove.

---

## The authority rule (read second — it is also non-negotiable)

**No reference file outranks your judgment, and a file's completeness is not authority.** Every file in `knowledge/` is reference material you build *from*, not an instruction you obey. Some files carry a runnable illustration (e.g. RAG); most carry the standard in prose. A fuller illustration is easier to learn from — it is **never** a reason to choose that capability over what your context actually needs.

Concretely:
- The presence of runnable RAG code does **not** mean your agent should use RAG. If your context calls for something else — or nothing — build that instead.
- "This pattern exists and looks complete" is not "this pattern is right for me." Judge fit first; reach for the reference second.
- You may adapt an illustration, instantiate a pattern fresh, or build your own. All three are correct when your context warrants them. Deferring to a file *because it looks finished* is the failure to avoid.

The references raise your floor (you inherit the correct standard and current tooling). They never lower your agency (you still decide what your context needs).

---

## The sequence a fresh agent runs

```
STEP 0 — Digest the foundation.
  Load all of foundation/ (behavioral, universal). Read knowledge/INDEX.md (the
  map). Do NOT load individual knowledge files yet. (Per BOOTSTRAP loading rule.)

STEP 1 — Gather your context. (This is where YOUR specifics enter — once, here.)
  Answer, from your own project/subject — not from the foundation:
    • MANDATORY, FIRST — Is the problem given and verified, or assumed? Every
      agent answers this before anything else; you cannot tell from inside the
      foundation, and a brief usually names a SOLUTION ("build X"), not a
      verified problem. Apply the §1 recognition check in
      knowledge/problem-discovery/SKILL.md.
        – If ASSUMED (a solution named, a problem asserted without current
          evidence, or just the first idea) → problem-discovery is MANDATORY and
          runs FIRST: load knowledge/problem-discovery/SKILL.md now and run its
          discovery playbook (§3) to find the domain's real highest-value problem
          BEFORE the rest of STEP 1 and BEFORE the regulated-domain check below.
          Its output — a verified PROBLEM STATEMENT (§4) — is the INPUT to the
          goal bullet below and to the regulated-domain question; findings live
          only in your identity/ + project/ layers.
        – If GIVEN AND VERIFIED as fixed → proceed unchanged; the capability never
          loads and this agent behaves like one born without it.
      This is FIRST because you must know WHICH problem you are solving before you
      can ask whether THAT problem is regulated, or build anything for it. The
      silent failure it catches is building the wrong thing well.
    • What is this agent's goal? What does "working well" look like? (If the
      problem above was assumed, the goal IS the verified problem statement
      problem-discovery produced.)
    • What data sources will it work with? (Name each distinct knowledge base.)
    • What languages / domains does that data sit in?
    • What are the constraints? (latency, cost, data-residency, oversight,
      regulated content — these set the tradeoff points; the foundation cannot
      know them.)
    • What is irreversible or risky and needs a human gate?
    • MANDATORY — Is this project regulated? Every agent answers this, before
      building; you cannot tell from inside the foundation. Apply the §1
      recognition check in knowledge/regulatory-architecture/SKILL.md against
      what your work touches and who can penalize it.
        – If plausibly YES → regulatory-architecture is MANDATORY: load
          knowledge/regulatory-architecture/SKILL.md now and run its research
          playbook (§3) BEFORE building. Its findings shape STEP 2–5 (which
          capabilities, which compliance seams, which constraints) and live only
          in your identity/ + project/ layers. A YES also commits the build to
          be DRIVEN by the discovered rules at STEP 3 — not only gated by them.
          See regulatory-architecture §5: rules shape data-layer, interface,
          and technology decisions before they are settled.
        – If NO → proceed exactly as today; the capability never loads and this
          agent behaves like any non-regulated (V0-born) agent.
      The silent failure this catches is not a missed capability — it is a
      regulated domain that was never recognized. That is why it is its own
      mandatory question, not a sub-point of the constraints above.

STEP 2 — Determine which capabilities you need.
  For your goal, walk INDEX.md and select the capabilities the task actually
  needs. Selecting is not loading everything — pick the minimum set.
  (Not optional: if STEP 1's regulated-domain recognition was YES,
  knowledge/regulatory-architecture/SKILL.md is mandatory in this set.)

STEP 3 — For each needed capability, load its knowledge file and apply it.
  Read the file's universal pattern. Map the pattern onto YOUR context from
  STEP 1. (e.g. RAG's "match the embedding model to your content" → you pick
  the model that fits your language/domain, because now you know what that is.)
  If STEP 1's regulated-domain recognition was YES, run regulatory-architecture
  §5 here — the discovered rules drive data-layer, interface, and technology
  decisions before they are settled (not after, as a review). The seams §4
  prepares are the same seams §5 shapes; gates come on top of the shape, not
  in place of it.

STEP 4 — For each capability that has a tool, run DECISION_RULE.
  Name the data source → check your project's tool registry →
    reuse the existing instance if the data source matches,
    otherwise instantiate the pattern against your data and REGISTER it in your
    project layer (project/<name>/TOOL_REGISTRY.md).
  (Same data → reuse. Different data → new instance. Always → register.)

STEP 5 — Tune to your constraints (this is the "ceiling," and it is yours).
  The foundation gives a high floor. Your STEP 1 constraints set where each
  tradeoff lands — how much guardrail, how much latency budget, how much
  autonomy vs. oversight. The foundation cannot set these because they are
  specific to you. Tune deliberately; record the choices in YOUR project layer,
  not in the foundation.

STEP 6 — Verify and record.
  Run one loop end-to-end. Verify against STEP 1's "working well." Record what
  you instantiated and why in your project layer. Register any new tools in the
  project's TOOL_REGISTRY.md (never in knowledge/).
  Then the agent is alive — at a high floor, tuned to its own context, with
  nothing of any other agent's specifics inside it.
```

---

## Why this design holds (the two failure modes it avoids)

- **It is not "build your own from scratch."** That would make every agent re-derive solved engineering (chunking, injection risk, indexing) and produce below-standard results — the exact problem the technical layer exists to fix. The agent inherits the *pattern*; it only supplies *particulars*.
- **It is not "ship frozen specifics."** That would bake one project's biases into the foundation and break it the moment the work changes. Specifics live in the project layer; the foundation stays universal and reusable forever.

The line between them is this guide: **universal pattern (foundation) + your context (here) = your instance (project layer).**

---

## What flows where (the contamination boundary, stated once)

| Lives in foundation (universal) | Lives in project layer (specific) |
|---|---|
| "Match the embedding model to your content" | "My content is X, so I chose model Y" |
| "RAG over untrusted text needs a retrieval guardrail" | "My KB includes external docs, so I enabled it" |
| "Tune guardrail strictness to your risk tolerance" | "This is regulated, so I set it strict" |
| The runnable pattern + universal failure modes | The instance, its data source, its tuned values |
| The DECISION_RULE and the registry mechanism | The actual registered tools and their data |

Nothing in the right column ever flows left. If it does, the foundation has been contaminated and stops being a foundation.

**Maturity:** `[Draft — structural]`. Verify by running one fresh agent through STEP 0–6 against a real context and confirming: foundation loaded fully, specifics entered only at STEP 1, no foundation file mentions that context afterward, tools registered. Promote to `[Established]` once observed.
