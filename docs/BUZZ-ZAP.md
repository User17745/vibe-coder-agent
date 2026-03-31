# BUZZ-ZAP.md - Bug Knowledge Base

## Entry Format
- **ID:** BZ-[number]
- **Title:** Brief title
- **Symptom:** What happened?
- **Root Cause:** Why?
- **Fix:** How it was fixed.
- **Detection:** How to detect it again.
- **Linked Test:** Path to regression test.
- **Status:** [Active | Fixed | Resolved]

---

## Active Issues
*None currently.*

## Fixed Issues
- **ID:** BZ-001
- **Title:** Missing Scaffolding Tools
- **Symptom:** `uvx agent-starter-pack` command not found in the environment.
- **Root Cause:** The environment lacks `uv` and the `agent-starter-pack` package.
- **Fix:** Manually implemented the repository structure and agent logic following the ADK guidelines.
- **Detection:** Check for existence of the required directories and files.
- **Linked Test:** N/A (structural check)
- **Status:** Resolved
