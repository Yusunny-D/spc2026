from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages([
    ('system', '당신은 작명가입니다.'),
    ('user', '다음 상품을 만드는 회사의 이름을 지어주세요. 상품: {product}')
])

filled_prompt = prompt.format_messages(product='자동차')
print("완성된 프롬프트: ", filled_prompt)

print('-'*60)


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')
res = llm.invoke(filled_prompt)

print(res.content)