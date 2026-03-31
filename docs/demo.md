# Demo - VibeCoder Agent

## Objective
Demonstrate the autonomous capabilities of VibeCoder in a production-grade environment.

## Prerequisites
- **Python 3.10+** (Current: 3.9.6, recommended for full ADK/MCP support).
- **GOOGLE_API_KEY** set in `.env`.
- **Requirements installed:** `pip install -r requirements.txt`.

## Step 1: Agent Initialization
Run the VibeCoder agent locally:
```bash
python3 -m src.vibe_coder.agent
```
**Expected Output:** "VibeCoder agent initialized and ready for execution."

## Step 2: Automated Structure Check
Verify that VibeCoder has correctly scaffolded the repository:
```bash
ls -R src/ tests/ docs/ .github/
```
**Expected Output:** A comprehensive list of files and directories as defined in the `README.md`.

## Step 3: Run Unit Tests
Execute the verification suite:
```bash
python3 -m pytest tests/test_agent.py
```
*(Note: Ensure `pytest` is installed in the current environment).*

## Step 4: Documentation Review
Review the Phase 1 artifacts:
- [Non-Technical Summary](file:///Users/abhishekaggarwal/Projects/Experiments/coding_buddy/docs/summary.md)
- [Technical Roadmap](file:///Users/abhishekaggarwal/Projects/Experiments/coding_buddy/docs/roadmap.md)
- [Architecture Artifacts](file:///Users/abhishekaggarwal/Projects/Experiments/coding_buddy/docs/architecture.md)
- [Technical Specifications](file:///Users/abhishekaggarwal/Projects/Experiments/coding_buddy/docs/specifications.md)
