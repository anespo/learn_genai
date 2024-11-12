import pypdf2
from langchain.llms import Ollama
from langchain.chains.summarize import load_summarize_chain

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = pypdf2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def summarize_text(text, llm):
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(text)
    return summary

def chat_with_document(query, text, llm):
    response = llm(f"Based on the following text, answer this question: {query}\n\nText: {text}")
    return response

# Example usage
if __name__ == "__main__":
    llm = Ollama(model="llama2:3b")
    pdf_path = "example.pdf"
    text = extract_text_from_pdf(pdf_path)
    summary = summarize_text(text, llm)
    print("Summary:", summary)

    query = "What is the main topic of this document?"
    answer = chat_with_document(query, text, llm)
    print("Answer:", answer)
