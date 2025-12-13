from typing_extensions import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph import add_messages
from langgraph.types import Command
from typing import Literal
from .triage import build_triage_messages, run_triage
from .agent import build_agent, create_prompt_factory
from .memory import store

class State(TypedDict):
    email_input: dict
    messages: Annotated[list, add_messages]

def build_email_agent(profile: dict, prompt_instructions: dict, toolset: list, hooks, model: str):
    def triage_router(state: State) -> Command[Literal["response_agent", "__end__"]]:
        msgs = build_triage_messages(profile, prompt_instructions, state["email_input"], examples=None)
        result = run_triage(msgs)
        if result.classification == "respond":
            goto = "response_agent"
            update = {
                "messages": [{
                    "role": "user",
                    "content": f"Respond to the email {state['email_input']}",
                }]
            }
        elif result.classification in ("ignore", "notify"):
            update = None
            goto = END
        else:
            raise ValueError(f"Invalid classification: {result.classification}")
        return Command(goto=goto, update=update)

    g = StateGraph(State)
    g = g.add_node("triage_router", triage_router)
    agent = build_agent(model, toolset, create_prompt_factory(profile, prompt_instructions), store)
    g = g.add_node("response_agent", agent)
    g = g.add_edge(START, "triage_router")
    return g.compile()
