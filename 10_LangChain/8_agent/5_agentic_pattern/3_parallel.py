from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel

load_dotenv()

parser = StrOutputParser()

# 병렬처리를 통해서 시간을 단축한다

vote_prompt = ChatPromptTemplate.from_template(
"""
당신은 번역 품질 평가원입니다. 다음 번역의 품질을 평가해 주세요.

원문(영어): {original}
번역(한국어): {translation}

평가점수: 1~5점 (리커트 척도)
"""
)

llm1 = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)
llm2 = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
llm3 = ChatOpenAI(model="gpt-4o-mini", temperature=1.0)

voter1 = vote_prompt | llm1 | parser
voter2 = vote_prompt | llm2 | parser
voter3 = vote_prompt | llm3 | parser


parallel_vote = RunnableParallel(
    # 동시에 3개를 부른다
    lambda x: voter1.invoke(x)
)

# 번역 전문 챗봇 솔루션...
# 1. 여러개의 모델을 써서
# 2. 평가하게 함 (사람이 평가하면 HITL, llm이 하면 LLM-as-judge)
# 3. 가장 좋은 선택을 함

# 시험 문장 넣고, 중간 번역결과 3개 출력하고,
# 최종 결과를 도출