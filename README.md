# Principia Agentica

A practical exploration into the architectural patterns of modern AI agents.

## About This Project

The world of AI agents is exploding with new frameworks, tools, and techniques. While exciting, it can be challenging to
navigate this rapidly changing landscape. Inspired by the foundational patterns outlined in Anthropic's excellent
article, ["Building effective agents"](https://www.anthropic.com/engineering/building-effective-agents), this repository is my journey to bridge the gap between theory and practice.

My goal is to implement key agentic patterns across several popular frameworks, not just to see *if* they can be built,
but to understand *how* they feel to build, maintain, and adapt. This is an exploration of architecture, developer
experience (DevEx), and the practical trade-offs we face as builders.

## What You'll Find Inside

* **Practical Implementations:** Working code examples for each pattern-framework combination.
* **Comparative Analysis:** Notes and insights on the architectural decisions, flexibility, and developer experience of
  each framework.
* **A Focus on the "Why":** An attempt to understand the underlying philosophy of each tool and when one might be a
  better choice than another.

## Core Patterns Under Investigation

This research focuses on a curated set of patterns that represent a journey from simple to complex agent design:

1. **Prompt Chaining:** The fundamental building block.
2. **Evaluator-Optimizer:** Introducing a loop for quality and refinement.
3. **Agent-Computer Interface (ACI):** A deep dive into the crucial art of designing tools for LLMs.
4. **Composed "Super-Workflow":** An advanced, nested pattern combining an Orchestrator with an Evaluator loop to handle
   complex, multistep tasks.

## Frameworks in the "Ring"

The analysis will initially focus on a selection of promising frameworks, including:

* **LangGraph**
* **Google's Agent Development Kit (ADK)**
* **Vercel AI SDK**
* **LangFlow**
* *(This list may evolve based on community feedback and findings.)*

## Philosophy

This project is guided by a simple philosophy: start simple, prioritize clarity, and always test for real-world
adaptability (the "Day 100" test).

## Contributing & Discussion

This is a living project and a personal learning journey. I welcome feedback, suggestions, corrections, and discussions.
Please feel free to open an issue or start a discussion. Let's learn together.
