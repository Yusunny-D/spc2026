from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_messages([
    ('system', "당신은 친절한 챗봇입니다."), # 나의 페르소나 (system)
    ('user', '{input}')                   # 나의 질문 (user), (human)
    # ('ai', '챗봇 답변')                  # 챗봇 답변 (ai), (assistant)
    # ('user', '{input}')                 # 나의 질문
])

chain = prompt | llm | StrOutputParser()
print(chain.invoke({'input': "안녕하세요. 나는 홍길동입니다."}))

print('-'*80)

prompt_with_history = ChatPromptTemplate.from_messages([
    ('system', "당신은 친절한 챗봇입니다."),
    MessagesPlaceholder('history'),
    ('user', '{input}')

])

chain2 = prompt | llm | StrOutputParser()

history_example = [
    HumanMessage(content='안녕하세요. 저는 홍길동 입니다.'),
    AIMessage(content='네, 홍길동님 반갑습니다.')
]

answer = chain2.invoke({
    "history": history_example,
    'input': "제 이름이 뭐였죠?"
})

print(answer)