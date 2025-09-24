from langgraph.prebuilt import create_react_agent
from .prompts import agent_system_prompt

def create_prompt_factory(profile: dict, prompt_instructions: dict):
    def create_prompt(state):
        return [{
            "role": "system",
            "content": agent_system_prompt.format(
                instructions=prompt_instructions["agent_instructions"],
                **profile,
            ),
        }] + state["messages"]
    return create_prompt

def build_agent(model: str, tools: list, create_prompt):
    return create_react_agent(model, tools=tools, prompt=create_prompt)
