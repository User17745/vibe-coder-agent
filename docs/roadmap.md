# Technical Roadmap - VibeCoder

## Milestone 1: Foundation (Current)
* **Goal:** Scaffolding and baseline documentation.
* **Scope:**
    * [x] Project structure initialization.
    * [x] Non-Technical Project Summary creation.
    * [/] Technical Roadmap creation.
    * [ ] Architecture and Specifications artifacts.
    * [ ] Infrastructure (Docker, .github/workflows) setup.
* **Functional Requirements:** Valid repo structure per `agent-description.md`.
* **Deployment & Demo:** Local structure check.

## Milestone 2: Core Agent Implementation
* **Goal:** A robust Staff-Level VibeCoder agent.
* **Scope:**
    * Implement `src/vibe_coder/agent.py` using `google.adk`.
    * Configure LLM tools for file operations and CLI.
    * Define prompt templates for task execution.
    * Implement SEMVER logic for releases.
* **Automated Tests:** Unit tests for agent logic and tools.
* **Deployment & Demo:** Initial walkthrough on a sample feature.

## Milestone 3: Quality Gates & CI/CD
* **Goal:** 100% automated verification.
* **Scope:**
    * Integration tests with Docker.
    * GitHub Actions pipeline setup (Lint, Build, Test, Coverage).
    * Bug Knowledge Base (`BUZZ-ZAP.md`) integration.
    * Lighthouse CI (if applicable).
* **Automated Tests:** Comprehensive integration and E2E tests.
* **Deployment & Demo:** Fully automated PR approval flow.

## Milestone 4: Production Release
* **Goal:** First stable release.
* **Scope:**
    * Final audit of documentation.
    * Secure deployment to Cloud Run.
    * Implementation of CD pipeline.
* **Non-Functional Requirements:** 100% test pass, >=80% coverage.
* **Automated Tests:** Full regression suite.
* **Deployment & Demo:** v1.0.0 release.
