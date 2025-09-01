"""
Functional API implementation for the Prompt Chaining pattern (01_prompt_chaining).

Exports:
- build_functional_app: returns an adapter wrapping the Functional API implementation.

This __init__ supports being imported either as a normal package or loaded directly
via importlib.spec_from_file_location (some tests/tools do this). In the latter case,
relative imports are not available, so we fall back to dynamic loading by file path.
"""
from __future__ import annotations

# First, try normal package-relative import
try:  # pragma: no cover - trivial import branch
    from .functional_app import build_functional_app  # type: ignore
except Exception:  # pragma: no cover - dynamic fallback used in direct-file loading
    import importlib.util
    from pathlib import Path

    _pkg_dir = Path(__file__).parent
    _func_path = _pkg_dir / "functional_app.py"
    _spec = importlib.util.spec_from_file_location(
        "langgraph_functional_impl_app", str(_func_path)
    )
    if _spec is None or _spec.loader is None:
        raise RuntimeError(
            "Failed to load functional_app.py spec in langgraph_functional_impl __init__ fallback"
        )
    _mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)  # type: ignore[attr-defined]
    build_functional_app = _mod.build_functional_app  # type: ignore[assignment]

__all__ = ["build_functional_app"]
