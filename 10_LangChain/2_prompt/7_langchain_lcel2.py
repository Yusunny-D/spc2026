import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import (
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template('당신은 브랜드 컨텐츠 기획자입니다.'),
    HumanMessagePromptTemplate.from_template('회사를 홍보하기 위한 {company} 회사의 {product} 상품을 기반으로 캐치프레이즈를 만들어 주세요.')
])

llm = ChatOpenAI(model='gpt-4o-mini')
parser = StrOutputParser()

# chain = prompt | llm | StrOutputParser()
# chain = prompt | llm | RunnableLambda(lambda x: {'respons': x})
chain = prompt | llm | parser | RunnableLambda(lambda x: {'respons': x})

inputs = {'company': '삼성전자', 'product': '메모리'}

result = chain.invoke(inputs)

# final_result = {'response': result}
print(result)