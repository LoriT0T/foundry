# SKILL — Deployment

> **Status:** concept `[Established]` · tooling `[Current as of June 2026 — re-verify quarterly]` · **illustration: prose only — the standard and pattern are documented; no runnable code yet.** This is reference material to build *from*; it does not outrank your judgment, and you decide whether your context needs this capability at all.
> **Trigger:** load when a task moves a system off localhost, or needs reproducible environments, scaling, or self-healing.
> **Phase:** Execute.

## 1. Stable concept `[Established]`
Running on one machine, configured by hand, is a demo. Production deployment makes a system reproducible, scalable, and recoverable:
- **Container** (Docker) — packages the app plus every dependency into a standard unit that runs identically anywhere. Kills "works on my machine."
- **Orchestrator** (Kubernetes) — runs many containers across many machines with auto-scaling and self-healing.
- **Infrastructure-as-code** (Terraform) — servers and resources defined as reproducible files, not clicked into existence.
- **CI/CD** — automated pipeline that tests and deploys on every change.
- **Environment separation** — distinct staging and production.
- **Secrets management** — keys/passwords in a vault, injected at runtime, never in code or config (this is a foundation red line, enforced here).

## 2. Current tooling `[Current as of June 2026 — re-verify]`
Docker (containers), Kubernetes (orchestration), Terraform (IaC), GitHub Actions / GitLab CI (pipelines), Vault or cloud secret managers (secrets). For data-residency-sensitive work, deploy to sovereign/on-prem rather than generic public cloud.

## 3. Key pattern
Containerize the agent and its dependencies → define infra as code → pipeline runs tests + eval gate, then deploys to staging, then prod → secrets injected from the vault at runtime. The foundation's localhost+launchd setup is the pre-deployment version; this is what makes it portable and recoverable.

## 4. Failure modes it guards
| Failure | Guard |
|---|---|
| "Works on my machine" only | Containerization |
| Manual server setup, unreproducible | Infrastructure-as-code |
| Bad change reaches users | CI/CD with test + eval gate, staging first |
| Secret leaked in code/config | Vault-injected secrets at runtime |
| One node dies, service down | Kubernetes self-healing |

## 5. Registry note
Deployment is infrastructure, not an agent tool — no registry entry. Its choices (sovereign vs public cloud, strictness) are project-specific tuning per INSTANTIATION_GUIDE.
