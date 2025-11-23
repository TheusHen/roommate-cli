.PHONY: help install dev-install run clean test lint format

help:
	@echo "Roommate CLI - Available commands:"
	@echo "  make install      - Install the package and dependencies"
	@echo "  make dev-install  - Install development dependencies"
	@echo "  make run          - Run the application"
	@echo "  make clean        - Remove build artifacts and cache files"
	@echo "  make test         - Run tests (if available)"
	@echo "  make lint         - Run linting checks"
	@echo "  make format       - Format code with black"

install:
	pip install -r requirements.txt

dev-install: install
	pip install -e ".[dev]"

run:
	python main.py

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	find . -type d -name '*.egg-info' -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ .pytest_cache/ .mypy_cache/

test:
	@echo "No tests configured yet. Add tests in the 'tests' directory."

lint:
	@command -v flake8 >/dev/null 2>&1 && flake8 main.py || echo "flake8 not installed. Run 'make dev-install' first."
	@command -v mypy >/dev/null 2>&1 && mypy main.py || echo "mypy not installed. Run 'make dev-install' first."

format:
	@command -v black >/dev/null 2>&1 && black main.py || echo "black not installed. Run 'make dev-install' first."
