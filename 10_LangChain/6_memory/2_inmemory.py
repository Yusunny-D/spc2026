from dotenv import load_dotenv
# 모델
from langchain_openai import ChatOpenAI
# 프롬프트
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# 파서
from langchain_core.output_parsers import StrOutputParser
# 기타
from langchain_core.chat_history import InMemoryChatMessageHistory

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_messages([
    ('system', "당신은 친절한 챗봇입니다."),
    MessagesPlaceholder('history'), 
    ('user', '{input}')
])

chain = prompt | llm | StrOutputParser()

history = InMemoryChatMessageHistory()

def chat(message):
    print(f'질문: {message}')
    answer = chain.invoke({
        'input': message,
        'history': history.messages,
    })
    print(f'답변: {answer}')
    history.add_user_message(message)
    history.add_ai_message(answer)

chat('안녕하세요.')
chat('제 이름은 곽길동입니다.')
chat('저는 겨울 바다 서핑을 좋아합니다.')
chat('제 이름과 취미가 뭐라고 했죠?')
