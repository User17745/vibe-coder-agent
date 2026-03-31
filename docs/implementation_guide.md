# VibeCoder Implementation Guide

This guide details how the **VibeCoder** agent is architected using the Google Agent Development Kit (ADK) and provides instructions on how to extend its capabilities.

## 1. Architectural Overview

VibeCoder is designed as a "Staff-Level Software Engineer" that autonomously handles the Software Development Lifecycle (SDLC). It is built on three main pillars:
1.  **Orchestration Engine:** Built using `google-adk`, leveraging `gemini-3-flash-preview` / `gemini-3.1-pro` for reasoning.
2.  **Tool Belt:** Custom Python functions wrapped as ADK tools to interact with the local filesystem, shell, and git.
3.  **Strict Policy Guardrails:** Persona instructions injected into the agent prompt, forcing it to follow Trunk-Based Development, SEMVER, and Milestone-driven execution.

## 2. Core Agent Implementation (`agent.py`)

The heart of the agent resides in `src/vibe_coder/agent.py`. It initializes the ADK `Agent` class:

```python
from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool
from .tools import read_file, write_file, list_recursive, run_shell_command, get_git_status, search_files

# 1. Define Persona & Guardrails
VIBECODER_INSTRUCTIONS = """
You are VibeCoder, an Autonomous Staff-Level Software Engineer & Release Manager...
"""

# 2. Wrap basic Python functions into ADK Tools
tools = [
    FunctionTool(func=read_file),
    FunctionTool(func=write_file),
    FunctionTool(func=run_shell_command),
    # ...
]

# 3. Instantiate Agent
vibe_coder = Agent(
    model='gemini-3-flash-preview', # Or your preferred model
    name='VibeCoder',
    description='Autonomous Staff-Level Software Engineer & Release Manager',
    instruction=VIBECODER_INSTRUCTIONS,
    tools=tools,
)
```

## 3. Creating and Registering Tools (`tools.py`)

Tools are simple Python functions with clear docstrings and type hinting. The ADK uses the signature and docstring to expose the tool to the LLM.

**Example: Adding a new tool**

1.  **Define the function in `tools.py`:**
    ```python
    import subprocess

    def run_formatter(path: str = ".") -> str:
        """Runs the Ruff formatter on the specified path.
        
        Args:
            path: Target directory or file to format.
        """
        try:
            result = subprocess.run(f"ruff format {path}", shell=True, capture_output=True, text=True, check=True)
            return result.stdout or "Formatting successful."
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"
    ```
2.  **Register the tool in `agent.py`:**
    ```python
    from .tools import run_formatter
    
    tools.append(FunctionTool(func=run_formatter))
    ```

## 4. Semantic Versioning Integration (`semver.py`)

VibeCoder calculates versions autonomously using helper functions in `semver.py`. 
When the LLM decides a feature requires a minor bump, it calls internal tools or uses its reasoning engine alongside the `suggest_bump_type` logic to update `src/vibe_coder/version.py`. This change is then picked up by the GitHub Actions `release.yml` workflow to trigger a deployment artifact.

## 5. Testing the Agent (`tests/`)

We enforce a strict testing policy (Unit, Integration, E2E, Regression):

-   **Unit Tests (`tests/unit/`)**: Quick checks testing logic like `semver.py` or `tools.py` independently of the LLM.
-   **Integration Tests (`tests/integration/`)**: Validating that `vibe_coder` instantiates correctly, has the right tools bounded, and parsing the `VIBECODER_INSTRUCTIONS`.
-   **Regression Tests (`tests/regression/`)**: Enforcing bug fixes. For example, ensuring the mandatory repository structure is present (referencing `BUZZ-ZAP.md`).

Execute tests via:
```bash
make test
```

## 6. CI/CD & Guardrails

VibeCoder's autonomy is counterbalanced by strict CI/CD pipelines (`.github/workflows/ci.yml`).
The agent **must** pass the following hooks before its code is merged/released:
1.  **Lint / Build**: `ruff check .` and `python -m compileall src/`
2.  **Test / Coverage**: `pytest` and `coverage report --fail-under=80`
3.  **Version Validation**: Ensures `version.py` changes if new features were added.

## 7. Extending VibeCoder

To extend VibeCoder for your organization:
1.  **New Capabilities**: Add tools for Jira automation, Slack notifications, or AWS deployment.
2.  **Rule Changes**: Edit `VIBECODER_INSTRUCTIONS` to alter its definition of done (DoD) or framework preferences.
3.  **Infrastructure Plugins**: Add new GitHub workflows or Docker compose setups into the scaffolding requirements.
