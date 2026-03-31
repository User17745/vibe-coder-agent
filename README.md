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
  source .venv/bin/activate
  pip install -r requirements.txt
  ```
- **Configuration:** Create a `.env` file with your `GOOGLE_API_KEY`.

## Testing
Run all tests using pytest:
```bash
pytest tests/
```

## CI/CD
All changes pushed to the `main` branch undergo a strict pipeline including linting, building, testing, and version validation.

## Deployment
Deployed to **Cloud Run** or **Vertex AI Agent Engine** based on project context.

## Demo
Please refer to [docs/demo.md](file:///Users/abhishekaggarwal/Projects/Experiments/coding_buddy/docs/demo.md) for instructions on how to run and verify the agent's capabilities.
