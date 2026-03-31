# Technical Specifications - VibeCoder

## Components List
1.  **VibeCoder Agent Core:** ADK application (`google.adk`) that handles task orchestration.
2.  **LLM Support:** Gemini 3 Pro/Flash for planning and code generation.
3.  **Tool Belt:**
    - **FS-Tool:** For file system operations (Search, Read, Write, Rename).
    - **Shell-Tool:** For running local commands (make, test, lint).
    - **Git-Tool:** For automated versioning and trunk-based workflows.
    - **Docker-Tool:** For building and testing containers.
4.  **Logging & Observability:** ADK observability for tracking agent steps and LLM token usage.

## Algorithms & Patterns
- **Trunk-Based Development (TBD):** Always push to `main` branch with pre-push quality checks.
- **Semantic Versioning (SEMVER):** Autonomous version calculation based on commit message intent.
- **Milestone-Driven Workflow:** Work is partitioned into deployable milestones with clear Definition of Done (DoD).
- **Quality Gates:** 100% test pass and mandatory documentation updates.

## Tooling Stack
- **Framework:** [Google ADK](https://github.com/google/adk) (Python).
- **Runtime:** Python 3.10+ (Current: 3.9.6, upgrade recommended for production).
- **Environment Management:** `uv` or `pip`.
- **Containers:** Docker.
- **CI/CD:** GitHub Actions.
- **Testing:** Pytest, Ruff (Linting).
- **Documentation:** Markdown with Mermaid.

## Security & compliance
- **Private Repositories:** Strictly enforced.
- **Sensitive Data:** All keys and secrets must be injected via environment variables (e.g., `GOOGLE_API_KEY`).
- **Gated Decisions:** Human intervention is required for tech stack or primary architecture changes.
