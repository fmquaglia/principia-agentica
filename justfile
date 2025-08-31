# justfile for Principia Agentica

# --- Setup ---
# Creates a new virtual environment using uv
setup:
    uv venv

# Installs dependencies from pyproject.toml into the virtual environment
install:
    uv pip install -e ".[dev]"

# --- Development ---
activate:
    source .venv/bin/activate

# Runs a Jupyter Lab session
lab:
    source .venv/bin/activate && jupyter lab

# --- Quality & Testing ---
# Formats the code using ruff
format:
    uv pip install ruff
    ruff format .

# Lints the code using ruff
lint:
    uv pip install ruff
    ruff check .

# Runs all tests using pytest
test:
    uv pip install pytest
    pytest

# --- TypeScript Implementations ---
# Installs dependencies for the Vercel AI SDK example
ts-install:
    cd vercel-sdk-impl && npm install

# Runs the TypeScript tests
ts-test:
    cd vercel-sdk-impl && npm test
