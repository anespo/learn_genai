#!/bin/bash

# Install Ollama
curl https://ollama.ai/install.sh | sh

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Download and set up Ollama models
ollama pull llama2:3b
ollama pull nomic-embed-text:latest

echo "Setup complete. Activate the virtual environment with 'source venv/bin/activate'"
