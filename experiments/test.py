import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

print(f"GOOGLE_API_KEY: {os.getenv('GOOGLE_API_KEY')}")

# Initialize the Gemini Pro model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

# Invoke the model with a prompt
response = llm.invoke("Sing a ballad of LangChain.")
print(response)
