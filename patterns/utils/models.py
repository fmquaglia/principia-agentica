import os
from langchain_google_genai import ChatGoogleGenerativeAI

from .schemas import SummaryAndSentiment, Tweet


def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        api_key=os.getenv("GEMINI_API_KEY"),
    )

def get_structured_summarizer(llm):
    """Returns an LLM configured to output the SummaryAndSentiment schema."""
    return llm.with_structured_output(SummaryAndSentiment)

def get_structured_tweeter(llm):
    """Returns an LLM configured to output the Tweet schema."""
    return llm.with_structured_output(Tweet)
