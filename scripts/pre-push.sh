#!/bin/bash
# Pre-Push Git Hook for VibeCoder
# Ensures lint, build, tests, coverage, and regression validation run successfully.

set -e

echo "=== VibeCoder Pre-Push Validation ==="

echo "1. Running Linter (ruff)..."
ruff check .

echo "2. Validating Build..."
python -m compileall src/

echo "3 & 4. Running Tests & Regression Validation..."
# Run pytest on the entire tests folder (unit, integration, e2e)
python -m pytest tests/

echo "5. Validating Coverage..."
coverage run -m pytest tests/
coverage report --fail-under=80

echo "All Pre-Push validations passed successfully!"
exit 0
