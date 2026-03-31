import pytest
from src.vibe_coder.semver import calculate_next_version, suggest_bump_type

def test_calculate_next_version_patch():
    assert calculate_next_version("1.0.0", "patch") == "1.0.1"

def test_calculate_next_version_minor():
    assert calculate_next_version("1.0.0", "minor") == "1.1.0"

def test_calculate_next_version_major():
    assert calculate_next_version("1.0.0", "major") == "2.0.0"

def test_suggest_bump_type():
    assert suggest_bump_type("Fixed a bug in auth") == "patch"
    assert suggest_bump_type("Add new tool for search") == "minor"
    assert suggest_bump_type("Overhaul architecture for scale") == "major"
