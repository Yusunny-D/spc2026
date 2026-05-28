from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages([
    ('system', '당신은 작명가입니다.'),
    ('user', '다음 상품을 만드는 회사의 이름을 지어주세요. 상품: {product}')
])

filled_prompt = prompt.format_messages(product='스마트폰')
print("완성된 프롬프트: ", filled_prompt)

filled_prompt = prompt.format_messages(product='자동차')
print("완성된 프롬프트: ", filled_prompt)

print('-'*60)

test_products = [
    "모바일 게임",
    '로봇 장난감',
    '가방',
    '영어 교육 플랫폼',
    '전기 자전거'
]

for p in test_products:
    filled_prompt = prompt.format(product=p)
    print(f'[{p}]', filled_prompt)