from __future__ import annotations

import importlib.util
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
MODULE_FILE = PROJECT_ROOT / "patterns" / "01_prompt_chaining" / "langgraph_impl" / "app.py"


def load_langgraph_impl():
    spec = importlib.util.spec_from_file_location("langgraph_impl_app", str(MODULE_FILE))
    if spec is None or spec.loader is None:
        raise RuntimeError("Failed to load langgraph_impl app module spec")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


def test_positive_flow_generates_tweet():
    m = load_langgraph_impl()
    app = m.build_app()

    ticket = (
        "Customer reported login bug yesterday. Our team deployed a fix overnight. "
        "User confirmed it's resolved this morning and said thanks for the quick response!"
    )

    result = app.invoke({"ticket": ticket})

    assert result.get("sentiment") == "Positive"
    assert "tweet" in result, "Tweet should be generated for positive sentiment"
    assert isinstance(result["tweet"], str)
    assert len(result["tweet"]) <= 280
    assert result.get("summary"), "Summary should be present"


def test_non_positive_exits_without_tweet():
    m = load_langgraph_impl()
    app = m.build_app()

    ticket = (
        "User reports that the export feature fails intermittently. Logs show timeouts. "
        "No resolution yet. We are investigating and will update."
    )

    result = app.invoke({"ticket": ticket})

    assert result.get("sentiment") in {"Neutral", "Negative"}
    assert "tweet" not in result, "Tweet should not be present for non-positive sentiment"
    assert result.get("summary"), "Summary should be present"
