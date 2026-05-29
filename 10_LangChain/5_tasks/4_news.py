# 목적: 뉴스를 분석한다 
# 뉴스 입력 -> 요약 
#          -> 감정분석 
#          -> 카테고리 분석
# RunnableParallel

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

prompt_summary = ChatPromptTemplate.from_template('다음 뉴스를 2~#문장으로 요약해줘.\n\n{news}')
summary_chain = prompt_summary | llm | StrOutputParser()

prompt_sentiment = ChatPromptTemplate.from_template('다음 뉴스의 전반적 감성을 한 단어로 분석해줘. (긍정/부정/중립)\n\n{news}')
sentiment_chain = prompt_sentiment | llm | StrOutputParser()

prompt_category = ChatPromptTemplate.from_template('다음 뉴스의 카테고리를 한 단어로 분석해줘. (정치/경제/사회/IT/스포츠/기타)\n\n{news}')
category_chain = prompt_category | llm | StrOutputParser()

final_chain = RunnableParallel({
    "summary": summary_chain,
    "sentiment": sentiment_chain,
    "category": category_chain
})

news = """(서울=연합뉴스) 이주영 기자 = 식물이 공기 중으로 내보내는 냄새 성분을 통해 주변 식물의 성장 속도를 파악하고, 이에 맞춰 스스로 성장과 방어 전략을 조절한다는 연구 결과가 나왔다.

식물도 서로 눈치 보며 자란다…"이웃에 맞춰 성장 속도 조절"
성장 속도가 다른 보리 품종을 이용한 실험 결과, 보리는 이웃 개체가 방출하는 휘발성유기화합물(VOCs)로 상대의 성장 전략을 감지하고 성장과 방어 사이
식물도 서로 눈치 보며 자란다…"이웃에 맞춰 성장 속도 조절"
성장 속도가 다른 보리 품종을 이용한 실험 결과, 보리는 이웃 개체가 방출하는 휘발성유기화합물(VOCs)로 상대의 성장 전략을 감지하고 성장과 방어 사이의 자원 배분 방식을 바꾸는 것으로 밝혀졌다. [Velemir Ninkovic 제공. 재판매 및 DB 금지]


스웨덴농업과학대(SLU) 벨레미르 닌코비치 박사팀은 29일 국제 학술지 실험 식물학 저널(Journal of Experimental Botany)에서 보리 식물이 이웃 개체가 방출하는 휘발성유기화합물(VOCs)로 상대의 성장 전략을 감지하고 성장과 방어 사이의 자원 배분 방식을 바꾼다는 사실을 실험으로 확인했다고 밝혔다.

닌코비치 박사는 "식물은 이웃 식물의 VOCs를 이용해 주변 경쟁 환경을 평가하는 것으로 보인다"며 "이 연구는 건강한 식물이 방출하는 VOCs가 주변 식물의 성장 전략에 영향을 주는 강력한 생태 신호로 작용할 수 있음을 보여준다"고 말했다.

휘발성유기화합물(VOCs)은 공기 중으로 쉽게 증발하는 탄소 기반 화학물질로, 식물은 초식동물이나 꽃가루받이 곤충, 다른 식물과 소통하기 위해 VOCs를 생성한다. 이런 VOCs는 식물이 내는 향기의 원천이기도 하고, 향수·화장품·식품·세정 제품 제조에도 사용된다.

연구팀은 식물이 내뿜는 VOCs에 대한 연구는 대부분 초식동물 등의 공격으로 손상된 식물이 방출해 주변 식물에 경고하는 현상에 초점을 맞춰왔다며 손상되지 않은 건강한 식물이 평상시 방출하는 VOCs의 역할은 거의 밝혀지지 않았다고 지적했다.

이들은 이 연구에서 성장 속도가 느린 보리 품종인 '페어리테일'(Fairytale)과 중간 속도인 '루카스'(Luhkas), 성장 속도가 빠른 '살로메'(Salome)를 이용해 식물이 이웃 식물의 냄새만으로 상대의 성장 전략을 파악할 수 있는지 실험했다.

느리게 자라는 페어리테일 품종과 빠르게 자라는 살로메 품종을 다른 품종에서 방출되는 VOCs에 25일 동안 노출한 다음, 식물의 생체량 등 물리적 특성과 유전자 발현 변화를 분석해 VOCs가 성장 및 방어 전략에 미치는 영향을 측정했다.

성장 속도가 다른 식물의 휘발성유기화합물에 노출됐을 때 변화
성장 속도가 비슷한 식물(Similar growth rate)의 휘발성유기화합물(VOCs)은 노출됐을 때는 거의 영향을 받지 않지만, 성장 속도가 빠른 식
성장 속도가 다른 식물의 휘발성유기화합물에 노출됐을 때 변화
성장 속도가 비슷한 식물(Similar growth rate)의 휘발성유기화합물(VOCs)은 노출됐을 때는 거의 영향을 받지 않지만, 성장 속도가 빠른 식물(Fast growth rate)이 성장이 느린 식물(Slow growth rate)의 VOCs에 노출되면 성장을 줄이는 대신 방어 체계에 더 많은 자원을 배분한다. 반대로 느리게 자라는 식물은 빠르게 자라는 식물의 VOCs에 노출되면 방어보다 성장에 더 많은 자원을 투입하게 된다. [Journal of Experimental Botany, Velemir Ninkovic et al. 제공. 재판매 및 DB 금지]


그 결과 서로 다른 VOCs에 노출된 식물은 전체 바이오매스 변화가 유도됐지만 성장 속도가 비슷한 식물의 VOCs는 거의 영향을 미치지 않는 것으로 나타났다.

성장 속도가 느린 페어리테일 품종은 성장이 빠른 살로메 품종의 VOCs에 노출됐을 때 생체량이 증가했으나, 반대로 페어리테일의 VOCs에 노출된 살로메 품종은 생체량이 감소했다.

연구팀은 이는 식물이 VOCs를 통해 이웃 식물의 성장 속도를 파악하고 경쟁 강도에 따라 자원을 배분한다는 뜻이라고 설명했다. 즉 이웃 식물이 빠르게 자라면 경쟁에서 뒤처지지 않기 위해 성장에 더 많은 자원을 투입한다는 것이다.

유전자 분석에서도 이런 변화가 확인됐다. 빠르게 자라는 살로메 VOCs에 노출된 페어리테일은 스트레스·방어 관련 유전자 발현이 줄었고, 느리게 자라는 페어리테일 VOCs에 노출된 살로메는 방어·스트레스 관련 유전자 발현이 증가했다.

연구팀은 VOCs 115종을 분석한 결과 품종마다 화합물 조성이 달랐고, 특히 살로메와 페어리테일의 차이가 가장 컸다며 이 가운데 벤질 니트릴, 리날룰, 옥탄알 등 일부 화합물이 성장 전략 변화와 강하게 연관된 것으로 분석됐다고 설명했다.

닌코비치 박사는 "이 연구는 건강한 식물도 끊임없이 자신만의 화학적 신호를 공기 중에 방출하고, 주변 식물은 이 신호를 적극적으로 파악해 자신의 방어 체계뿐 아니라 전체 성장 전략까지 조정한다는 것을 보여준다"고 말했다.

이어 "이런 휘발성유기물질을 기반으로 한 식물 간 상호작용 연구가 병충해 저항성과 작물 생산성을 동시에 높이는 새로운 혼합재배 전략을 개발하는 데 활용될 수 있을 것으로 기대한다"고 덧붙였다."""

result = final_chain.invoke({"news": news})
print(f"원문: {news}")
print(f"요약: {result['summary']}")
print(f"감정 분석: {result['sentiment']}")
print(f"카테고리: {result['category']}")
