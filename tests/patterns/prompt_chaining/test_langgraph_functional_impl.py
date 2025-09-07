from patterns.prompt_chaining.langgraph_functional_impl.functional_app import build_functional_app


def test_functional_positive_flow_generates_tweet():
    app = functional_app.build_functional_app()

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


def test_functional_non_positive_exits_without_tweet():
    app = functional_app.build_functional_app()

    ticket = (
        "User reports that the export feature fails intermittently. Logs show timeouts. "
        "No resolution yet. We are investigating and will update."
    )

    result = app.invoke({"ticket": ticket})

    assert result.get("sentiment") in {"Neutral", "Negative"}
    assert "tweet" not in result, "Tweet should not be present for non-positive sentiment"
    assert result.get("summary"), "Summary should be present"
