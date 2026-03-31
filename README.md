# VibeCoder - Production-Grade Autonomous Vibe Coding Agent

## Overview
VibeCoder is an autonomous Staff-Level Software Engineer and Release Manager designed to handle the entire software development lifecycle (SDLC) for "Vibe-Coded" projects. Built using the Google Agent Development Kit (ADK), it ensures that all development activities—including planning, documentation, architecture, implementation, testing, and CI/CD—are performed autonomously with production-grade quality.

## Project Structure
```text
/src                 → Core application code (VibeCoder agent)
/tests               → Unit, integration, and e2e tests
/docs                → Comprehensive documentation (Summary, Roadmap, Architecture, Specs)
/docs/adr            → Architecture Decision Records
/docker              → Dockerfiles and infrastructure helpers
/scripts             → Automation and developer scripts
/.github/workflows   → CI/CD pipelines (GitHub Actions)
README.md            → This file
.gitignore           → Git exclusion rules
```

## Quick Setup (Developers)
- **Runtime:** Python 3.10+
- **Installation:**
  ```bash
  make install
  ```
- **Configuration:** Create a `.env` file with your `GOOGLE_API_KEY`.
- **Git Hooks:** Initialize local validation hooks:
  ```bash
  make setup-hooks
  ```

## Development & Operations
This project uses a `Makefile` for standard development tasks:
- `make install`: Install dependencies.
- `make test`: Run all tests (Unit, Integration, E2E, Regression).
- `make lint`: Run code analysis (Ruff).
- `make playground`: Launch the VibeCoder agent.
- `make setup-hooks`: Configure pre-push git hooks.

## Testing
Comprehensive testing is enforced:
- **Unit Tests**: Logic verification.
- **Integration Tests**: Core agent and tool belt verification.
- **Regression Tests**: Historical bug tracking (see `BUZZ-ZAP.md`).
- **Coverage**: Minimum 80% coverage required for all pushes.

## CI/CD
All changes pushed to the `main` branch undergo a strict pipeline including linting, building, testing, and version validation. Automated releases are triggered upon version bumps.

## Maintenance & Bugs
Track all historical and active issues in [docs/BUZZ-ZAP.md](file:///Users/abhishekaggarwal/Projects/Experiments/coding_buddy/docs/BUZZ-ZAP.md).

## Demo
Please refer to [docs/demo.md](file:///Users/abhishekaggarwal/Projects/Experiments/coding_buddy/docs/demo.md) for instructions on how to run and verify the agent's capabilities.
