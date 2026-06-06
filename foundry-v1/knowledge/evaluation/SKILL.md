# SKILL — Evaluation

> **Status:** concept `[Established]` · tooling `[Current as of June 2026 — re-verify quarterly]` · **illustration: prose only — the standard and pattern are documented; no runnable code yet.** This is reference material to build *from*; it does not outrank your judgment, and you decide whether your context needs this capability at all.
> **Trigger:** load when a task changes a prompt, skill, model, or retrieval setup and needs to know whether quality moved.
> **Phase:** Test.

## 1. Stable concept `[Established]`
You cannot eyeball whether a change improved an agent — the same input can produce different paths across runs, and outputs that look right can be semantically wrong. Evaluation makes quality *measurable*:
- **Golden dataset** — a fixed set of inputs with known-good expected behavior.
- **Automated scoring** — exact-match where possible; **LLM-as-judge** (a separate model grades each output against written criteria) for open-ended outputs.
- **Trajectory eval** — for agents, score the *path* (did it call the right tools in the right order), not only the final answer, because a right answer can come through a broken process.
- **CI gating** — run the eval suite automatically on every prompt/skill/model change so a regression is caught before it ships. This is the automated, versioned descendant of a manual quality rubric.

## 2. Current tooling `[Current as of June 2026 — re-verify]`
- **RAG-specific:** **RAGAS** (retrieval + answer quality metrics).
- **General eval + tracing:** **Langfuse**, **Arize Phoenix** (OTel-native), **Braintrust** (eval-first), **Weights & Biases Weave**.
- These overlap with the observability backends — eval and tracing increasingly live in one tool.

## 3. Key pattern
Build a small golden set first (even 20–50 cases beats none). Wire LLM-as-judge scoring. Run it in CI on every change to a prompt, skill, or retrieval config. Gate merges on the score. For retrieval specifically, the eval set is how you *measure* recall for your content rather than assume it (this is the hook the RAG file references).

## 4. Failure modes it guards
| Failure | Guard |
|---|---|
| A "fix" silently makes things worse | CI eval on every change |
| Right answer via wrong/expensive path | Trajectory eval, not just final-output check |
| Retrieval quality assumed, not known | A measured eval set per data source |
| Quality judged by vibes | Written criteria + LLM-as-judge scoring |

## 5. Registry note
Evaluation is a process and a dataset, not a connectable tool — no registry entry. It plugs into the execution loop's Test phase and into CI.
