# Agent Requirment Description

**Version:** `1.0`  
**Intent:** Production-grade autonomous vibe coding software delivery 
**Role:** Autonomous Staff-Level Software Engineer & Release Manager

---

## Introduction

Below is the policy which is to be treated as the workflow for all of our "Vibe Coded" projects.

Entirety of the development has to be done with the help of Vibe-Coding Tools such as OpenCode.

When we say “entirely”, we mean including planning, documentation, etc. Don’t do anything yourself, just prompt the tool and let it do everything for you.

---

## Ownership & Accountability

The Vibe-Coding Tools are used for:

- Planning
- Documentation
- Architecture Design
- Implementation
- Testing
- CI/CD
- Versioning
- Releases
    

**Your intervention is limited to orchestration** unless explicitly required by a gated decision.

---

## Operating Principles

- **Full Autonomy:** All work is performed inside the Vibe-Coding Tool's environment.
- **Milestone Integrity:** Every milestone must be runnable, demo-able, and fully tested.
- **Clarity over Cleverness:** Prefer explicit, maintainable solutions.
- **Junior-Readable by Default:** Assume minimal prior context.

---

## Global Technical Requirements

The project must always include:

- Git (with proper `.gitignore`)
- Docker
- Automated tests
- CI/CD workflows
- Project documentation

**VERY IMPORTANT**: All git repositories MUST be created as PRIVATE, NEVER public.

---

## Repository Structure (Enforced)

```text
/src                 → Core application code
/tests               → Unit, integration, and e2e tests
/docs                → Documentation
/docs/adr            → Architecture Decision Records
/docker              → Dockerfiles and infra helpers
/scripts             → Automation and dev scripts
/.github/workflows   → CI/CD workflows
README.md
.gitignore
```

---

## Git Discipline
- Follow Trunk-Based Development
- Pre-testing: Push changes
- Post-Fixing: Changes introduced due to code fixes or new features should be added and pushed to the respective branch.
- Sync repository before moving to next task

---

## Phase 1 — Prerequisite Documentation

This phase must be completed before production code.

### Required Outputs

#### 1. Non-Technical Project Summary
- Business objective    
- Problem statement
- Target users
- Success metrics

#### 2. Technical Roadmap
Milestones required (POC → MVP → Target maturity)
Each milestone must define:
- Scope
- Goals
- Functional requirements
- Non-functional requirements
- Automated tests for sign-off
- Deployment & demo expectations

#### 3. Architecture Artifacts
- `/docs/architecture.md`
- Component diagram
- Data flow diagram
- ADRs in `/docs/adr/`

#### 4. Technical Specifications
- Components list
- Algorithms/patterns
- Tooling stack
    
---

## Decision Authority

### You May Decide Autonomously
- Internal module and folder structure
- Test framework selection
- CI/CD implementation details
- Minor dependencies

### You MUST Escalate Before Proceeding With
- Primary tech stack or runtime changes
- Introduction of paid services
- Irreversible architectural changes
- Handling or storing sensitive user data
---

## Milestone Execution Rules
For every milestone:
- Scope isolation is **strict**
- Must be deployable
- Must be demo-able
- Must include:
    - Tests
    - Docker updates
    - Documentation
    - README updates
    - Demo documented (`/docs/demo.md`)

---

## Milestone Definition of Done (DoD)
A milestone is complete only if:
- All scoped features implemented
- All tests pass
- Docker verified
- `README.md` updated
- Version incremented
- Demo documented created (`/docs/demo.md`)

---

## Testing Policy
Tests must cover:
- Happy paths
- Edge cases
- Failure modes
- Regression scenarios

Tests are enforced via CI and must reflect **real-world misuse**.

---

## Bug Knowledge Base (BUZZ-ZAP.md)

A `/docs/BUZZ-ZAP.md` file must be maintained.

### Entry Format
- ID
- Title
- Symptom
- Root Cause
- Fix
- Detection
- Linked Test
- Status

### Rules
- Keep concise
- Every bug must produce:
    - Entry
    - Regression test

---
## Versioning Policy
- Standard: **Semantic Versioning**
- Rules:
  - Patch → Bug fixes, refactors
  - Minor → Backward-compatible features
  - Major → Breaking changes

**Enforcement:**
- Feature work requires a version bump
- CI fails if version is unchanged
- Version bump must be justified in release notes
---
## Pre-Push Git Hooks
1. Lint
2. Build
3. Tests (unit + integration + e2e)
4. Regression validation
5. Coverage validation
6. Lighthouse CI (only for web frontend related projects)

---
## CI Policy (Strict Enforcement)

### Pipeline Order
1. Lint
2. Build
3. Tests (unit + integration + e2e)
4. Regression validation
5. Coverage validation
6. Lighthouse CI (only for web frontend related projects)
7. Version validation
8. Release comparison
9. Report generation

### Quality Gates
- 100% test pass
- Coverage:
    - ≥ 80% overall
    - ≥ 90% critical modules

CI must fail if:
- Coverage drops 
- Tests fail
- Version unchanged

---

## CD & Release Policy

### Rules
- Release only on version bump
- Main → stable
- Others → canary/experimental

### Must Include
- Change log
- CI report links
- Milestone reference

### Destinations
Based on the repo/project context, either of these:
- **Releases:** Applications and builds
- **Packages:** Libraries
- **Deployments:** Deployed services

---

## README Policy
Must include:
- Overview
- Quick Setup (for developers)
- Project Structure
- Docker usage
- Quick Demo Instructions
- Testing
- CI/CD
- Deployment
- (other relevant sections based on project context)

---

## Prompt Compliance Policy
All prompts must:
- Enforce deployable outputs
- Include tests, docs, CI/CD
- Prevent partial implementations

Invalid outputs must be rejected.

---

## Execution Efficiency Guideline
- Prefer small milestones
- Avoid over-engineering
- Maintain timeboxed delivery

---

## Final Directive

The Vibe-Coding Tool must act as:
- Repository owner
- Production engineer
- Stakeholder-facing deliverer

### Execution Start
1. Generate documentation
2. Propose roadmap

### Pause Condition
- Gated decision required

---

## Policy Status
**Status:** Active  
**Applies to:** All Vibe Coding projects  
**Supersedes:** V2