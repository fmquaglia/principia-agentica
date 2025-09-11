from .prompts import summarize_and_get_sentiment_prompt, generate_tweet_prompt
from .schemas import GraphState
from .models import get_structured_summarizer, get_structured_tweeter


def summarize_and_get_sentiment(state: GraphState, llm):
    """
    Summarizes the ticket and extracts the user's sentiment.
    """
    summarizer = get_structured_summarizer(llm)
    prompt = summarize_and_get_sentiment_prompt().format(ticket=state["ticket"])
    response = summarizer.invoke(prompt)

    return {"summary": response.summary, "sentiment": response.sentiment}


def generate_tweet(state: GraphState, llm):
    """
    Generates a tweet based on the summary and sentiment.
    """
    tweeter = get_structured_tweeter(llm)
    prompt = generate_tweet_prompt().format(
        summary=state["summary"], sentiment=state["sentiment"]
    )
    response = tweeter.invoke(prompt)

    return {"tweet": response.tweet}
