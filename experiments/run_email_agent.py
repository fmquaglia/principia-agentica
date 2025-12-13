import os, argparse
from dotenv import load_dotenv
from email_agent import profile, prompts as pr, tools as t, graph as g, hooks

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--author", required=True)
    ap.add_argument("--to", required=True)
    ap.add_argument("--subject", required=True)
    ap.add_argument("--body", required=True)
    ap.add_argument("--model", default=os.getenv("MODEL", "google_genai:gemini-2.5-pro"))
    ap.add_argument("--user_id", default="fabricio")
    return ap.parse_args()

def main():
    args = parse_args()
    load_dotenv()
    h = hooks.MemoryHooks()
    toolset = t.tools()
    graph = g.build_email_agent(profile.profile, pr.prompt_instructions, toolset, h, model=args.model)
    email_input = {
        "author": args.author,
        "to": args.to,
        "subject": args.subject,
        "email_thread": args.body,
    }
    _ = graph.invoke(
        {"email_input": email_input},
        config={
            "configurable": {
                "langgraph_user_id": args.user_id
            }
        }
    )
    print("✅ done")

if __name__ == "__main__":
    main()
