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

def run_shell_command(command: str) -> str:
    """Runs a shell command and returns the output.
    
    Args:
        command: The command string to execute.
    """
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"
