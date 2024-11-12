# Generative AI Learning Package v1.0.0

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)]
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]

A comprehensive learning package for Generative AI, featuring practical examples using local resources. This project demonstrates key concepts in AI development including document summarization, retrieval-augmented generation (RAG), and multi-agent systems.

## 🚀 Features

- **Document Summarizer**: PDF text extraction and intelligent summarization
- **RAG with FAISS**: Vector-based document retrieval and generation
- **LangGraph Agents**: Multi-agent system demonstrations
- **Local Execution**: All examples run locally using Ollama

## 📋 System Requirements

- Python 3.8 or higher
- RAM: 8GB minimum (16GB recommended)
- Storage: 5GB free space
- CPU: 4 cores recommended
- GPU: Optional, but recommended for better performance
- Operating System: Windows 10+, macOS 10.15+, or Linux

## 🛠️ Installation

1. Clone this repository:
```bash
git clone https://github.com/fbanespo1/learn_genai.git
cd learn_genai
chmod 775 setup.sh #for automatic installation
#or manually
python -m venv venv

# On Windows
.\venv\Scripts\activate
# On Unix/MacOS
source venv/bin/activate

# Verify activation
which python  # Should point to venv

pip install -r requirements.txt

# Verify installation
python -c "import langchain, faiss; print('Setup successful!')"
# Follow Ollama installation instructions for your OS
ollama pull llama2:3b
python scripts/verify_setup.py
jupyter notebook notebooks/01_document_summarizer.ipynb
learn_genai/
├── notebooks/
│   ├── 01_document_summarizer.ipynb
│   ├── 02_rag_with_faiss.ipynb
│   └── 03_langgraph_agents.ipynb
├── data/
│   └── sample_documents/
├── scripts/
│   └── verify_setup.py
├── requirements.txt
└── README.md
# Reset Ollama installation
ollama rm llama2
ollama pull llama2:3b
pytest tests/
