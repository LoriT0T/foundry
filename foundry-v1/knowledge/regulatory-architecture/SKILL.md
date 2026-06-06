# SKILL — Regulatory Architecture

> **What this is.** The universal discipline of operating as an agent in a *regulated* domain — without containing any rule. It carries **zero regulations, zero named regimes, zero sample regulatory content**: only how to *recognize* you are regulated, the recurring *categories* of constraint (as questions, never answers), the *method* to research your project's actual current rules at instantiation, and the *architecture* that lets whatever you find attach at a seam instead of being baked into logic. Regulations are the most project-specific thing there is; this file is the most universal thing about handling them.
>
> **Where it sits.** `~/Foundry/knowledge/regulatory-architecture/SKILL.md`. Loaded on trigger from `knowledge/INDEX.md`. It is an instance of `knowledge/INSTANTIATION_GUIDE.md` (your specifics enter once, at birth; nothing flows back), it builds its seams on `foundation/COMPARTMENTALIZATION.md`, it routes uncertainty through `foundation/THINKING.md` (tiers) and `foundation/MISTAKE_ENGINE.md` ("name the gap"), and it is backed by the regulation red line in `foundation/RED_LINES.md`.
>
> **Status.** Discipline `[Established]` — composed from already-established foundation discipline. Full instantiation path `[Draft — structural]` until a real regulated agent has run it end to end. **Bias-free: it names no jurisdiction, regime, authority, or rule as content.**
>
> **Trigger.** Load when the project operates in a regulated domain — apply the §1 check. If §1 is negative, this file never loads and the agent behaves exactly as one born without it.
>
> **Phase.** Plan (recognize + research at instantiation) and Execute (build the seams).

---

## The governing test (state it, design against it)

**One Foundry instantiates every regulated agent identically.** From *this exact file, unchanged*, it must be possible to instantiate — concretely and interchangeably — a **Saudi health** agent, a **UK health** agent, and a **German finance** agent, with zero edits to anything here. Those three are arbitrary stand-ins for *any* maximally-different regimes; what matters is the **neutrality**, not the names.

> If any sentence in this file would serve one of those agents better than another — leaning toward a jurisdiction, a domain, a regime, or a specific rule — it has leaked project bias and is **wrong**: delete it. (`README.md` contamination boundary; `INSTANTIATION_GUIDE.md` bias rule.)

---

## 1. Recognition — am I in a regulated domain?

You cannot tell from inside the foundation whether your project is regulated: the foundation is domain-blind by construction, and your training data is neither current nor authoritative on the question. So you must **actively check at instantiation**, by interrogating what the work *touches* and *who can penalize it* — never by matching a domain name.

Ask, of the project's real work:
- **Subject.** Does it handle data or take actions about identifiable people — their bodies/health, finances, communications, location, beliefs, biometrics, legal status, or other intimate facts?
- **Authority.** Is there an outside party — a government, regulator, professional body, standards regime, or binding contract — that can impose penalties for *how* the work is done, not merely whether it succeeds?
- **Externality.** Could doing the work wrongly harm third parties, create legal liability, or cost a license — consequences that land beyond the principal?
- **Inherited rules.** Are there rules over this work that the agent did not author and cannot change, that persist regardless of the principal's preference?
- **Peers' machinery.** Do others doing this work visibly carry compliance apparatus — consent flows, audit logs, retention schedules, named compliance officers, certifications, mandated disclosures?
- **Borders.** Does data or action cross a jurisdictional boundary?

> **The trigger.** If *any* answer is plausibly yes, treat the domain as regulated and **stop**: do **not** proceed on assumed, remembered, or invented rules. "I don't know the rule" is the signal to run the research playbook (§3), never to guess. Proceeding on an invented rule is the precise failure the regulation red line forbids (`RED_LINES.md`).

---

## 2. The seed categories — constraints framed as questions

These are the categories of constraint that recur across **most** regulated domains. Each is stated **only as a question to answer per project** — never as an answer, because the answer is exactly the project-specific, jurisdiction-specific, dynamic content this file must not carry. Instantiate each question with *your* data classes and actions; answer it in the research playbook (§3).

1. **Data residency.** Where must each class of data physically live — at storage, processing, and backup — and *which authority* mandates that location? Which classes are bound, which are exempt?
2. **Consent & lawful basis.** On what recognized basis is each use of data permitted? Is consent required; if so, what makes it valid (informed, specific, freely given, revocable), and what is the basis if consent is absent or withdrawn?
3. **Data retention & deletion.** For how long may — or must — each data class be kept? What triggers deletion, must deletion be provable, and is there an overriding duty to retain (or to destroy)?
4. **Audit trail & traceability.** What must be recorded, in what detail, kept for how long, protected how (tamper-evidence), and who is entitled to inspect it?
5. **Identity assurance & authentication strength.** How strongly must a party's identity be established before a given action? What assurance level does each action demand, and who counts as an authoritative verifier?
6. **Breach / incident handling.** What counts as a reportable incident? To whom must it be reported, within what deadline, containing what — and who else must be told (authorities, affected parties)?
7. **Cross-border transfer.** Under what conditions may data or action cross a jurisdictional boundary? What mechanism legitimizes a transfer, and which destinations are restricted or forbidden?

> **This seed is deliberately incomplete — a floor, not a checklist.** It covers categories about *data and identity*; your domain will almost certainly impose categories this list does not name. **You must propose the additional categories your specific project requires** and carry them through §3 and §4 exactly like the seed.
>
> *How to find them:* for each authority you identify in §3, enumerate the obligation-types it imposes and add any not already covered. This file deliberately gives **no examples** of further categories — naming them would bias you toward them and away from the ones your domain actually has. Derive them from your authorities, not from this file. **No false completeness:** a project is not "fully mapped" because the seven seed questions are answered.

---

## 3. The research playbook — discover the actual rules at instantiation

The categories are universal; **their answers are not — and they are in neither this file nor your training data.** This is the universal *method* for finding them. You, the instantiating agent, execute it for your project; the **findings live in your own `identity/` and `project/` layers, never back in Foundry.**

```
STEP A — Map the governing authorities.  (jurisdiction[s] × domain)
  Who can make and enforce rules over THIS work? Enumerate every layer that
  applies — supranational, national, regional, sectoral, professional body,
  standards regime, binding contract, and the principal's own downstream
  obligations. Expect several, stacked. Name each; note what it governs.

STEP B — Find the CURRENT applicable rules.  (rules are DYNAMIC)
  For each authority, get the rule in force NOW from its authoritative current
  source — the official text, the regulator's own publication — not from memory
  and not from a summary. Training data is a stale snapshot by construction;
  never state a regulatory rule from it as current. Confirm the version/date in
  force. Prefer primary sources; corroborate secondary ones.

STEP C — Answer each category for your project.  (the seed + the ones you added)
  For every category in §2, record: the rule · the authority · the instrument /
  reference · the date confirmed · the data classes / actions it binds.

STEP D — Flag what you cannot confirm.  (uncertainty, never a guess)
  Where a rule is ambiguous, authorities conflict, no primary source is
  reachable, or you simply cannot verify it: record it as an OPEN question with
  its uncertainty tier (THINKING.md), name the gap (MISTAKE_ENGINE.md), and GATE
  any action that depends on it (RED_LINES.md irreversibility gate) until a
  qualified human resolves it. An admitted unknown is safe; a confident guess
  about a binding rule is not. You are not the legal authority — high-stakes
  rules get a competent human's confirmation before reliance.

STEP E — Record findings in YOUR layers (never in Foundry).
  • identity/USER.md   — the principal's jurisdiction(s) + domain: the CONTEXT
                         that makes this project regulated (USER.md §1–§2). The
                         rules themselves bind the WORK, so they live below.
  • project/<name>/COMPLIANCE.md  (create it in YOUR project layer) — the
                         category → rule → authority → reference → confirmed-date
                         table from STEP C, plus the OPEN items from STEP D.
  • project/ARCHITECTURE.md — which seam (§4) each confirmed rule attaches to,
                         and the component that owns enforcing it.
  • project/AGENT.md   — compliance as success criteria (its §3) and each
                         unconfirmed rule as a named gap/blocker (its §5).
  • project/<name>/TOOL_REGISTRY.md — any seam realized as a tool (DECISION_RULE).
  • runtime/memory/<date>.md — the research session itself.

STEP F — Set a re-verification cadence.  (because the rules move)
  A confirmed rule carries a freshness date, like volatile tooling in INDEX.md.
  Record when each must be re-checked and what event forces an early re-check
  (a known reform, a new market, a new data class). A rule confirmed once is not
  confirmed forever.
```

> **The split that keeps Foundry clean:** the **playbook** is universal and lives here; the **findings** are specific and live in the instantiation. Nothing in the right-hand column of `INSTANTIATION_GUIDE.md`'s contamination table ever flows back into this file.

---

## 4. The attachment pattern — seams, not hardcoded rules

A researched rule is worthless if it is baked into business logic, because the rule is **dynamic** (§3 STEP F) — it will change, and a hardcoded rule means a rewrite each time. `COMPARTMENTALIZATION.md` already gives the remedy: **one concern, one unit; a rule lives in its owning unit and is fixed there once.** This capability only names *which seams the regulatory concerns map onto*. Build the seam; let the research finding plug in as that seam's rule.

These are **questions of architecture, not specific rules** — each names a boundary to *prepare*, not a value to set:

| Compliance seam | The owning boundary (per `COMPARTMENTALIZATION.md`) | The architecture question (the rule plugs in here) |
|---|---|---|
| **Identity / auth** | the unit that establishes & asserts who a party is | Which actions demand which assurance level — enforced at this one unit? *(cat. 5)* |
| **Data residency** | the unit(s) that own where each data source is stored / processed | Does each data class's location satisfy its residency rule — checked at the unit that owns that store? *(cat. 1)* |
| **Audit log** | the unit that records the trace | Does the trace capture what must be logged, kept as long as required, protected from tampering? *(cat. 4)* |
| **Consent / retention** | the unit(s) that own lawful-basis capture and data lifecycle | Is each use gated on a valid basis, and is each data class on a retention/deletion clock? *(cat. 2, 3)* |
| **Escalation / breach** | the single structured exit | Does an incident route to the right authority + affected-party notice, within the deadline, through one defined exit? *(cat. 6)* |
| **Cross-border** | the egress boundary any data/action crosses to leave the jurisdiction | Is every cross-border flow legitimized by an approved mechanism, and blocked otherwise? *(cat. 7)* |

**The discipline:**
- **One seam per concern; the rule lives at the seam.** When the rule changes, you change *one unit*, not the system (`COMPARTMENTALIZATION.md` payoff; the guardrail-at-owning-unit hook of `MISTAKE_ENGINE.md`).
- **Prepare the seam even before the rule is known.** A seam with a narrow interface can receive whatever §3 finds — including a finding that arrives later, or changes.
- **A seam can be a tool.** If a seam is realized as a service (a residency-aware store, an audit sink, an identity verifier), register the instance in `project/<name>/TOOL_REGISTRY.md` via `DECISION_RULE.md` — never in `knowledge/`.
- **Add seams for the categories you added in §2.** The six above pair with the seed; a category you discovered needs its own seam. Same law: one concern, one unit.
- **Gate the dangerous moment structurally.** Where a rule guards an irreversible act, make compliance a structural gate at the seam (fail-closed), not a judgment call (`RELIABILITY.md`, `RED_LINES.md`).

---

## 5. Failure modes (and the guard for each)

| Failure | Cause | Guard |
|---|---|---|
| Agent states a plausible regulation that is wrong or stale | trained on a stale, over-general snapshot | recognition trigger (§1) + playbook STEP B (current primary source) + regulation red line |
| A rule is hardcoded into logic and breaks when it changes | no seam prepared | attachment pattern (§4): the rule lives at its seam, changed in one unit |
| An unconfirmable rule is silently skipped or filled with a guess | discomfort with an open unknown | playbook STEP D: flag with a tier, name the gap, gate the action, escalate |
| Findings written back into Foundry | convenience at instantiation | contamination boundary: findings live in `identity/` + `project/` only (§3 STEP E) |
| "We've covered the rules" when categories are missing | the seed treated as exhaustive | §2 is an explicit floor: propose-more instruction, no false completeness |
| One jurisdiction's rule generalized to another | anchoring on a known regime | the governing test: swap the jurisdiction and nothing here changes |
| A once-confirmed rule silently goes stale | rules are dynamic; confirmation treated as permanent | playbook STEP F: freshness date + re-verify trigger on every finding |

---

> **For working memory:** You can't tell from inside whether you're regulated — check what the work touches and who can penalize it (§1). The categories are universal *questions* (§2, deliberately incomplete — propose more); the *answers* are researched fresh per project and live in your own layers, never in Foundry (§3); a rule you can't confirm is flagged, never guessed; whatever you find plugs into a prepared **seam**, never hardcoded (§4). No invented rule, no named regime, no sample regulation — ever.

**Maturity.** Discipline `[Established]`; full instantiation `[Draft — structural]` — promote once a real regulated agent has run §1–§4 end to end and a maintainer confirms: foundation loaded, specifics entered only at instantiation, no rule or regime written into this file, findings recorded only in the agent's own layers. Snapshot before any future rewrite to `runtime/iterations/` (`QUALITY_RUBRIC.md` crit. 5). **Sync invariants:** adding/changing this file → add/keep its `knowledge/INDEX.md` row (trigger = "the project operates in a regulated domain") in the same change; it is referenced by the regulation red line in `foundation/RED_LINES.md`; its findings update `identity/USER.md` + `project/<name>/COMPLIANCE.md` + `project/ARCHITECTURE.md` + `project/AGENT.md` per §3 STEP E.
