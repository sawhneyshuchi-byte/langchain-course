from typing import List
from pydantic import BaseModel,Field
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

load_dotenv()

class Source(BaseModel):
    """Schema for source used by agent"""

    url: str = Field(..., description="The URL of the source")
    title: str = Field(..., description="The title of the source")
    snippet: str = Field(..., description="A snippet of the source content")

class AgentResponse(BaseModel):
    """Schema for agent response"""

    answer: str = Field(..., description="The answer provided by the agent")
    content: str = Field(..., description="The content of the agent's response")
    sources: List[Source] = Field(default_factory=list, description="A list of sources used by the agent")

llm = ChatGroq(model="llama-3.1-8b-instant",temperature=0)
tools = [TavilySearch(max_results=5, return_sources=True)]
#agent = create_agent(model="llama-3.1-8b-instant",tools=tools,system_prompt="You are a helpful assistant. When the user asks for current or real-time information, always use the search tool.")
agent = create_agent(model=llm,tools=tools,system_prompt="You are a helpful assistant. When the user asks for current or real-time information, always use the search tool.")

def main():
    print("Hello From Langchain!")
    result = agent.invoke({"messages": [HumanMessage(content="Search for EA Assistant job openings in Delhi/NCR")]})
    #print(result["messages"][-1].content)
    print(result)

if __name__ == "__main__":

    main()
