# CLAUDE.md

This file provides guidance for Claude Code when working in this repository.

## Project Overview

**Principia Agentica** is a practical research and educational project exploring architectural patterns for modern AI agents. It implements key agentic patterns (Prompt Chaining, Evaluator-Optimizer, ACI, Composed Super-Workflow) across multiple frameworks (LangGraph, Google ADK, Vercel AI SDK, LangFlow) and publishes findings via an MkDocs documentation site.

## Repository Structure

```
principia-agentica/
├── patterns/               # Numbered agentic pattern implementations
│   └── 0X_pattern_name/
│       ├── README.md
│       ├── workflow.py     # Core graph/workflow logic
│       ├── nodes.py        # Individual agent nodes (optional)
│       ├── prompts.py      # System prompts and templates
│       └── tests/
│           └── test_workflow.py
├── publication/            # MkDocs documentation site
│   ├── mkdocs.yml
│   └── docs/
│       ├── blog/posts/
│       ├── assets/
│       └── stylesheets/
├── articles/               # Jupyter notebooks for long-form exploration
├── pyproject.toml
├── justfile                # Task runner
└── AGENTS.md               # AI agent conventions (authoritative reference)
```

## Environment & Dependencies

- **Python:** 3.12+ (enforced via `.python-version`)
- **Package manager:** `uv`
- **Key dependencies:** `langgraph`, `mkdocs-material`

```bash
# Initial setup
uv venv
uv pip install -e ".[dev]"

# Or sync from lock file
just sync
```

## Common Commands

```bash
# Tests
pytest                                          # run all tests
pytest path/to/test_file.py -v                 # specific file
pytest path/to/test_file.py::test_name -v      # specific test
pytest -k "pattern" -v                         # match by name

# Linting & formatting
ruff format .
ruff check . --fix
mypy .

# Documentation site
just serve    # serve locally at http://localhost:8000
just build    # build static site
just publish  # deploy via scp

# Jupyter Lab
just lab

# TypeScript (Vercel AI SDK)
just ts-install
just ts-test
```

## Code Style

- Strict type hints on all function signatures and class attributes
- Modern syntax: `list[str]`, `dict[str, Any]`, `X | Y` (not `List`, `Dict`, `Union`)
- `snake_case` for variables/functions, `PascalCase` for classes, `UPPER_SNAKE_CASE` for constants
- Private members prefixed with `_`
- Line length: 100 characters (Ruff-enforced)
- Google-style docstrings for all public modules, classes, and functions
- Group imports: stdlib → third-party → local; no wildcard imports
- Catch specific exceptions only; never bare `except:`
- No hardcoded secrets — use `os.getenv()` or `.env` files

## Key Conventions

- Read a file fully before modifying it
- When adding a new pattern, follow the `patterns/0X_pattern_name/` directory structure above
- After modifying source code, run the relevant tests and linters
- When writing LangGraph code, use StateGraphs and pure functions for nodes
- Use `temperature=0.0` in evaluation/test scripts for deterministic results
- Never hardcode API keys (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, etc.)
- Update `publication/docs/` when adding a new pattern

See [AGENTS.md](./AGENTS.md) for the full authoritative agent instructions.
