import os
import pytest

def test_bz001_scaffolding_structure():
    """Regression test for BZ-001: Ensures core project structure is preserved."""
    required_dirs = [
        "src",
        "tests",
        "docs",
        "docs/adr",
        "docker",
        "scripts",
        ".github/workflows",
    ]
    required_files = [
        "README.md",
        ".gitignore",
        "Makefile",
        "requirements.txt",
        "src/vibe_coder/agent.py",
        "src/vibe_coder/tools.py",
        "docs/BUZZ-ZAP.md",
        "docs/roadmap.md",
    ]
    
    for d in required_dirs:
        assert os.path.isdir(d), f"Missing required directory: {d}"
        
    for f in required_files:
        assert os.path.isfile(f), f"Missing required file: {f}"

def test_bz001_adk_installed():
    """Regression test for BZ-001: Ensures ADK is discoverable."""
    try:
        import google.adk
    except ImportError:
        pytest.fail("google-adk package is not installed.")
