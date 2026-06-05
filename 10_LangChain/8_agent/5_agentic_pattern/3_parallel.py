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


parallel_vote = RunnableParallel({
    # 동시에 3개를 부른다
    'voter1': voter1,
    'voter2': voter2,
    'voter3': voter3
})

original = """
I can't tell you why
But something inside is dancing with fire
Eyes lit like the sky
Turned tears into diamonds, got good at goodbyes

Just know that I will find my way from you
Like flowers from a tomb while you decide who you are
And I can see right through, ooh-ooh, like shadows on the moon
And it's all bad news
"""
translation = """
이유는 말할 수 없지만
내 안의 무언가가 불꽃과 춤을 추고 있어
하늘처럼 빛나는 눈동자
눈물을 다이아몬드로 바꾸고, 이별에 능숙해졌어

그저 알아줘, 난 너에게서 내 길을 찾아낼 거라는 걸
네가 네 정체성을 찾아가는 동안, 무덤에서 피어나는 꽃처럼
그리고 난 꿰뚫어 볼 수 있어, 우-우, 달에 드리운 그림자처럼
그리고 이건 전부 나쁜 소식일 뿐이야
"""


result = parallel_vote.invoke({'original': original, 'translation': translation})
print(f"1. 평가:\n{result['voter1']}\n\n")
print(f"2. 평가:\n{result['voter2']}\n\n")
print(f"3. 평가:\n{result['voter3']}\n\n")

# 번역 전문 챗봇 솔루션...
# 1. 여러개의 모델을 써서
# 2. 평가하게 함 (사람이 평가하면 HITL, llm이 하면 LLM-as-judge)
# 3. 가장 좋은 선택을 함

# 시험 문장 넣고, 중간 번역결과 3개 출력하고,
# 최종 결과를 도출