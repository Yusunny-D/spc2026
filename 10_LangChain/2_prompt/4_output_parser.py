from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages([
    ('system', '브랜드 기획자입니다.'),
    ('user', """회사를 홍보하기 위한 catch-phrase를 5개 만들어줘.
회사명:{company} 상품: {product}
출력 결과는 콤마로 구분된 리스트(CSV)로 만들어줘."""
    )
])

filled_prompt = prompt.format_messages(company='테슬라',product='Model s')
# print("완성된 프롬프트: ", filled_prompt)

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')
res = llm.invoke(filled_prompt)

print(res.content)

from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import CommaSeparatedListOutputParser

parser1 = StrOutputParser()
parser2 = CommaSeparatedListOutputParser()

result_str = parser1.invoke(res)
result_csv = parser2.invoke(res)

print('문자열결과: ', result_str)
print('CSV결과: ', result_csv)