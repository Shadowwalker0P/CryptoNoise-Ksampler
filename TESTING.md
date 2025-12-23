# Testing Guide

## Running Tests Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_crypto.py

# Run with verbose output
pytest -v
```

## Coverage Requirements

- Minimum coverage: 70%
- View coverage report: `coverage report`
- Generate HTML coverage report: `coverage html`

## Code Quality
```bash
# Run linter
flake8 . --max-line-length=127

# Format code
black .

# Security scan
bandit -r .
```

## Pre-commit Hooks
```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```
