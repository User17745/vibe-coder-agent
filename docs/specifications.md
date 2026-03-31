# Technical Specifications - VibeCoder

## Components List
1.  **VibeCoder Agent Core:** ADK application (`google.adk`) that handles task orchestration.
2.  **LLM Support:** Gemini 3 Pro/Flash for planning and code generation.
3.  **Tool Belt:**
    - **FS-Tool:** For file system operations (`read_file`, `write_file`, `list_recursive`).
    - **Search-Tool:** For regex codebase analysis (`search_files`).
    - **Shell-Tool:** For running local commands (`run_shell_command`).
    - **Git-Tool:** For repository state and versioning (`get_git_status`, `SEMVER`).
4.  **SEMVER Orchestrator:** Logic for autonomous version calculation (`src/vibe_coder/semver.py`).
5.  **Logging & Observability:** ADK observability for tracking agent steps and LLM token usage.

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
