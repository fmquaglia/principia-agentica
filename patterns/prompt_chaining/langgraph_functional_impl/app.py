import os
from dotenv import load_dotenv
from langgraph.func import entrypoint, task
from typing import TypedDict

load_dotenv()

# The user must have a GEMINI_API_KEY environment variable set for this to work.
if os.getenv("GEMINI_API_KEY") is None:
    print("Please set the GEMINI_API_KEY environment variable.")



# Define workflow state
class State(TypedDict):
    ticket: str
    summary: str
    sentiment: str
    tweet: str

# Node 1: Summarization and Sentiment Extraction
@task
def summarize_and_sentiment(ticket: str):
    # Replace with call to your LLM
    summary = "Extracted summary here."
    sentiment = "Positive"  # or "Neutral"/"Negative"
    return {"summary": summary, "sentiment": sentiment}

# Gate function: only proceed for positive sentiment
def check_positive(summary: str, sentiment: str):
    return "Continue" if sentiment == "Positive" else "Exit"

# Node 2: Tweet Generator
@task
def generate_tweet(summary: str):
    tweet = "Solution-oriented tweet here."
    return {"tweet": tweet}

# Define Workflow Entry Point
@entrypoint()
def centinel_prompt_chain(ticket: str):
    result1 = summarize_and_sentiment(ticket).result()
    if check_positive(result1["summary"], result1["sentiment"]) == "Continue":
        result2 = generate_tweet(result1["summary"]).result()
        return {**result1, **result2}
    else:
        return result1  # No tweet generated

# Example usage
if __name__ == "__main__":
    state = centinel_prompt_chain("Customer reported a login bug yesterday. Fix shipped overnight. User confirmed it’s resolved.").result()
    print(state)
