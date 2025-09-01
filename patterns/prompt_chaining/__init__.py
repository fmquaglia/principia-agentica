"""
Import-friendly alias for the 01_prompt_chaining implementation.

Why: Python cannot import a package name starting with a digit (e.g.,
`patterns.01_prompt_chaining...`). This module provides a stable import path:

    from patterns.prompt_chaining import build_app

which loads and re-exports the existing implementation at
patterns/01_prompt_chaining/langgraph_impl/app.py
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Any

# Resolve the existing file-based implementation
_THIS_DIR = Path(__file__).resolve().parent
_APP_FILE = _THIS_DIR.parent / "01_prompt_chaining" / "langgraph_impl" / "app.py"

if not _APP_FILE.exists():
    raise FileNotFoundError(f"Expected implementation at {_APP_FILE} not found")

_spec = importlib.util.spec_from_file_location(
    "patterns_prompt_chaining_impl", str(_APP_FILE)
)
if _spec is None or _spec.loader is None:
    raise ImportError("Failed to create spec for prompt_chaining implementation")

_module: ModuleType = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)  # type: ignore[attr-defined]

# Re-export the public API we want to expose
build_app = getattr(_module, "build_app")  # type: ignore[assignment]

__all__ = ["build_app"]
