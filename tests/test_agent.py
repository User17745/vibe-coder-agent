import pytest
from src.vibe_coder.agent import vibe_coder

def test_agent_initialization():
    """Verifies that the VibeCoder agent is initialized with correct properties."""
    assert vibe_coder.name == "VibeCoder"
    assert "Autonomous Staff-Level Software Engineer" in vibe_coder.description
    assert vibe_coder.model == "gemini-3-flash-preview"

def test_agent_tools():
    """Verifies that the agent has the necessary tools."""
    tool_names = [tool.name for tool in vibe_coder.tools]
    assert "read_file" in tool_names
    assert "write_file" in tool_names
    assert "list_recursive" in tool_names
    assert "run_shell_command" in tool_names

@pytest.mark.asyncio
async def test_agent_instruction():
    """Verifies that the agent instruction is not empty."""
    assert len(vibe_coder.instruction) > 100
    assert "Staff-Level Software Engineer" in vibe_coder.instruction
