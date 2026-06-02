from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain.agents import create_agent


load_dotenv()

# 구글 검색은 원래 구글API키로 하면 됨 (근데 어려움)
# => 이걸 쉽게 만들어주는 다양한 사이트가 있음... Serf, Serper, Tavily

# pip install langchain-tavily

web_search = TavilySearch(max_reults=3)
llm = ChatOpenAI(model="gpt-4o-mini")
agent = create_agent(llm, [web_search])

result = agent.invoke({"messages": [('user', "Langchain의 최신 버전은??")]})

print(f"{result["messages"][-1].content}")
