
# Learn GenAI

A package to learn Generative AI through practical examples.

## Prerequisites

1. Install Ollama:
   Follow the instructions at [Ollama's official website](https://ollama.ai/) to install Ollama for your operating system.

## Installation

You can install Learn GenAI using either pip or Poetry.

### Using pip

```bash
pip install learn_genai
```

### Using Poetry

1. If you haven't installed Poetry yet, install it first:
   ```bash
   pip install poetry
   ```

2. Create a new project or navigate to your existing project directory.

3. Add Learn GenAI to your project:
   ```bash
   poetry add learn_genai
   ```

## Usage

### If installed with pip

After installation, run the application with:

```bash
learn_genai
```

### If installed with Poetry

1. Activate the Poetry shell:
   ```bash
   poetry shell
   ```

2. Run the application:
   ```bash
   learn_genai
   ```

Alternatively, you can run it without activating the shell:

```bash
poetry run learn_genai
```

This will open a Streamlit interface in your default web browser, where you can explore three use cases:

1. Text Summarizer
2. RAG Chatbot
3. LangGraph Agents

Each use case demonstrates different aspects of Generative AI using the Llama3.2:3b model and other advanced NLP techniques.

## Troubleshooting

If you encounter any issues:

1. Ensure Ollama is properly installed and running.
2. Check that you're using a compatible Python version (3.8 or higher recommended).
3. If using Poetry, make sure you're in the correct project directory.
4. Try updating the package to the latest version:
   - With pip: `pip install --upgrade learn_genai`
   - With Poetry: `poetry update learn_genai`

For more detailed information or if you encounter any problems, please refer to our [GitHub repository](https://github.com/fbanespo1/learn_genai) or open an issue.
```
