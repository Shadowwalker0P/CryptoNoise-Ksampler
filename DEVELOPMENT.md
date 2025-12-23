# Development Guide

## Setup Development Environment
```bash
# Clone the repository
git clone https://github.com/Shadowwalker0P/CryptoNoise-Ksampler
cd CryptoNoise-Ksampler

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install in editable mode with dev dependencies
pip install -e .
pip install -r requirements.txt
```

## Running CI/CD Locally
```bash
# Install GitHub Actions runner (optional)
# See: https://docs.github.com/en/actions/hosting-your-own-runners

# Or simulate locally with act:
# brew install act
# act push
```

## Code Style

- Use Black for formatting
- Follow PEP8 standards
- Maximum line length: 127 characters
- Type hints are recommended

## Submitting Changes

1. Create a feature branch
2. Make changes and test thoroughly
3. Ensure all tests pass: `pytest`
4. Ensure coverage meets minimum: `coverage report --fail-under=70`
5. Push and open a pull request
