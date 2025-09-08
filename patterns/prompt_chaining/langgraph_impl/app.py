import os
from dotenv import load_dotenv
from typing import Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, END

from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# The user must have a GEMINI_API_KEY environment variable set for this to work.
if os.getenv("GEMINI_API_KEY") is None:
    print("Please set the GEMINI_API_KEY environment variable.")


class GraphState(TypedDict):
    ticket: str
    summary: str
    sentiment: Literal["Positive", "Negative", "Neutral"]
    tweet: str | None

class SummaryAndSentiment(BaseModel):
    """The summary of the ticket and the sentiment of the user."""

    summary: str = Field(description="A summary of the support ticket.")
    sentiment: Literal["Positive", "Negative", "Neutral"] = Field(
        description="The sentiment of the user who wrote the ticket."
    )

class Tweet(BaseModel):
    """A tweet to be sent out to the user."""

    tweet: str = Field(
        description="A tweet to be sent out to the user, under 280 characters."
    )


def build_app():
    # Initialize the LLM.
    # The user must have a GEMINI_API_KEY environment variable set for this to work.
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        api_key=os.getenv("GEMINI_API_KEY"),
    )

    summarize_and_get_sentiment_prompt = PromptTemplate.from_template(
        """You are an expert at summarizing support tickets and extracting user sentiment.

        Here is the support ticket:
        {ticket}

        Please provide a summary of the ticket and the user's sentiment.
        """
    )

    generate_tweet_prompt = PromptTemplate.from_template(
        """You are an expert at writing empathetic and solution-oriented tweets.

        Here is a summary of a resolved support ticket:
        {summary}

        The user's sentiment was {sentiment}.

        Please draft a tweet (under 280 characters) to announce that the problem has been solved.
        """
    )

    structured_summarizer_llm = llm.with_structured_output(SummaryAndSentiment)
    structured_tweet_llm = llm.with_structured_output(Tweet)

    def summarize_and_get_sentiment(state: GraphState):
        """
        Summarizes the ticket and extracts the user's sentiment.
        """
        response = structured_summarizer_llm.invoke(
            summarize_and_get_sentiment_prompt.format(ticket=state["ticket"])
        )
        return {"summary": response.summary, "sentiment": response.sentiment}

    def generate_tweet(state: GraphState):
        """
        Generates a tweet based on the summary and sentiment.
        """
        response = structured_tweet_llm.invoke(
            generate_tweet_prompt.format(
                summary=state["summary"], sentiment=state["sentiment"]
            )
        )
        return {"tweet": response.tweet}

    def should_generate_tweet(state: GraphState):
        """
        Determines whether to generate a tweet based on the sentiment.
        """
        if state["sentiment"] == "Positive":
            return "generate_tweet"
        else:
            return "__end__"

    # Define the graph
    workflow = StateGraph(GraphState)

    # Add the nodes
    workflow.add_node("summarize_and_get_sentiment", summarize_and_get_sentiment)
    workflow.add_node("generate_tweet", generate_tweet)

    # Set the entrypoint
    workflow.set_entry_point("summarize_and_get_sentiment")

    # Add the conditional edge
    workflow.add_conditional_edges(
        "summarize_and_get_sentiment",
        should_generate_tweet,
    )
    workflow.add_edge("generate_tweet", END)

    # Compile the graph
    return workflow.compile()

if __name__ == "__main__":
    app = build_app()
    print(app)
    state = app.invoke(
        {
            "ticket": "The user reported a porblem with his account. We successfulyly helped him fix a configuration issue."
        }
    )
    print("Initial Ticket")
    print(state["ticket"])
    print("Summary and Sentiment")
    print(state["summary"], state["sentiment"])
    if state["tweet"] is not None:
        print("Tweet")
        print(state["tweet"])
