# 다양한 목적에 맞는 이메일을 작성해준다.

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("당신은 기업의 커뮤니케이션 전문가입니다. 포멀하게 전문가 톤으로 이메일을 작성하시오."),
    HumanMessagePromptTemplate.from_template('수신자 "{recipient}" 에게 다음 주제 "{topic}" 에 대한 미팅을 요청하는 메일을 작성하시오.')
])

# chain = chat_prompt | llm | RunnableLambda(lambda x: {'email': x.content.strip()})
chain = chat_prompt | llm | StrOutputParser()

# 다양한 수신자와 다양한 주제
recipients = [
    '마케팅팀', 
    '개발팀', 
    '영업팀', 
    '인사팀'
    ]
topics = [
    '신제품 출시 전략', 
    '분기별 개발 성과 지표', 
    '개인별 배출 목표치 달성 현황', 
    '개발을 잘 못해서 맨날 버그만 발생시키는 개발자 해고'
    ]

for recipient, topic in zip(recipients, topics):
    print('-'*80)
    print(f'To: {recipient}, Topic: {topic}')
    print('-'*80)
    result = chain.invoke({"recipient": recipient, 'topic': topic})
    print(result)