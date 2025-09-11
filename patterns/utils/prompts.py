from langchain_core.prompts import PromptTemplate

def summarize_and_get_sentiment_prompt():
    return PromptTemplate.from_template(
        """You are an expert at summarizing support tickets and extracting user sentiment.
    
        Here is the support ticket:
        {ticket}
    
        Please provide a summary of the ticket and the user's sentiment.
        """
    )

def generate_tweet_prompt():
    return PromptTemplate.from_template(
        """You are an expert at writing empathetic and solution-oriented tweets.

        Here is a summary of a resolved support ticket:
        {summary}
    
        The user's sentiment was {sentiment}.
    
        Please draft a tweet (under 280 characters) to announce that the problem has been solved.
        """
    )
