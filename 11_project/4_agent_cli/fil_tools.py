# 금융 도우기 에이전트 챗봇 만들기

# 1. 네이버 뉴스를 가져온다. 
# 2. 구글 검색으로 해당 기업 개요/최근 정보 조회 
# 3. 환율을 조회한다. 
# 4. 주가를 조회한다.
import os
import re
import requests

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()


@tool
def get_news(query: str) -> str:
    """ 네이버 뉴스에서 키워드로 최신기사 제목/링크를 검색한다."""
    naver_cid = os.getenv("NAVER_CLIENT_ID")
    naver_secret = os.getenv("NAVER_CLIENT_SECRET")
    if not (naver_cid and naver_secret):
        return "네이버 뉴스 못 가져옴!"
    
    resp = requests.get("https://openapi.naver.com/v1/search/news.json",
                        params={"query": query, "display": 5},
                        headers={})
    
    items = resp.json().get('items', [])
    if not items:
        return f"'{query}' 관련 뉴스 없음"

    return "\n".join(f"- {re.sub(r'<[^>]+>', '', it['title'])} ({it['link']})" for it in items)

@tool
def get_company_info(company: str) -> str:
    """ 회사명을 입력받아 구글에 검색해 회사 정보를 반환한다. """
    web_search = TavilySearch(max_results=3)
    return web_search.invoke(company)


@tool
def get_exchange_rate(base: str="USD", target: str="KRW") -> str:
    """ 환율을 조회한다. """
    resp = requests.get(f"https://open.er-api.com/v6/latest/{base.upper()}")
    rate = resp.json().get("rates", {}).get(target.upper())
    if rate is None:
        return f"{base} -> {target} 환율 조회 실패"
    return f"1 {base.upper()} = {rate} {target.upper()}"


@tool
def get_stock_price(ticker):
    """ yfinance로 다양한 기업의 주가를 가져온다.
    예) 애플('APPL')과 삼성전자('005930.KS') """
    
    # pip install yfinance
    import yfinance as yf
    data = yf.Ticker(ticker).history(period="1d")
    if data.empty:
        return f"'{ticker}' 조회에 실패. "
    return "미구현"


TOOLS = [get_news, get_company_info, get_exchange_rate, get_stock_price]