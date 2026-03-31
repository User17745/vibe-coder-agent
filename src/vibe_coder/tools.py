import os
import subprocess
from typing import List, Optional

def read_file(path: str) -> str:
    """Reads the content of a file.
    
    Args:
        path: The absolute or relative path to the file.
    """
    with open(path, 'r') as f:
        return f.read()

def write_file(path: str, content: str) -> str:
    """Writes content to a file. Creates parent directories if they don't exist.
    
    Args:
        path: The absolute or relative path to the file.
        content: The text content to write.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    return f"File written successfully to {path}"

def list_recursive(path: str = '.') -> List[str]:
    """Lists all files in a directory recursively.
    
    Args:
        path: The directory to list. Defaults to the current directory.
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.relpath(os.path.join(root, file), path))
    return file_list

def run_shell_command(command: str, timeout: int = 30) -> str:
    """Runs a shell command and returns the output.
    
    Args:
        command: The command string to execute.
        timeout: Timeout in seconds.
    """
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            check=True,
            timeout=timeout
        )
        return result.stdout or "Success (No Output)"
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"
    except subprocess.TimeoutExpired:
        return f"Error: Command timed out after {timeout} seconds"

def search_files(pattern: str, path: str = '.') -> str:
    """Searches for a regex pattern in files within a directory.
    
    Args:
        pattern: The regex pattern to search for.
        path: The directory to search in.
    """
    try:
        # Use grep -r to find matches
        result = subprocess.run(
            f"grep -rnE '{pattern}' {path} --exclude-dir=.git",
            shell=True,
            capture_output=True,
            text=True
        )
        return result.stdout or "No matches found."
    except Exception as e:
        return f"Error during search: {str(e)}"

def get_git_status() -> str:
    """Returns the current git status of the repository."""
    return run_shell_command("git status")
