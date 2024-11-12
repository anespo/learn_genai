from langgraph.graph import Graph, END
from langchain.chat_models import ChatOllama
from langchain.schema import HumanMessage, AIMessage
from typing import TypedDict, Annotated, Sequence

class AgentState(TypedDict):
    messages: Annotated[Sequence[str], "The messages in the conversation"]
    next: Annotated[str, "The next agent to use"]

def researcher(state):
    messages = state['messages']
    llm = ChatOllama(model="llama2:3b")
    result = llm.invoke(messages + [HumanMessage(content="Act as a researcher and provide relevant information for the given topic.")])
    return {
        "messages": messages + [AIMessage(content=f"Researcher: {result.content}")],
        "next": "writer"
    }

def writer(state):
    messages = state['messages']
    llm = ChatOllama(model="llama2:3b")
    result = llm.invoke(messages + [HumanMessage(content="Act as a writer and create a concise summary based on the researcher's information.")])
    return {
        "messages": messages + [AIMessage(content=f"Writer: {result.content}")],
        "next": END
    }

workflow = Graph()

workflow.add_node("researcher", researcher)
workflow.add_node("writer", writer)

workflow.set_entry_point("researcher")
workflow.add_edge("researcher", "writer")

chain = workflow.compile()

# Example usage
if __name__ == "__main__":
    result = chain.invoke({
        "messages": [HumanMessage(content="Explain the importance of renewable energy.")],
        "next": "researcher"
    })
    for message in result['messages']:
        print(message.content)
