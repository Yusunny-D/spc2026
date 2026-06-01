# 목적: 질문 유형에 따라 적합한 항목으로 답변한다.
# 질문 유형 -> 배송조회  
#          -> 결제관련 
#          -> 기술지원
# RunnableBranch

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables import RunnableBranch

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

category_prompt = ChatPromptTemplate.from_template(
    "고객의 요청사항을 **아래의 3가지 유형으로만** 분류하시오.\n"
    "(배송조회/결제관련/기술지원)\n\n"
    "고객 요청사항:\n"
    "{requirement}"
)
category_chain = category_prompt | llm | StrOutputParser()

