from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel, Field

load_dotenv()

class MovieReview(BaseModel):
    """ 영화 리퓨 분석 결과 """
    title: str = Field(description="영화 제목")
    sentimant: str = Field(description="감성 분류: 긍정, 부정, 중립")
    score: int = Field(description="1~10 점수")
    summary: str = Field(description="리뷰 요약")
    keywords: list[str] = Field(description="핵심 키워드 3개")

llm = ChatOpenAI(model="gpt-4o-mini")
parser = PydanticOutputParser(pydantic_object=MovieReview)

# print("포멧 명령문: ")
# print(parser.get_format_instructions())

prompt = ChatPromptTemplate.from_template(
    """ 다음 영화 리뷰를 분석해주세요.
리뷰: {review}

{format_instructions}
"""
)

chain = prompt | llm | parser

reviews = [
"The Dark Knight는 단순한 히어로 영화를 넘어 인간의 정의와 혼돈에 대해 깊이 고민하게 만드는 작품이다. 특히 조커의 강렬한 존재감과 긴장감 넘치는 전개가 영화 전체를 압도한다. 액션과 서사를 모두 완성도 높게 담아낸 최고의 히어로 영화 중 하나다.",
"Coco는 가족의 소중함과 꿈을 따뜻하게 그려낸 감동적인 애니메이션이다. 화려한 색감과 아름다운 음악이 멕시코 전통 문화를 매력적으로 표현한다. 마지막 장면에서는 자연스럽게 눈물이 날 정도로 깊은 감동을 전해준다.",
"Avengers: Endgame는 오랜 시간 이어진 이야기의 대미를 장식하는 웅장한 블록버스터 영화다. 수많은 캐릭터들의 서사를 하나로 연결하며 팬들에게 큰 감동과 전율을 선사한다. 화려한 액션뿐 아니라 이별과 희생의 감정까지 잘 담아낸 작품이었다."
]

for review in reviews:
    result = chain.invoke({
        "review": review,
        'format_instructions': parser.get_format_instructions()
    })
    
    print(f'제목: {result.title}')
    print(f'감성: {result.sentimant} (점수: {result.score}/10)')
    print(f'요약: {result.summary}')
    print(f'키워드: {result.keywords}')
    print('-'*70)
