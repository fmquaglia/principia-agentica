import os
import typer
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from patterns.utils.schemas import GraphState
from patterns.utils.models import get_llm
from patterns.utils.nodes import summarize_and_get_sentiment, generate_tweet

load_dotenv()

def should_generate_tweet(state: GraphState):
    """
    Determina si debemos generar un tweet.
    Nuestra puerta (gate) que dirige el flujo del grafo.
    """
    if state["sentiment"] == "Positive":
        # Si el sentimiento es positivo, continuamos al nodo 'generate_tweet'
        return "generate_tweet"
    else:
        # De lo contrario, el flujo termina aquí
        return END

def build_graph():
    """
    Construye y compila el grafo de LangGraph.
    Esta función es el corazón de la orquestación.
    """

    llm = get_llm()

    summarizer_with_llm = summarize_and_get_sentiment.bind(llm=llm)
    tweet_generator_with_llm = generate_tweet.bind(llm=llm)
    # Define el grafo con nuestro estado compartido
    workflow = StateGraph(GraphState)

    # 1. Añade los nodos
    #    Cada nodo es una función que realiza una acción.
    #    El segundo argumento es el nombre que usaremos para referirnos a él en el grafo.
    workflow.add_node("summarizer", summarizer_with_llm)
    workflow.add_node("tweet_generator", tweet_generator_with_llm)

    # 2. Define las aristas (las conexiones entre nodos)
    #    Esto define el flujo de control.

    # El grafo siempre comenzará en el nodo 'summarizer'
    workflow.set_entry_point("summarizer")

    # Después del nodo 'summarizer', tomaremos una decisión...
    workflow.add_conditional_edges(
        "summarizer",
        should_generate_tweet,
        {
            # Si la función 'should_generate_tweet' devuelve "generate_tweet", vamos a ese nodo.
            "generate_tweet": "tweet_generator",
            # Si devuelve END (o "__end__"), el grafo termina.
            END: END
        }
    )

    workflow.add_edge("tweet_generator", END)

    return workflow.compile(checkpointer=None)


def main(
        ticket: str = typer.Argument(
            ..., # El "..." lo hace un argumento obligatorio
            help="The support ticket text to process."
        )
):
    """
    Summarizes a support ticket, extracts sentiment, and generates a tweet if positive.
    """
    # Construye la aplicación del grafo
    app = build_graph()

    # Define el input inicial
    initial_input = {"ticket": ticket}

    print("🚀 Invoking the agent with the ticket...")

    # Invoca el grafo con el input
    final_state = app.invoke(initial_input)

    print("\n--- Initial Ticket ---")
    print(final_state["ticket"])

    print("\n--- Summary and Sentiment ---")
    print(f"Summary: {final_state['summary']}")
    print(f"Sentiment: {final_state['sentiment']}")

    if final_state.get("tweet"):
        print("\n--- Generated Tweet ---")
        print(final_state["tweet"])

    print("\n✅ Process finished.")


if __name__ == "__main__":
    typer.run(main)
