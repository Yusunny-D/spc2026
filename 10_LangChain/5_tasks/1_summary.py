from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

template = "다음의 긴 내용을 3개의 문장으로 요약하시오:\n\n{article}"
chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("당신은 전문 요약가입니다."),
    HumanMessagePromptTemplate.from_template(template=template)
])

chain = chat_prompt | llm | RunnableLambda(lambda x: {'summary': x.content.strip()})

input_text = {
    "article": """우리나라 국민 10명 가운데 4명가량이 챗GPT 등 생성형 인공지능(AI)을 이용한 경험이 있는 것으로 나타났습니다.

생성형 AI 이용이 빠르게 일상화하는 가운데 허위 정보 생성과 범죄 악용 등 역기능에 대한 우려도 함께 커지고 있는 것으로 조사됐습니다.

방송미디어통신위원회와 정보통신정책연구원(KISDI)은 오늘(28일) 이런 내용을 담은 ‘2025년 지능정보사회 이용자 패널조사’ 결과를 발표했습니다.

조사는 스마트폰을 이용하며 하루 한 차례 이상 인터넷을 사용하는 전국 17개 시도 만 18∼72세 국민 4천 324명을 대상으로 진행됐습니다.

조사 결과 전체 응답자의 38.9%가 생성형 AI를 이용한 경험이 있다고 답했습니다. 이는 2024년 24.0%, 2023년 12.3%와 비교해 3년 연속 증가한 수치입니다. 생성형 AI 이용이 빠르게 대중화 단계에 접어들고 있음을 보여주는 결과로 풀이됩니다. 생성형 AI 이용자의 하루 평균 이용 시간은 49.6분으로 집계됐습니다.

생성형 AI 이용 동기로는 ‘정보 검색에 효율적이다’가 86.0%로 가장 높았습니다. 이어 시간 관리 도움(72.6%), 학습 활동 지원(68.2%), 복잡한 문제 해결(64.8%), 일상 업무 지원(64.8%) 순으로 나타났습니다.

반면 생성형 AI 역기능에 대한 우려도 확대됐습니다. 허위 정보 유포 우려가 전년 대비 9.6%포인트 증가해 가장 큰 상승 폭을 보였고 범죄 악용(+9.0%포인트), 진위 구별이 어려운 콘텐츠 생성(+8.9%포인트) 우려도 뒤를 이었습니다.

업무 대체와 창의력 저하, 저작권 침해, 편향·차별 콘텐츠 생성 등에 대한 부정적 인식도 전반적으로 높아졌습니다.

생성형 AI를 이용하지 않는 이유로는 ‘사용 방법이 어렵다’는 응답이 63.5%로 가장 많았으며 서비스 비용 부담과 개인정보 침해 우려, 윤리 문제 등이 뒤를 이었습니다.

방미통위는 “이번 조사 결과를 향후 AI 이용자 보호 정책 마련에 적극 활용할 계획”이라고 밝혔습니다."""
}

result = chain.invoke(input_text)
print("요약 결과: ", result['summary'])