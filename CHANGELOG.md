# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2026-03-31
### Added
- Integrated regression testing framework and historical bug tracking linked to `BUZZ-ZAP.md`.
- Multi-tier testing structure (Unit, Integration, E2E, Regression).
- Standardized `Makefile` for developer operations and hook setup.
- Automated Docker build verification job in CI.
- Enhanced, production-hardened `Dockerfile`.
- Comprehensive documentation audit and v1.2.0 finalization.

## [1.1.0] - 2026-03-31
### Added
- Enhanced tool belt: `search_files` and `get_git_status` for better code orchestration.
- Autonomous SEMVER logic in `src/vibe_coder/semver.py`.
- Refined agent instructions for full SDLC autonomy.
- Unit tests for versioning logic.
- Robust CI/CD workflow fixes.

## [1.0.0] - 2026-03-31
### Added
- Initial setup for VibeCoder agent using Google ADK.
- File system and shell command tools for agentic workflow execution.
- Phase 1 Architecture, Technical roadmap, and specifications documentation.
- Dockerfile, CI workflow, and Makefile orchestration.
