from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant",temperature=0)

tools = [TavilySearch(max_results=3, search_type="web", search_mode="realtime")]
#agent = create_agent(model="llama-3.1-8b-instant",tools=tools,system_prompt="You are a helpful assistant. When the user asks for current or real-time information, always use the search tool.")
agent = create_agent(model=llm,tools=tools,system_prompt="You are a helpful assistant. When the user asks for current or real-time information, always use the search tool.")

def main():
    print("Hello From Langchain!")
    result = agent.invoke({"messages": [HumanMessage(content="Search the job openings for EA Assistant in Delhi/NCR location")]})
    print(result["messages"][-1].content)

if __name__ == "__main__":

    main()
