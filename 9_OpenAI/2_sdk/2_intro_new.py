import openai

from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv('OPENAI_KEY')
client = openai.OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': '당신은 나의 질문에 답변을 주는 챗봇입니다.'},
        {'role': 'user', 'content': '안녕? 반가워.'},
    ]
)

final_res = response.choices[0].message.content
print(final_res)