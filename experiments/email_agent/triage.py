from pydantic import BaseModel, Field
from typing_extensions import Literal
from langchain.chat_models import init_chat_model
from .prompts import triage_system_prompt, triage_user_prompt

class Router(BaseModel):
    reasoning: str = Field(description="Step-by-step reasoning behind the classification.")
    classification: Literal["ignore", "respond", "notify"]

llm = init_chat_model("google_genai:gemini-2.5-pro")
llm_router = llm.with_structured_output(Router)

def build_triage_messages(profile: dict, prompts, email_input: dict, examples=None):
    system_prompt = triage_system_prompt.format(
        full_name=profile["full_name"],
        name=profile["name"],
        user_profile_background=profile["user_profile_background"],
        triage_no=prompts["triage_rules"]["ignore"],
        triage_notify=prompts["triage_rules"]["notify"],
        triage_email=prompts["triage_rules"]["respond"],
        examples=examples,
    )
    user_prompt = triage_user_prompt.format(
        author=email_input["author"],
        to=email_input["to"],
        subject=email_input["subject"],
        email_thread=email_input["email_thread"],
    )
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

def run_triage(messages) -> Router:
    result = llm_router.invoke(messages)
    print(f"📬 TRIAGE → {result.classification}")
    return result
