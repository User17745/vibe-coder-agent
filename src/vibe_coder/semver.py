import re
from typing import Optional

def calculate_next_version(current_version: str, bump_type: str) -> str:
    """Calculates the next version string based on SEMVER rules.
    
    Args:
        current_version: The current version string (e.g. "1.0.0").
        bump_type: One of "patch", "minor", "major".
    """
    major, minor, patch = map(int, current_version.split('.'))
    
    if bump_type.lower() == "major":
        major += 1
        minor = 0
        patch = 0
    elif bump_type.lower() == "minor":
        minor += 1
        patch = 0
    elif bump_type.lower() == "patch":
        patch += 1
    else:
        raise ValueError(f"Invalid bump type: {bump_type}")
        
    return f"{major}.{minor}.{patch}"

def suggest_bump_type(task_description: str) -> str:
    """Suggests a SEMVER bump type based on the task description.
    
    Args:
        task_description: A description of the changes made.
    """
    # Simple regex based suggestion
    if re.search(r"break|major|rewrite|overhaul", task_description, re.IGNORECASE):
        return "major"
    if re.search(r"add|feature|new|capability", task_description, re.IGNORECASE):
        return "minor"
    return "patch"
