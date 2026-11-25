from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

@tool
def search(query: str) -> str:
    """Tool that Search over the internet
    Args:
        query : The query to search for
    Returns: 
        The search results
    
    """
    return "This is a test search result"

# Cloud APIs: Anthropic has no credits; OpenAI key is expired.
# llm = ChatAnthropic(model="claude-sonnet-4-5", temperature=0)
# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llm = ChatOllama(model="llama3.2", temperature=0)
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main() -> None:
    print("Hello from langchain-course Tavily search agent!")
    result = agent.invoke(
        {"messages": [HumanMessage(content="what is the weather in India.")]}
    )
    print(result)

if __name__ == "__main__":
    main()  
