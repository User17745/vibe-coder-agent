# DESIGN_SPEC.md - VibeCoder Agent

## Overview
**VibeCoder** is an autonomous Staff-Level Software Engineer and Release Manager designed to handle the entire software development lifecycle (SDLC) for "Vibe-Coded" projects. Built using the Google Agent Development Kit (ADK), VibeCoder acts as the repository owner, production engineer, and stakeholder-facing deliverer.

The agent leverages large language models (LLMs) to perform planning, documentation, architecture design, implementation, testing, CI/CD setup, versioning, and releases with minimal human intervention.

## Example Use Cases

### 1. Project Initialization
- **Input:** "Initialize a new project for a financial summary dashboard."
- **Output:** Fully scaffolded repository with `src/`, `tests/`, `docs/`, `docker/`, and CI/CD workflows, plus initial design documentation.

### 2. Feature Implementation
- **Input:** "Implement a secure login module with MFA support."
- **Output:** Working code in `src/`, unit and integration tests, updated architecture docs, and a demo record in `docs/demo.md`.

### 3. Release Management
- **Input:** "The current features are stable. Prepare a minor release v1.1.0."
- **Output:** Updated `CHANGELOG.md`, incremented version, verified CI/CD reports, and a published release artifact.

## Tools Required

- **File System Tools:** For creating and modifying project files and directories.
- **Terminal/Shell:** For running commands (`uv`, `make`, `pytest`, `docker`, `terraform`).
- **Git Plugin:** For repository management, branching, and trunk-based development.
- **Docker Tool:** For containerizing applications and running integration tests.
- **GitHub/Cloud Build Integration:** For orchestration of CI/CD pipelines.

## Constraints & Safety Rules

- **Autonomy:** All work MUST be performed inside the Vibe-Coding environment.
- **Milestone Integrity:** Every milestone must be runnable, demo-able, and fully tested.
- **Transparency:** Assumptions must be documented in ADRs (`/docs/adr/`).
- **Git Discipline:** Strictly follow Trunk-Based Development.
- **Security:** Use PRIVATE repositories only. NEVER expose API keys or sensitive data.
- **Approval:** ESCALATE before primary tech stack changes or irreversible architectural decisions.

## Success Criteria

1. **Clean Scaffolding:** 100% compliance with the repository structure defined in `agent-description.md`.
2. **Quality Gates:** 100% test pass rate and ≥80% code coverage.
3. **Automated Release:** Successfully creates a release artifact on version bump.
4. **Documentation:** Every feature is accompanied by updated `README.md`, `architecture.md`, and `demo.md`.

## Edge Cases to Handle

1. **Merge Conflicts:** If a conflict occurs, VibeCoder must autonomously attempt to resolve it or escalate if ambiguous.
2. **CI/CD Failures:** On pipeline failure, VibeCoder must analyze the logs, fix the root cause, and re-trigger the pipeline.
3. **Dependency Conflicts:** If a new dependency breaks the build, VibeCoder must revert or find an alternative version.
4. **Invalid Prompts:** If a request violates safety rules or the "staff-level" persona, VibeCoder must reject it with a clear explanation.
