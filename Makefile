.PHONY: install test lint playground setup-hooks

install:
	pip install -r requirements.txt
	pip install .

test:
	pytest tests/

lint:
	ruff check .

playground:
	python -m src.vibe_coder.agent

setup-hooks:
	chmod +x scripts/pre-push.sh
	ln -sf ../../scripts/pre-push.sh .git/hooks/pre-push
	@echo "Pre-push hook installed successfully."
