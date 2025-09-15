# justfile for Principia Agentica

set dotenv-load := true

# --- Variables ---
REQUIREMENTS_FILE := "requirements.txt"

# --- Setup ---
# Creates a new virtual environment using uv
setup:
    uv venv

# Installs dependencies from pyproject.toml into the virtual environment
install:
    uv pip install -e ".[dev]"

# Lock the project dependencies into a requirements.txt file
lock:
    @echo "Locking dependencies from pyproject.toml -> {{REQUIREMENTS_FILE}}..."
    @uv pip compile pyproject.toml -o {{REQUIREMENTS_FILE}}
    @echo "✅ Dependencies locked."

# Sync the virtual environment with the lock file
sync:
    @echo "Syncing environment with {{REQUIREMENTS_FILE}}..."
    @uv pip sync {{REQUIREMENTS_FILE}}
    @echo "✅ Environment synced."

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

# --- Website ---
serve:
    @just sync
    cd publication && mkdocs serve

build:
    @just sync
    cd publication && mkdocs build

publish:
    @just build
    sshpass -e scp -r publication/site/* $SSH_USER@$SITE_HOST:$SITE_PATH
