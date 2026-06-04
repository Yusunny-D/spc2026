from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

# [1단계] 리서치 중
# 다음 주제에 대해 핵심 사실을 5가지 간결하게 정리   
research_prompt = ChatPromptTemplate.from_template(
    "다음 주제에 대해 핵심 사실을 5가지 간결하게 정리해주세요."
    "\n\n주제: {topic}"
)

research_chain = research_prompt | llm | parser


# [2단계] 게이트 검증 중
gate_prompt = ChatPromptTemplate.from_template(
    "다음 리서치 결과가 적합한지 평가해 주세요."
    "\n리서치 결과: \n{research}"
    "\n\n평가 기준:\n1. 사실 5가지가 올바르게 포함되어 있는가? "
    "\n2. 각 사실이 구체적이고 검증 가능한가? "
    "\n3. 주제와 관련이 있는가?"
    "\n\n결과:\nPASS 또는 FAIL로만 답하고, PASS인 경우 아무런 설영도 없이 PASS만, 실패인 경우 이유를 한줄로 설명하시오."
)
gate_chain = gate_prompt | llm | parser

# 다음 리서치 결과가 적합한지 평가해 주세요.
# 리서치 결과: {}
# 평가 기중: 1. 사실 5가지가 올바르게 포함되어 있는가? 
# 2. 각 사실이 구체적이고 검증 가능한가? 
# 3. 주제와 관련이 있는가?
# 결과:
# PASS 또는 FAIL로만 답하고, PASS인 경우 아무런 설영도 없이 PASS만, 실패인 경우 이유를 한줄로 설명하시오.

# [3단계] 분석 중
analysis_prompt = ChatPromptTemplate.from_template(
    "다음 리서치 결과를 바탕으로 심층 분석 내용을 작성해주시오."
    "\n리서치 결과: \n{research}"
    "\n\n다음을 포함해주세요:"
    "\n- 핵심 트렌드 또는 패턴"
    "\n- 시사점"
    "\n- 향후 전장"
)

analysis_chain = analysis_prompt | llm | parser
# 다음 리서치 결과를 바탕으로 심층 분석 내용을 작성해주시오.
# 리서치 결과: {}
# 다음을 포함해주세요:
# - 핵심 트렌드 또는 패턴
# - 시사점
# - 향후 전장

# [4단계] 보고서 생성 중
report_prompt = ChatPromptTemplate.from_template(
"다음 리서치와 분석 된 내용을 바탕으로 간결한 보고서를 작성하시오."
"\n리서치: \n{research} \n\n분석: \n{analysis} \n\n출력형식:\n- 제목\n- 요약 (3줄)\n- 핵심 발견사항\n- 결론"

)

report_chain = report_prompt | llm | parser
# 다음 리서치와 분석 된 내용을 바탕으로 간결한 보고서를 작성하시오.
# (CEO에게 보고를 위한, 실무자가 팀장에게 보고하는 형태의, 초등학생도 이해할 수 있도록 쉽게, 등등 다양하게 바꿔 볼 것)
# 리서치: {}
# 분석: {}
# 출력형식:
# - 제목
# - 요약 (3줄)
# - 핵심 발견사항
# - 결론


def run_chaining_pipeline(topic):
    # 1단계: 리서치
    print("[1단계] 리서치 중")
    research = research_chain.invoke({'topic': topic})

    # 2단계: 게이트 검증
    print("[2단계] 게이트 검증 중")
    gate_result = gate_chain.invoke({'research': research})
    if gate_result.lower() in 'fail':
        print('게이트 검증 실패')

    # 3단계: 분석 수행
    print("[3단계] 분석 중")
    analysis = analysis_chain.invoke({'research': research})


    # 4단계: 보고서 생성
    print("[4단계] 보고서 생성 중")
    report = report_chain.invoke({'research': research, 'analysis': analysis})
    return report



# 질문
# 1. 2026년도 생성형 AI 시장 동향 조사를 해오시오.
topic = '2026년도 생성형 AI 시장 동향 조사를 해오시오.'

result = run_chaining_pipeline(topic)
print('-'*80)
print('최종 보고서:')
print('-'*80)

print(result)