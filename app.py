import streamlit as st
import sys
import os
from agents import create_agent_chain


# Add the project directories to the Python path
sys.path.append('./projects/document_summarizer')
sys.path.append('./projects/rag_with_faiss')
sys.path.append('./projects/langgraph_agents')

from summarizer import extract_text_from_pdf, summarize_text, chat_with_document
from rag import create_vectorstore, query_vectorstore
from agents import create_agent_chain
from langchain.llms import Ollama
from langchain.embeddings import OllamaEmbeddings
from langchain.chat_models import ChatOllama
from langchain.schema import HumanMessage

# Set page config and theme
st.set_page_config(page_title="Ollama LLaMa 3.2 Chatbot", page_icon="🤖", layout="wide")

# Apply custom CSS for dark theme
st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .stTextInput > div > div > input {
        color: #FAFAFA;
    }
    .stSelectbox > div > div > select {
        color: #FAFAFA;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Ollama models
llm = Ollama(model="llama2:3b")
chat_llm = ChatOllama(model="llama2:3b")
embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")

# Streamlit app
st.title("Ollama LLaMa 3.2 Chatbot")

# Sidebar for use case selection
use_case = st.sidebar.selectbox(
    "Select Use Case",
    ("Document Summarizer", "RAG System", "Multi-Agent System")
)

# Main chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is your question?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if use_case == "Document Summarizer":
            if "document" not in st.session_state:
                st.session_state.document = None

            uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")
            if uploaded_file is not None:
                with open("temp.pdf", "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.session_state.document = extract_text_from_pdf("temp.pdf")
                os.remove("temp.pdf")

            if st.session_state.document:
                if "summarize" in prompt.lower():
                    response = summarize_text(st.session_state.document, llm)
                else:
                    response = chat_with_document(prompt, st.session_state.document, llm)
            else:
                response = "Please upload a PDF document first."

        elif use_case == "RAG System":
            if "vectorstore" not in st.session_state:
                st.session_state.vectorstore = None

            uploaded_file = st.sidebar.file_uploader("Choose a text file", type="txt")
            if uploaded_file is not None:
                with open("temp.txt", "w") as f:
                    f.write(uploaded_file.getvalue().decode("utf-8"))
                st.session_state.vectorstore = create_vectorstore("temp.txt", embeddings)
                os.remove("temp.txt")

            if st.session_state.vectorstore:
                response = query_vectorstore(st.session_state.vectorstore, prompt, llm)
            else:
                response = "Please upload a text file first."

        elif use_case == "Multi-Agent System":
            chain = create_agent_chain(chat_llm)
            result = chain.invoke({
                "messages": [HumanMessage(content=prompt)],
                "next": "researcher"
            })
            response = "\n".join([msg.content for msg in result['messages'] if msg.content.startswith(("Researcher:", "Writer:"))])

        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Instructions
st.sidebar.markdown("""
## Instructions

1. Select a use case from the dropdown menu above.
2. For Document Summarizer and RAG System, upload a file in the sidebar.
3. Type your question or command in the chat input at the bottom.
4. For the Document Summarizer, use "summarize" in your prompt to get a summary.

Enjoy interacting with the Ollama LLaMa 3.2 Chatbot!
""")
