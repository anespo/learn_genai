# Generative AI Learning Package

This package is designed to teach generative AI concepts to employees using their laptops. It includes Ollama with the llama2:3b model for text generation and nomic-embed-text for embeddings, along with three example projects demonstrating key concepts in generative AI.

## Prerequisites

- Python 3.8+
- Git

## Installation

1. Clone this repository:
```sh
git clone https://github.com/fbanespo1/learn_genai.git
```

2. Run the setup script:
```sh
chmod +x setup.sh ./setup.sh
```

3. Activate the virtual environment:
```sh
source venv/bin/activate
```


## Usage

1. Start Jupyter Notebook:

2. Navigate to the `notebooks/` directory and open the desired notebook:
- 01_document_summarizer.ipynb
- 02_rag_with_faiss.ipynb
- 03_langgraph_agents.ipynb

3. Follow the instructions in each notebook to run the projects and learn about generative AI concepts.

## Project Descriptions

1. Document Summarizer and Chat: Demonstrates how to extract text from PDFs, summarize documents, and create a simple chat interface to interact with document contents.

2. RAG with FAISS: Implements a basic Retrieval-Augmented Generation (RAG) system using FAISS as the vector database for efficient similarity search.

3. Agents with LangGraph: Creates a simple multi-agent system using LangGraph, demonstrating agent communication and task solving.

## Additional Resources

- [Ollama Documentation](https://github.com/jmorganca/ollama)
- [LangChain Documentation](https://python.langchain.com/en/latest/)
- [FAISS Documentation](https://github.com/facebookresearch/faiss)
- [LangGraph Documentation](https://github.com/langchain-ai/langgraph)

## Support

For any questions or issues, please contact [your-email@company.com].
