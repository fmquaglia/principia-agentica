"""
LangGraph implementation for the Prompt Chaining pattern (01_prompt_chaining).

Exports:
- build_app: returns a compiled LangGraph application implementing the workflow (Graph API).
- build_functional_app: returns an adapter wrapping the Functional API implementation.

This __init__ supports being imported either as a proper package or loaded directly
via importlib.spec_from_file_location (as done in tests). When loaded directly,
relative imports are not available, so we fall back to dynamic loading by file path.
"""
# First, try normal package-relative imports
try:
    from .app import (
        build_app,
        summarize_and_extract_sentiment,
        generate_tweet,
        check_sentiment,
    )
    from ..langgraph_functional_impl.functional_app import build_functional_app  # type: ignore
except Exception:
    # Fallback for direct execution where relative imports fail
    import importlib.util
    from pathlib import Path

    _pkg_dir = Path(__file__).parent

    # Load app.py
    _app_path = _pkg_dir / "app.py"
    _app_spec = importlib.util.spec_from_file_location("langgraph_impl_app", str(_app_path))
    if _app_spec is None or _app_spec.loader is None:
        raise RuntimeError("Failed to load app.py spec in langgraph_impl __init__ fallback")
    _app_mod = importlib.util.module_from_spec(_app_spec)
    _app_spec.loader.exec_module(_app_mod)  # type: ignore[attr-defined]

    build_app = _app_mod.build_app  # type: ignore[attr-defined]
    summarize_and_extract_sentiment = _app_mod.summarize_and_extract_sentiment  # type: ignore[attr-defined]
    generate_tweet = _app_mod.generate_tweet  # type: ignore[attr-defined]
    check_sentiment = _app_mod.check_sentiment  # type: ignore[attr-defined]

    # Load functional_app.py
    _func_path = _pkg_dir.parent / "langgraph_functional_impl" / "functional_app.py"
    _func_spec = importlib.util.spec_from_file_location("langgraph_impl_functional_app", str(_func_path))
    if _func_spec is None or _func_spec.loader is None:
        raise RuntimeError(
            "Failed to load functional_app.py spec in langgraph_impl __init__ fallback"
        )
    _func_mod = importlib.util.module_from_spec(_func_spec)
    _func_spec.loader.exec_module(_func_mod)  # type: ignore[attr-defined]

    build_functional_app = _func_mod.build_functional_app  # type: ignore[attr-defined]

__all__ = [
    "build_app",
    "summarize_and_extract_sentiment",
    "generate_tweet",
    "check_sentiment",
    "build_functional_app",
]
