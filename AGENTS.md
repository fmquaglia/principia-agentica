# Agent Instructions (`AGENTS.md`)

Welcome to the `principia-agentica` repository. You are an autonomous AI coding agent operating in this codebase. Your primary directive is to assist the user in building, exploring, and documenting architectural patterns for modern AI agents across various frameworks (e.g., LangGraph, Vercel AI SDK, LangFlow).

Please adhere strictly to the rules, commands, and conventions outlined in this document. These instructions form the baseline for your operations here.

---

## 1. Build, Lint, and Test Commands

We use standard, modern Python tooling. Ensure you run the appropriate checks before concluding any task to maintain repository health.

### Environment Setup
- This project uses **Python >= 3.12** (enforced via `.python-version`).
- The preferred package manager is **`uv`**. Install the project and its dependencies:
  ```bash
  uv venv                    # create virtual environment
  uv pip install -e ".[dev]" # install project + dev extras
  just sync                  # alternatively, sync from requirements.txt lock file
  ```

### Testing Workflow (Pytest)
We use `pytest` for all unit and integration testing.

- **Run all tests in the repository:**
  ```bash
  pytest
  ```
- **Run a specific test file:**
  ```bash
  pytest path/to/test_file.py -v
  ```
- **Run a single test function (crucial for targeted debugging):**
  ```bash
  pytest path/to/test_file.py::test_function_name -v
  ```
- **Run tests matching a specific string or pattern:**
  ```bash
  pytest -k "pattern_name" -v
  ```

*Agent Rule:* Always run the relevant tests after modifying any source code. If you implement a new architectural pattern, you MUST write an accompanying test to verify its functionality.

### Linting & Formatting (Ruff)
We use `ruff` for extremely fast, uncompromising linting and formatting.

- **Format code automatically:**
  ```bash
  ruff format .
  ```
- **Lint code (and apply auto-fixable errors):**
  ```bash
  ruff check . --fix
  ```

*Agent Rule:* Never leave formatting or linting errors in the codebase. Run these commands before declaring your task complete.

### Type Checking (Mypy)
- **Run static type checks:**
  ```bash
  mypy .
  ```

---

## 2. Code Style & Architecture Guidelines

Because this repository serves as an educational and practical exploration of AI agent architectures, clarity, readability, and consistency are our highest priorities.

### Python Version & Typing
- Assume Python 3.12+.
- **Strict Type Hinting:** You must use type hints for ALL function signatures (arguments and return types) and class attributes.
- Use modern type syntax: `list[str]` instead of `List[str]`, `dict[str, Any]` instead of `Dict`, and `X | Y` instead of `Union[X, Y]`.
- Avoid `Any` unless strictly necessary (e.g., when dealing with highly dynamic, unstructured LLM JSON outputs).

### Naming Conventions
- **Variables, Functions, & Methods:** `snake_case` (e.g., `execute_prompt_chain`, `agent_state`).
- **Classes:** `PascalCase` (e.g., `EvaluatorOptimizer`, `AgentWorkflow`).
- **Constants:** `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`, `DEFAULT_MODEL_NAME`).
- **Private Attributes/Methods:** Prefix with a single underscore (e.g., `_internal_state`, `_process_response()`).

### Imports
- Group imports logically with empty lines between groups:
  1. Standard library imports (e.g., `import os`, `import json`).
  2. Third-party imports (e.g., `from langgraph.graph import StateGraph`).
  3. Local application imports (e.g., `from patterns.common import utils`).
- Use absolute imports over relative imports where possible.
- Avoid wildcard imports (`from module import *`) at all costs.

### Error Handling
- Never use bare `except:` clauses. Always catch specific exceptions (e.g., `except KeyError:`, `except httpx.HTTPError:`).
- Raise descriptive exceptions. Create custom exception classes for domain-specific errors (e.g., `class LLMResponseError(Exception): pass`).
- Log errors contextually rather than silently swallowing them.

### Formatting & Structure
- Limit line length to 100 characters (this will be enforced by Ruff).
- Use modular design. Keep files small and focused on a single pattern, node, or component.
- Separate prompts from execution logic. Store complex system prompts in separate text files, Markdown, or dedicated constants modules.

### Comments & Documentation
- **Docstrings:** Use Google-style docstrings for all modules, classes, and public functions. Briefly explain what the function does, its arguments (`Args:`), and return values (`Returns:`).
- **Inline Comments:** Focus strictly on the *why*, not the *what*. Explain complex LLM orchestration logic, tricky workarounds, or unintuitive framework quirks.
- **Markdown Docs:** This project uses MkDocs (Material theme). When you add a new pattern, ensure you update or create the corresponding `.md` file in the `publication/docs/` directory.

---

## 3. Repository Structure & Adding New Patterns

Top-level layout:

```
principia-agentica/
├── patterns/               # Numbered agentic pattern implementations
├── publication/            # MkDocs documentation site
│   ├── mkdocs.yml
│   └── docs/
│       ├── blog/posts/
│       ├── assets/
│       └── stylesheets/
├── articles/               # Jupyter notebooks for long-form exploration
├── pyproject.toml
└── justfile                # Task runner
```

This repository is organized around specific architectural patterns (e.g., `patterns/01_prompt_chaining/`). When generating a new pattern, follow this standard structure:

```text
patterns/0X_pattern_name/
├── README.md         # Explains the pattern, use cases, and framework trade-offs
├── workflow.py       # Core implementation logic (e.g., LangGraph graph definition)
├── nodes.py          # (Optional) Individual agent nodes/functions
├── prompts.py        # System prompts and templates
└── tests/
    └── test_workflow.py # Tests ensuring the pattern executes correctly
```

### Task Runner (just)
Common workflows are automated via `justfile`. Prefer these over running tools directly:

```bash
# Setup
just sync           # sync environment from requirements.txt

# Development
just lab            # launch Jupyter Lab

# Testing & Quality
just test           # run all tests with pytest
just format         # ruff format .
just lint           # ruff check .

# Documentation site
just serve          # serve locally at http://localhost:8000
just build          # build static site
just publish        # deploy via scp

# TypeScript (Vercel AI SDK)
just ts-install     # npm install in vercel-sdk-impl/
just ts-test        # npm test in vercel-sdk-impl/
```

### Documentation Workflow
To preview documentation locally while modifying MkDocs files:
```bash
just serve
```

---

## 4. Core Mandates for Agentic Operations

1. **Context First:** Before modifying a file, read it entirely using your read tools. Understand its dependencies and how it fits into the broader architecture.
2. **Framework Alignment:** When writing LangGraph code, strictly follow LangGraph paradigms (StateGraphs, pure functions for nodes, deterministic state updates). Do not mix paradigms across frameworks unless instructed.
3. **Reproducibility:** AI outputs are stochastic. When writing evaluation or test scripts for the patterns, ensure you use lower temperatures (`temperature=0.0`) or seeded models where applicable to make tests deterministic.
4. **No Destructive Operations:** Do not delete large directories, wipe Git history, or execute arbitrary `rm -rf` operations without explicit user confirmation.
5. **No Secrets in Code:** Never hardcode API keys (e.g., `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`). Always load them from environment variables or `.env` files using `os.getenv()`.
6. **Self-Correction Loop:** If a test fails or a linter throws an error after you've made a change, read the error message carefully, reason about the root cause, and implement a fix before returning control to the user. Do not give up after one failure.