import pytest
from src.vibe_coder.agent import vibe_coder

def test_vibe_coder_initialization():
    """Integration test: Ensures vibe_coder agent is correctly configured."""
    assert vibe_coder.name == "VibeCoder"
    assert "Autonomous Staff-Level" in vibe_coder.description
    assert len(vibe_coder.tools) >= 5
    
    tool_names = [tool.name for tool in vibe_coder.tools]
    assert "read_file" in tool_names
    assert "get_git_status" in tool_names
    assert "search_files" in tool_names

@pytest.mark.asyncio
async def test_vibe_coder_instruction_validation():
    """Integration test: Ensures instructions contain core SEMVER and SDLC principles."""
    assert "SEMVER" in vibe_coder.instruction
    assert "Staff-Level" in vibe_coder.instruction
    assert "Mandatory Project Structure" in vibe_coder.instruction
