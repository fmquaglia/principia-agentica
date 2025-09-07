# Principia Agentica

## Project Overview

This project, "Principia Agentica," is a Python-based initiative focused on the practical exploration of architectural patterns for modern AI agents. It aims to bridge the gap between the theory and practice of agentic design by implementing key patterns in various frameworks. The primary goal is to analyze and compare the developer experience, architectural decisions, and trade-offs associated with each approach.

The project is structured around a case study called "The Sentinel Project," which involves building an AI agent to analyze customer feedback for a fictional SaaS company. This narrative-driven approach provides a realistic context for implementing and evolving the agent's capabilities.

**Key Technologies:**

*   **Python:** The core programming language.
*   **LangGraph:** The primary framework used for building the agentic patterns.
*   **Just:** A command runner for automating project tasks.
*   **Ruff:** Used for code formatting and linting.
*   **Pytest:** The framework for running tests.

## Building and Running

The project uses a `justfile` to define and manage common tasks.

*   **Setup:** To create a new virtual environment, run:
    ```bash
    just setup
    ```

*   **Install Dependencies:** To install the project's dependencies, run:
    ```bash
    just install
    ```

*   **Running Tests:** To run the test suite, use the following command:
    ```bash
    just test
    ```

*   **Linting and Formatting:** To check for code quality and format the code, run:
    ```bash
    just lint
    just format
    ```

## Development Conventions

*   **Code Style:** The project uses `ruff` for code formatting and linting, ensuring a consistent code style.
*   **Testing:** Tests are implemented using `pytest` and are located in the `tests/` directory. The project emphasizes a test-driven approach to ensure the reliability of the agentic patterns.
*   **Modularity:** The project is organized into distinct patterns, each in its own directory within the `patterns/` folder. This modular structure allows for clear separation of concerns and easy comparison of different implementations.
*   **Documentation:** The project includes detailed `README.md` files at both the root and in the `patterns/` directory, providing a comprehensive overview of the project's goals, structure, and the narrative behind the implemented patterns.
