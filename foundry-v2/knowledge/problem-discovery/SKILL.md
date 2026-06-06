# SKILL — Problem Discovery

> **What this is.** The universal discipline of determining *which problem in a domain is actually worth solving* — **before** any of it is built. It is "build the **right** thing," upstream of building it *well* (`COMPARTMENTALIZATION.md`) and building it *compliantly* (`regulatory-architecture/SKILL.md`). It carries **zero findings, zero markets, zero domains, zero named problems**: only how to *recognize* that a problem has been assumed rather than verified, the recurring *lines of inquiry* for finding the real problem (as questions, never answers), the *method* to discover it from current primary sources at instantiation, and the *handoff* that turns a verified problem into the brief the rest of the build consumes. The problem is the most project-specific thing there is; this file is the most universal thing about finding it.
>
> **Where it sits.** `~/Foundry/knowledge/problem-discovery/SKILL.md`. Loaded on trigger from `knowledge/INDEX.md`. It is an instance of `knowledge/INSTANTIATION_GUIDE.md` (your specifics enter once, at birth; nothing flows back), it routes uncertainty through `foundation/THINKING.md` (tiers) and `foundation/MISTAKE_ENGINE.md` ("name the gap"), and it is backed by the problem-verification red line in `foundation/RED_LINES.md`. It runs **first** — upstream of the regulated-domain recognition in `regulatory-architecture/SKILL.md`, and upstream of the standard build.
>
> **Status.** Discipline `[Established]` — composed from already-established foundation discipline. Full instantiation path `[Draft — structural]` until a real agent has run it end to end. **Bias-free: it names no domain, market, or problem as content.**
>
> **Trigger.** Load when the project's problem is *assumed rather than verified* — apply the §1 check. If the problem is already given and verified as fixed, this file never loads and the agent behaves exactly as one born without it.
>
> **Phase.** Plan (recognize + discover at instantiation) — upstream of everything else.

---

## The governing test (state it, design against it)

**One Foundry interrogates every domain identically.** From *this exact file, unchanged*, it must be possible to interrogate — concretely and interchangeably — a project in **Domain-A in one jurisdiction**, a project in **Domain-B in another**, and a project in **Domain-C in a third**, and arrive at *that* domain's own real highest-value problem, with zero edits to anything here. Those three are arbitrary stand-ins for *any* maximally-different domains; what matters is the **neutrality**, not the names — swap Domain-A / Domain-B / Domain-C and every sentence below must read identically true.

> If any sentence in this file would steer one of those interrogations toward a particular domain, market, or problem — leaning toward a kind of pain, a kind of user, a kind of solution — it has leaked project bias and is **wrong**: delete it. (`README.md` contamination boundary; `INSTANTIATION_GUIDE.md` bias rule.)

---

## 1. Recognition — is my problem verified, or assumed?

You cannot tell from inside the foundation whether the problem you were handed is the *real* highest-value problem in its domain: the foundation is domain-blind by construction, and a brief almost always arrives describing a *solution* or a *symptom*, not a verified problem. So you must **actively check at instantiation**, by interrogating the *form* of what you were given — never by trusting that the brief is already correct.

Ask, of the brief you were handed:
- **Solution-named or problem-named?** Does the brief name a *thing to build* ("build X") rather than a *verified pain to relieve*? A named solution is an assumed problem wearing a disguise.
- **Evidence or assertion?** Is the problem backed by current evidence of who suffers it and how much — or is it asserted ("everyone knows," "obviously," a single anecdote, a hunch)?
- **Stated or revealed?** Is the problem what someone *said* is the problem, or what the domain's actual behavior *reveals* is the problem? The two are routinely different.
- **Whose pain, how acute?** Can you name who concretely has the pain and what it costs them — or is the sufferer abstract?
- **Fixed by mandate, or still open?** Was the problem genuinely given and fixed by the principal as non-negotiable, or is it merely the first idea — still open to being wrong?

> **The trigger.** If the problem is *assumed* — named as a solution, asserted without evidence, taken from a stated rather than a revealed source, or simply the first idea — treat it as **unverified** and **stop**: do **not** build it as though it were verified. Run the discovery playbook (§3) to find the domain's real highest-value problem first. Building an assumed problem *well* is the precise failure the problem-verification red line forbids (`RED_LINES.md`) — the danger this whole capability guards: **building the wrong thing well.** **If the problem is genuinely given and verified as fixed** — set by the principal as non-negotiable and backed by evidence — this file does not fire; proceed to the regulated-domain check (`regulatory-architecture/SKILL.md` §1) and the build.

---

## 2. The discovery questions — the search for the real problem, framed as questions

These are the recurring lines of inquiry that surface the real problem across **most** domains. Each is stated **only as a question to answer per domain** — never as an answer, because the answer is exactly the domain-specific, market-specific, dynamic content this file must not carry. Instantiate each question with *your* domain; answer it in the discovery playbook (§3).

1. **Who has the pain, and how acute is it?** Who concretely feels it, how often, how badly — and what does it cost them today in money, time, risk, or forgone value? Is it a sharp pain for a few or a dull ache for many?
2. **Assumed problem vs. underlying problem.** What problem does the brief *assume* — and one layer down, what is the problem that *that* problem is a symptom of? Which layer is actually worth solving?
3. **Where is value lost in the domain today?** Following the domain's value from end to end, where does it leak — waste, delay, error, friction, abandonment — and where does the *largest* leak sit?
4. **Stated vs. revealed.** What do the domain's actors *say* the problem is, versus what their behavior — what they do, pay for, work around — *reveals* it to be? Where the two diverge, the revealed one is the real one.
5. **What would they fund?** Which version of the problem would someone with the pain actually pay to remove, or divert budget and effort toward — as opposed to merely complain about? Willingness to fund separates a real problem from an annoyance.
6. **Obvious solution vs. real bottleneck.** What is the obvious solution everyone reaches for — and is the true constraint actually there, or somewhere the obvious solution never touches? The gap between the obvious solution and the real bottleneck is where the highest-value problem usually hides.
7. **Why is it still unsolved?** If the problem is real and valuable, what has kept it unsolved — genuine difficulty, a recent change that only just made it solvable, or the fact that it is *not actually the problem*?

> **This seed is deliberately incomplete — a floor, not a checklist.** It names the lines of inquiry that recur; your domain will demand questions this list does not contain. **You must propose the additional discovery questions your specific domain requires** and carry them through §3 and §4 exactly like the seed.
>
> *How to find them:* for each actor and value-flow you map in §3, ask what *that* domain makes salient that the generic seed cannot reach. This file deliberately gives **no example problems and no example domains** — naming one would bias you toward it and away from the one your domain actually has. Derive them from your domain, not from this file. **No false completeness:** a domain is not "understood" because the seven seed questions are answered.

---

## 3. The discovery playbook — find the real problem at instantiation

The questions are universal; **their answers are not — and they are in neither this file nor your training data.** This is the universal *method* for finding them. You, the instantiating agent, execute it for your domain; the **findings live in your own `identity/` and `project/` layers, never back in Foundry.**

```
STEP A — Map the domain's actors and value flow.
  Who are the parties, and how does value move among them end to end — who
  creates it, who captures it, who pays, who loses? Name each actor; trace the
  flow. The real problem lives somewhere on this map; you cannot find it without
  drawing the map first.

STEP B — Find where pain and cost concentrate — from CURRENT primary sources.
  Locate where the largest pain, cost, or lost value actually sits, from the
  domain's authoritative CURRENT sources — what the actors do, pay, and abandon
  now — not from assumption and not from training memory. Training data is a
  stale, over-general snapshot by construction; never state a market "fact" from
  it as current. Prefer primary / direct evidence; corroborate secondary
  sources; confirm the recency of whatever you rely on.

STEP C — Separate the stated problem from the revealed one.
  For each candidate problem, record what the actors SAY versus what their
  behavior REVEALS (§2 q.4). Where the two diverge, weight the revealed signal.
  Distinguish a loud complaint from a funded priority (§2 q.5).

STEP D — Size each candidate problem.
  For every candidate, record: who has it · how acute · how much value is at
  stake · what they would fund · why it is still unsolved. Rank value-at-stake
  against solvability. The highest-value *solvable* problem is the output.

STEP E — Flag what you cannot confirm.  (uncertainty, never a guess)
  Where evidence is thin, sources conflict, no primary source is reachable, or a
  market claim cannot be verified: record it as an OPEN question with its
  uncertainty tier (THINKING.md), name the gap (MISTAKE_ENGINE.md), and do NOT
  let an unverified problem pass as verified — GATE the commit to building it
  until the gap is closed or a qualified human resolves it (RED_LINES.md). An
  admitted unknown is safe; a confident guess about which problem matters is not.

STEP F — Record findings in YOUR layers (never in Foundry).
  • identity/USER.md   — the principal's domain + who they serve: the CONTEXT in
                         which the problem is being sought.
  • project/<name>/PROBLEM.md  (create it in YOUR project layer) — the actor /
                         value-flow map, the candidate problems, the sizing from
                         STEP D, the chosen problem, and the OPEN items from STEP E.
  • project/AGENT.md   — the verified problem as the goal + success criteria
                         (its §3); each unverified assumption as a named gap (its §5).
  • runtime/memory/<date>.md — the discovery session itself.

STEP G — Set a re-verification trigger.  (because domains move)
  A chosen problem carries a freshness assumption: the conditions that made it
  the highest-value problem can change. Record what event forces a re-check — a
  shift in the domain, a new actor, evidence the pain has moved. A problem
  verified once is not verified forever.
```

> **The split that keeps Foundry clean:** the **playbook** is universal and lives here; the **findings** are specific and live in the instantiation. Nothing project-specific ever flows back into this file (`INSTANTIATION_GUIDE.md` contamination table).

---

## 4. The handoff — the verified problem becomes the brief

Problem-discovery produces exactly one thing: a **problem statement** — the domain's real highest-value problem, verified, sized, and sourced. That statement is the **input** to everything downstream. The order is fixed, and problem-discovery is **first**:

```
problem-discovery (THIS file)          →  produces the verified PROBLEM STATEMENT
        ↓
regulated-domain recognition            →  asks: is THIS problem regulated?
(regulatory-architecture/SKILL.md §1)       (you cannot ask until you know the problem)
        ↓
the standard build                       →  builds the right thing, well, compliantly
(THINKING.md loop + COMPARTMENTALIZATION.md + regulatory §3–§5 if regulated)
```

- **Problem-discovery runs first.** You cannot ask whether *the problem* is regulated, nor build the seams that serve it, until you know *which problem* you are solving. Recognition (§1) is therefore the first gate in the birth sequence — ahead of the regulated-domain question (`BOOTSTRAP.md` birth question 1; `INSTANTIATION_GUIDE.md` STEP 1).
- **The output is a written problem statement, not a verbal hunch.** It records: the problem · who has the pain and how acute · where value is lost · the stated-vs-revealed evidence · the size and what they would fund · why it is still unsolved · the uncertainty tier of each claim and any OPEN gaps (§3 STEP F's `project/<name>/PROBLEM.md`).
- **It becomes the goal.** The verified problem is what fills the Goal / "working well" of the birth questions and the success criteria in `project/AGENT.md`. Everything the agent later builds is measured against *this* problem — not the assumed one it started with.
- **A flagged problem does not hand off as verified.** If §3 STEP E left the problem unconfirmed, the handoff carries the gap forward explicitly (honest status, `THINKING.md` Phase 4) — the downstream build is told the problem is provisional, never that it is settled.

---

## 5. Failure modes (and the guard for each)

| Failure | Cause | Guard |
|---|---|---|
| The assumed problem is built well — the wrong thing, done right | the problem was never verified, only inherited | recognition trigger (§1) + the problem-verification red line: a named solution is an assumed problem |
| Discovery bends toward a pre-chosen solution | confirmation bias — the answer was decided before the question | §2 q.4 + q.6 (revealed-not-stated, bottleneck-not-obvious-solution); §3 STEP C weights revealed signal over asserted |
| A market "fact" is stated from stale training memory | training data treated as current and authoritative | §3 STEP B: current primary sources only; never state a market fact from memory |
| "We understand the domain" when the real problem is unfound | the seed treated as exhaustive | §2 is an explicit floor: propose-more instruction, no false completeness |
| An unverifiable problem is passed off as verified | discomfort with an open unknown | §3 STEP E: flag with a tier, name the gap, gate the commit-to-build, escalate |
| Discovery findings written back into Foundry | convenience at instantiation | contamination boundary: findings live in `identity/` + `project/` only (§3 STEP F) |
| One domain's problem generalized to another | anchoring on a problem found elsewhere | the governing test: swap the domain and nothing here changes — the *method* transfers, the *problem* never does |

---

> **For working memory:** You can't tell from inside whether the problem is real — check whether the brief names a *solution* or a *verified pain* (§1). The discovery questions are universal *questions* (§2, deliberately incomplete — propose more); the *answers* are found fresh per domain from current primary sources and live in your own layers, never in Foundry (§3). The output is one **verified problem statement** that becomes the brief the rest of the build consumes — and problem-discovery runs **first**, upstream of the regulated-domain question and the build (§4). A problem you can't verify is flagged, never presumed. No invented market, no named domain, no example problem — ever; an assumed problem is researched or flagged, never built as if verified.

**Maturity.** Discipline `[Established]`; full instantiation `[Draft — structural]` — promote once a real agent has run §1–§4 end to end (recognition → discovery → sized candidates → verified problem statement handed off) and a maintainer confirms: foundation loaded, specifics entered only at instantiation, no domain / market / problem written into this file, findings recorded only in the agent's own layers. Snapshot before any future rewrite to `runtime/iterations/` (`QUALITY_RUBRIC.md` crit. 5). **Sync invariants:** adding/changing this file → add/keep its `knowledge/INDEX.md` row (trigger = "the project's problem is assumed rather than verified") in the same change; it is referenced by the problem-verification red line in `foundation/RED_LINES.md`; it is positioned **first** in the birth sequence (`BOOTSTRAP.md` + `INSTANTIATION_GUIDE.md`), ahead of the regulated-domain recognition; its findings update `identity/USER.md` + `project/<name>/PROBLEM.md` + `project/AGENT.md` per §3 STEP F.
