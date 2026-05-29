# 목적: 여행 계획 작성
# 여행지 도시 -> 음식 추천 
#            -> 관광지 추천 
#            -> 호텔 추천
# 사용자 입력의 00을 보고, 시간표/동선/교통수단 vs 음식/관광지/호텔
# RunnableParallel, RunnableBranch

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')
