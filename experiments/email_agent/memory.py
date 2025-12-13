from langgraph.store.memory import InMemoryStore

store = InMemoryStore(
    index={"embed": "google_vertexai:gemini-embedding-001"}
)
