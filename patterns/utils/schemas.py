from typing import Literal, TypedDict
from pydantic import BaseModel, Field


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
